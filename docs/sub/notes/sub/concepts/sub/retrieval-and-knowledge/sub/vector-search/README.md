# Vector Search

Legacy residual retained for ANN evaluation, index/candidate tuning, representation-migration, and retrieval-lifecycle guidance that are intentionally outside the canonical Vector Search concept owner.

> **Migration note:** Vector-search identity, semantic-retrieval separation, exact-versus-approximate nearest-neighbor boundaries, index-family variability, metric/representation compatibility, score non-comparability, and separation from the canonical Embeddings and Vector Databases owners are already preserved in `docs/sub/concepts/sub/information-retrieval/sub/vector-search/`. The remaining material below stays here until its exact learning, retrieval-engineering, evaluation, vector-database, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## ANN evaluation residual

Measure approximate-nearest-neighbor behavior against an exact-search or otherwise appropriate reference on representative data when recall loss matters to the workload. Evaluate under the concrete vector distribution, metric, filters, candidate budget, concurrency, and hardware rather than selecting index settings from synthetic benchmarks alone.

Keep nearest-neighbor recall separate from application relevance or answer quality: recovering the mathematically nearest vectors does not prove that those items contain the evidence the downstream task needs.

## Index and candidate-tuning residual

Tune search/candidate breadth, index parameters, memory/storage use, latency, and target recall together. More aggressive approximation can reduce resource use or latency while missing useful neighbors; wider candidate exploration can improve recall while increasing computation and downstream reranking cost.

Use the similarity/distance metric and normalization contract required by the stored representation rather than choosing a metric by convention.

## Representation and lifecycle residual

Treat embedding/model version, vector dimension, preprocessing, normalization, and other representation-contract changes as index lifecycle events. Re-encode and rebuild or migrate stored vector state when compatibility is not explicitly preserved, and keep source/version identity sufficient to remove stale derived vectors.

Apply metadata and authorization constraints through their canonical filtering/access-control contracts, and account for deletion, replacement, versioning, and stale-index cleanup so obsolete vectors do not remain retrievable after source changes.

These evaluation, tuning, representation-migration, and lifecycle practices remain migration source material until their exact learning, retrieval-engineering, evaluation, vector-database, or decision-support owners are verified.
