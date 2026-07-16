# Model Context Protocol (MCP)

Model Context Protocol is an open protocol for connecting AI applications to external tools, contextual data, reusable prompts, and related capabilities through a consistent client-server interface.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

## MCP versus tool calling

[Tool calling](../tool-calling/) is the model-facing behavior of selecting an available operation and supplying arguments. MCP is one way an AI application can discover and expose external operations and context to that tool-calling layer.

A model can use tools without MCP, and an MCP server can expose more than executable tools because resources and prompts are also protocol primitives.

## MCP versus function calling

[Function calling](../function-calling/) usually describes a structured model API in which available functions are represented by schemas and the model returns a function name with arguments.

MCP operates at a wider application-integration boundary. It defines client-server discovery, lifecycle, capability negotiation, context primitives, invocation, notifications, and transports. An MCP host may translate discovered MCP tools into the function- or tool-calling format expected by a selected model provider.

## MCP versus ordinary APIs and plugins

An MCP server often wraps an ordinary API, local application, database, filesystem, or service. MCP does not replace the underlying API; it provides a standardized AI-facing integration layer around it.

Compared with a platform-specific plugin system, MCP is intended to be reusable across compatible hosts. Actual portability still depends on protocol-version support, authentication, optional capabilities, tool schemas, host policies, and implementation quality.

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
- MCP GitHub organization: https://github.com/modelcontextprotocol
