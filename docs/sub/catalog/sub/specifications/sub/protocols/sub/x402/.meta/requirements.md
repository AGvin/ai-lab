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

## Scoped original-source qualification — 2026-11-07

- x402 is the HTTP-402-based internet-native payment protocol for machine-readable payment requirements, payment proof and resource access. Its v2 specification and launch distinguish protocol-level message/extension semantics from optional facilitators, payment networks, clients and SDK implementations.
- An HTTP 402 response does not itself transfer funds or prove wallet ownership, merchant trust, finality, chargeback/dispute outcome or legally compliant handling. Network identifiers, schemes, facilitator requirements, wallet/session identity and developer integration behavior are version-, provider- and jurisdiction-dependent.
- Verified primary source 1: https://github.com/x402-foundation/x402/blob/main/specs/x402-specification-v2.md
- Verified primary source 2: https://x402.org/x402-v2-launch/
- Existing open payment-protocol identity/source accepted only; no wallet, balance transfer, settlement, facilitator security or production integration tested; complete legal/financial/security audit, whole-repository clean pass and final gates not performed.
