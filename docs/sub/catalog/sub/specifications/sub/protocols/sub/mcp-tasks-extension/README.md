# MCP Tasks Extension

**MCP Tasks Extension** is the official stable optional Model Context Protocol extension `io.modelcontextprotocol/tasks` for long-running tool operations that return durable task handles instead of blocking until a result is ready. Its stable released specification/schema revision is **2026-07-28**, distinct from the earlier experimental Tasks design in the 2025-11-25 MCP core release and from ongoing development drafts. [Official Tasks extension](https://tasks.extensions.modelcontextprotocol.io/).

## Task lifecycle and protocol boundary

A client opts in through extension capabilities, and a server may respond to a supported `tools/call` with a new task identifier. The client polls status using `tasks/get`, updates or cancels the task with the supported methods, and retrieves outcomes according to the released schema. Cancellation is cooperative; a cancellation acknowledgment does not guarantee the task reached a cancelled terminal state.

Stable task identifiers must be unguessable because they can authorize access to stored task state; **there is no `tasks/list` enumeration method**. Support for update, status notifications, subscribed streams, retention, TTL and terminal states must follow the active released revision rather than assumptions from an older experimental implementation. [Tasks extension overview](https://tasks.extensions.modelcontextprotocol.io/).

## Operational and security limits

A task handle is a protocol mechanism, not a complete distributed job system, transactional guarantee or proof of permission to run an agent indefinitely. Real deployments must control task ownership, authorization, result retention, sensitive input or output, cancellation side effects and transport reliability. Check client/server version support before using the extension.

## Official resources

- [Tasks extension overview](https://tasks.extensions.modelcontextprotocol.io/)
- [Stable 2026-07-28 specification](https://github.com/modelcontextprotocol/ext-tasks/tree/main/specification/2026-07-28)
- [MCP 2026-07-28 release notes](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
