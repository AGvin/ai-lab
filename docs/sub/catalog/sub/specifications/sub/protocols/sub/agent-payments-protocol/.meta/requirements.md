# Documentation Requirements

## Requirements

- Present Agent Payments Protocol (AP2) as an open protocol for securing agent-performed payment transactions through an explicit agent-authorization model, signed mandates/receipts, verification responsibilities, and dispute evidence.
- Treat the current released AP2 specification as normative authority and keep role, mandate, receipt, authorization, evidence, and flow details aligned with that source.
- Record the v0.2 released revision as the current research baseline without assuming future revisions retain identical structures or requirements.
- Distinguish AP2 from a commerce protocol such as Universal Commerce Protocol (UCP): AP2 supplies payment-authorization and transaction-security semantics and is designed to operate inside a wider commerce flow rather than defining the whole commerce lifecycle.
- Keep SDKs, sample implementations, payment-network integrations, and provider-specific services separate from the formal protocol identity.

## Validation

- Normative and version-sensitive claims are traceable to the current released AP2 specification or official repository.
- AP2 is not described as a generic commerce protocol, payment processor, wallet, or agent framework.
- Compatibility with UCP or other protocols is not presented as identity equivalence or replacement.

## Scoped original-source qualification — 2026-11-07

- AP2 is the payment authorization and verification protocol for agent-performed transactions, using agent roles, mandates and verifiable evidence for human-present or delegated autonomous flows. The current source describes v0.2; exact mandate structures, actors and supported cryptographic credentials depend on the released specification.
- AP2 is not a wallet, processor or general merchant checkout integration and does not make payments risk-free, dispute-free or globally compliant. Checkout, payment-handler settlement, human consent, merchant trust and privacy obligations must be assessed independently; broader commerce flows such as UCP are different protocol scopes.
- Verified primary source 1: https://ap2-protocol.org/ap2/specification/
- Verified primary source 2: https://github.com/google-agentic-commerce/AP2
- Bounded existing protocol/source qualification only; no payment, card data, agent transaction, issuer/processor verification, risk/compliance evaluation, full code/protocol-security audit, root-wide schema/cache/CI/render, clean pass or final gate.
