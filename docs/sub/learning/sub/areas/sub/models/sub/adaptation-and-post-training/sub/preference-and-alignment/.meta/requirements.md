# Documentation Requirements

## Requirements

- Teach Preference and Alignment as post-training from preference, reward, or comparison signals while keeping broad alignment goals/risks with Trustworthy AI.
- Version the base or SFT checkpoint, preference dataset, judge/reward artifacts, annotation protocol, training configuration, and resulting policy together.
- Define comparison criteria, prompt/context distribution, candidate-generation process, judge/annotator population, tie/abstain behavior, and quality-control rules before collecting preference data.
- Measure judge agreement, systematic disagreement, calibration, domain gaps, and proxy shortcuts when they materially determine the training signal; keep independent evidence when the same model or reward pipeline participates in generation, labeling, or optimization.
- Evaluate preference outcomes together with task correctness, factuality/grounding, safety, refusal calibration, diversity, retained capabilities, latency/cost, and other acceptance criteria.
- Keep representative holdout prompts and a sufficiently independent final acceptance set so repeated tuning does not overfit the evaluation protocol.
- Preserve known-good policy artifacts and rollback paths because broad behavior can regress outside the targeted preference dimension.

## Validation

- Pairwise win rate or reward score is not treated as sufficient acceptance evidence.
- Preference optimization is distinguished from SFT and from broad trustworthy-AI alignment ownership.
- Data/judge/policy provenance remains auditable across iterations.
