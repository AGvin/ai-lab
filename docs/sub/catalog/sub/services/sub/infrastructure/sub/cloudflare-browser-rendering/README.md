# Cloudflare Browser Run

Cloudflare Browser Run, formerly **Browser Rendering**, is Cloudflare's managed browser-execution and page-rendering service for Chromium automation, DevTools/CDP sessions, screenshots, HTML or accessibility extraction, PDF output and supported crawl/scrape workflows. The April 15, 2026 rename preserves the existing service identity rather than introducing a new product. [Browser Run documentation](https://developers.cloudflare.com/browser-run/).

## Browser infrastructure boundary

Browser Run provides managed browser sessions and Quick Actions, separately from Cloudflare Agents' agent runtime, Workers AI inference, AI Search ingestion/RAG, Vectorize and the Cloudflare CDN. Exposing browser tools to an agent is an integration into this service rather than proof all agent-browser tool features share its release lifecycle. Specific live-view, recording, WebMCP and integrated agent functionality may be beta. [Browser Run features](https://developers.cloudflare.com/browser-run/).

## Safety and operational constraints

Confirm account entitlement, supported REST/CDP methods, browser concurrency, session reuse, timeout and persistence, authentication scopes, pricing, regional routing, proxy/egress behavior and target-site permission. Browser execution and HTML extraction are not authorization to bypass access controls, scraping restrictions or privacy requirements. Protect session cookies, tokens, captured page contents and resulting screenshots.

## Relations

- Produced by [Cloudflare](../../../../../producers/sub/c/sub/cloudflare/).

## Official resources

- [Cloudflare Browser Run](https://developers.cloudflare.com/browser-run/)
- [Browser Rendering API](https://developers.cloudflare.com/api/resources/browser_rendering/)
- [2026 rename note](https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/)
