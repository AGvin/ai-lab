# Documentation Requirements

## Requirements

- Identify this checkpoint as the released AliceAI-T5 sparse encoder-decoder model with roughly 34.35B unique parameters and approximately 0.6B active-parameter naming semantics in the upstream identifier.
- Preserve first-party facts such as 512 experts per MoE layer, top-8 routing, 128K-context configuration, and `trust_remote_code` usage only at the exact model-card scope.
- Preserve its **base** text-to-text release identity; do not conflate it with an instruction-tuned Alice chat assistant or a generic decoder-only serving format.
- Treat the official `trust_remote_code=True` example as execution of model-supplied custom architecture code requiring security review and exact revision pinning.
- Treat benchmarks, quantizations, finetuning scripts, inference-provider availability, runtime compatibility, licenses and revisions as freshness-sensitive.

## Validation

- Membership resolves to AliceAI-T5.
