# Preference Optimization

Legacy residual retained for preference-data collection, judge calibration/independence, multi-metric evaluation, regression monitoring, and rollback guidance that are intentionally outside the canonical Preference Optimization concept owner.

> **Migration note:** Preference-optimization identity, SFT distinction, preference-signal source variability, RLHF-versus-direct-objective boundaries, context-dependent judgment semantics, proxy/reward limitations, reward-model versus policy quality, method-specific constraints, and RLHF/DPO descendant ownership are already preserved in `docs/sub/concepts/sub/models/sub/training-and-adaptation/sub/preference-optimization/`. The remaining material below stays here until its exact learning, post-training engineering, evaluation, governance, or experiment-management owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Preference-data residual

Define comparison criteria, prompt/context distribution, candidate-generation process, annotator/judge population, tie/abstain handling, and versioned policy instructions before collecting preference data. Preserve enough provenance to distinguish a change in the learned policy from a change in who or what supplied the judgments.

Include ambiguous, adversarial, safety-relevant, style-sensitive, and factual cases when those dimensions matter to the target behavior rather than collecting only easy quality comparisons.

## Judge and calibration residual

Measure agreement and systematic disagreement among human annotators, rule-based checks, or model judges when they materially determine the training signal. Do not use one related model or reward/judge pipeline as the only generator, labeler, and evaluator when independent evidence is needed.

Calibrate judge preferences against task-grounded correctness or expert review where persuasive wording, verbosity, refusal style, or other superficial properties can dominate the proxy score.

## Multi-metric evaluation residual

Evaluate the preference objective together with task correctness, factuality/grounding, safety, refusal calibration, diversity, retained capabilities, latency/cost, and other acceptance criteria. A higher pairwise win rate can coexist with regressions that matter more to the application.

Use representative holdout prompts and preserve a sufficiently independent final acceptance set so repeated preference tuning does not overfit the evaluation protocol itself.

## Regression and rollback residual

Version the base/SFT checkpoint, preference dataset, judge/reward artifacts, training configuration, and resulting policy together. Keep a known-good prior artifact and rollback path when post-training can change broad behavior beyond the targeted preference dimension.

These data, judge, evaluation, regression, and rollback practices remain migration source material until their exact learning, post-training engineering, evaluation, governance, or experiment-management owners are verified.
