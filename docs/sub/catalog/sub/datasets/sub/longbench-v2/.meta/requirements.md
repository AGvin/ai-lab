# Documentation Requirements

## Requirements

- Keep LongBench v2 distinct from original LongBench v1, state 503 cases and six categories, and pin hosted dataset/context permissions separately from the repository LICENSE.
- Use the pinned original publisher README to identify the dataset and version; distinguish evaluator, harness, source data, and external models.
- Rights and safety: The pinned source repository has MIT terms; the separately hosted LongBench-v2 dataset carries its own license metadata and upstream document/code context rights need independent review. Context contamination, retrieval settings, model versions and inference budgets can change results.
- This is a metadata-only source acceptance. No benchmark data download, untrusted code execution, model inference, external service access, or full rights audit has been performed.
- Keep one frozen identity, valid parent Datasets navigation, and no duplicate acceptance credit.

## Validation

- Confirm metadata, requirements and reader are consistent with the original source snapshot.
- Do not award unperformed schema-wide CI, cache/render, runtime or whole-catalog clean-pass gates.
