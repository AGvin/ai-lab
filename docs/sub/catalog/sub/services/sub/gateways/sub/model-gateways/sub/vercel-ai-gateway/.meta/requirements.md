# Documentation Requirements

## Requirements

- Identify Vercel AI Gateway as Vercel's producer-operated unified model gateway and API layer.
- Cover current model/provider access, routing/failover, protocol/API compatibility, usage visibility, BYOK or billing behavior, and AI SDK integration only when current Vercel documentation supports them.
- Distinguish Vercel AI Gateway from the installable Vercel AI SDK; integration between them does not make them one canonical product.
- Keep model counts, provider coverage, pricing, routing policy, protocol compatibility, and limits freshness-sensitive.

- Render the standard `entity-relations` block from validated current-entity relations with the canonical producer name and resolving link.

## Validation

- Vercel AI Gateway is not treated as an installable self-managed gateway.
- The gateway does not become the canonical owner of routed third-party models.

## Scoped original-source qualification — 2026-11-06

- Vercel AI Gateway is Vercel-operated model routing, provider selection and billing, distinct from installable Vercel AI SDK and the model authors whose requests are routed. Official BYOK documentation says the gateway first uses team-shared provider credentials, then can retry with Vercel system credentials on failure; this fallback is charged against the team's AI Gateway credit balance. Provider routing can use allowlists and an ordered fallback selection.
- Do not label BYOK as strict key-only billing or single-provider data residency without explicit fallback restrictions. Check provider selection, credential scope, costs and data path before sending confidential prompts; models, routing and prices remain service state.
- Verified first-party source 1: https://vercel.com/docs/ai-gateway/authentication-and-byok/byok
- Verified first-party source 2: https://vercel.com/docs/ai-gateway/models-and-providers/provider-options
- This is a bounded identity/source qualification, not live service execution, credential review, security/privacy certification, complete license/ownership clearance, independent benchmarking, full schema/cache/CI/render, clean-group acceptance or final-delivery credit.
