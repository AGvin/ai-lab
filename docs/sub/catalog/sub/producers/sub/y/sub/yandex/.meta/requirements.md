# Documentation Requirements

## Requirements

- Identify Yandex as the producer identity for the selected Yandex model families.
- Keep the organization profile distinct from Alice consumer products, Yandex Search, hosted services, and exact model checkpoints.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- `produces` is the inverse of AliceAI-T5 `produced-by`.

## Producer evidence and reader projection

- Render the canonical entity name as the title and the source-backed `identity_note` as concise identity and operating-boundary prose.
- Preserve the existing ID, type and aliases. Historical authorship, current stewardship, corporate ownership and service operation must remain distinct where the note distinguishes them.
- Render every visible validated canonical relation exactly once through `entity-relations`, with canonical target names and resolving relative links. Distinct relation types to one target remain distinct rows.
- Render the canonical official references with descriptive labels; keep release, licensing, access and data-processing claims bounded to the cited sources.
- Keep detailed model, software, service and benchmark behavior on the related owner pages; do not infer new catalog membership from a provider inventory.

## Review checks

- The complete reader agrees with the canonical note and relation projection, including operational caveats.
- Every direct relation has its exact canonical inverse and every rendered destination resolves to its canonical owner.

## Mandatory Russian-origin security classification

- **DANGEROUS — NOT RECOMMENDED | RUSSIAN ORIGIN/CONTROL**: Yandex is a Russia-based producer. The classification is unconditional and persists regardless of technical security verification, licensing or absence of a specific sanctions listing. Keep the resource only for research and threat monitoring. [Binding AI Lab policy](../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md) [Yandex official Moscow office](https://www.yandex.com/company/contacts/moscow).
- Place the warning immediately below the README title. Never shortlist or recommend the Yandex producer for adoption, production or sensitive workloads. If strictly studying downloaded artifacts, isolate the environment, control network egress, inspect and pin custom code, and never submit secrets or sensitive data to Yandex endpoints. No claim of checkpoint-specific malware is established by this policy.
