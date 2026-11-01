# Documentation Requirements

## Requirements

- Present Browserbase as producer-operated browser infrastructure for programmatic and agent-driven web interaction, with remote isolated browser sessions as the primary product boundary.
- Cover session execution, browser automation connectivity, proxies/stealth, persistent context, debugging/session replay, and agent-oriented surfaces only where current first-party documentation supports them.
- Keep Browserbase distinct from web-data APIs whose primary identity is returning search/crawl/extraction data rather than exposing a managed browser runtime.
- Keep the separately installable Stagehand browser-agent SDK under the independent software identity `catalog/software/agent-frameworks/stagehand`; SDK use with managed sessions does not create an additional hosted Browserbase service.
- Do not split Browserbase Agents, Search, Fetch or other named hosted feature surfaces into separate service identities solely because they have individual names; reassess if an independently durable service emerges.
- Treat supported browser versions, regions, concurrency, proxy options, limits, and pricing as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Primary classification remains managed browser infrastructure.
- Feature breadth does not create duplicate service nodes.
- Producer provenance resolves to Browserbase, Inc.
