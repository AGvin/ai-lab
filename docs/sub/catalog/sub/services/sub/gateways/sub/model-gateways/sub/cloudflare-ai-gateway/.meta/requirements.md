# Documentation Requirements

## Requirements

- Identify Cloudflare AI Gateway as Cloudflare's producer-operated gateway for observing and controlling AI application traffic across Cloudflare and third-party model providers.
- Cover current logging/analytics, caching, rate limiting, retries, fallback, spend controls, provider/model access, and compatible API surfaces only when current Cloudflare documentation supports them.
- Keep Cloudflare Workers AI, Vectorize, Agents, and other Cloudflare AI products distinct even when they integrate with AI Gateway.
- Keep plans, provider coverage, unified-billing behavior, pricing, limits, and API compatibility freshness-sensitive.

## Validation

- AI Gateway is not represented as the owner of models it routes to.
- Hosted Cloudflare operation is not misclassified as self-managed gateway software.

## Scoped original-source qualification — 2026-11-06

- Cloudflare AI Gateway is a Cloudflare-operated intermediary for managing requests to Cloudflare Workers AI and external model providers. Current documentation covers request analytics, caching and configurable fixed/sliding-window rate limiting. Gateway logs can include submitted prompts, responses, providers and matched guardrail/DLP information; customers whose first gateway was created on or after 2026-09-24 have a different logs pricing/retention regime from legacy customers.
- Treat logging, access policy, request caching, key custody, Unified Billing and data-retention settings as security-critical; enable gateway authentication and review DLP/logging before forwarding confidential data. AI Gateway is not Workers AI inference or a model producer; per-plan limits and provider routing remain mutable.
- Verified first-party source 1: https://developers.cloudflare.com/ai-gateway/observability/logging/
- Verified first-party source 2: https://developers.cloudflare.com/ai-gateway/features/rate-limiting/
- Verified first-party source 3: https://developers.cloudflare.com/ai-gateway/reference/limits/
- This is a bounded identity/source qualification, not live service execution, credential review, security/privacy certification, complete license/ownership clearance, independent benchmarking, full schema/cache/CI/render, clean-group acceptance or final-delivery credit.
