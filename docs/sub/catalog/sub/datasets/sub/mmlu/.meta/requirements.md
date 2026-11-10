# Documentation Requirements

## Requirements

- Identify MMLU (Massive Multitask Language Understanding) as the concrete evaluation dataset/test introduced by Hendrycks et al. for broad multitask language-model knowledge and problem-solving evaluation.
- Keep the concrete question/test data distinct from the broader benchmark protocol, scoring/reporting practice, model results, and generic benchmark/evaluation concepts.
- Preserve the original subject-group breadth at a stable level without implying that MMLU is a representative sample of all real-world knowledge, reasoning, or deployment workloads.
- Treat dataset files, mirrors, preprocessing, prompt/evaluation protocol, few-shot setup, answer formatting, and reported scores as separate or version-sensitive facts that must be source-backed when expanded.
- Preserve contamination/exposure risk: long-public benchmark data may no longer function as an independently held-out test for every modern model.
- Include the upstream repository and original paper as canonical research references.

## Validation

- The profile describes the MMLU dataset identity rather than reproducing a historical leaderboard.
- Benchmark scores are not compared without matching dataset/protocol conditions.
- Public availability is not treated as proof of uncontaminated held-out evaluation for current models.
- Coverage is described as broad multitask academic/professional knowledge rather than universal model capability.

## Scoped original-source qualification — 2026-11-08

- **MMLU (Massive Multitask Language Understanding)** is the original **Hendrycks et al. ICLR 2021** broad multitask language-model knowledge test. The upstream `hendrycks/test` repository links the original paper and released evaluation dataset, with academic/professional subject groups and separate evaluation scripts and historical model results.
- The original dataset/test is not the `MMLU-Pro` successor, a held-out current leaderboard, a generic knowledge metric or a guaranteed clean test for current models. Differences in prompts, answer options, few-shot setup, mirrors, exposure, scoring and preprocessing prevent direct score comparison without exact protocol details.
- Verified original authors' sources: https://github.com/hendrycks/test and https://arxiv.org/abs/2009.03300
- Source gate covers existing benchmark identity, original authorship and original released test/evaluation context only. No independent scoring, complete data corpus provenance or rights audit, contamination assurance, whole-repository schema/cache/CI/render, clean or final gates.
