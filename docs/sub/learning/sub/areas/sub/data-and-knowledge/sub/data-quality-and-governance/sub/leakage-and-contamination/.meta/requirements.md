# Documentation Requirements

## Requirements

- Teach Leakage and Contamination as failures of evaluation independence or information boundaries that can make measured performance look stronger than real generalization.
- Check more than exact duplicates: shared source documents/entities, generated or paraphrased derivatives, future information, benchmark exposure, entity/session/repository overlap, and labels derived from protected/future state can invalidate independence.
- Choose split boundaries according to the data dependency structure rather than assuming row-level randomization is sufficient.
- Preserve a sufficiently independent final acceptance set; repeated checkpoint, prompt, hyperparameter, filter, or model selection against the same final test set makes it part of the selection process.
- Treat leakage findings as dataset-version defects requiring traceable correction and reassessment of dependent training/evaluation evidence.

## Validation

- A small train/validation gap is not trusted until dependence/leakage has been examined.
- Synthetic derivatives are considered when checking split independence.
- Evaluation contamination is distinguished from ordinary model overfitting while recognizing their interaction.
