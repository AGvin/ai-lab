# Documentation Requirements

## Requirements

- Identify Baseten Model APIs as Baseten's managed hosted API surface for accessing supported public models without managing a custom deployment.
- Keep Model APIs distinct from custom Truss deployments, dedicated deployment configuration, and other Baseten infrastructure products.
- Keep third-party model identity, licensing, lifecycle, and intrinsic capabilities with their model owners rather than attributing them to Baseten because the service hosts them.
- Treat model inventory, API compatibility, pricing, quotas, latency/throughput, regions, and other hosted-service state as mutable facts requiring current verification.
- Render the standard `entity-relations` block from validated current-entity relations and preserve Baseten Labs, Inc. as the producer.

## Validation

- The page remains a hosted-service profile rather than a duplicate model catalog.
- Custom deployment features are not generalized into Model APIs behavior without source support.
- The `produces` / `produced-by` relation pair resolves consistently to Baseten Labs, Inc.

## Scoped original-source qualification — 2026-11-06

- Baseten Model APIs is a managed hosted model-access surface for supported public models, separate from user-managed Truss/custom model deployments and broader Baseten infrastructure. First-party documentation provides model-specific entry points and rate-limit/deprecation guidance. Hosted third-party model names and licenses remain with their upstream model authors.
- Do not project custom Truss deployment isolation, hardware control, model support, free limits, latency or exact rates onto the hosted Model APIs without checking the selected model and account.
- Verified first-party source 1: https://docs.baseten.co/inference/model-apis/overview
- Verified first-party source 2: https://docs.baseten.co/inference/model-apis/deprecation
- This bounded source qualification does not establish a full freshness audit, independently validated runtime, legal/model-license clearance, current pricing or entitlements, global schema/cache/CI/render or final publication.
