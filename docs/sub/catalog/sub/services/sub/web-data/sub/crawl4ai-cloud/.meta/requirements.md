# Documentation Requirements

## Requirements

- Identify **Crawl4AI Cloud** as a released, publicly documented, provider-operated **web-data API** distinct from the Apache-2.0 installable Crawl4AI Python library and customer-operated Docker server. Its core purpose is acquiring/transforming authorized web content into Markdown and structured extracted data for AI agents and RAG, so keep it under `catalog/services/web-data` rather than managed-browser infrastructure.
- Preserve source-backed lifecycle as **public live soft launch** based on [current first-party hosted Cloud site](https://api.crawl4ai.com/), [hosted API docs](https://api.crawl4ai.com/docs/), [original v0.9.5 repository README](https://github.com/unclecode/crawl4ai/blob/v0.9.5/README.md) and **2026-10-15** effective legal service Terms. Public live service is not a proven enterprise SLA, stability certification or availability guarantee; prices, plans and rate limits are subject to change during soft launch.
- Describe one service with `/scrape` (web to Markdown/HTML), `/extract` (typed JSON), `/search`, optional batch/queued jobs and MCP integration; keep `/serp` **Beta** and `/answer` **experimental** as endpoint maturity caveats, not distinct service or trained model identities.
- Distinguish provider-hosted browsers, proxies, model calls, remote queues, usage records and cached source material from local Crawl4AI code, CLI and customer Docker server. The repository's Apache-2.0 license does **not** control the Cloud service contract, stored user data, hosting pricing, third-party model providers or target-site rights.
- One legal operator **CONTEXT4AI PTE LTD** is named by [current first-party Terms](https://crawl4ai.com/legal/) and privacy policy. Do not conflate this corporation with the separately documented original Python-package author handle `Unclecode`; the legal relationship, corporate shareholders, voting control, indirect ownership and Russian stakes are **not independently verified**. Do not infer nationality or Tier 1/2 from names, domicile or speculation.
- The cloud API requires authorization credentials, and the user controls requested URLs and data. Review permitted target access, robots directives, website terms, intellectual property, privacy, URL/SSRF and sensitive-data transmission boundaries, idempotency/retries, service quotas, retention and deletion. The [Cloud privacy policy](https://crawl4ai.com/legal/) names infrastructure, model, proxy, identity and payment service providers; check current actual subprocessor list and data processing regions before sensitive use. Public documentation/claims are not independent certification or security review.
- Keep product limits, default caching, data residency/routing, backend behavior, endpoint availability, billing-credit rules and plan costs freshness-sensitive. Do not assert current open-now capacity or performance from vendor marketing, free-credit examples, benchmark comparisons or old closed-beta docs pages; authenticate and test an actual tenant before production adoption.
- Preserve one exact `produced-by` relation to the independently identified legal hosted-service operator and its reciprocal `produces` edge. Do not add `Unclecode produced-by` to the Cloud node or `CONTEXT4AI PTE LTD produces` the local Python package without independent authorship/ownership evidence.

## Validation

- One managed web-data service identity owns all documented Cloud endpoints; no duplicate local-software, hosted-browser infrastructure, individual endpoint or generic model identities.
- The original legal disclosure, Cloud API documentation and repository establish publication/operation, while live performance, provider controls, contract/ownership and universal endpoint stability remain unverified.
- Producer inverse resolves to `catalog/producers/c/context4ai-pte-ltd`; Cloud and local Crawl4AI remain separate catalog records.

## Scoped original-source qualification — 2026-11-06

- Crawl4AI Cloud is an operator-hosted web-data API distinct from the installable Apache-2.0 Crawl4AI library and self-managed server. Current hosted docs publish /scrape, /extract and /search, optional batch/queue, beta /serp introduced 2026-10-08 and experimental /answer; public soft-launch status does not establish enterprise SLA or stable semantics for all endpoints.
- The first-party Terms (effective 2026-10-15) identify CONTEXT4AI PTE LTD as legal operator of the hosted API and place source URL selection, site terms, privacy and intellectual-property rights on the caller. This legal operator must not be silently reattributed to the original local-code author handle or used to infer beneficial ownership or nationality.
- Cloud-model/proxy/infrastructure subprocessors, caching, request logs, retained source text, API tokens, prices, processing regions, quota and data deletion require current account and contract review. An Apache-2.0 license for local code is not automatically the Cloud API's commercial/data contract.
- Verified first-party source 1: https://api.crawl4ai.com/docs/
- Verified first-party source 2: https://api.crawl4ai.com/legal/
- Verified first-party source 3: https://api.crawl4ai.com/
- Accept only original provider service identity and source-scoped API, maturity, content-rights and data boundaries. No new metadata/entity, reader repair, authenticated traffic execution, complete freshness/legal/security/privacy audit, whole-repository schema/cache/CI/render, clean pass, final-delivery or merge credit.
