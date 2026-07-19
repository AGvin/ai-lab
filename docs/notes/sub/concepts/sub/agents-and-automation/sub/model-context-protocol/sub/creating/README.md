# Creating MCP Servers

This tutorial builds a small Model Context Protocol server from first principles, then extends it with a resource, a prompt, a controlled mutation tool, tests, and production safeguards.

The examples use Python and the official MCP Python SDK. The architecture and safety rules apply to other official SDKs as well.

## Learning objectives

After completing this guide, you should be able to:

- decide whether MCP is the right integration boundary;
- choose between tools, resources, and prompts;
- build and run a local stdio server;
- validate input and return useful errors;
- add a mutation without making writes implicit;
- test capability discovery and failure behavior;
- prepare a server for remote deployment and authorization.

## 1. Decide whether to build an MCP server

Build an MCP server when several compatible AI hosts should access the same tools or contextual data through a standard protocol.

Prefer another abstraction when:

| Need | Better fit |
|---|---|
| Reusable procedure with no new external capability | Agent Skill |
| One deterministic operation inside an existing application | Local function or tool |
| Ordinary service-to-service integration with no AI-facing discovery | Conventional API |
| Platform-specific bundle of skills, hooks, and configuration | Plugin |
| Shared AI-facing tools, resources, or prompts | MCP server |

An MCP server often wraps an existing API. MCP does not replace authorization, business logic, or data validation in that API.

## 2. Define the server contract

Write the contract before code:

```text
Server name: project-status
Users: developers working in one repository
Transport: local stdio
Tools:
  - get_project_status (read-only)
  - set_project_note (write, explicit confirmation required)
Resources:
  - project://configuration
Prompts:
  - summarize_project
Filesystem access: one configured project root
Network access: none
Credentials: none
Failure behavior: structured error; no partial write
Logging: stderr only
```

For every capability specify:

- who controls invocation;
- required input;
- returned data;
- side effects;
- authorization;
- timeout;
- idempotency;
- audit evidence.

## 3. Create the project

Requirements:

- Python 3.10 or newer;
- `uv` or another isolated Python environment;
- an official MCP SDK version compatible with the target clients.

```bash
uv init project-status-mcp
cd project-status-mcp
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
```

Create this layout:

```text
project-status-mcp/
├── pyproject.toml
├── server.py
├── tests/
│   └── test_server.py
└── README.md
```

## 4. Build a minimal server

`server.py`:

```python
from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("project-status")


def project_root() -> Path:
    raw = os.environ.get("PROJECT_ROOT")
    if not raw:
        raise RuntimeError("PROJECT_ROOT is required")

    root = Path(raw).expanduser().resolve()
    if not root.is_dir():
        raise RuntimeError(f"PROJECT_ROOT is not a directory: {root}")
    return root


@mcp.tool()
def get_project_status() -> dict[str, object]:
    """Return a read-only summary of the configured project."""
    root = project_root()
    return {
        "project": root.name,
        "path": str(root),
        "has_readme": (root / "README.md").is_file(),
        "has_git": (root / ".git").exists(),
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The SDK derives the tool schema from the function signature and docstring. Keep the docstring precise because hosts may present it to the model and user.

Run it:

```bash
PROJECT_ROOT=/absolute/path/to/project uv run server.py
```

A stdio server waits for protocol messages. It is normal for it to appear idle when started directly.

## 5. Configure a host

Conceptual host configuration:

```json
{
  "mcpServers": {
    "project-status": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/project-status-mcp",
        "run",
        "server.py"
      ],
      "env": {
        "PROJECT_ROOT": "/absolute/path/to/project"
      }
    }
  }
}
```

Use absolute paths. Keep credentials outside committed configuration.

## 6. Keep protocol stdout clean

For stdio transport, stdout carries JSON-RPC messages. Ordinary output can corrupt the connection.

Bad:

```python
print("starting server")
```

Good:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("starting server")
```

Configure logging to stderr or a file. Never print debugging payloads to stdout in a stdio server.

## 7. Add a resource

Resources expose application-controlled contextual data. Add a configuration resource:

```python
@mcp.resource("project://configuration")
def read_configuration() -> str:
    """Return the project's public AI configuration."""
    path = project_root() / "AGENTS.md"
    if not path.is_file():
        return "No AGENTS.md file is present."
    return path.read_text(encoding="utf-8")
```

Do not expose arbitrary paths from user-supplied URIs unless path containment and authorization are enforced.

A safe containment helper:

```python
def inside_project(relative_path: str) -> Path:
    root = project_root()
    candidate = (root / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError("path escapes PROJECT_ROOT")
    return candidate
```

## 8. Add a prompt

Prompts are reusable interaction templates selected by the user or host:

```python
@mcp.prompt()
def summarize_project(audience: str = "developer") -> str:
    """Prepare a project-summary request for a selected audience."""
    return (
        "Read project://configuration and call get_project_status. "
        f"Summarize the project for a {audience}. "
        "Separate observed facts from recommendations."
    )
```

A prompt does not grant access. The client still controls which resources and tools are available.

## 9. Add a controlled mutation tool

Writes require stronger design than reads. Use an explicit confirmation field and avoid overwriting existing data silently:

```python
@mcp.tool()
def set_project_note(note: str, confirm: bool = False) -> dict[str, object]:
    """Create PROJECT_NOTE.md after the caller explicitly confirms the write."""
    if not confirm:
        return {
            "written": False,
            "requires_confirmation": True,
            "target": "PROJECT_NOTE.md",
            "preview": note,
        }

    target = project_root() / "PROJECT_NOTE.md"
    if target.exists():
        raise FileExistsError("PROJECT_NOTE.md already exists")

    target.write_text(note.rstrip() + "\n", encoding="utf-8")
    return {
        "written": True,
        "path": str(target),
        "bytes": target.stat().st_size,
    }
```

The confirmation field is defense in depth, not a replacement for host approval or backend authorization.

For production mutations also consider:

- authenticated user identity;
- role and scope checks;
- idempotency keys;
- optimistic concurrency;
- transaction boundaries;
- audit records;
- rollback or compensation.

## 10. Validate inputs and outputs

Use narrow types and bounds. Reject ambiguous values before calling a backend.

```python
@mcp.tool()
def read_text_file(relative_path: str, max_bytes: int = 100_000) -> str:
    """Read one UTF-8 text file inside PROJECT_ROOT."""
    if not 1 <= max_bytes <= 1_000_000:
        raise ValueError("max_bytes must be between 1 and 1,000,000")

    path = inside_project(relative_path)
    if not path.is_file():
        raise FileNotFoundError(relative_path)
    if path.stat().st_size > max_bytes:
        raise ValueError("file exceeds max_bytes")
    return path.read_text(encoding="utf-8")
```

Do not return secrets, unrestricted environment dumps, raw database errors, or oversized payloads by default.

## 11. Error handling

Errors should be visible and actionable without leaking sensitive internals.

Distinguish:

- invalid caller input;
- denied authorization;
- missing resource;
- dependency unavailable;
- timeout;
- conflict or duplicate request;
- internal server failure.

Log detailed diagnostics under a correlation ID. Return a sanitized category and next action to the client.

Do not convert every failure into a plausible success string.

## 12. Test the server

Test the business functions directly before protocol-level tests:

```python
from pathlib import Path

import server


def test_status_reports_readme(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "README.md").write_text("# Example\n", encoding="utf-8")
    monkeypatch.setenv("PROJECT_ROOT", str(tmp_path))

    result = server.get_project_status()

    assert result["project"] == tmp_path.name
    assert result["has_readme"] is True


def test_note_requires_confirmation(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("PROJECT_ROOT", str(tmp_path))

    result = server.set_project_note("hello", confirm=False)

    assert result["written"] is False
    assert not (tmp_path / "PROJECT_NOTE.md").exists()
```

Then test through an MCP client or inspector:

1. initialize and negotiate protocol version;
2. list tools, resources, and prompts;
3. verify schemas and descriptions;
4. call every read capability;
5. test malformed and denied input;
6. test mutation preview without write;
7. test confirmed write in a temporary directory;
8. verify duplicate and rollback behavior;
9. test shutdown and restart.

## 13. Security tests

At minimum test:

- `../` path traversal;
- symlink escape from the allowed root;
- oversized input and output;
- malformed encoding;
- missing and over-scoped credentials;
- prompt injection inside resource data;
- repeated mutation calls;
- concurrent updates;
- timeout and cancellation;
- secret leakage in logs and errors.

Treat tool descriptions and server-provided annotations as untrusted unless the server itself is trusted.

## 14. Choose transport for deployment

Use stdio for a local process owned by one host. Use Streamable HTTP for a managed remote service.

When moving to HTTP add:

- TLS;
- real user authentication;
- audience and scope validation;
- tenant isolation;
- rate limiting;
- request-size limits;
- secure session identifiers;
- origin and redirect controls;
- centralized logging and metrics;
- deployment health checks.

Do not use an MCP session identifier as authentication.

## 15. Versioning and compatibility

Version:

- server implementation;
- tool and resource schemas;
- backend API dependencies;
- supported MCP protocol versions;
- authorization policy.

Treat these as breaking changes when applicable:

- renamed or removed capabilities;
- changed required arguments;
- broader write scope;
- new mandatory credential;
- changed output shape;
- changed resource URI semantics.

Maintain fixtures for every supported client and protocol version.

## 16. Production checklist

- [ ] MCP is the correct integration boundary.
- [ ] Tools, resources, and prompts have clear ownership and descriptions.
- [ ] Input schemas are narrow and validated.
- [ ] Filesystem and network access use least privilege.
- [ ] Stdio logging never writes ordinary output to stdout.
- [ ] Mutations have authorization, approval, idempotency, and verification.
- [ ] Resources and tool results are treated as untrusted data.
- [ ] Errors are actionable but sanitized.
- [ ] Protocol, business-logic, security, and failure tests pass.
- [ ] Transport and authentication match the deployment model.
- [ ] Versions, compatibility, rollback, and operational ownership are documented.

## References

- MCP documentation: https://modelcontextprotocol.io/docs/
- Build an MCP server: https://modelcontextprotocol.io/docs/develop/build-server
- Official SDKs: https://modelcontextprotocol.io/docs/sdk
- Python SDK: https://py.sdk.modelcontextprotocol.io/
- Security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Using MCP: ../using/
- MCP concept: ../../
