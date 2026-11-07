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

## Scoped original-source qualification — 2026-11-08

- **Humanity's Last Exam (HLE)** is a released expert-authored **multimodal academic-knowledge benchmark** by the **Center for AI Safety and Scale AI**, represented by the upstream `centerforaisafety/hle` repository and `cais/hle` dataset. First-party documentation describes **2,500** difficult questions spanning numerous subjects and including multiple-choice and short-answer formats. That is the described release scope, not a timeless count across all future revisions.
- The official Hugging Face distribution is **gated** and explicitly warns against **public redistribution of the dataset**, including questions and answers. The author-maintained canary is contamination mitigation, not proof models were never exposed to the problems. The accompanying evaluation/judge scripts, dynamic leaderboards and separately collected model responses are not independent source-dataset identities.
- Original publisher sources: https://github.com/centerforaisafety/hle ; https://huggingface.co/datasets/cais/hle ; https://lastexam.ai/
- Source acceptance is limited to the existing published identity, first-party release/citation, publicly described distribution restrictions and scoring boundaries. No gated data copied, questions disclosed, external rights audit, judge/model evaluation, independently verified results, whole-repo schema/cache/CI/render, clean or final gate.
