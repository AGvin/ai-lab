# Documentation Requirements

## Requirements

- Teach validity as whether an evaluation supports the intended conclusion, reliability as whether the measurement is sufficiently consistent/reproducible under its stated procedure, and calibration as whether stated confidence/probability corresponds to observed outcome frequency under a defined scope.
- Keep the three ideas distinct. A measurement can be reliable but invalid, a model can be accurate but poorly calibrated, and a calibrated score on one population can become miscalibrated after distribution or workflow changes.
- Begin from the exact claim being evaluated and identify the target behavior/system layer, population/workload, data source, preprocessing, model/artifact/configuration, metric or judge method, and decision/acceptance use that define the evidence scope.
- Explain construct/content/criterion or other validity concerns only as useful reasoning frames where they clarify whether the chosen measurement actually represents the intended capability, quality, safety, or system outcome; avoid pretending one terminology taxonomy is universal across all AI evaluation practice.
- Explain reliability through repeatability/reproducibility and measurement variance. Re-run, resample, inter-rater, prompt/judge, environment, and stochastic variation can matter depending on the evaluation method.
- Treat model confidence/logit/softmax-derived scores as model outputs, not automatically calibrated probabilities. Calibration must be checked empirically against outcomes for the relevant task/population and can vary across classes, slices, thresholds, domains, versions, and operating points.
- Explain common calibration evaluation families such as reliability diagrams, expected/maximum calibration error, Brier-style scoring, log loss, and threshold/coverage analyses without making any one metric universally sufficient.
- Distinguish calibration from uncertainty estimation and from correctness. A model can be uncertain yet calibrated, confident and wrong, or have useful ranking quality while probability calibration remains poor.
- Explain that parameter count, model family, benchmark reputation, training loss, or confidence magnitude are not substitutes for task-specific validity/reliability/calibration evidence.
- Treat data distribution and preprocessing as part of the evaluation contract. Dataset shift, class imbalance, prompt/context changes, input normalization, truncation, filtering, sampling, or post-processing can change both performance and calibration.
- Report uncertainty and sample limitations when they materially affect conclusions. Small or unrepresentative samples, correlated cases, leakage/contamination, repeated benchmark exposure, judge dependence, and cherry-picked slices can make a precise-looking score misleading.
- When evaluation supports a consequential threshold or automated action, validate the threshold/operating point under representative conditions and monitor whether its error/calibration behavior remains acceptable after model/data/workflow changes.
- Separate learning methodology from evidence records. Concrete scores, calibration curves, benchmark runs, model comparisons, dated findings, test artifacts, and experiment outputs remain with evidence/project owners.

## Validation

- Validity, reliability, calibration, accuracy, uncertainty, and confidence are not collapsed into synonyms.
- A softmax/logit/confidence value is never treated as calibrated probability without empirical evidence.
- Evaluation scope includes the relevant data/preprocessing/model/configuration and decision boundary.
- Parameter count or nominal model properties are not used as proxies for validated task quality.
- Mutable measurements remain evidence-owned and date/configuration bounded.
