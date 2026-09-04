# Documentation Requirements

## Requirements

- Teach Machine Learning Fundamentals as the shared vocabulary and evaluation discipline needed before specific learning paradigms or model families.
- Materialize only selected children with source-backed content; this package materializes `train-validation-and-test/` and `overfitting-and-underfitting/`.
- Separate data used for fitting, tuning/model selection, and final acceptance according to the actual dependency structure of the data and experiment.
- Explain generalization as performance on relevant unseen data rather than low training loss or success on repeatedly inspected evaluation examples.
- Keep concrete dataset lifecycle engineering with Data and Knowledge and model-specific training mechanics with Models.

## Validation

- Final acceptance evidence remains sufficiently independent from iterative selection.
- Generalization claims remain tied to representative unseen data and experiment design.
- Fundamentals do not duplicate model-specific adaptation/training implementation.
