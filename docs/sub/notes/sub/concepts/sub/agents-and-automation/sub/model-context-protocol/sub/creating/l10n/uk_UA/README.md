<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:83b11657a8c049857b4b18feb0eb53020f186df1
  mode: translated
-->

# Створення MCP servers

Цей tutorial будує невеликий server Model Context Protocol із базових принципів, а потім розширює його resource, prompt, контрольованим mutation tool, tests і production safeguards.

У прикладах використано Python та офіційний MCP Python SDK. Архітектура й safety rules також застосовні до інших офіційних SDK.

## Переклади

- [English](../../)
- Українська

## Навчальні цілі

Після завершення цього guide ви повинні вміти:

- визначати, чи є MCP правильною integration boundary;
- вибирати між tools, resources і prompts;
- створювати й запускати локальний stdio server;
- validate input і повертати корисні errors;
- додавати mutation, не роблячи writes неявними;
- тестувати capability discovery і failure behavior;
- готувати server до remote deployment і authorization.

## 1. Визначте, чи потрібно створювати MCP server

Створюйте MCP server, коли кілька сумісних AI hosts повинні отримувати доступ до тих самих tools або contextual data через standard protocol.

Віддайте перевагу іншій abstraction, коли:

| Потреба | Кращий варіант |
|---|---|
| Повторно використовувана procedure без нової external capability | Agent Skill |
| Одна deterministic operation у наявній application | Локальна function або tool |
| Звичайна service-to-service integration без AI-facing discovery | Conventional API |
| Platform-specific bundle skills, hooks і configuration | Plugin |
| Спільні AI-facing tools, resources або prompts | MCP server |

MCP server часто обгортає наявний API. MCP не замінює authorization, business logic або data validation у цьому API.

## 2. Визначте contract server

Опишіть contract до написання code:

```text
Назва server: project-status
Користувачі: developers, які працюють в одному repository
Transport: локальний stdio
Tools:
  - get_project_status (read-only)
  - set_project_note (write, потрібне explicit confirmation)
Resources:
  - project://configuration
Prompts:
  - summarize_project
Filesystem access: один налаштований project root
Network access: відсутній
Credentials: відсутні
Failure behavior: structured error; без partial write
Logging: лише stderr
```

Для кожної capability визначте:

- хто контролює invocation;
- required input;
- returned data;
- side effects;
- authorization;
- timeout;
- idempotency;
- audit evidence.

## 3. Створіть project

Вимоги:

- Python 3.10 або новіший;
- `uv` або інше isolated Python environment;
- version офіційного MCP SDK, сумісна з target clients.

```bash
uv init project-status-mcp
cd project-status-mcp
uv venv
source .venv/bin/activate
uv add "mcp[cli]"
```

Створіть таку structure:

```text
project-status-mcp/
├── pyproject.toml
├── server.py
├── tests/
│   └── test_server.py
└── README.md
```

## 4. Створіть мінімальний server

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

SDK формує tool schema з function signature і docstring. Зберігайте docstring точним, оскільки hosts можуть показувати його model і user.

Запустіть server:

```bash
PROJECT_ROOT=/absolute/path/to/project uv run server.py
```

Stdio server очікує protocol messages. Коли його запускають безпосередньо, нормальним є вигляд, наче він неактивний.

## 5. Налаштуйте host

Концептуальна host configuration:

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

Використовуйте absolute paths. Зберігайте credentials поза committed configuration.

## 6. Зберігайте protocol stdout чистим

Для stdio transport stdout переносить JSON-RPC messages. Звичайний output може пошкодити connection.

Погано:

```python
print("starting server")
```

Добре:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("starting server")
```

Налаштуйте logging у stderr або file. Ніколи не друкуйте debugging payloads у stdout stdio server.

## 7. Додайте resource

Resources надають contextual data, якими керує application. Додайте configuration resource:

```python
@mcp.resource("project://configuration")
def read_configuration() -> str:
    """Return the project's public AI configuration."""
    path = project_root() / "AGENTS.md"
    if not path.is_file():
        return "No AGENTS.md file is present."
    return path.read_text(encoding="utf-8")
```

Не надавайте arbitrary paths із user-supplied URIs, якщо не enforce path containment і authorization.

Безпечний containment helper:

```python
def inside_project(relative_path: str) -> Path:
    root = project_root()
    candidate = (root / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError("path escapes PROJECT_ROOT")
    return candidate
```

## 8. Додайте prompt

Prompts — повторно використовувані interaction templates, які вибирає user або host:

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

Prompt не надає access. Client і далі контролює, які resources і tools доступні.

## 9. Додайте контрольований mutation tool

Writes потребують сильнішого design, ніж reads. Використовуйте explicit confirmation field і не перезаписуйте наявні data без попередження:

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

Confirmation field — defense in depth, а не заміна host approval або backend authorization.

Для production mutations також врахуйте:

- authenticated user identity;
- role і scope checks;
- idempotency keys;
- optimistic concurrency;
- transaction boundaries;
- audit records;
- rollback або compensation.

## 10. Validate inputs і outputs

Використовуйте narrow types і bounds. Відхиляйте ambiguous values до виклику backend.

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

За замовчуванням не повертайте secrets, unrestricted environment dumps, raw database errors або oversized payloads.

## 11. Error handling

Errors мають бути видимими й actionable без витоку sensitive internals.

Розрізняйте:

- invalid caller input;
- denied authorization;
- missing resource;
- dependency unavailable;
- timeout;
- conflict або duplicate request;
- internal server failure.

Log detailed diagnostics під correlation ID. Повертайте client sanitized category і next action.

Не перетворюйте кожний failure на правдоподібний success string.

## 12. Протестуйте server

Спочатку тестуйте business functions безпосередньо, до protocol-level tests:

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

Потім тестуйте через MCP client або inspector:

1. виконайте initialize і negotiate protocol version;
2. отримайте lists tools, resources і prompts;
3. перевірте schemas та descriptions;
4. викличте кожну read capability;
5. протестуйте malformed і denied input;
6. протестуйте mutation preview без write;
7. протестуйте confirmed write у temporary directory;
8. перевірте duplicate і rollback behavior;
9. протестуйте shutdown і restart.

## 13. Security tests

Щонайменше протестуйте:

- path traversal через `../`;
- symlink escape з allowed root;
- oversized input і output;
- malformed encoding;
- відсутні та over-scoped credentials;
- prompt injection у resource data;
- repeated mutation calls;
- concurrent updates;
- timeout і cancellation;
- leakage secrets у logs та errors.

Розглядайте tool descriptions і server-provided annotations як untrusted, якщо сам server не є trusted.

## 14. Виберіть transport для deployment

Використовуйте stdio для локального process, яким володіє один host. Використовуйте Streamable HTTP для managed remote service.

Під час переходу на HTTP додайте:

- TLS;
- справжню user authentication;
- audience і scope validation;
- tenant isolation;
- rate limiting;
- request-size limits;
- secure session identifiers;
- origin і redirect controls;
- centralized logging і metrics;
- deployment health checks.

Не використовуйте MCP session identifier як authentication.

## 15. Versioning і compatibility

Version такі компоненти:

- server implementation;
- tool і resource schemas;
- backend API dependencies;
- supported MCP protocol versions;
- authorization policy.

За відповідних умов вважайте breaking changes:

- renamed або removed capabilities;
- changed required arguments;
- broader write scope;
- new mandatory credential;
- changed output shape;
- changed resource URI semantics.

Підтримуйте fixtures для кожного supported client і protocol version.

## 16. Production checklist

- [ ] MCP є правильною integration boundary.
- [ ] Tools, resources і prompts мають чітких owners та descriptions.
- [ ] Input schemas вузькі й validated.
- [ ] Filesystem і network access використовують least privilege.
- [ ] Stdio logging ніколи не записує звичайний output у stdout.
- [ ] Errors actionable, але sanitized.
- [ ] Protocol, business-logic, security і failure tests проходять.
- [ ] Transport і authentication відповідають deployment model.
- [ ] Versions, compatibility, rollback і operational ownership задокументовано.

## Джерела

- Документація MCP: https://modelcontextprotocol.io/docs/
- Створення MCP server: https://modelcontextprotocol.io/docs/develop/build-server
- Офіційні SDK: https://modelcontextprotocol.io/docs/sdk
- Python SDK: https://py.sdk.modelcontextprotocol.io/
- Найкращі практики безпеки: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- [Використання MCP](../../../using/l10n/uk_UA/)
- [Концепція MCP](../../../../l10n/uk_UA/)
