# Documentation Requirements

## Requirements

- Identify MLE-bench as OpenAI's released benchmark for evaluating AI agents on machine-learning engineering tasks drawn from real Kaggle competitions.
- Preserve the machine-learning-engineering boundary around end-to-end competition work such as data preparation, model training, experimentation, and submission rather than reducing the benchmark to code generation.
- Treat competition inventory, Kaggle data/access dependencies, agent scaffold, resource budget, human baselines, contamination analysis, evaluation harness, model roster, and reported scores as freshness-sensitive.
- Keep the benchmark distinct from Kaggle itself, individual competition datasets, generic AutoML tools, model-training frameworks, and agent scaffolds used to run the evaluation.
- Attribute benchmark results to the exact model/scaffold/resource setup; do not generalize one agent configuration into a universal model capability claim.
- Preserve OpenAI producer provenance.

## Validation

- MLE-bench remains a concrete benchmark identity rather than a generic ML-engineering task category.
- Kaggle competitions are benchmark inputs/members, not automatically separate canonical datasets.
- Results remain scoped to the evaluated scaffold and compute/resource budget.
- OpenAI provenance resolves bidirectionally.
