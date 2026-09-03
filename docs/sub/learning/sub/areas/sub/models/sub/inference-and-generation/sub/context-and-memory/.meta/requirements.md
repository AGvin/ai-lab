# Documentation Requirements

## Requirements

- Present Context and Memory as the model-inference learning group for runtime state and capacity effects driven by active context, KV/cache reuse, reusable prefix/context computation, and memory allocation/headroom.
- Keep architectural long-context extension mechanisms with `architectures-and-representations/position-and-context/`; this group teaches runtime implications after a model/context mechanism exists.
- Distinguish in-request KV caching from cross-request context/prefix caching, response/semantic caching, persistent application/agent memory, and external retrieval. Similar words do not imply the same state, lifecycle, isolation, or correctness contract.
- Explain that the current materialized subset focuses on `kv-cache/` and `context-caching/` because both have source-backed legacy workload/capacity/operational teaching ready for migration.
- Do not imply that unmaterialized selected siblings `context-windows/` or `memory-management/` are absent from the logical architecture; standard navigation reflects only physical children.
- Treat usable context/concurrency as a joint workload/resource property. Advertised context limit, weight fit, or nominal memory capacity does not prove the accepted workload fits once cache/runtime/concurrency state is included.
- Keep runtime/provider-specific cache formats, APIs, thresholds, prices, retention, compatibility, and dated benchmark measurements with catalog/evidence owners.
- Link model-level memory optimization such as KV-cache quantization/compression/offload to `optimization-and-efficiency/memory-efficiency/` rather than duplicating advanced optimization depth here.

## Validation

- KV cache and context/prefix caching remain distinct mechanisms.
- Runtime context/memory teaching is not conflated with architectural context-extension methods or persistent application memory.
- Current navigation exposes only materialized selected children.
- Mutable provider/runtime cache facts remain evidence/catalog-owned.
