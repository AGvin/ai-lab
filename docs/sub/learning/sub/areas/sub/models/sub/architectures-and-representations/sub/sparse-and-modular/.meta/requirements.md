# Documentation Requirements

## Requirements

- Teach Sparse and Modular Architectures as model structures where only selected parameters, experts, routes, or modules participate in a given computation, distinct from model scale, quantization, pruning, or deployment mode.
- Explain total parameter count, active parameter count, resident memory, communication, and compute per token/request as distinct measurements when they affect workload fit.
- Keep architectural sparsity separate from compression-created sparsity: pruning can introduce sparse weights, but that does not make every pruned model equivalent to a routing/sparse-activation architecture.
- Materialize only source-backed selected children; this package materializes `mixture-of-experts/`.
- Keep concrete model topology, expert counts, routing policy, active/total parameter values, runtime support, and benchmark evidence source-backed with catalog/evidence owners.

## Validation

- Dense/sparse labels are not used as synonyms for small/large.
- Architecture alone is not treated as proof of speed, cost, hardware fit, or quality.
- Current navigation exposes only materialized selected children.
