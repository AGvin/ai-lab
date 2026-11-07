# Documentation Requirements

## Requirements

- Present Universal Commerce Protocol (UCP) as an open interoperability protocol for agentic commerce that provides common commerce services, capabilities, schemas, discovery/profile conventions, and transport contracts across participating platforms and businesses.
- Treat the current released specification as normative authority. The current research baseline is release `v2026-08-25`; re-check the official announcements/specification before recording exact capability, schema, transport, or version details.
- Preserve UCP's date-versioned capability and service model without assuming every capability advances in lockstep with the protocol-level release.
- Distinguish UCP from Agent Payments Protocol (AP2): UCP owns the broader commerce interaction surface while AP2 provides compatible payment-authorization and transaction-security semantics.
- Describe compatibility with A2A, MCP, AP2, and payment handlers only where the current UCP specification explicitly supports it; do not present those protocols as interchangeable.
- Keep merchant/platform implementations and provider-specific commerce products separate from the formal protocol contract.

## Validation

- Normative and current-version claims are traceable to official UCP specification/release sources.
- UCP is not reduced to a payment protocol and is not described as replacing A2A, MCP, or AP2.
- Date-versioned details are treated as mutable rather than timeless architecture facts.

## Scoped original-source qualification — 2026-11-07

- Universal Commerce Protocol (UCP) is a release-versioned interoperable agentic-commerce contract for merchant/platform discovery, services, capabilities, checkout and payment-handling integrations. The first-party announcement identifies **v2026-08-25** as the released baseline, with separate dates and semantic versions for individual commerce capabilities.
- The later September 25 lodging/booking capability is explicitly a **draft**, not automatic evidence that every merchant or UCP v2026-08-25 deployment already supports lodging. Distinguish broad commerce lifecycle from compatible AP2 payment-mandate and authorization semantics, MCP tool transport, and A2A inter-agent messaging; independent implementations require distinct authentication and conformance checks.
- Verified first-party source 1: https://ucp.dev/documentation/announcements/
- Verified first-party source 2: https://ucp.dev/specification/overview
- Existing UCP specification/source gate only; no merchant enrollment, hotel booking, payment, consent, processor settlement, cross-protocol interoperability, complete legal/privacy/security audit, root-wide schema/cache/CI/render, clean pass or final gate.
