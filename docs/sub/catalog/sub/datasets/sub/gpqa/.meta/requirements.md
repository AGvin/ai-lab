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
