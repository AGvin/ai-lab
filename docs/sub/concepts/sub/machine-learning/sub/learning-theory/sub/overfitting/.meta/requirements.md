# Documentation Requirements

## Requirements

- Use the reader-facing title `Overfitting`.
- Define overfitting as a generalization failure in which a learned model, hypothesis, or selection procedure adapts too strongly to sample-specific, noisy, accidental, or repeatedly reused characteristics of the data/experience used for fitting or selection, causing worse performance on appropriately unseen data from the intended target distribution than the apparent fit suggests.
- Anchor the concept in generalization rather than training loss. Low or zero training error, high likelihood on training data, exact interpolation, memorized examples, or continued optimization is not sufficient evidence of overfitting without a degradation/excess gap in relevant unseen performance.
- Explain the generalization gap as a useful diagnostic quantity but do not label every nonzero gap as overfitting. Finite samples naturally produce uncertainty; the concern is an excessive/problematic gap relative to the target task, data, uncertainty, and available alternatives.
- Present a common learning-curve pattern carefully: training performance can continue improving while validation performance plateaus or worsens. This is a strong practical signal in many settings, not a universal temporal signature required by the definition.
- Distinguish overfitting from memorization. A model can memorize some training examples while still generalizing well overall, and a model can overfit through sample-specific decision boundaries or selection effects without literal verbatim memorization.
- Distinguish overfitting from interpolation. Modern overparameterized models can fit/interpolate training data exactly and still achieve strong unseen performance; interpolation/high capacity therefore cannot be used as a standalone overfitting test.
- Distinguish overfitting from model size/capacity alone. Capacity interacts with data volume/diversity/noise, inductive bias, optimization, regularization, augmentation, architecture, initialization, and task structure; there is no universal parameter-count threshold at which a model becomes overfit.
- Distinguish overfitting from data leakage and evaluation contamination. Leakage can expose target/test information during training or feature construction and invalidate evaluation; repeated tuning against a validation/test set can overfit the selection process to that set, but leakage itself is a separate evaluation/data-integrity problem.
- Distinguish overfitting from distribution shift. A model can generalize correctly to the distribution it was trained/evaluated for and still fail when deployment data changes; conversely, poor unseen performance on the same intended distribution can indicate overfitting without distribution shift.
- Distinguish overfitting from underfitting. Underfitting occurs when the learner fails to capture relevant structure even on the available training/selection evidence; overfitting concerns excessive adaptation to finite-sample specifics relative to unseen performance.
- Explain that overfitting can affect model parameters, prompt/policy selection, hyperparameters, architecture choices, feature engineering, data preprocessing, stopping criteria, retrieval/reranking settings, or any repeatedly optimized decision if the same finite evaluation evidence is reused.
- Explain training-data characteristics that can increase risk without calling them deterministic causes: small effective sample size, duplicate/highly correlated examples, label noise, spurious shortcuts, narrow coverage, high flexibility relative to evidence, aggressive repeated selection, and insufficiently independent validation can all increase overfitting risk.
- Explain mitigation as conditional families rather than guarantees: more representative/diverse data, deduplication, data augmentation, regularization, early stopping, capacity/architecture changes, ensembling, robust feature/design choices, independent validation/test sets, nested cross-validation, and limiting repeated adaptation to holdout evidence can help depending on the regime.
- Make clear that early stopping is a model-selection/regularization strategy requiring an independent evaluation boundary. Stopping because a metric was repeatedly inspected on the final test set simply transfers overfitting risk to that test set.
- Explain evaluation requirements: use genuinely unseen data representative of the intended target distribution, report uncertainty where relevant, preserve a final test boundary after model/hyperparameter selection, and compare against simpler/baseline models or earlier checkpoints when that helps isolate a generalization regression.
- For fine-tuning/adaptation contexts, mention possible symptoms such as narrowed behavior, brittle adherence to training formats, repetitive outputs, degradation of unrelated capabilities, or excessive imitation of examples only as empirical manifestations; they do not redefine overfitting for all ML.
- Do not claim PEFT, LoRA, QLoRA, full fine-tuning, pretraining, or any optimizer is inherently immune or inherently prone to overfitting. Risk depends on the data, objective, trainable degrees of freedom, optimization, regularization, and selection/evaluation procedure.
- Keep concrete training curves, checkpoints, datasets, validation splits, hyperparameters, early-stopping thresholds, benchmark outcomes, and remediation choices with their applicable experiment/evidence/project/training owners.
- Use the canonical entity references as research inputs for classical generalization/capacity framing and modern overparameterized/interpolation caveats when reader-facing rendering is activated.

## Validation

- Overfitting is defined through unseen/generalization performance, not training fit alone.
- Memorization, interpolation, high capacity, model size, or continued loss reduction is not treated as sufficient proof of overfitting.
- Data leakage/evaluation contamination and distribution shift are distinguished from overfitting.
- Validation/test reuse and selection-procedure overfitting are covered, not only parameter fitting.
- Mitigation techniques are conditional strategies rather than guaranteed cures.
- Fine-tuning-specific symptoms do not replace the general ML definition.
- Concrete experiments, splits, thresholds, checkpoints, and mitigation decisions remain outside the reusable concept owner.
