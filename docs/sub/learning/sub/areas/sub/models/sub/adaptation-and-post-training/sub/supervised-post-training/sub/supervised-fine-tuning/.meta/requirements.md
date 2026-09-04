# Documentation Requirements

## Requirements

- Teach Supervised Fine-Tuning as supervised post-training over target examples, broader than instruction-only datasets and distinct from preference objectives.
- Curate examples around acceptance criteria, including ordinary cases, important edge/failure cases, uncertainty or abstention where needed, and relevant formats/domains.
- Review generated/imported targets for correctness, duplicated examples, leakage, secrets, accidental personal data, unsafe patterns, and hidden assumptions before training.
- Keep tokenizer/processor, chat-template, role/separator, masking, truncation, and preprocessing behavior aligned with the intended inference path and record enough preprocessing detail to reproduce effective training targets.
- Separate training, validation, and final holdout data sufficiently to detect memorization and near-duplicate leakage; evaluate target behavior and retained capabilities under representative inference settings.
- Preserve the exact SFT artifact, dataset lineage, baseline, and evaluation evidence before handing off to preference optimization or another later stage.

## Validation

- Training loss is not treated as a substitute for held-out task evidence.
- SFT is not conflated with preference optimization.
- Post-training handoff preserves stage attribution.
