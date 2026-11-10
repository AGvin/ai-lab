# Documentation Requirements

## Requirements

- Present Agentic Commerce Protocol (ACP) as an open specification for programmatic commerce flows among buyers, AI agents, sellers, and payment providers.
- Cover Agentic Checkout, delegated payment, capability negotiation, extensions, trust boundaries, and current protocol versioning only from authoritative ACP documentation.
- Record that current official material identifies Stripe and OpenAI as ACP's original developers without forcing a single-producer relation into the specification identity.
- Treat active API-version headers, schema fields, extensions, payment-handler revisions, participating platforms/providers, and implementation status as freshness-sensitive.

## Validation

- ACP remains a protocol/specification rather than a commerce service or agent framework.
- Version-sensitive examples match the current released ACP documentation when rendered.

## Scoped original-source qualification — 2026-11-07

- Agentic Commerce Protocol (ACP) is an open seller/agent-facing commerce integration contract developed by Stripe and OpenAI, not the separately named Agent Client Protocol or a guaranteed payment settlement service. It describes merchant-controlled checkout sessions, inventory/pricing/tax/fulfillment state, buyer-agent interactions, supported payment handler handoff and protocol extensions.
- The official Checkout API documentation uses merchant-hosted authenticated endpoints with versioned checkout/capability metadata. An ACP checkout implementation does not cause automatic product listing on all AI platforms, bypass merchant approval, confer PCI compliance, or verify a payment credential's consent, issuer trust, fraud risk or successful capture. Product availability and payment integrations remain implementation-specific.
- Verified first-party source 1: https://www.agenticcommerce.dev/
- Verified first-party source 2: https://www.agenticcommerce.dev/docs/reference/checkout
- Verified first-party source 3: https://www.agenticcommerce.dev/docs/changelog
- Existing distinct ACP original-source identity only; no checkout request, card data, financial authorization, live merchant API, contract/privacy/security/legal certification, root-wide schema/cache/CI/render, clean/final or merge gate.
