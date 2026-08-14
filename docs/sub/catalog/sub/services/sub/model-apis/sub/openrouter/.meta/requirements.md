# Documentation Requirements

## Requirements

- Identify OpenRouter as OpenRouter, Inc.'s hosted Model API service for accessing and routing requests across third-party generative-model providers through a unified API surface.
- Preserve the effective data path: client to OpenRouter to the selected model provider. Make clear that provider identity, model terms, logging, retention, training, region, and availability remain independently material.
- Preserve useful legacy routing controls at a stable level: explicit provider selection/allowlisting, fallback control, data-collection restrictions, zero-data-retention routing, and price/latency/throughput preferences where currently supported.
- Preserve current OpenRouter privacy boundary: prompt/completion content logging and product-use permissions are configurable and off by default in current documentation, while request metadata is retained for service/reporting functions; selected providers have their own policies.
- Do not describe OpenRouter as gateway software installed by the user; it is a hosted intermediary/model API service.
- Keep exact model lists, provider availability, pricing, routing algorithms, account limits, regional options, and other mutable service state source-backed and time-scoped when expanded.
- Link the canonical OpenRouter, Inc. producer profile.
- Include current official documentation, Privacy, and Terms references.

## Validation

- The page does not collapse OpenRouter with the downstream providers/models it routes to.
- ZDR or disabled OpenRouter logging is not misrepresented as a guarantee about every downstream provider unless provider routing satisfies that constraint.
- The profile remains a hosted service, not gateway software.
- The producer relation resolves to OpenRouter, Inc.
