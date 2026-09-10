# Documentation Requirements

## Requirements

- Present Evaluation Foundations as the entry group for deciding what an evaluation result can legitimately support before choosing specific metrics, datasets, judges, benchmarks, or online experiments.
- Establish validity, reliability, calibration, scope/population, uncertainty, and offline-versus-online boundaries as prerequisites to interpreting model/system scores.
- Explain that the current materialized subset focuses on `validity-reliability-and-calibration/` because legacy sources contain source-backed warnings about parameter-count proxies, confidence interpretation, data distribution, preprocessing, and unsupported evaluation conclusions.
- Do not imply that unmaterialized selected siblings `what-to-evaluate/` or `offline-vs-online-evaluation/` are absent from the logical architecture; standard navigation reflects only physical children.
- Distinguish validity from reliability: a repeatable measurement can consistently measure the wrong thing, while a valid target can still be measured noisily or inconsistently.
- Treat calibration as correspondence between stated confidence/probability and observed outcome frequencies under a defined task/data/evaluation setup, not as a property inferred from softmax/logit scaling alone.
- Require evaluation conclusions to state the population/workload, data/preprocessing/configuration, metric/judge method, uncertainty, and material limitations when those boundaries affect interpretation.
- Keep concrete current benchmark results, model rankings, test-set scores, confidence curves, dated calibration measurements, and experiment artifacts with evidence/project owners.

## Validation

- Reliability is not used as a synonym for validity.
- Numerically bounded confidence output is not automatically called calibrated probability.
- Evaluation conclusions expose their scope and evidence boundary.
- Current navigation exposes only materialized selected children.
