# Documentation Requirements

## Requirements

- Identify Cloudflare Browser Rendering as the independently operated Cloudflare account-scoped managed Chromium/browser execution and rendering API with DevTools/CDP browser sessions, page screenshots, HTML and accessibility/snapshot extraction, scraping, PDF generation and crawl workflows; the exact surface depends on API/product release.
- Distinguish managed browser session execution and rendered-content extraction from Cloudflare Workers AI model serving, Vectorize, AI Search, Agents durable execution, general CDN, web search engines and Browserbase/Browser Use Cloud third-party products.
- Preserve current official REST API endpoints and browser session/CDP connect/reuse capabilities only in their published support/lifecycle state. Browser tools exposed inside Cloudflare Agents may be beta and should remain a consumer integration/feature rather than being conflated with all of Browser Rendering's GA service lifecycle.
- Keep API token scope, account entitlements, billing, browser concurrency, session timeout, persisted storage, egress/proxy/anti-bot limitations, supported Chromium versions, region, automation restrictions, execution cost and data-handling controls current and first-party sourced; no credential values or permissive security defaults in examples.
- Do not assume every browser-rendered page can be legally or technically scraped, or that Browser Rendering bypasses target-site access controls. Respect permission and privacy constraints for any agent workflow.
- Keep the Cloudflare producer source-backed and reciprocal, with browser-execution service boundaries distinct from the independently published AI Search managed RAG service.

## Validation

- Browser Rendering has an official separately addressable API/service contract rather than being duplicated as a Cloudflare Agents convenience action.
- Core CDP/HTML/screenshot/scrape interfaces are correctly scoped; beta integrated tools do not imply universal lifecycle stability.
- Cloudflare producer `produces` inverses this exact service `produced-by` relation.
