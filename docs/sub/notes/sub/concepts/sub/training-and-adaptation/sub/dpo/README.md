# DPO

Legacy residual retained for preference-pair construction, reference/log-probability reproducibility, beta/configuration comparison, matched baseline evaluation, and regression monitoring guidance that are intentionally outside the canonical Direct Preference Optimization concept owner.

> **Migration note:** DPO identity, direct-objective versus common RLHF pipeline distinction, reward-semantics derivation, SFT separation, reference-policy role, beta/configuration boundary, preference-data limitations, later-variant separation, and non-guarantees for alignment/factuality/safety/generalization are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/preference-optimization/sub/dpo/`. The remaining material below stays here until its exact learning, post-training engineering, evaluation, governance, or experiment-management owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Preference-pair residual

Construct chosen/rejected pairs under explicit criteria and preserve the prompt/context, candidate-generation policy, annotator/judge source, tie/abstain handling, and data version. Weak rejected answers that are trivially bad can teach superficial separation, while factually incorrect but stylistically preferred chosen answers can optimize the wrong behavior.

Inspect pair balance, duplicate/near-duplicate prompts, candidate-length/style artifacts, safety/refusal cases, domain coverage, and factual correctness before interpreting pair count as data quality.

## Reference and reproducibility residual

Pin the exact policy/reference checkpoints, tokenizer or processor, chat template, preprocessing, sequence truncation, log-probability implementation, and cached reference values where used. A change in any of these can alter the effective DPO objective even when the preference pairs are unchanged.

Treat beta or related scaling values as implementation/formulation-specific experiment settings. Compare candidate configurations under matched data and evaluation instead of importing one default value across libraries or DPO-family variants.

## Matched-evaluation residual

Compare DPO against the unchanged/SFT reference and, when relevant to the decision, RLHF or another preference method using the same prompt distribution, candidate/evaluation criteria, and downstream acceptance metrics. Do not conclude that a simpler training loop is better if data, objectives, or evaluation differ materially.

Measure preference win rate together with factuality/grounding, safety, refusal calibration, diversity, retained capabilities, calibration, latency/cost, and target-task correctness. Keep an independent final acceptance set so repeated beta/data/variant selection does not overfit the evaluation protocol.

## Regression residual

Version preference data, policy/reference artifacts, trainer/objective variant, hyperparameters, and resulting checkpoint together. Keep a known-good prior policy and rollback path because direct preference optimization can change unrelated behavior even when pairwise preference accuracy improves.

These pair-construction, reproducibility, comparison, evaluation, and regression practices remain migration source material until their exact learning, post-training engineering, evaluation, governance, or experiment-management owners are verified.
