# Documentation Requirements

## Requirements

- Teach Overfitting and Underfitting as generalization failures diagnosed from the relationship between training behavior and performance on relevant unseen data rather than from training loss alone.
- Track training and validation behavior across checkpoints and record the model/data/configuration state corresponding to each measurement so regressions can be reproduced.
- In adaptation work, evaluate target-task quality together with retained capabilities; narrowing to training formats, repetitive imitation, or unrelated-task degradation can signal overfitting even while the supervised objective improves.
- Preserve an independent final holdout boundary and check leakage before interpreting a small generalization gap as trustworthy.
- Compare remediations against the observed failure rather than applying every regularizer mechanically; plausible remedies can include data cleanup/diversification, deduplication, augmentation, early stopping, regularization, lower effective capacity, different optimization, stronger split independence, or a simpler baseline.
- Measure remediation under the same acceptance criteria and preserve the previous checkpoint/configuration so improvements in one metric do not hide regressions in target behavior, latency, cost, or retained capabilities.

## Validation

- Overfitting is distinguished from leakage, distribution shift, and underfitting.
- Repeated test-set selection is treated as selection-procedure overfitting.
- Remediation choices remain evidence-driven and reversible.
