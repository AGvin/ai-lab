# RLHF

Legacy residual retained for annotation-protocol design, reward-model validation, rollout/RL stability, proxy-versus-task evaluation, and rollback guidance that are intentionally outside the canonical Reinforcement Learning from Human Feedback concept owner.

> **Migration note:** RLHF identity, broader-than-InstructGPT definition, human-feedback form variability, SFT-versus-preference-signal distinction, explicit reward-model role, reward-model-versus-policy quality, PPO non-universality, KL/reference constraints, annotator-context dependence, reward hacking, and DPO separation are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/preference-optimization/sub/rlhf/`. The remaining material below stays here until its exact learning, post-training engineering, evaluation, governance, or experiment-management owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Annotation-protocol residual

Define comparison criteria, annotator instructions, prompt/context distribution, candidate-generation policy, tie/abstain behavior, quality-control checks, and disagreement handling before collecting feedback. Version the protocol together with the resulting preference data so later changes in policy behavior are not confused with changes in annotation rules.

Measure inter-annotator agreement and systematic subgroup/domain disagreements when those differences materially affect the reward signal. Include factual, safety, refusal-calibration, ambiguity, style, and adversarial cases according to the real acceptance criteria rather than collecting only easy helpfulness comparisons.

## Reward-model residual

Evaluate the reward model on held-out comparisons and on candidate distributions that differ from its training set before using it as a scalable optimization signal. Inspect calibration, domain gaps, preference shortcuts, and examples where higher predicted reward conflicts with task correctness or expert review.

Do not use the reward model as the sole evaluator of the policy it directly optimized when independent evidence is required; reward hacking and distribution shift can make proxy scores improve while underlying behavior worsens.

## RL stability and operations residual

Monitor policy reward, KL/reference divergence, entropy/diversity, value/policy losses where applicable, rollout quality, invalid/unsafe outputs, and target-task metrics during RL updates. Preserve checkpoints frequently enough to compare or roll back before proxy overoptimization or instability propagates through a long run.

Measure rollout generation cost, reward inference cost, communication/storage, wall-clock time, and accepted-result improvement together. RLHF can be operationally expensive even when the resulting policy checkpoint is no larger than its base.

## Evaluation and rollback residual

Evaluate the final policy against the SFT/reference baseline on preference win rate **and** factuality/grounding, safety, refusal calibration, diversity, retained capabilities, latency/cost, and other application criteria. Keep an independent acceptance set and a known-good previous policy for rollback.

These annotation, reward-model, RL stability, evaluation, and rollback practices remain migration source material until their exact learning, post-training engineering, evaluation, governance, or experiment-management owners are verified.
