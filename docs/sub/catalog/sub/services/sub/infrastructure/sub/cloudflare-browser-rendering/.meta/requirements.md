# Documentation Requirements

## Requirements

- Identify Cloudflare Browser Run as the independently operated Cloudflare account-scoped managed Chromium/browser execution and rendering API with DevTools/CDP browser sessions, page screenshots, HTML and accessibility/snapshot extraction, scraping, PDF generation and crawl workflows; the exact surface depends on API/product release.
- Distinguish managed browser session execution and rendered-content extraction from Cloudflare Workers AI model serving, Vectorize, AI Search, Agents durable execution, general CDN, web search engines and Browserbase/Browser Use Cloud third-party products.
- Preserve current official REST API endpoints and browser session/CDP connect/reuse capabilities only in their published support/lifecycle state. Browser tools exposed inside Cloudflare Agents may be beta and should remain a consumer integration/feature rather than being conflated with all of Browser Run's GA service lifecycle.
- Keep API token scope, account entitlements, billing, browser concurrency, session timeout, persisted storage, egress/proxy/anti-bot limitations, supported Chromium versions, region, automation restrictions, execution cost and data-handling controls current and first-party sourced; no credential values or permissive security defaults in examples.
- Do not assume every browser-rendered page can be legally or technically scraped, or that Browser Run bypasses target-site access controls. Respect permission and privacy constraints for any agent workflow.
- Keep the Cloudflare producer source-backed and reciprocal, with browser-execution service boundaries distinct from the independently published AI Search managed RAG service.

- Preserve Browser Rendering and Cloudflare Browser Rendering as former-name aliases of Browser Run; this naming change does not establish an additional service.

## Validation

- Browser Run has an official separately addressable API/service contract rather than being duplicated as a Cloudflare Agents convenience action.
- Core CDP/HTML/screenshot/scrape interfaces are correctly scoped; beta integrated tools do not imply universal lifecycle stability.
- Cloudflare producer `produces` inverses this exact service `produced-by` relation.

## Scoped original-source qualification — 2026-11-06

- Cloudflare renamed Browser Rendering to Browser Run on April 15, 2026, without creating a second product. The official docs distinguish Quick Actions for stateless screenshots, PDF, Markdown or extraction tasks from Browser Sessions controlled via Puppeteer, Playwright, CDP and other supported browser integrations.
- Browser Run's execution and account-scope restrictions are distinct from Cloudflare Agents and Workers AI. Browser concurrency, per-plan usage, session controls, target-site terms, data privacy, authentication, network egress and anti-bot behavior remain scenario-dependent; browser tooling is not a right to bypass access restrictions.
- Verified first-party source 1: https://developers.cloudflare.com/browser-run/
- Verified first-party source 2: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/
- Scope: originally documented hosted service identity and lifecycle/usage limits only; not a complete freshness/legal/security review, independent runtime execution, full schema/cache/CI/render, clean pass or final delivery gate.
