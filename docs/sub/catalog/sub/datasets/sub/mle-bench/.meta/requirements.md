# Documentation Requirements

## Requirements

- Identify MLE-bench as OpenAI's released benchmark for evaluating AI agents on machine-learning engineering tasks drawn from real Kaggle competitions.
- Preserve the machine-learning-engineering boundary around end-to-end competition work such as data preparation, model training, experimentation, and submission rather than reducing the benchmark to code generation.
- Treat competition inventory, Kaggle data/access dependencies, agent scaffold, resource budget, human baselines, contamination analysis, evaluation harness, model roster, and reported scores as freshness-sensitive.
- Keep the benchmark distinct from Kaggle itself, individual competition datasets, generic AutoML tools, model-training frameworks, and agent scaffolds used to run the evaluation.
- Attribute benchmark results to the exact model/scaffold/resource setup; do not generalize one agent configuration into a universal model capability claim.
- Preserve OpenAI producer provenance.

- Ground operational guidance in the direct openai/mle-bench repository: 75-competition full evaluation, 22-competition Low/Lite split, Kaggle credential/rule dependencies, reconstructed train/test splits, and competition-specific CSV grading.
- Preserve the repository notice dated 2026-04-24 that new leaderboard submissions are paused. Its known-issues section documents preparation and label-leakage defects and describes planned v2 fixes; do not infer benchmark retirement or present planned fixes as already in the selected release.
- When comparing results, retain the repository guidance to report split-specific Any Medal percentage with repeated seeds and uncertainty, plus agent/model, runtime and compute. Do not mix a Low/Lite score with the full benchmark.
- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [MLE-bench publication](https://openai.com/index/mle-bench/); [MLE-bench repository, preparation, grading, and known issues](https://github.com/openai/mle-bench).

## Validation

- MLE-bench remains a concrete benchmark identity rather than a generic ML-engineering task category.
- Kaggle competitions are benchmark inputs/members, not automatically separate canonical datasets.
- Results remain scoped to the evaluated scaffold and compute/resource budget.
- OpenAI provenance resolves bidirectionally.

## Scoped original-source qualification — 2026-11-08

- **MLE-bench** is OpenAI's released **2024-10-10** benchmark evaluating ML-engineering agents on **75 curated Kaggle competitions** spanning data preparation, model training, experiments and submissions. The full benchmark, low/lite 22-competition subset, compute time budgets, Kaggle credentials and task-specific graders are distinct evaluation configurations; a result on one cannot be directly compared to another without matching model/scaffold/resources and sampling.
- The first-party `openai/mle-bench` repository states **on 2026-04-24** that it is **not accepting new leaderboard submissions** while it designs a more comparable review process; this is not evidence the released corpus was withdrawn. Original known grading/preparation errors and **planned** v2 fixes remain open source-quality concerns, not proof v2 was published. Kaggle competition data have independent access, copyright, reuse and quota requirements.
- First-party sources: https://openai.com/index/mle-bench/ ; https://github.com/openai/mle-bench
- Existing identity, authorship/release, public competition/scoring scope and paused-submission boundary are source-qualified. No Kaggle data downloaded, GPU or agent runs, grading reproduction, individual competition rights audit, complete CI/security/legal/freshness, clean or final gate.
