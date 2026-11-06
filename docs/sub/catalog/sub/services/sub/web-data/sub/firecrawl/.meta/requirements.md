# Documentation Requirements

## Requirements

- Present Firecrawl's hosted offering as a web-data service for scraping, crawling, searching, mapping, and extracting web content for AI applications and agents.
- Classify by primary product identity: browser execution, agent features, or browser-backed extraction do not by themselves move the hosted Firecrawl service into managed-browser infrastructure while its main contract remains web-content acquisition and transformation.
- Keep the hosted service identity distinct from independently self-hostable Firecrawl software/source distribution; materialize a software node only when the catalog needs that complete self-managed identity and can maintain the relationship without duplication.
- Treat endpoint inventory, supported formats, extraction behavior, crawl limits, pricing, and hosted capacity as freshness-sensitive.
- Do not create one service entity per API endpoint or feature.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Hosted Firecrawl is classified under web-data by primary job.
- Hosted and self-managed identities are not conflated.
- Producer provenance resolves to SideGuide Technologies, Inc.

## Scoped original-source qualification — 2026-11-06

- Firecrawl's hosted service documents a v2 live-web context API for scraping pages to Markdown/HTML, crawling site structures, searching, map discovery and additional agent/browser interaction surfaces. Its core hosted data-acquisition identity remains distinct from standalone self-hosted Firecrawl source distribution and from dedicated browser-session infrastructure.
- The publisher's current quickstart permits a limited initial scrape request without an account key and explicitly recommends an API key for higher rate limits; this does not mean all v2 endpoints are unrestricted or all hosted features are available in a local deployment. Endpoint, payload, output formats, model use, quotas, storage and regional routing depend on plan and version.
- Scraped data provenance, copyright, access authorization, private/sensitive information, deletion and token security require independent handling. Hosted access or apparent public reachability is not a universal license to crawl every site or redistribute its contents.
- Verified first-party source 1: https://docs.firecrawl.dev/introduction
- Verified first-party source 2: https://docs.firecrawl.dev/api-reference/introduction
- Accept only original provider service identity and source-scoped API, maturity, content-rights and data boundaries. No new metadata/entity, reader repair, authenticated traffic execution, complete freshness/legal/security/privacy audit, whole-repository schema/cache/CI/render, clean pass, final-delivery or merge credit.
