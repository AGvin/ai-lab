# Reproducibility

Reproducibility is the ability to repeat an experiment or workflow under documented conditions and obtain comparable results.

## Core idea

Generative systems are probabilistic and providers may update models, so byte-identical output is not always possible. Practical reproducibility means recording enough information to explain and compare changes: model version, prompt, parameters, data, tools, runtime, hardware, and evaluation method.

## Practical requirements

- Pin model and dependency versions where possible.
- Store prompts and schemas in version control.
- Version datasets and retrieval indexes.
- Record seeds and sampling parameters.
- Capture hardware and runtime configuration for performance tests.
- Preserve raw results before aggregation.

## Trade-offs and limitations

Hosted models may change behind stable names. Parallel hardware kernels can be nondeterministic. Exact reproducibility may be expensive or impossible, so define acceptable tolerance for the task.

## Common mistakes

- Recording only the model family name.
- Changing prompts and datasets in the same comparison.
- Assuming a seed guarantees identical hosted output.
- Publishing aggregate scores without raw configuration.

## Related concepts

- [Evaluation and Operations](../../)
- [Evals](../evals/)
- [Tracing](../tracing/)
- [Sampling Parameters](../../../model-usage-and-generation/sub/sampling-parameters/)
