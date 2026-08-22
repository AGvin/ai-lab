# Documentation Requirements

## Requirements

- Present this scenario for a software engineer with a capable business laptop, strong development/Linux skills, but no useful local discrete GPU for model inference.
- Preserve compact CPU-local coding candidates such as Qwen2.5-Coder 3B/7B Instruct and Qwen3 8B for private bounded generation, explanation, test drafting, or edits; treat roughly 16–32 GB RAM and the legacy 32 GB laptop example only as planning context and measure the exact artifact/runtime/context.
- Preserve Gemma 4 E2B/E4B Instruct as bounded local multimodal helpers for screenshots, UI, documents, and coding context when the exact runtime supports those modalities; warn that preprocessing and long context can make CPU latency impractical.
- Preserve an on-demand GPU route for heavier work, with Qwen3 14B and Qwen3 30B-A3B as legacy evaluation candidates; require exact artifact, quantization/precision, GPU memory, runtime, context, startup/storage/shutdown behavior, and accepted-result quality to be measured.
- Treat an RTX 3090/4090-class 24 GB rental only as legacy capacity context, not a guaranteed fit or a purchase recommendation. Include forgotten-idle billing and resource lifecycle in the route comparison.
- Preserve hosted coding assistants/agents such as Cursor or Codex as a time-sensitive route when their source-code data path, usage limits, cost, and organization policy are acceptable.
- State that a generic CPU VPS may be slower than a modern laptop despite higher advertised vCPU/RAM; benchmark the exact host, model artifact, context, and runtime before committing to that route.
- Require code/repository data classification and complete client/provider path review; using a local model endpoint does not prove an IDE/agent client keeps all code local.
- Keep coding-task model rankings in `decision-guides/software-development/` and agent safeguards in `decision-guides/agents-and-automation/`; this scenario owns the no-local-GPU route trade-off, not generic coding-model selection.
- Escalate when CPU latency, context, agent-loop performance, multimodal needs, task quality, or accepted-result cost makes local CPU inference less useful than hosted or temporary-GPU alternatives.

## Validation

- The scenario is specifically constrained by absence of a useful local GPU and is distinct from the approved but not yet materialized local-GPU professional route.
- RAM/GPU classes, active parameters, or model loading are not treated as practical-fit guarantees.
- Cloud GPU lifecycle and idle billing are included in cost/operation trade-offs.
- Hosted coding routes include source-code data-path and policy constraints.
