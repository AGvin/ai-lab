# Documentation Requirements

## Requirements

- Teach DPO as a direct preference objective distinct from common reward-model-plus-RL pipelines while remaining part of broader preference post-training.
- Construct chosen/rejected pairs under explicit criteria and preserve prompt/context, candidate-generation policy, annotator/judge source, tie/abstain handling, and data version.
- Inspect pair quality for duplicate prompts, candidate-length/style artifacts, domain coverage, factual correctness, refusal/safety cases, and trivially weak rejected answers that can create superficial shortcuts.
- Pin exact policy/reference checkpoints, tokenizer or processor, chat template, preprocessing, sequence truncation, log-probability implementation, and cached reference values when used.
- Treat beta and related scaling/configuration values as formulation/library-specific experiment settings and compare configurations under matched data/evaluation conditions.
- Compare DPO against unchanged/SFT references and relevant preference alternatives using matched prompt distributions and acceptance metrics.
- Measure preference outcomes together with factuality/grounding, safety, refusal calibration, diversity, retained capabilities, calibration, latency/cost, and target-task correctness; keep an independent final acceptance set.
- Version preference data, objective/trainer variant, artifacts, hyperparameters, and resulting policy together and retain a known-good rollback point.

## Validation

- A simpler training loop is not automatically interpreted as superior preference optimization.
- Reference/configuration details are sufficient to reproduce the effective objective.
- Pairwise preference accuracy is not treated as protection against unrelated regressions.
