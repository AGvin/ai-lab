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

## Scoped original-source qualification — 2026-11-06

- Browserbase's first-party platform exposes remote cloud browser sessions through the Browser API, with separate Search, Fetch, Agents and Functions interfaces. Its Sessions API and CDP/Playwright connectivity identify managed browser infrastructure; Stagehand remains a distinct installable SDK, not the producer identity of browser hosting.
- Contexts may preserve authentication state across sessions, and debugging/session recordings can capture sensitive page contents, cookies and network traces. Protect API keys, stored contexts and replay access; verify project entitlements, privacy terms and target-site authorization rather than assuming these capabilities are universally accessible or safe.
- Browserbase documents Authenticated Fetch using previously saved Context cookies (2026-10-27 update), a separate noninteractive retrieval path rather than proof that a session itself can interact with every target. Agent/search/fetch functionality does not justify duplicate service or model identities.
- Verified first-party source 1: https://docs.browserbase.com/welcome/introduction
- Verified first-party source 2: https://www.browserbase.com/changelog
- Verified first-party source 3: https://www.browserbase.com/templates/getting-started-with-browserbase
- Acceptance scope: present hosted infrastructure identity and publisher-documented feature/version boundaries only. No model/runtime execution, complete freshness, independent security/legal review, rights clearance, root-wide schema/cache/CI/render, clean pass, final-delivery or merge credit.
