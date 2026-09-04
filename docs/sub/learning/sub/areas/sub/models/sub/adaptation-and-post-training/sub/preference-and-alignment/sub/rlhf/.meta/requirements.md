# Documentation Requirements

## Requirements

- Teach RLHF as preference-based post-training that may use supervised/reference policies, learned reward models, rollout generation, and reinforcement-learning updates; do not reduce the family to one optimizer such as PPO.
- Version annotation criteria, candidate-generation policy, tie/abstain handling, quality-control rules, and disagreement policy together with collected preference data.
- Evaluate reward models on held-out comparisons and shifted candidate distributions; inspect calibration, shortcut features, and cases where predicted reward conflicts with task-grounded correctness or expert review.
- Do not use the reward model as the sole evaluator of the policy it directly optimized when independent acceptance evidence is required.
- Monitor reward, reference/KL divergence, diversity/entropy, applicable policy/value losses, rollout quality, invalid outputs, and target-task metrics during updates; checkpoint frequently enough for diagnosis and rollback.
- Measure rollout/reward-inference cost, wall-clock time, storage/communication, and accepted-result improvement together.
- Evaluate final policies against the SFT/reference baseline across preference outcomes and independent factuality, grounding, safety, refusal calibration, diversity, retained-capability, latency/cost, and task metrics.

## Validation

- Proxy/reward improvement is not equated with policy quality.
- Annotation protocol changes remain distinguishable from policy-training changes.
- Rollback and independent acceptance evidence remain practical.
