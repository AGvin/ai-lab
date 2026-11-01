# Documentation Requirements

## Requirements

- Identify Stagehand as Browserbase's independently packaged open-source SDK/framework for browser agents and AI-assisted browser automation, separate from Browserbase's managed browser infrastructure and from browser-agent alternatives such as Browser Use.
- Document original `act()`, `observe()`, and `extract()` browser primitives, with local Chrome/browser control or provider-managed Browserbase sessions as deployment choices. The TypeScript and Python SDKs are maintained in the original multi-language repository; additional language bindings are freshness-sensitive.
- Preserve the stable Stagehand 4.3 source-backed lifecycle: the original publisher announced version 4.3 on 2026-10-20, with published `@browserbasehq/stagehand` package version 4.3.0. Source metadata at the reviewed revision declares Node.js >=22.18.0 for the TypeScript SDK and Python >=3.11 for the Python SDK. Version and platform support may change.
- Keep Stagehand's browser-agent SDK distinct from the Browserbase cloud service, Stagehand API/server variants, browser instances, separate model providers, CLI/skills helpers, and upstream Playwright or other browser libraries; these are not automatic duplicate framework nodes.
- Distinguish self-managed local browser/model credentials from hosted browser sessions and remote model services. Model-provider tokens, session cookies, proxy use, browser control, rate limits, inference charges, storage, and regional/privacy terms must be assessed per deployment.
- Browser agents can encounter hostile website content, indirect prompt injection, insecure tool instructions, authenticated sessions and external side effects. Enforce permitted domains, scoped agent actions, explicit approvals for state changes, session isolation, audit and secret redaction. Do not equate selector-based password entry with proof that all sensitive page content is hidden from the model.
- Pin SDK, browser/driver, model, provider integration, selected server and underlying automation dependencies for reproducibility. Test critical flows and fallback behavior; `act()` self-healing and model-driven extraction are not correctness guarantees.
- Retain root MIT source license scope without assuming model, cloud, third-party website, data, proxy or embedded-asset rights are included. Do not claim verified agent security, performance, supply-chain or website authorization from upstream examples alone.
- Link the exact existing Browserbase, Inc. producer as one reciprocal `produced-by` / `produces` pair, without adding a duplicate legal producer.

## Validation

- The canonical entity is one software agent-framework identity, not a new managed service or independent model.
- Original Browserbase changelog, SDK package metadata and repository establish release, functionality, license and producer provenance.
- The producer inverse targets `catalog/software/agent-frameworks/stagehand` and Browserbase remains `catalog/services/infrastructure/browserbase`.
- Parent software index navigation resolves directly; runtime claims stay separated from verified source documentation.
