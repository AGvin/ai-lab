# Documentation Requirements

## Requirements

- Present Machine Payments Protocol (MPP) as a protocol for machine/agent payments to web and API services, extensible across payment methods and service integrations.
- Keep current relays, SDK/harness integrations, identity support, EVM/x402 compatibility, service integrations, and payment-method details as protocol capabilities/evolution rather than peer entities.
- Treat protocol/SDK versions, supported payment methods/chains, integrations, live endpoints, and release status as freshness-sensitive.

## Validation

- MPP remains a protocol/specification rather than a hosted payment service identity.
- Current protocol claims resolve to authoritative MPP documentation.

## Scoped original-source qualification — 2026-11-07

- Machine Payments Protocol (MPP) is an agent/machine-to-service payment exchange protocol. First-party documentation distinguishes request-level payment negotiation from ecosystem integrations such as relays, SDK hooks, generic EVM payment methods, x402 compatibility and paid API service implementations.
- Protocol support and SDK convenience do not guarantee that an agent has authorization to spend, that a payment is reversible or disputes are covered, or that every service implements every chain, currency, account policy or settlement path. Relays and third-party payment processors are separate parties with their own security and financial obligations.
- Verified first-party source 1: https://mpp.dev/
- Verified first-party source 2: https://mpp.dev/blog
- Existing MPP source/identity only; no wallet/key/token material supplied, no payment executed, no provider account, regulatory/PCI/security verification, repository-wide schema/cache/CI/render, clean pass or final gate.
