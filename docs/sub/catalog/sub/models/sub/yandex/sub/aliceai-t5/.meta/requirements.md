# Documentation Requirements

## Requirements

- Identify AliceAI-T5 as Yandex's open encoder-decoder language-model family using sparse mixture-of-experts layers and UL2-style text-to-text modeling.
- Link the released AliceAI-T5-35B-A0.6B checkpoint and preserve its unusual encoder-decoder/MoE identity rather than folding it into decoder-only LLM families.
- Treat architecture details, context length, benchmark claims, finetuning guidance, custom-code requirements, license, and runtime support as freshness-sensitive.

## Validation

- Producer provenance resolves to Yandex.
- Family identity is not conflated with the consumer Alice assistant/product.

## Mandatory Russian-origin security classification

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL**: Yandex is a Russia-based producer. The classification is unconditional and persists regardless of technical security verification, licensing or absence of a specific sanctions listing. Keep the resource only for research and threat monitoring. [Binding AI Lab policy](../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex official Moscow office](https://www.yandex.com/company/contacts/moscow).
- Place the warning immediately below the README title. Never shortlist or recommend this Yandex model or model index for adoption, production or sensitive workloads. If strictly studying downloaded artifacts, isolate the environment, control network egress, inspect and pin custom code, and never submit secrets or sensitive data to Yandex endpoints. No claim of checkpoint-specific malware is established by this policy.
