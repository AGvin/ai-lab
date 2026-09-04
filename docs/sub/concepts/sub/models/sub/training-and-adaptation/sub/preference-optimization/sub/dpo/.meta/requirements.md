# Documentation Requirements

## Requirements

- Use the reader-facing title `Direct Preference Optimization (DPO)`.
- Define DPO as a direct preference-optimization method that trains a policy/model from preference pairs such as chosen and rejected responses by optimizing a classification/logistic-style objective derived from a KL-constrained reward-maximization formulation.
- Explain the central distinction from common RLHF pipelines: original DPO does not require separately fitting an explicit reward model and then running an online reinforcement-learning policy-optimization loop; preference pairs are used directly in the policy objective.
- Do not state that DPO has `no reward model` in the stronger conceptual sense. The original derivation establishes a mapping between the optimal policy and an underlying reward function, then substitutes that relationship into the preference model/objective so a separate learned reward-model training stage is unnecessary.
- Distinguish DPO from supervised fine-tuning. SFT optimizes likelihood of target demonstrations, while DPO uses relative chosen-versus-rejected preference information and a reference/policy relationship to increase preferred behavior relative to dispreferred behavior.
- Explain the role of a reference policy/model in the original formulation: preference updates are regularized relative to a reference behavior through the derived objective. Concrete implementations can represent or cache reference log-probabilities differently, so do not require one memory/execution implementation.
- Explain `beta` or equivalent scaling as controlling the strength/temperature of the preference-versus-reference trade-off in the standard DPO objective, while avoiding one universal numeric interpretation/default independent of formulation and implementation.
- Make clear that preference pairs inherit the collection process's biases, noise, ambiguity, annotator/evaluator assumptions, candidate-generation policy, prompt distribution, and coverage gaps. DPO does not turn a chosen response into objective truth or globally optimal behavior.
- Explain that DPO can overfit preference data, exploit dataset artifacts, change unrelated capabilities, or trade off diversity/calibration/robustness; direct optimization is not an automatic alignment, safety, factuality, or generalization guarantee.
- Distinguish original/offline pairwise DPO from later DPO-family variants that alter the preference model, reference handling, online data collection, robustness assumptions, multi-objective setup, or loss. Do not redefine the base concept around one later variant.
- Distinguish DPO from generic pairwise ranking/classification. Its policy objective is tied to model log-probabilities, preference pairs, and the reference/KL-constrained derivation rather than being any classifier trained on two labels.
- Keep concrete preference datasets, chosen/rejected pair construction, beta/reference choices, log-probability caching, trainers/frameworks, variant algorithms, training hyperparameters, benchmark results, and model-selection recommendations with their applicable catalog, evidence, learning, engineering, governance, or decision owners.
- Use the canonical entity references as research inputs for DPO's direct objective, reference-policy relationship, and reward-model/RLHF distinction when reader-facing rendering is activated.

## Validation

- DPO is not described as ordinary SFT, generic pairwise classification, or RLHF with PPO removed while everything else remains identical.
- The absence of a separately trained explicit reward-model stage is not misrepresented as absence of reward/preference semantics in the derivation.
- The reference-policy/KL-constrained relationship is preserved without universalizing one storage/training implementation or beta value.
- Preference pairs are not treated as objective truth, safety labels, or universally representative human values.
- Original DPO is distinguished from later online, reference-free, robust, or other DPO-family variants.
- Direct optimization is not presented as an automatic guarantee of alignment, factuality, safety, or better generalization than RLHF/SFT.
- Concrete data, hyperparameters, trainers, variants, and evaluation results remain outside the abstract concept owner.
