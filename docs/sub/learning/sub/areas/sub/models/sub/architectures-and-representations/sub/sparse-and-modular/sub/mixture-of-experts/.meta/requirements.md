# Documentation Requirements

## Requirements

- Teach Mixture of Experts as a modular architecture that routes each token/example or computation unit through a subset of expert parameters rather than activating every expert on every step.
- Record and interpret **total** and **active** parameter counts separately for concrete MoE models because they answer different storage/capacity versus per-step-compute questions.
- Explain that routing, expert parallelism, communication, memory residency, load balance, kernel/runtime implementation, batch/concurrency, and hardware topology can materially affect realized performance.
- Do not infer that MoE is automatically faster, cheaper, smaller in memory, locally practical, higher quality, or frontier merely because fewer parameters are active per token.
- Keep exact expert counts, router details, active/total parameter values, runtime compatibility, hardware behavior, and benchmark measurements source-backed with catalog/evidence owners.

## Validation

- Active parameter count is not substituted for total parameter count when discussing storage/residency/model size.
- Total parameter count is not substituted for active compute when discussing per-token execution.
- Architecture labels do not replace representative workload evidence.
