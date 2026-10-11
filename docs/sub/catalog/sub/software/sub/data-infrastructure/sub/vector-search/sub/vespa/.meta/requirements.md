# Documentation Requirements

## Requirements

- Identify Vespa as a released open-source distributed AI search and serving platform, with search/retrieval over vectors, text, tensors, and structured data plus learned ranking/inference at query time.
- Keep Vespa's primary role under self-managed `software/data-infrastructure/vector-search` while acknowledging its broader serving and ranking capabilities. Avoid splitting vector search and ranking features into duplicate canonical products.
- Distinguish self-managed Vespa from independently operated Vespa Cloud; local/Docker/Kubernetes modes do not automatically imply separate product identities.
- Retain Vespa.ai as current producer and preserve the project's earlier Yahoo-origin history only as historical provenance; the independent Vespa.ai spin-out was announced in 2023.
- Treat release cadence/version, distribution architecture, supported ranking models, scale and performance, self-hosting capabilities, supported runtimes, tenancy and deployment requirements as freshness-sensitive.
- Source performance claims to explicit official or independent evaluations with matched hardware, dataset, query mix, cluster size, replication, and ranking configuration.

## Validation

- The independently released self-managed/OSS identity is not conflated with managed provider services or ancillary SDK/CLI features.
- Current source references and producer provenance resolve to the correct canonical owners.
- Mutable performance, service feature, and compatibility claims remain scoped to verifiable release/workload configurations.
- Reciprocal producer relation is present and matches the entity identity.
