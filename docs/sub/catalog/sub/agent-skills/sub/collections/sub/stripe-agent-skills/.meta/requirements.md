# Documentation Requirements

## Requirements

- Identify Stripe Agent Skills as Stripe's official collection of reusable Agent Skills for building and integrating Stripe functionality with AI coding/agent harnesses.
- Preserve the collection boundary rather than creating a peer catalog entity for every individual Stripe skill by default.
- Keep Stripe's hosted MCP server, `@stripe/ai-sdk`, `@stripe/token-meter`, provider-specific plugin packages, Agent Plugins packaging, payment APIs, and Agentic Commerce Protocol as separate products/specifications or distribution surfaces rather than parts of the skill identity.
- Preserve current support for official plugin/install routes only while first-party documentation supports them; client-specific plugin commands, manual `npx skills` installation, skill inventory, and duplicated provider packaging are freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The collection remains a first-party Stripe skill collection, not a generic AI SDK or MCP product.
- Producer provenance resolves bidirectionally to Stripe.
