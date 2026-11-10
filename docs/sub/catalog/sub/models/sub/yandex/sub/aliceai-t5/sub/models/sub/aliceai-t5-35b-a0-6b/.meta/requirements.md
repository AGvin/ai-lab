# Documentation Requirements

## Requirements

- Identify this checkpoint as the released AliceAI-T5 sparse encoder-decoder model with roughly 34.35B unique parameters and approximately 0.6B active-parameter naming semantics in the upstream identifier.
- Preserve first-party facts such as 512 experts per MoE layer, top-8 routing, 128K-context configuration, and `trust_remote_code` usage only at the exact model-card scope.
- Preserve its **base** text-to-text release identity; do not conflate it with an instruction-tuned Alice chat assistant or a generic decoder-only serving format.
- Treat the official `trust_remote_code=True` example as execution of model-supplied custom architecture code requiring security review and exact revision pinning.
- Treat benchmarks, quantizations, finetuning scripts, inference-provider availability, runtime compatibility, licenses and revisions as freshness-sensitive.

## Validation

- Membership resolves to AliceAI-T5.

## Mandatory Russian-origin security classification

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL**: Yandex is a Russia-based producer. The classification is unconditional and persists regardless of technical security verification, licensing or absence of a specific sanctions listing. Keep the resource only for research and threat monitoring. [Binding AI Lab policy](../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex official Moscow office](https://www.yandex.com/company/contacts/moscow).
- Place the warning immediately below the README title. Never shortlist or recommend this Yandex model or model index for adoption, production or sensitive workloads. If strictly studying downloaded artifacts, isolate the environment, control network egress, inspect and pin custom code, and never submit secrets or sensitive data to Yandex endpoints. No claim of checkpoint-specific malware is established by this policy.
