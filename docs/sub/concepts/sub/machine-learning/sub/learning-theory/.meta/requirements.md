# Documentation Requirements

## Requirements

- Use the reader-facing title `Learning Theory`.
- Define learning theory as the study of when, why, and under what assumptions learning procedures can generalize from finite observations or experience to performance on unseen cases, future interactions, or an explicitly defined target distribution/task.
- Distinguish empirical/training performance from population/expected/generalization performance. Learning-theory claims concern the relationship between observed finite-sample behavior and performance beyond the data used to fit or select the learner.
- Make assumptions explicit. Results can depend on the data-generating process, independence/stationarity assumptions, hypothesis/function class, loss, sampling scheme, noise, feedback model, optimization/selection procedure, and target distribution; a bound or theorem outside its assumptions is not a universal guarantee.
- Cover hypothesis/model capacity and complexity as families of concepts rather than equating them with parameter count. VC-style complexity, norm/margin controls, effective capacity, algorithmic stability, compression, implicit bias, and other measures can characterize different learning settings.
- Explain generalization gap as the difference between performance measured on training/selection experience and performance on the intended unseen population/evaluation setting. A nonzero finite-sample gap is not automatically pathological; magnitude and acceptable uncertainty depend on the task and evaluation design.
- Distinguish underfitting and overfitting as different failures. Underfitting reflects insufficient fit/expressiveness/optimization for relevant structure, while `overfitting/` owns the selected concept of fitting sample-specific structure in a way that harms generalization.
- Explain bias and variance as analytical perspectives rather than a universal two-number decomposition for every modern learner/loss. Classical U-shaped capacity intuition is useful but must not be presented as an invariant law for modern overparameterized models.
- Explain sample complexity as the amount/type of data or experience needed to achieve a specified generalization/accuracy/confidence target under stated assumptions; do not reduce it to a fixed examples-per-parameter rule.
- Explain learnability as setting-dependent. PAC/statistical learning, online learning/regret, reinforcement-learning sample complexity, transductive/semi-supervised settings, and other theories use different objects and guarantees; this parent does not select those as descendants unless architecture says so.
- Distinguish theoretical guarantees from empirical validation. Bounds can be loose or assumption-sensitive, while strong benchmark/validation performance does not by itself establish a theorem about future data.
- Explain regularization broadly as constraints, penalties, data/optimization procedures, early stopping, augmentation, priors, implicit optimization bias, or other mechanisms that can improve generalization in a defined setting; regularization is not synonymous with one penalty term.
- Explain model/hyperparameter selection as part of the generalization problem. Reusing validation/test data repeatedly can adapt decisions to that finite sample and invalidate an apparently independent estimate even when the final model's training procedure is unchanged.
- Distinguish distribution shift from ordinary in-distribution generalization. Theory/evaluation must state which target distribution or environment is being generalized to; failure after a target distribution changes is not automatically overfitting to the original distribution.
- Keep optimization success separate from generalization. Lower empirical loss can coexist with better, unchanged, or worse unseen performance depending on the regime; reaching a global/interpolating training solution does not itself establish overfitting.
- Keep concrete datasets, training runs, bounds calculated for one experiment, benchmark results, hyperparameters, model checkpoints, and task-specific mitigation decisions with their applicable evidence/project/training owners.
- Keep `overfitting/` as the currently selected direct child and do not infer additional learning-theory descendants from terminology in legacy pages.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Use the canonical entity reference as a research input for generalization, capacity, and underfitting/overfitting boundaries when reader-facing rendering is activated.

## Validation

- Learning theory is not reduced to neural networks, supervised learning, VC dimension, parameter count, or one classical bias-variance curve.
- Generalization claims identify their target distribution/setting and material assumptions.
- Training/optimization success is distinguished from unseen/generalization performance.
- Theoretical guarantees and empirical evaluation are not treated as interchangeable evidence.
- Distribution shift is distinguished from ordinary finite-sample generalization failure.
- Concrete runs, datasets, calculated bounds, and tuning decisions remain outside the reusable parent owner.
- Direct-child navigation contains only currently materialized selected descendants.
