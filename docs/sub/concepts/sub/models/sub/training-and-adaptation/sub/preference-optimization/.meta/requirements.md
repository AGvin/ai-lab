# Documentation Requirements

## Requirements

- Use the reader-facing title `Preference Optimization`.
- Define preference optimization as post-training/adaptation methods that use relative judgments, comparisons, rankings, ratings, rewards, or other preference signals over candidate behaviors to update a model or policy toward preferred behavior.
- Distinguish preference optimization from supervised fine-tuning. SFT learns from target demonstrations/labels; preference optimization learns from relative preference or reward information about alternative behaviors. A training pipeline can use both stages.
- Explain that preference signals can originate from humans, AI systems, rules/constitutions, simulations, reward functions, or mixed sources depending on the method. `Human preference` is therefore not a universal requirement of the parent family even though RLHF specifically requires human feedback.
- Distinguish explicit reward-model plus reinforcement-learning approaches from direct preference objectives. RLHF commonly learns or otherwise uses a human-feedback-derived reward signal and optimizes a policy through RL, while methods such as DPO optimize a policy directly from preference pairs without requiring a separately trained reward model or online RL loop in the base algorithm.
- Explain that preference data expresses judgments under a collection protocol, annotator/evaluator population, prompt/context distribution, candidate-generation process, policy/version, and comparison criteria. Preference labels are not context-free objective truth.
- Make clear that optimizing a preference proxy can improve preferred behavior while degrading unrelated capabilities, diversity, calibration, factuality, or other properties and can exploit weaknesses in the feedback/reward process. Preference optimization is not a general safety/alignment guarantee.
- Distinguish reward/preference-model fit from policy quality. A reward model can be inaccurate or exploitable outside its training distribution, and a direct preference objective can inherit bias/noise from the preference pairs and reference-policy assumptions.
- Explain that reference/KL-style constraints, regularization, sampling policies, candidate generation, reward scaling, temperature/beta parameters, and optimization algorithms are method-specific design dimensions rather than universal preference-optimization requirements.
- Keep `rlhf/` and `dpo/` as distinct selected descendants. Do not collapse DPO into RLHF merely because its derivation relates to a reward/RL formulation, and do not redefine all preference optimization as DPO.
- Keep concrete preference datasets, annotator policies, reward models, training runs, hyperparameters, provider post-training services, experiment results, and model-selection recommendations with their applicable catalog, evidence, learning, engineering, governance, or decision owners.
- Use the canonical entity references as research inputs for RLHF-style and direct-preference optimization boundaries when reader-facing rendering is activated.

## Validation

- Preference optimization is not equated with supervised fine-tuning, generic reinforcement learning, RLHF alone, or DPO alone.
- Human feedback is not stated as a requirement of every preference-optimization method.
- Preference labels/rewards are not treated as objective truth or automatic evidence of safety/alignment.
- Explicit reward-model/RL pipelines are distinguished from direct preference objectives without claiming the latter have no reward/preference semantics.
- Method-specific KL/reference constraints, algorithms, and hyperparameters are not universalized.
- Concrete preference data, reward models, training results, and recommendations remain outside the abstract concept owner.
