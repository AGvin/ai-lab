# Supervised Fine-Tuning

Legacy residual retained for dataset curation, template consistency, holdout evaluation, generalization checks, and post-training handoff guidance that are intentionally outside the canonical Supervised Fine-Tuning concept owner.

> **Migration note:** SFT identity, broader-than-instruction-tuning scope, terminology overlap, supervised-target versus preference-objective distinction, loss/template variability, parameter-update independence, target-quality risks, and non-guarantees for generalization/factuality/safety are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/fine-tuning/sub/supervised-fine-tuning/`. The remaining material below stays here until its exact learning, training-engineering, dataset-engineering, evaluation, or post-training-workflow owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Dataset-curation residual

Curate examples around the actual acceptance criteria rather than maximizing raw volume. Include representative ordinary cases, important edge/failure cases, desired uncertainty or abstention behavior, and the range of formats/domains the adapted model must handle.

Review generated or imported targets for correctness, hidden assumptions, unsafe patterns, duplicated/near-duplicated examples, leakage, secrets, and accidental personal data before treating them as supervised truth.

## Template and preprocessing residual

Keep the training representation compatible with the intended model/tokenizer/processor and inference path. For chat-style data, verify roles, separators, special tokens, masking, truncation, and chat-template behavior end to end; do not mix incompatible templates or preprocessing conventions silently.

Record enough preprocessing and dataset-version information to reproduce which tokens/targets actually contributed to training.

## Evaluation residual

Separate training, validation, and final holdout data sufficiently to detect memorization and near-duplicate leakage. Evaluate both the target behavior and important retained capabilities under representative inference settings rather than accepting low training loss as proof of success.

Inspect failures outside the supervised distribution and compare against the unchanged base or another relevant baseline under matched prompts, decoding, tools, and data when those factors affect the decision.

## Post-training handoff residual

If SFT precedes preference optimization or another post-training stage, preserve the exact SFT artifact, dataset lineage, evaluation baseline, and behavioral changes so later gains/regressions can be attributed to the correct stage. Preference optimization should not be used to hide a poorly curated supervised foundation.

These dataset, template, evaluation, and handoff practices remain migration source material until their exact learning, training-engineering, dataset-engineering, evaluation, or post-training-workflow owners are verified.
