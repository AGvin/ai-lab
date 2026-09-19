# Documentation Requirements

## Requirements

- Present x402 as an open internet-native payment protocol that uses HTTP `402 Payment Required` flows so clients, including applications and AI agents, can programmatically pay for resources and services.
- Treat the current released x402 v2 specification as normative authority and keep payment requirements/payloads, facilitator interfaces, schemes, transports, extensions, and security semantics aligned with that source.
- Record v2 as the current released research baseline without assuming future releases preserve identical schemas, headers, network identifiers, or extension behavior.
- Keep payment-network-specific schemes, facilitator services, SDK behavior, and provider integrations separate from the core protocol identity.
- Distinguish x402 from wider agent-commerce protocols and from other HTTP-402 payment specifications such as Machine Payments Protocol (MPP); similar transport primitives do not make them the same protocol.

## Validation

- Normative claims are traceable to the released x402 specification rather than only SDK behavior or ecosystem articles.
- x402 is not described as a generic agent framework, commerce lifecycle protocol, blockchain, token, or payment processor.
- Version-specific transport and scheme details are not presented as timeless.
