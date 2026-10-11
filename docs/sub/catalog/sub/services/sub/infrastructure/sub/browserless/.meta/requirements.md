# Documentation Requirements

## Requirements

- Identify Browserless as a producer-operated managed browser-as-a-service platform providing remote headless-browser sessions for automated applications and agents, with cloud Playwright/Puppeteer WebSocket/CDP connectivity and REST/GraphQL endpoints for rendering, scraping, screenshots and PDFs.
- Preserve **one primary Browserless platform identity** across shared cloud, dedicated private managed deployments, self-hosted open-source Docker and separately licensed self-hosted enterprise deployments. Self-hosting is a delivery/deployment boundary, not by itself proof of an independent software product catalog identity; some capabilities differ by license and deployment.
- Distinguish raw remote browser execution and scripts from the provider's separately documented AI browser-agent API, AI/MCP integration surfaces, and BrowserQL. The `/agent/run` managed AI agent interface is explicitly **BETA**, cloud-plan-only in the current documentation; do not imply that its interface, availability or schema is stable or universal.
- Keep Browserless distinct from Browserbase's browser infrastructure, Browser Use Cloud's fully hosted agent tasks and Cloudflare Browser Rendering's account-scoped CDP/content extraction service even where the supported automation protocols overlap.
- Treat concurrency, browser versions, region, session retention, authentication/proxies, enterprise license, queues, agent-run quotas, pricing, security and access privileges as plan/version-sensitive; consider compliance with target websites and secure handling of API tokens and persistent session profiles.
- Preserve the Browserless producer identity and exact reciprocal `produced-by`/`produces` relationship; do not infer legal incorporation name from marketing without first-party proof.

## Validation

- Official first-party documentation substantiates hosted managed browsers and distinct self-host deployment modes.
- The current first-party Agent Run documentation labels the managed agent interface BETA rather than stable.
- Exact producer inverse resolves to `catalog/producers/b/browserless`.
