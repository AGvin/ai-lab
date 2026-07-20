# Model Context Protocol (MCP)

Model Context Protocol is an open protocol for connecting AI applications to external tools, contextual data, reusable prompts, and related capabilities through a consistent client-server interface.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Learning path

- [Using Model Context Protocol](./sub/using/) — select, configure, verify, secure, update, and remove MCP servers.
- [Creating MCP Servers](./sub/creating/) — build a server with tools, resources, prompts, tests, authorization, and deployment safeguards.
- [Agent Skills](../agent-skills/) — reusable workflows that may orchestrate capabilities exposed through MCP.
- [Plugins](../plugins/) — platform-specific packages that may configure or distribute MCP integrations.

## Purpose

Without a shared protocol, every AI application and external integration needs a custom adapter. MCP defines common discovery, invocation, lifecycle, and transport behavior so compatible hosts and servers can interoperate without a bespoke connector for every pair.

MCP standardizes context exchange. It does not define how an application selects a model, plans an agent workflow, stores memory, evaluates results, or decides whether retrieved context is trustworthy.

## Architecture

MCP uses three participant roles:

- **Host** — the AI application that coordinates MCP connections and decides how capabilities are presented to the model or user.
- **Client** — a host component that maintains one connection to one MCP server.
- **Server** — a local or remote program that exposes capabilities and contextual information.

A host may create several clients, with each client maintaining an independent connection to a different server.

## Core server primitives

MCP servers can expose three main primitives:

- **Tools** — executable operations such as querying an API, modifying a file, or running a database command.
- **Resources** — contextual data such as file contents, database records, schemas, or API responses.
- **Prompts** — reusable interaction templates, instructions, or examples.

Clients discover capabilities through protocol methods rather than assuming that a fixed list is available. Servers can also notify clients when supported lists change.

Control normally differs by primitive:

- prompts are generally user-selected;
- resources are generally selected and managed by the application;
- tools are generally selected by the model under host and user policy.

The host remains responsible for consent, authorization, presentation, and approval.

## Client capabilities

Depending on negotiated support, servers may request capabilities from the client, including:

- model sampling through the host application;
- user elicitation for additional input or confirmation;
- structured logging and progress reporting.

These capabilities are negotiated and are not guaranteed to exist in every client or server implementation.

## Lifecycle and capability negotiation

MCP is stateful. A connection starts with initialization, protocol-version negotiation, identity exchange, and capability declaration. The client and server must use only mutually supported features and should terminate the connection when they cannot agree on a compatible protocol version.

Capability negotiation matters because MCP implementations may support different protocol versions, primitives, notifications, authorization methods, or optional client features.

## Data and transport layers

The MCP data layer uses JSON-RPC 2.0 messages for requests, responses, notifications, lifecycle operations, and primitive-specific methods.

The transport layer carries those messages. The principal transports are:

- **stdio** — direct standard-input and standard-output communication with a local server process;
- **Streamable HTTP** — HTTP-based communication for local or remote servers, with optional streaming and normal HTTP authentication mechanisms.

The same server concept can run locally or remotely. “MCP server” describes its protocol role, not its physical location.

For stdio servers, ordinary logging must not be written to stdout because stdout carries protocol messages. Use stderr or a file for diagnostics.

## MCP versus tool calling

[Tool calling](../tool-calling/) is the model-facing behavior of selecting an available operation and supplying arguments. MCP is one way an AI application can discover and expose external operations and context to that tool-calling layer.

A model can use tools without MCP, and an MCP server can expose more than executable tools because resources and prompts are also protocol primitives.

## MCP versus function calling

[Function calling](../function-calling/) usually describes a structured model API in which available functions are represented by schemas and the model returns a function name with arguments.

MCP operates at a wider application-integration boundary. It defines client-server discovery, lifecycle, capability negotiation, context primitives, invocation, notifications, and transports. An MCP host may translate discovered MCP tools into the function- or tool-calling format expected by a selected model provider.

## MCP versus Agent Skills

An [Agent Skill](../agent-skills/) packages procedural knowledge: when a workflow applies, which steps to follow, what evidence to collect, and where approvals are required.

MCP supplies capabilities and context. A skill may instruct an agent to use one or more MCP tools or resources, but the skill does not create the connection or grant permissions.

Example:

- an MCP server exposes `list_failed_jobs` and `retry_job`;
- a troubleshooting skill defines diagnosis, evidence collection, approval before retry, and post-action verification.

## MCP versus plugins

A [plugin](../plugins/) is a platform-specific installation and distribution package. It may contain skills, hooks, agents, commands, connector declarations, or MCP server configuration.

MCP is a protocol; a plugin is packaging. Installing a plugin that configures MCP creates separate trust boundaries for the plugin and the server.

## MCP versus ordinary APIs

An MCP server often wraps an ordinary API, local application, database, filesystem, or service. MCP does not replace the underlying API; it provides a standardized AI-facing integration layer around it.

Actual portability depends on protocol-version support, authentication, optional capabilities, tool schemas, host policies, and implementation quality.

## Security and trust boundaries

Connecting an MCP server expands the host's trust boundary. Review:

- who operates and maintains the server;
- whether it runs locally or remotely;
- what files, services, accounts, and credentials it can access;
- which tools can cause writes, commands, purchases, messages, or other side effects;
- what data is sent over the network;
- how authentication tokens are stored and scoped;
- whether tool outputs or resources contain untrusted instructions;
- whether the host asks for approval before consequential actions;
- how server updates, dependencies, and supply-chain risks are controlled.

Protocol compatibility is not a security endorsement. Hosts should apply least privilege, explicit approval gates, input and output validation, logging, and isolation according to the consequence of each capability.

Servers must implement real authorization for protected actions. Session identifiers are not authentication. Hosts must not rely only on tool descriptions or model judgment to enforce access control.

## Practical example

A database MCP server could expose:

- a resource containing the database schema;
- a prompt with safe query examples;
- a read-only query tool;
- an administrative mutation tool available only under a stricter permission policy.

The host discovers these capabilities, decides which to enable, presents allowed tool schemas to the model, obtains user approval where required, invokes the selected operation, and returns the result to the application workflow.

## Limitations

MCP does not automatically provide:

- safe or correct tools;
- trustworthy server output;
- compatible behavior across every host;
- authorization appropriate to the requested action;
- sandboxing of a local process;
- protection against prompt injection or malicious contextual data;
- correct model decisions about when or how to use a capability;
- stable compatibility when protocol versions or optional features differ.

Treat MCP as an interoperability protocol that still requires product-level security, permissions, validation, observability, and lifecycle management.

## References

- MCP documentation: https://modelcontextprotocol.io/docs/
- Architecture overview: https://modelcontextprotocol.io/docs/learn/architecture
- MCP specification: https://modelcontextprotocol.io/specification/
- Build an MCP server: https://modelcontextprotocol.io/docs/develop/build-server
- Security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- MCP GitHub organization: https://github.com/modelcontextprotocol
