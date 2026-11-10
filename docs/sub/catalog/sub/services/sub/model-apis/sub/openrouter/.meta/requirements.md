# Documentation Requirements

## Requirements

- Identify OpenRouter as OpenRouter, Inc.'s hosted Model API service for accessing and routing requests across third-party generative-model providers through a unified API surface.
- Preserve the effective data path: client to OpenRouter to the selected model provider. Make clear that provider identity, model terms, logging, retention, training, region, and availability remain independently material.
- Preserve useful legacy routing controls at a stable level: explicit provider selection/allowlisting, fallback control, data-collection restrictions, zero-data-retention routing, and price/latency/throughput preferences where currently supported.
- Preserve current OpenRouter privacy boundary: prompt/completion content logging and product-use permissions are configurable and off by default in current documentation, while request metadata is retained for service/reporting functions; selected providers have their own policies.
- Do not describe OpenRouter as gateway software installed by the user; it is a hosted intermediary/model API service.
- Keep exact model lists, provider availability, pricing, routing algorithms, account limits, regional options, and other mutable service state source-backed and time-scoped when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current official documentation, Privacy, and Terms references.

## Validation

- The page does not collapse OpenRouter with the downstream providers/models it routes to.
- ZDR or disabled OpenRouter logging is not misrepresented as a guarantee about every downstream provider unless provider routing satisfies that constraint.
- The profile remains a hosted service, not gateway software.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.

## Scoped original-source qualification — 2026-11-06

- OpenRouter is a hosted intermediary with provider-selection, fallback, privacy and routing controls. The client-to-OpenRouter-to-model-provider data path must remain explicit; a Zero Data Retention filter is a routing policy and does not by itself guarantee every downstream provider's compliance.
- Document model and provider identity, permitted endpoint, fallback and logging policies per request. Provider listings, live prices and default routes are mutable and do not prove model author provenance.
- Verified first-party source 1: https://openrouter.ai/docs/guides/routing/provider-selection
- Verified first-party source 2: https://openrouter.ai/privacy
- This accepts only the existing service identity and bounded source facts, not a full freshness/license/ownership audit, independent benchmarks, permission to process sensitive data, runtime tests, complete schema/cache/CI/render or final delivery.
