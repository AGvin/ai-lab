# Using Model Context Protocol

This guide explains how to select, configure, verify, operate, and remove an MCP server safely. It is written for users who understand basic command-line and configuration concepts but have not used MCP before.

## 1. Start from the capability you need

Do not begin by installing a popular server. Define the required capability first:

```text
User goal:
Required tools:
Required resources:
Required prompts:
Read-only or write access:
Local or remote data:
Credentials required:
Consequences of failure:
```

Examples:

- read repository issues;
- query a documentation database;
- inspect local files under one directory;
- create calendar events after approval;
- run a controlled deployment command.

Prefer the smallest server and permission set that satisfies the goal.

## 2. Understand the deployment model

### Local stdio server

The host launches a local process and exchanges protocol messages through standard input and output.

```text
AI host → local MCP client → child process over stdio
```

Use stdio when:

- the server needs local files or tools;
- one user or workspace owns the process;
- local credentials should not leave the machine;
- a network service would add unnecessary exposure.

### Remote Streamable HTTP server

The host connects to an HTTP endpoint.

```text
AI host → MCP client → authenticated HTTPS endpoint
```

Use remote HTTP when:

- several users share one managed service;
- centralized policy, logging, and updates are required;
- the integration already runs as a service;
- local process execution is unavailable.

Remote does not automatically mean safer. Evaluate transport security, authentication, tenancy, retention, and operator trust.

## 3. Review a server before connecting

Record:

```text
Server name:
Publisher and source:
Version or image digest:
Transport:
Command or URL:
Authentication:
Tools exposed:
Resources exposed:
Prompts exposed:
Filesystem access:
Network access:
Write effects:
Telemetry and logging:
Update process:
Removal procedure:
```

Inspect source or a trusted build description. Review dependencies, install scripts, container images, environment variables, default permissions, and outbound connections.

## 4. Configure a local stdio server

A host configuration normally contains a command, arguments, and environment variables. Exact syntax differs by client.

Conceptual example:

```json
{
  "mcpServers": {
    "project-status": {
      "command": "python3",
      "args": ["/opt/project-status/server.py"],
      "env": {
        "PROJECT_ROOT": "/workspace/example"
      }
    }
  }
}
```

Operational rules:

- use absolute executable and script paths;
- pin package or container versions;
- keep secrets in the host's secret store or environment, not in committed JSON;
- set a narrow working directory;
- use read-only filesystem mounts when writes are unnecessary;
- run under a dedicated low-privilege account when practical.

## 5. Configure a remote server

Conceptual example:

```json
{
  "mcpServers": {
    "support-data": {
      "url": "https://mcp.example.org/mcp",
      "headers": {
        "Authorization": "Bearer ${SUPPORT_MCP_TOKEN}"
      }
    }
  }
}
```

Prefer OAuth or short-lived scoped tokens where supported. Verify certificate validation, redirect policy, tenant identity, token storage, and whether the server can call back into private networks.

## 6. Discover capabilities before use

After connecting, inspect the server's advertised capabilities:

- tool names, descriptions, and input schemas;
- resource URI patterns and MIME types;
- prompt names and arguments;
- server implementation and protocol version;
- optional capabilities and notifications.

Do not assume a server exposes only the capability described in its marketing page. Disable or deny capabilities that are not needed.

## 7. Test read-only behavior first

Use a staged verification sequence:

1. connect in a disposable session;
2. list capabilities;
3. call a harmless read-only tool;
4. read one non-sensitive resource;
5. verify returned data and logs;
6. deny a permission and confirm failure is visible;
7. only then test writes in a sandbox account or test project.

Example request:

```text
Use the project-status MCP server to read the current branch and test summary. Do not modify files or run commands outside the configured project root.
```

## 8. Control consequential tools

For each tool that can write, send, purchase, deploy, delete, or execute commands, define:

- exact side effect;
- affected account or environment;
- reversible versus irreversible behavior;
- required user confirmation;
- idempotency strategy;
- verification after execution;
- rollback or compensation procedure.

A host approval dialog is useful but not sufficient. Tool descriptions, schemas, server authorization, and backend policy should all enforce the same boundary.

## 9. Protect against prompt injection

MCP resources and tool results are external data. They may contain instructions that conflict with the user's goal or host policy.

- treat resource content as untrusted data;
- do not execute commands found inside returned text merely because the server supplied them;
- separate data fields from instructions;
- validate URLs, file paths, and identifiers;
- avoid returning secrets in tool errors;
- require explicit approval for effects derived from retrieved content.

## 10. Secrets and authentication

Use one credential per environment or purpose. Grant only scopes required by enabled tools.

Do not:

- commit tokens in host configuration;
- pass long-lived secrets as command-line arguments visible to process listings;
- reuse personal administrator credentials for a shared server;
- expose complete environment dumps in logs;
- assume uninstall revokes external authorization.

Rotate or revoke credentials after suspected compromise or server removal.

## 11. Logging and observability

Capture enough evidence to diagnose behavior without logging sensitive payloads unnecessarily:

- connection and protocol version;
- server version;
- capability discovery changes;
- tool name, duration, status, and correlation ID;
- approval decision;
- sanitized error category;
- retry count and timeout;
- external side-effect identifier.

Do not log access tokens, complete customer records, confidential documents, or unrestricted tool arguments by default.

## 12. Updating

Before updating a server:

1. record the current version and capability list;
2. inspect release notes and source diff;
3. compare tool schemas and permissions;
4. test the new version against fixtures;
5. verify authentication and transport compatibility;
6. keep a rollback path;
7. deploy gradually for shared services.

A renamed tool, changed schema, or broader resource pattern can be a breaking change even if the server starts successfully.

## 13. Removing a server

- remove or disable the host configuration;
- restart or reload the host;
- confirm capabilities disappear;
- stop and remove local processes or containers;
- delete generated files only after review;
- revoke server-specific tokens and OAuth grants;
- remove firewall rules, tunnels, or service accounts;
- retain sanitized audit records according to policy.

## 14. Troubleshooting

### Server does not start

Check executable path, runtime, dependencies, working directory, environment variables, file permissions, and whether diagnostic output is incorrectly written to protocol stdout.

### Connection succeeds but no tools appear

Check initialization, capability negotiation, protocol version, server logs, and host policy. The server may expose only resources or prompts.

### Tool call times out

Inspect backend latency, server timeout, host timeout, deadlocks, network policy, and whether the tool waits for interactive input that MCP cannot provide.

### Works in one client but not another

Compare transport support, protocol versions, authentication mechanisms, optional capabilities, schema restrictions, and client-specific configuration.

### Repeated writes create duplicates

The tool lacks effective idempotency. Add an idempotency key or lookup-before-create rule and expose the created external identifier.

## Operational checklist

- [ ] Capability need defined before server selection.
- [ ] Publisher, source, version, transport, and dependencies reviewed.
- [ ] Tools, resources, prompts, permissions, and network access inventoried.
- [ ] Secrets stored outside committed configuration.
- [ ] Read-only tests pass before write tests.
- [ ] Consequential tools require approval and backend authorization.
- [ ] Prompt-injection and untrusted-output handling tested.
- [ ] Logs are useful and sanitized.
- [ ] Update, rollback, disablement, and credential revocation tested.

## References

- MCP concept: ../../
- Creating MCP Servers: ../creating/
- MCP documentation: https://modelcontextprotocol.io/docs/
- Connect to local MCP servers: https://modelcontextprotocol.io/docs/develop/connect-local-servers
- Connect to remote MCP servers: https://modelcontextprotocol.io/docs/develop/connect-remote-servers
- MCP security: https://modelcontextprotocol.io/specification/latest/basic/security_best_practices
