# Documentation Requirements

## Requirements

- Identify Chroma as open-source vector-search and retrieval infrastructure, usable locally, embedded or in a self-hosted client/server deployment.
- Preserve primary ownership under self-managed `software/data-infrastructure/vector-search`, distinct from `services/data-infrastructure/vector-search/chroma-cloud` for the managed hosted Chroma Cloud product.
- Treat Python, TypeScript, Rust and other SDKs, embedded/client-server modes, and retrieval integrations as surfaces of the Chroma software identity rather than automatically creating peer entities.
- Use current official documentation and the Chroma repository for released search, storage, filtering, indexing, persistence, deployment, and API behavior.
- Keep cloud-only features, availability limits, throughput, benchmarks, retention, license, version-specific behavior, and support claims freshness-sensitive.
- Preserve Chroma producer provenance and its inverse `produces` relation.

## Validation

- Chroma open-source software is not conflated with Chroma Cloud managed service.
- Official references are current and match canonical entity metadata.
- Deployment modes and SDKs are not duplicated as independent products.
- Reciprocal producer relations resolve to the existing Chroma producer.
