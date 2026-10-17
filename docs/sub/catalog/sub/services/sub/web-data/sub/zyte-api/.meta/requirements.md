# Documentation Requirements

## Requirements

- Identify Zyte API as the producer-operated hosted web extraction and browser-assisted retrieval service supporting a REST extract endpoint, proxy transport, managed/automatic extraction, browser requests, CDP features and a documented Search API, distinct from the open-source Scrapy web-crawling framework.
- Preserve differences between Zyte API HTTP extraction, proxy-mode requests, browser automation and source-specific automatic extraction. Session consistency does not necessarily imply a persistent single browser/tab; first-party docs expressly distinguish session state and live CDP browser persistence.
- Do not collapse Zyte API into the separate Zyte Scrapy Cloud hosted spider-job platform, and do not create duplicate service records for every API usage mode or official SDK/MCP coding-agent add-on.
- Pin response type/structured output schema, browser versus proxy capabilities, geo restrictions, cookie sessions, supported targets, rate limits, anti-bot conditions and current pricing; do not assume a proxy path offers all regular REST features.
- Respect destination content policies, personal-data handling, authentication and storage; agentic web extraction needs lawful rights and explicit data retention assumptions.
- Keep Zyte API with first-party Zyte producer rather than making Scrapy framework, target websites or SDKs alternative producers.

## Validation

- Published first-party documentation demonstrates a live publicly documented hosted service rather than roadmap-only capability.
- Scope/feature maturity and site/data access limits are source-backed and not overgeneralized.
- Exact `produced-by` relation has an inverse `produces` link in the named vendor producer.
