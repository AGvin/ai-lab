# Documentation Requirements

## Requirements

- Identify GPQA as the Graduate-Level Google-Proof Q&A benchmark/dataset for difficult expert-authored science questions.
- Keep the dataset identity distinct from the upstream baseline code, retrieval setup, model-specific prompts, and generic question-answering evaluation concepts.
- Preserve named subsets or variants only when current upstream sources define them, and do not compare results across different subsets as though they were identical test sets.
- Preserve contamination controls such as the published canary when discussed without treating them as proof of uncontaminated model training.
- Treat dataset revisions, prompt formats, evaluation setup, and benchmark results as version-sensitive facts.

## Validation

- GPQA is not collapsed with broad knowledge benchmarks such as MMLU or HLE.
- Baseline implementation details are not presented as intrinsic dataset requirements.
- Results from different subsets or evaluation setups are not compared without matching conditions.

## Scoped original-source qualification — 2026-11-08

- **GPQA (Graduate-Level Google-Proof Q&A Benchmark)** is the original expert-authored graduate-level **science** question dataset published by **David Rein et al.**, first released as a 2023 preprint and later accepted at **COLM 2024**. The original paper describes **448** biology, physics and chemistry multiple-choice questions. These are the historical released dataset's scope, not a guarantee that every redistributed split currently has 448 rows.
- The research authors' `idavidrein/gpqa` repository and original Hugging Face distribution identify the original dataset. Its canary string, `main` and other named subsets, answer-order shuffling and open-book retrieval baselines are distinct data/protocol boundaries; a published canary is not proof that model training is uncontaminated.
- Verified original sources: https://github.com/idavidrein/gpqa and https://huggingface.co/datasets/idavidrein/gpqa and https://arxiv.org/abs/2311.12022
- Qualification covers the existing dataset identity, authorship, original academic release and publicly described dataset/split/evaluation scope. No model inference, expert question revalidation, unrestricted dataset reuse rights, independent contamination test, security/privacy/legal audit, repository-wide schema/cache/CI/render, clean or final credit.
