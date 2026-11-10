# Documentation Requirements

## Requirements

- Identify Zyte API as the producer-operated hosted web extraction and browser-assisted retrieval service supporting a REST extract endpoint, proxy transport, managed/automatic extraction, browser requests, CDP features and a documented Search API, distinct from the open-source Scrapy web-crawling framework.
- Preserve differences between Zyte API HTTP extraction, proxy-mode requests, browser automation and source-specific automatic extraction. Session consistency does not necessarily imply a persistent single browser/tab; first-party docs expressly distinguish session state and live CDP browser persistence.
- Do not collapse Zyte API into the separate Zyte Scrapy Cloud hosted spider-job platform, and do not create duplicate service records for every API usage mode or official SDK/MCP coding-agent add-on.
- Pin response type/structured output schema, browser versus proxy capabilities, geo restrictions, cookie sessions, supported targets, rate limits, anti-bot conditions and current pricing; do not assume a proxy path offers all regular REST features.
- Respect destination content policies, personal-data handling, authentication and storage; agentic web extraction needs lawful rights and explicit data retention assumptions.
- Keep Zyte API with first-party Zyte producer rather than making Scrapy framework, target websites or SDKs alternative producers.

- Preserve the live CDP connection boundary: each session has its own browser, IP and cookie jar; separate connections do not inherit that session state. Current CDP access requires a paid subscription or configured pay-as-you-go spending limit and business verification; keep these requirements freshness-sensitive.

## Validation

- Published first-party documentation demonstrates a live publicly documented hosted service rather than roadmap-only capability.
- Scope/feature maturity and site/data access limits are source-backed and not overgeneralized.
- Exact `produced-by` relation has an inverse `produces` link in the named vendor producer.

## Scoped original-source qualification — 2026-11-06

- Zyte API is the publisher-managed web-data extract service with REST /v1/extract, proxy mode, browser-rendered requests, automatic extraction, SERP Search API and CDP-managed browser connections. The official docs explicitly distinguish proxy mode feature limitations from REST and CDP, while hosted Zyte API remains distinct from Scrapy OSS and hosted Scrapy Cloud.
- Current CDP documentation requires a subscription or configured pay-as-you-go spending limit plus completed business verification; a CDP connection has its own browser, IP and cookie jar, and separate browser connections cannot resume its state. Automatic sessions in REST browser requests are different products/semantics. CDP metering uses navigation count or session duration and can continue after script disconnect unless the browser is explicitly terminated.
- Service-managed browser behavior is not universal permission to automate private sites; confirm customer business rights, legal content reuse, personal-data handling, target restrictions, proxy geography, costs and retention. Publisher anti-bot and extraction-success rates are not independently certified.
- Verified first-party source 1: https://docs.zyte.com/zyte-api/usage/index.html
- Verified first-party source 2: https://docs.zyte.com/zyte-api/usage/cdp.html
- Verified first-party source 3: https://docs.zyte.com/zyte-api/usage/proxy-mode.html
- Qualification is existing original-provider identity and bounded API/data/license/version claims, not live authenticated tests, full terms/privacy/legal review, independent benchmark, new entity/metadata, reader repair, global schema/cache/CI/render, clean pass, final-delivery gate or merge.
