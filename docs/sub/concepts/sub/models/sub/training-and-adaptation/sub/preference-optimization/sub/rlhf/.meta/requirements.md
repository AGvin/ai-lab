# Documentation Requirements

## Requirements

- Use the reader-facing title `Reinforcement Learning from Human Feedback (RLHF)`.
- Define RLHF as reinforcement learning in which human feedback is used to define, learn, shape, or evaluate a reward/preference signal and that signal guides optimization of a policy/model through reinforcement-learning methods.
- Keep the definition broader than the InstructGPT pipeline. Training an SFT policy, collecting pairwise rankings, fitting a separate reward model, and applying PPO with a KL/reference constraint is a canonical modern LLM implementation, not the universal definition of RLHF.
- Explain that human feedback can take comparisons, rankings, ratings, demonstrations converted into reward information, critiques, trajectory judgments, or other evaluated preference signals depending on the method. The exact collection protocol determines what preference signal is learned.
- Distinguish supervised demonstrations from RLHF preference feedback. Human-written desired responses can be used for SFT, while rankings/comparisons can train or define the reward used for RL; a pipeline may use both but they are different training signals.
- Explain the role of an explicit reward model when used: it approximates human preferences from labeled comparisons or related feedback so the policy can receive scalable reward during RL. The reward model is a learned proxy and can be wrong, exploitable, or poorly calibrated outside its training distribution.
- Distinguish reward-model training from policy optimization. Reward-model accuracy on held-out comparisons does not prove that optimizing the model will produce globally preferred, truthful, safe, or robust behavior.
- Present PPO as an important LLM RLHF algorithm rather than a defining requirement. Other policy-gradient, actor-critic, bandit, offline/online RL, or related optimization methods can use human-derived feedback under a broader RLHF formulation.
- Explain that KL/reference penalties and other regularizers are commonly used to limit policy drift from a reference/SFT model and reduce exploitation/instability, but the exact divergence, coefficient, clipping, reward normalization, and optimization design are method-specific.
- Make clear that human feedback represents judgments from particular annotators/evaluators under specified instructions, cultural/contextual assumptions, candidate distributions, and interfaces. RLHF does not convert those judgments into objective truth or universal human values.
- Explain reward hacking/overoptimization as a risk: a policy can exploit inaccuracies in the learned reward or feedback process and improve proxy reward while degrading the underlying human objective or other capabilities.
- Treat online sample generation, exploration, reward computation, and policy updates as part of the concrete RL training loop when used; do not assume every RLHF pipeline uses the same rollout volume, batch structure, sampling policy, or environment.
- Distinguish RLHF from DPO. DPO uses preference pairs to optimize a policy through a direct objective and, in its original form, avoids a separately trained reward model and online RL policy-optimization loop; this different optimization mechanism is why it has a separate selected child.
- Keep concrete annotator instructions, preference datasets, reward-model architectures, PPO parameters, KL coefficients, rollout infrastructure, provider post-training systems, benchmark results, and model-selection recommendations with their applicable catalog, evidence, learning, engineering, governance, or decision owners.
- Use the canonical entity references as research inputs for human-preference reward modeling and RL policy-optimization boundaries when reader-facing rendering is activated.

## Validation

- RLHF is not defined as synonymous with PPO or the exact three-stage InstructGPT pipeline.
- Human SFT demonstrations and human preference/ranking feedback are not collapsed into one training signal.
- A learned reward model is described as a proxy rather than objective truth, safety, or universal human preference.
- Reward-model fit is not treated as proof that policy optimization will preserve all desired behavior.
- KL/reference constraints and PPO hyperparameters are not universalized.
- RLHF is distinguished from DPO/direct preference optimization rather than treating all human-preference training as one algorithm.
- Concrete data, annotator populations, reward models, training runs, and evaluation outcomes remain outside the abstract concept owner.
