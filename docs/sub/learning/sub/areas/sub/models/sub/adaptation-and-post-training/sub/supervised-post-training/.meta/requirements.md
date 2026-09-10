# Documentation Requirements

## Requirements

- Teach Supervised Post-Training as supervised behavior adaptation after pretraining, with `instruction-tuning/` and `supervised-fine-tuning/` kept distinct where their dataset/task framing differs.
- Curate datasets around actual acceptance criteria, representative normal cases, important edge/failure cases, uncertainty/refusal behavior where required, and the formats/domains the adapted model must handle.
- Review imported, generated, or transformed targets for correctness, hidden assumptions, unsafe patterns, duplicates, leakage, secrets, personal data, and superficial shortcuts before treating them as supervised truth.
- Keep training representation aligned with the intended tokenizer/processor and inference interface, including roles, templates, special tokens, masking, truncation, and tool-call examples where relevant.
- Separate validation and final holdout evidence enough to detect memorization and near-duplicate leakage; evaluate retained base capabilities as well as target behavior.
- Preserve exact supervised-post-training artifacts and baselines before later preference/alignment stages so behavior changes can be attributed to the correct stage.

## Validation

- Low training loss is not treated as proof of generalization or factual reliability.
- Interface formatting is not treated as an authorization or security control.
- Dataset lineage and stage boundaries remain auditable.
