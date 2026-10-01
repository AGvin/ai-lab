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
