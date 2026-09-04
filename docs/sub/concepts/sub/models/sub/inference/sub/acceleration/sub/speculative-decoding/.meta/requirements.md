# Documentation Requirements

## Requirements

- Use the reader-facing title `Speculative Decoding`.
- Define speculative decoding as an inference-time acceleration technique for autoregressive generation in which a cheaper proposal/draft process generates one or more candidate continuation tokens and the target model evaluates those candidates so several output tokens can potentially be accepted per sequential target-model step.
- Make the target model authoritative for the final decoding distribution or output rule. The draft/proposal path accelerates candidate production; it does not replace the target model's verification/correction contract.
- Explain that exact-distribution speculative sampling uses an acceptance/rejection and correction procedure designed so the resulting samples follow the target model distribution within the algorithm/numerical assumptions; do not reduce the method to accepting tokens only when draft and target argmax tokens match.
- Distinguish stochastic speculative sampling from greedy/deterministic speculative decoding variants. Their acceptance/correction logic and output-equivalence guarantees differ and must be stated for the concrete algorithm rather than generalized from one variant.
- Present a smaller draft model as a common proposal mechanism, while acknowledging alternative proposal sources such as prompt lookup, n-gram predictors, early-exit/self-drafting, multi-token heads, or other cheaper approximations; one separate small model is not a universal requirement.
- Distinguish speculative decoding from model routing, fallback, cascading, or ensemble selection. Routing chooses which model/path provides an answer; speculative decoding uses proposal work to accelerate generation whose final decoding semantics remain governed by the target path.
- Explain that speedup depends on proposal cost, target verification cost, accepted-token/run length, batch/concurrency, sequence shape, hardware parallelism, memory pressure, model-loading/residency overhead, and runtime implementation. Acceptance rate alone is not an end-to-end performance metric.
- Make clear that loading or retaining an additional draft model/state can increase memory and startup cost, and that a weak or expensive proposal path can provide little or negative benefit.
- Distinguish speculative decoding from quantization/compression. The draft and target may independently use different representations or optimizations, but speculative decoding is the proposal/verification algorithm rather than a numerical compression technique.
- Explain that preserving the target decoding distribution does not imply identical wall-clock scheduling, floating-point execution order, random-number implementation, or byte-identical outputs across different runtimes/seeds; guarantees must be scoped to the concrete algorithm and determinism contract.
- Keep concrete draft-model choices, acceptance thresholds/algorithms, prompt-lookup settings, multi-token-head implementations, runtime flags, memory footprints, benchmark speedups, and deployment/model-selection recommendations with their applicable catalog/runtime, evidence, engineering, or decision owners.
- Use the canonical entity references as research inputs for target-distribution preservation and proposal/verification boundaries when reader-facing rendering is activated.

## Validation

- The page does not describe the draft/proposal model as the final authority for generated output.
- Speculative decoding is not equated with routing, fallback, ensembles, quantization, or ordinary batching.
- A separate smaller draft model is not presented as the only valid proposal mechanism.
- Exact-distribution sampling guarantees are not incorrectly generalized to every greedy or heuristic speculative variant.
- Acceptance rate is not treated as a complete latency/throughput metric, and no fixed speedup multiplier is universalized.
- Distribution preservation is not presented as a universal bitwise-determinism guarantee across runtimes/hardware.
- Legacy draft-selection/performance advice is preserved only as implementation-dependent evaluation boundaries rather than canonical recommendations.
