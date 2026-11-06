# Documentation Requirements

## Requirements

- Identify Replicate as Replicate, LLC's hosted service for running AI models through a web interface or API, including public/official models and user deployments.
- Preserve the distinction between Replicate service identity and the independent authors, publishers, licenses, and versions of models available through the service.
- Preserve the official-model stability boundary: current Replicate documentation describes official models as always-on, actively maintained, predictably priced, and exposed through stable input/output APIs; do not generalize that guarantee to every community or custom model.
- Explain that non-official/versioned models and deployments can have different lifecycle, version, warm/cold-start, pricing, and availability characteristics.
- Keep exact model inventory, pricing, hardware, limits, cold-start behavior, deployment options, and API details source-backed and time-scoped when expanded.
- Render the standard `entity-relations` block from validated current-entity relations.
- Include current official documentation, Privacy, and Terms references.

## Validation

- The page remains a hosted model/API service profile rather than a duplicate model catalog.
- Stable-API claims are scoped to the service surfaces for which Replicate currently makes that commitment.
- Third-party model identity and terms are not attributed to Replicate merely because Replicate hosts or routes the model.
- The `produces` / `produced-by` relation pair resolves consistently to Replicate, LLC.

## Scoped original-source qualification — 2026-11-06

- Replicate hosts official models and versioned/community or custom models. Official-model documentation specifically promises maintained warm availability, stable API input/output and predictable usage-based pricing for that subset; model versions for other listings can require explicit revision selection.
- Do not generalize official-model warm-start promises, model maintenance, licensing, or price/latency assumptions to every community or custom deployment.
- Verified first-party source 1: https://replicate.com/docs/topics/models/official-models
- Verified first-party source 2: https://replicate.com/docs/topics/models/versions
- This accepts only the existing service identity and bounded source facts, not a full freshness/license/ownership audit, independent benchmarks, permission to process sensitive data, runtime tests, complete schema/cache/CI/render or final delivery.
