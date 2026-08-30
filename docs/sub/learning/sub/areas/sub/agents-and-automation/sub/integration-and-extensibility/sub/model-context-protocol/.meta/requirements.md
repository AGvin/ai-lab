# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Context Protocol` and treat this node as the canonical learning entrypoint for understanding, using, building, testing, and operating MCP integrations.
- Begin with a plain-language explanation of what problem MCP solves and how hosts, clients, and servers relate, then link the reusable abstract MCP concept and formal MCP specification as separate owners.
- Distinguish MCP from ordinary application APIs, direct function/tool definitions, Agent Skills, and host-specific Plugins; explain how they can complement one another.
- Make the materialized `using-mcp/` and `building-mcp-servers/` children discoverable and explain what each reader will learn.
- Teach the host/client/server architecture as a practical mental model while making clear that exact cardinality, lifecycle, negotiation, and message semantics are versioned specification concerns rather than fixed learning facts.
- Teach the major capability classes conceptually: servers can expose contextual data/resources, reusable prompts, callable tools/actions, and version-dependent optional/extension capabilities; readers should verify the current specification before relying on an exact primitive/capability set.
- Explain the control boundary around MCP capabilities: discovery or protocol compatibility does not grant trust or authorization, and the host/application remains responsible for what reaches the model/user and which consequential actions are allowed.
- Teach local-versus-remote topology and transport choice as implementation concerns. Readers should understand process/network/trust-boundary consequences without freezing one current transport list as timeless learning truth.
- Teach capability/version negotiation and graceful degradation as interoperability practice: two implementations can both support MCP while differing in protocol version, capabilities/extensions, transport/auth assumptions, or feature maturity.
- Teach debugging by separating protocol/transport success from capability/business success. Readers should inspect connection/protocol errors, capability availability, operation errors, partial outcomes, side effects, logs/traces, and concrete retry/cancellation/idempotency behavior rather than treating a successful MCP exchange as proof that the task succeeded.
- Teach the stdio diagnostic principle where applicable: protocol-bearing stdout must not be polluted by ordinary diagnostic output; current exact transport requirements remain specification/implementation-owned.
- Teach MCP security as layered integration practice: review server/operator provenance, local/remote execution, data and credential scope, side-effecting tools, network destinations, untrusted returned/instruction-like content, approval boundaries, updates/dependencies, isolation, validation, observability, and revocation according to consequence.
- Distinguish authentication, authorization, user consent, and session/correlation state. A successful connection or identity exchange must not be taught as authorization for every resource/action/user, and obsolete historical session/lifecycle behavior must not be presented as current normative MCP behavior.
- Keep exact protocol-version rules, message/schema requirements, normative authorization behavior, and other conformance language sourced from the formal specification rather than frozen as independent learning truth.
- Keep concrete server/client/SDK/product identities and mutable compatibility/support facts with applicable catalog/platform/evidence owners.
- Preserve a clear continuation path for later selected MCP learning children such as architecture/lifecycle, primitives, clients, authorization/security, testing/debugging, and deployment/operations without materializing empty nodes now.

## Validation

- The entrypoint is useful to a first-time MCP learner while accurately routing advanced builders/operators.
- It does not duplicate the formal protocol specification or concrete implementation catalog.
- It does not preserve obsolete required initialize/session behavior as current MCP truth.
- Protocol compatibility/discovery is not presented as trust, permission, or business-operation success.
- Transferable architecture, interoperability, debugging, and security guidance remains useful without freezing mutable protocol or implementation details.
- Standard direct-child navigation includes only currently materialized learning children.
