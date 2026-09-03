# Documentation Requirements

## Requirements

- Teach train/validation/test roles as distinct experiment boundaries: fitting, iterative tuning/model selection, and final acceptance evidence.
- Choose split boundaries according to real dependence in the data such as user, source document, entity, session, time, repository, device, or another grouping when row-level randomization would leak correlated evidence.
- Search for exact and near-duplicate leakage, shared source material, synthetic derivatives, temporal look-ahead, entity overlap, benchmark exposure, and labels derived from future/protected state.
- Preserve a sufficiently independent final acceptance set; repeated checkpoint, prompt, hyperparameter, data-filter, or model selection against it makes it part of the optimization loop.
- Keep split assignments versioned with the effective dataset state so experiment evidence can be reproduced.

## Validation

- Validation evidence is used for iteration while final test/holdout evidence remains protected from routine tuning.
- A random split is not treated as automatically independent.
- Split leakage remains distinguishable from model overfitting while both are checked before accepting generalization claims.
