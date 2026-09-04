# Documentation Requirements

## Requirements

- Teach Vector Search as exact or approximate nearest-neighbor retrieval over a defined representation contract, not as a synonym for semantic relevance or a complete retrieval system.
- Measure approximate-search behavior against an exact or otherwise appropriate reference when neighbor recall matters, using representative vectors, metrics, filters, candidate budgets, concurrency, and hardware.
- Keep nearest-neighbor recall separate from application relevance and final task quality; mathematically nearest vectors may still lack required evidence.
- Tune candidate breadth, index parameters, memory/storage use, latency, and target recall together rather than optimizing one dimension in isolation.
- Use the similarity/distance metric and normalization contract required by the stored representation rather than choosing by convention.
- Treat embedding/model version, dimension, preprocessing, normalization, and representation changes as index-lifecycle events; rebuild or migrate derived vector state when compatibility is not preserved.
- Preserve source/version identity and explicit deletion/replacement paths so stale vectors do not remain retrievable after source changes.
- Materialize and link `vector-indexes-and-stores/` for index/store and operational ownership teaching.

## Validation

- ANN recall is not treated as application relevance or answer quality.
- Representation changes trigger explicit compatibility/rebuild decisions.
- Obsolete source data does not remain silently reachable through stale vectors.
