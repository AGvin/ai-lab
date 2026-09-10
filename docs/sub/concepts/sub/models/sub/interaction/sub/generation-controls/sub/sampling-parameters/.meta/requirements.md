# Documentation Requirements

## Requirements

- Use the reader-facing title `Sampling Parameters`.
- Define sampling parameters as inference-time controls that modify how a generative model selects the next output unit from model scores/probabilities or from a filtered candidate set.
- Explain temperature as a control that rescales relative logits/probabilities before sampling, changing concentration of the distribution without creating new model knowledge or changing trained parameters.
- Explain top-k as restricting consideration to a fixed number of highest-scoring candidates and top-p/nucleus sampling as restricting consideration to a dynamic smallest candidate set whose cumulative probability mass reaches a threshold; qualify these as common definitions rather than guarantees about every provider's implementation details.
- Explain that sampling controls can be composed, but their combined effect depends on operation order, model distribution, implementation, and additional processors such as minimum-probability filters, repetition/frequency/presence penalties, logit biases, or provider-specific heuristics.
- Treat greedy/argmax decoding and other deterministic or search-based decoding strategies as related alternatives to stochastic sampling rather than values of one universal sampling parameter.
- Distinguish random seed/reproducibility controls from the sampling distribution itself. A fixed seed can improve repeatability only within the determinism guarantees of the exact model, runtime, hardware, batching, provider, and execution path.
- Make clear that lower temperature or narrower sampling does not guarantee factuality, correctness, safety, calibration, or schema compliance, while higher diversity does not create missing capability or knowledge.
- Avoid universal task presets such as `temperature=0 for extraction` or one fixed top-p value. Parameter tuning belongs to evaluated task/runtime configuration and may change across models or releases.
- Keep current provider parameter names/ranges/defaults, unsupported combinations, benchmark-tuned presets, and model-selection recommendations with their applicable catalog, evidence, or decision owners.
- Use the canonical entity references as research inputs for probabilistic decoding and nucleus-sampling boundaries when reader-facing rendering is activated.

## Validation

- Temperature, top-k, and top-p are described as distinct controls rather than interchangeable randomness sliders.
- The page does not claim temperature zero or a fixed seed universally guarantees byte-identical output.
- Sampling settings are not presented as factuality, safety, calibration, or schema-validity guarantees.
- Provider-specific defaults and parameter interactions are not generalized as universal semantics.
- No one preset is recommended as universally optimal for a task category.
- Legacy operational tuning advice is preserved only as qualified boundaries rather than canonical presets.
