# Documentation Requirements

## Requirements

- Use the reader-facing title `FlashAttention`.
- Define FlashAttention as an IO-aware family of algorithms/implementations for computing exact dense attention more efficiently by reorganizing computation into tiles that exploit faster on-chip memory and reduce reads/writes to slower high-bandwidth device memory.
- Use `exact` in the algorithmic sense that FlashAttention computes the same dense attention function rather than replacing it with an approximate attention mechanism; acknowledge that floating-point operation ordering, numerical format, kernel generation, and implementation details can still produce ordinary finite-precision differences.
- Distinguish FlashAttention from the attention mechanism itself. The model can retain the same attention architecture and trained weights while the runtime substitutes a different compatible kernel/algorithm for the attention computation.
- Explain that the main mechanism is IO reduction and memory-efficient tiling/online normalization rather than eliminating the full-attention pairwise computation. Do not claim that FlashAttention by itself changes the asymptotic arithmetic complexity of standard dense attention from quadratic in sequence length.
- Explain that avoiding materialization of the full attention score/probability matrix in device memory can substantially reduce intermediate-memory requirements, while model weights, activations, KV cache, outputs, and other runtime state retain their own memory costs.
- Distinguish FlashAttention from block-sparse or other approximate/sparse attention variants. A FlashAttention-family implementation can support additional sparse modes, but sparse approximation is not the defining property of exact FlashAttention.
- Distinguish FlashAttention from context extension. Lower attention memory/IO can make longer supported sequences more practical, but it does not change positional training/support or guarantee effective long-context behavior.
- Explain that FlashAttention generations and compatible vendor/runtime kernels can differ in work partitioning, supported hardware, data types, head dimensions, attention masks/features, backward-pass support, and other implementation details; the concept must not freeze one version's compatibility surface.
- Make clear that enabling a runtime flag, selecting a backend label, or installing a package does not prove that the intended FlashAttention kernel is used for every operation. Runtime dispatch/fallback and measured execution remain concrete implementation evidence.
- Do not encode fixed speedup multipliers. Realized latency, throughput, and memory benefits depend on sequence shape, batch size, head dimensions, mask/layout, numerical precision, hardware memory hierarchy, compiler/runtime, and competing bottlenecks.
- Keep concrete FlashAttention versions, build/install instructions, kernel feature matrices, GPU architecture requirements, runtime backend flags, benchmark results, and deployment recommendations with their applicable catalog/runtime, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for the exact-attention, IO-awareness, and implementation-generation boundaries when reader-facing rendering is activated.

## Validation

- The page does not describe FlashAttention as approximate attention, quantization, context extension, or a different trained model architecture.
- `Exact` is not interpreted as bitwise-identical output across every floating-point implementation/order.
- Reduced intermediate-memory traffic is not misrepresented as eliminating KV-cache, weight, activation, or total runtime memory.
- FlashAttention is not claimed to remove the quadratic pairwise arithmetic of standard dense attention by itself.
- One runtime flag, kernel version, GPU family, numerical format, or fixed speedup is not universalized.
- Legacy practical performance guidance is preserved only as workload-dependent implementation boundaries rather than canonical benchmark claims.
