# Browserless

Browserless is a hosted browser-as-a-service platform for running remote headless-browser sessions through automation interfaces such as Playwright, Puppeteer and the Chrome DevTools Protocol, alongside rendering, scraping, screenshot and PDF APIs. Its focus is managed browser infrastructure rather than a general web-search service. [Browserless overview](https://docs.browserless.io/overview/intro).

## Execution and deployment boundaries

The provider supports shared managed cloud, private enterprise configurations and licensed/self-hosted modes; their features, capacity and data boundaries are not necessarily identical. Those delivery modes remain within the existing Browserless platform identity unless an independent product is established.

BrowserQL, MCP integrations and browser automation are adjacent interfaces, not new model identities. The independently documented managed **Agent Run API** at `/agent/run` is currently labeled **BETA** and Cloud-plan-only, and should not be treated as a stable feature in every self-hosted installation. [Agent Run lifecycle](https://docs.browserless.io/rest-apis/agent-run).

## Operational and access boundaries

Check browser version, supported automation protocols, token handling, concurrency, queue time, session storage, region, proxies, licensing and pricing. Remote browser access neither bypasses websites' authorization controls nor removes privacy, scraping-consent and terms obligations. Protect query-parameter tokens and any persisted profiles or screenshots.

## Relations

- Produced by [Browserless](../../../../../producers/sub/b/sub/browserless/).

## Official resources

- [Browserless](https://www.browserless.io/)
- [Platform documentation](https://docs.browserless.io/overview/intro)
- [Agent Run API (beta)](https://docs.browserless.io/rest-apis/agent-run)
