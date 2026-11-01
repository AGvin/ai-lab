# Crawl4AI Cloud

[Crawl4AI Cloud](https://api.crawl4ai.com/) is a **provider-operated web-data API** for scraping, extracting and searching web content for LLM and agent workflows. It is separate from the open-source [Crawl4AI Python library](../../../../../software/sub/application-frameworks/sub/data-and-retrieval/sub/crawl4ai/), where customers run their own browsers and control their own infrastructure.

## Public soft launch and API boundary

The original [Cloud API docs](https://api.crawl4ai.com/docs/) describe authenticated JSON endpoints for `/scrape`, `/extract`, `/search`, batched crawling and MCP tools. `/serp` remains **Beta** and `/answer` **experimental**; these are features within the same hosted service, not independent canonical products. Current provider pages describe an **available soft launch**, not a verified production SLA. Endpoints, usage caps, models, regions, prices, credits and support terms can change.

The hosted operator runs browser sessions, proxies, queues and provider integrations and may retain request metadata or cached content. This differs materially from the local library's Apache-2.0 license and self-managed resource/secret boundaries. API keys, website access permissions, sensitive target URLs, regional processing, external model and proxy transfers, retention/deletion and billing caps need a direct contract and deployment review. Customer instructions or a search result never authorize bypassing target-site access controls.

## Operator and provenance

[CONTEXT4AI PTE LTD](../../../../../producers/sub/c/sub/context4ai-pte-ltd/) is identified as the service operator by [Crawl4AI's current legal terms](https://crawl4ai.com/legal/), effective 2026-10-15. This establishes the operator identity **only**; it does not prove legal ownership of the original software author **Unclecode** or independently establish current beneficial ownership, controlling shareholders, indirect Russia-linked stakes or service security certification.

## Official resources

- [Hosted Crawl4AI Cloud](https://api.crawl4ai.com/)
- [Cloud API reference](https://api.crawl4ai.com/docs/)
- [Cloud legal, privacy and acceptable-use terms](https://crawl4ai.com/legal/)
- [Original independently installable software](https://github.com/unclecode/crawl4ai)
