# Overfitting

Legacy residual retained for experiment monitoring, holdout discipline, remediation comparison, and adaptation-regression guidance that are intentionally outside the canonical Overfitting concept owner.

> **Migration note:** Overfitting identity, generalization-gap semantics, training-loss and learning-curve boundaries, memorization/interpolation/capacity distinctions, leakage/shift/underfitting separation, selection-procedure overfitting, conditional mitigation families, and evaluation independence are already preserved in `docs/sub/concepts/sub/machine-learning/sub/learning-theory/sub/overfitting/`. The remaining material below stays here until its exact learning, training-engineering, evaluation, experiment-management, or decision-support owner is verified.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Experiment-monitoring residual

Track training and validation behavior across checkpoints rather than only the final loss. Record the model/data/configuration state corresponding to each evaluation so an apparent regression can be reproduced and compared with earlier checkpoints or the unchanged base.

Monitor target-task quality together with important retained capabilities. In adaptation work, narrowing to the training format, repetitive output, excessive imitation, or degradation on unrelated representative tasks can be useful warning signals even when the supervised objective continues improving.

## Holdout-discipline residual

Use validation evidence for tuning and stopping while preserving a sufficiently independent final test/holdout boundary for the accepted configuration. Repeatedly choosing prompts, checkpoints, hyperparameters, data filters, or model variants against the same final test set turns that set into part of the selection process.

Check for exact and near-duplicate leakage, shared source documents/entities, synthetic derivatives, temporal look-ahead, and other dependence across splits before interpreting a small generalization gap as trustworthy.

## Remediation residual

Compare plausible mitigations against the actual observed failure rather than applying every regularizer mechanically. Depending on the regime, useful changes can include data cleanup/diversification, deduplication, augmentation, early stopping, regularization, lower effective capacity, different optimization, stronger split independence, or a simpler baseline.

Measure the remediation on the same acceptance criteria and preserve the previous checkpoint/configuration so a mitigation that improves one metric but damages target behavior, latency, cost, or retained capabilities is visible.

These monitoring, holdout, remediation, and adaptation-regression practices remain migration source material until their exact learning, training-engineering, evaluation, experiment-management, or decision-support owners are verified.
