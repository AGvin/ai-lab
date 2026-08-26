# Documentation Requirements

## Requirements

- Use the reader-facing title `Data-Centric Machine Learning` and introduce `data-centric AI` as a common broader term.
- Define this domain as the systematic design, collection, generation, labeling, curation, transformation, validation, documentation, evaluation, maintenance, and governance of data so an ML/AI system has evidence appropriate to its intended task, population, environment, and lifecycle.
- Distinguish data-centric work from simply collecting more data. Additional volume can add duplicates, bias, noise, stale information, privacy risk, or irrelevant coverage; data quantity is only one dimension of fit-for-purpose evidence.
- Distinguish data-centric ML from model-centric iteration. The approaches are complementary: one changes or improves data and its lifecycle, the other changes model architecture/objective/optimization/runtime; production systems commonly require both.
- Treat data quality as task- and context-dependent rather than one universal score. Accuracy/correctness, coverage, representativeness, label consistency, completeness, diversity, freshness, provenance, balance, duplication, privacy, fairness, accessibility, and format/schema quality can matter differently by use case.
- Distinguish source/raw data, curated datasets, labels/annotations, derived features/representations, synthetic/augmented data, training/validation/test sets, inference-time inputs, feedback data, and operational monitoring data where the lifecycle requires different controls.
- Explain dataset construction as a selection process that defines what the learner can observe. Sampling, filtering, deduplication, exclusion criteria, label policy, preprocessing, chunking, aggregation, and train/evaluation splits can introduce inductive assumptions or blind spots even when individual records are correct.
- Explain provenance and lineage as core reproducibility/governance concerns. Record material source, collection/generation process, transformations, label origin, versions, licenses/permissions, and known limitations so downstream results can be traced to data changes.
- Distinguish dataset quality from model performance. A dataset can be well documented and internally consistent yet poorly matched to a target task; conversely, strong model performance on one benchmark does not prove the data are broadly representative or safe.
- Treat label quality as more than annotator agreement. Label definitions, ambiguity, expertise, adjudication, missingness, class boundaries, temporal/contextual validity, and systematic annotator/model bias can all affect supervision quality.
- Explain coverage in relation to the intended population/environment, including rare but important cases, languages, modalities, geographies, devices, user groups, failure modes, and temporal changes where relevant. Balance alone does not prove representative coverage.
- Distinguish data errors from distribution shift. Cleaning mislabeled/corrupt examples addresses quality defects; a deployment population changing over time requires monitoring/recollection/reweighting or other adaptation even if historical data were correct.
- Explain data leakage and contamination as lifecycle failures. Training or selection data must not incorporate information from protected evaluation/test targets in a way that invalidates the estimate; near-duplicates, derived records, prompt/test reuse, and temporal leakage can matter even without exact duplicate rows.
- Explain data maintenance as ongoing. Real systems can require refresh, versioning, deprecation, deletion propagation, re-labeling, drift checks, access changes, and re-evaluation after source/model/policy changes rather than treating a dataset as permanently fixed.
- Treat data documentation as an evidence artifact, not a guarantee. Datasheets/cards/metadata can record provenance, intended use, composition, collection, limitations, and risks, but claims still require validation against the concrete dataset/version.
- Explain privacy/security/legal constraints as data-design requirements without duplicating their canonical owners. Minimization, access control, retention, consent/permission, licensing, residency, secret handling, and sensitive-attribute treatment can constrain what data may be collected or shared.
- Explain that data-centric interventions can occur before, during, and after model training: data collection/selection, cleaning, labeling, augmentation/generation, curriculum/reweighting, hard-example mining, evaluation-set design, feedback acquisition, and operational data maintenance are mechanism families rather than one workflow.
- Keep `synthetic-data/` as the currently selected direct child and do not infer additional data-centric children such as datasets, labeling, augmentation, data valuation, active learning, weak supervision, or data quality until architecture explicitly selects them.
- Keep concrete datasets and dataset versions in `catalog/datasets/`; keep experiment-specific splits, annotations, generated files, quality measurements, data pipelines, and remediation decisions with their applicable catalog/evidence/project owners.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Use the canonical entity references as research inputs for data-centric lifecycle and trustworthy-data boundaries when reader-facing rendering is activated.

## Validation

- Data-centric ML is not defined as `more data` or as a replacement for model-centric development.
- Data quality/coverage claims are scoped to the intended task/population/environment rather than treated as context-free.
- Provenance, versioning, data leakage/contamination, and lifecycle maintenance remain explicit.
- Strong benchmark/model performance is not treated as proof that a dataset is broadly representative or trustworthy.
- Concrete datasets, files, splits, pipelines, measurements, and remediation decisions remain outside the reusable domain owner.
- Direct-child navigation contains only currently materialized selected descendants.
