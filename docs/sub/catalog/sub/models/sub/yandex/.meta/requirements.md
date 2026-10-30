# Documentation Requirements

## Requirements

- Identify this node as the Yandex model-domain view rather than a duplicate organization profile.
- Link current material Yandex model families selected by catalog intake, including AliceAI-T5 and the separately pretrained AliceAI Foundation.
- Keep hosted Alice/Yandex product experiences, search products, APIs, quantized derivatives, and third-party deployments separate from model identity.
- Treat family membership and exact release inventory as freshness-sensitive.

## Validation

- Canonical producer provenance remains under `catalog/producers/y/yandex`.

## Mandatory Russian-origin security classification

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL**: Yandex is a Russia-based producer. The classification is unconditional and persists regardless of technical security verification, licensing or absence of a specific sanctions listing. Keep the resource only for research and threat monitoring. [Binding AI Lab policy](../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex official Moscow office](https://www.yandex.com/company/contacts/moscow).
- Place the warning immediately below the README title. Never shortlist or recommend this Yandex model or model index for adoption, production or sensitive workloads. If strictly studying downloaded artifacts, isolate the environment, control network egress, inspect and pin custom code, and never submit secrets or sensitive data to Yandex endpoints. No claim of checkpoint-specific malware is established by this policy.

- Include the separately released experimental [AliceAI Foundation base checkpoint](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base) without claiming it is a variant of AliceAI-T5. Preserve the existing **DANGEROUS — NOT RECOMMENDED** Yandex Tier 1 warning and do not recommend either family for adoption.
