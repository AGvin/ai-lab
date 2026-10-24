# Documentation Requirements

## Requirements

- Identify Humanity's Last Exam (HLE) as the concrete multimodal frontier academic-knowledge benchmark/dataset distributed by the upstream project.
- Keep the dataset identity distinct from the project's example inference/evaluation scripts, leaderboard results, model providers, and generic benchmark concepts.
- Preserve the broad subject and mixed question-format scope from current upstream sources without turning one score snapshot into a dataset property.
- Preserve contamination controls such as the upstream canary when discussed, while avoiding any claim that a canary proves a model was not exposed to the benchmark.
- Treat dataset revisions, question counts, scoring configuration, public availability, and benchmark results as version-sensitive or mutable facts where applicable.

## Validation

- HLE is profiled as a benchmark dataset, not as an evaluation framework or model ranking.
- Benchmark scores are not generalized across mismatched prompts, models, graders, or dataset revisions.
- Contamination risk is not presented as solved merely because the dataset publishes a canary.
