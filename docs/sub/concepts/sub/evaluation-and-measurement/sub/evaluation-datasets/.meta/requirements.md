# Documentation Requirements

## Requirements

- Use the reader-facing title `Evaluation Datasets`.
- Define an evaluation dataset as a versioned collection or sampling specification of inputs, cases, contexts, trajectories, expected properties, references, labels, annotations, rubrics, metadata, or related evidence inputs used to evaluate a model, component, workflow, or AI system under a defined evaluation design.
- Distinguish an evaluation dataset from a benchmark. The dataset supplies evaluation cases/data; a benchmark additionally specifies the task/protocol, metrics/scoring, constraints, and comparison/reporting rules.
- Distinguish an evaluation dataset from a metric, judge, or result. Labels/references/rubrics can support scoring, while the measurement procedure and resulting values remain separate concepts/evidence.
- Treat representativeness as relative to an intended population, workload, operating environment, risk surface, or decision. Do not describe a dataset as inherently `representative` without stating what distribution/use it is intended to represent and what important coverage limitations remain.
- Explain that evaluation datasets can be static or dynamically sampled, public or private, naturally observed or deliberately constructed, human-curated or synthetic/model-generated, and can contain ordinary, edge, rare, negative, adversarial, multilingual, multimodal, long-context, safety, regression, or historical-incident cases according to the evaluation need.
- Require documented provenance and construction context where relevant: source/population, collection/sampling process, time period, inclusion/exclusion criteria, annotation process, transformations/filtering/deduplication, synthetic generators, licenses/consent/privacy constraints, known biases, and intended/unsupported uses.
- Require dataset/version identity for reproducible comparison. Adding/removing cases, changing inputs, references, labels, rubrics, metadata, preprocessing, sampling weights, or scoring-relevant annotations can create a materially new evaluation version and must not be silently compared as the same test set.
- Distinguish training/development/validation use from held-out evaluation use. Reusing a test set for prompt/model/tool tuning, repeated model-selection optimization, or manual debugging can leak evaluation information and reduce its value as independent generalization evidence.
- Explain contamination and overlap risks beyond exact duplicates. Near-duplicates, paraphrases, benchmark-derived training data, public answer keys, synthetic transformations of known cases, or repeated exposure can make a nominally held-out dataset less independent.
- Explain that references/labels/rubrics are evidence artifacts rather than automatic ground truth. Human labels can disagree or contain errors; synthetic/model-generated labels can reproduce generator biases/errors; open-ended tasks can have multiple acceptable outputs. Ambiguity and adjudication policy should be represented explicitly where material.
- Distinguish class/task balance from deployment prevalence. Deliberately oversampling rare or high-risk failures can improve diagnostic power without representing real-world frequency; evaluation reports must interpret weighted/stratified results according to the sampling design.
- Include important subgroup, boundary, rare-event, and failure-category coverage when those dimensions affect the intended use or risk, while avoiding unsupported claims that one finite dataset covers all future users, attacks, environments, or distribution shifts.
- Explain that dataset size alone does not determine evaluation quality. Coverage, independence, label/reference quality, variance, difficulty, diversity, temporal relevance, and fit to the evaluation question can matter more than raw example count.
- Distinguish source data retention from evaluation artifacts when verification requires access to originals. Derived transcripts, crops, OCR text, retrieved chunks, or synthetic transformations can lose information needed to audit errors.
- Keep concrete evaluation dataset identities, files/records, dataset cards/datasheets, current versions, licenses, download locations, annotations, benchmark membership, access restrictions, and concrete test cases with their applicable catalog/dataset/evidence/project owners.
- Use the canonical entity references as research inputs for documented test-set conditions and dataset provenance/composition/use boundaries when reader-facing rendering is activated.

## Validation

- An evaluation dataset is not equated with a benchmark, metric, judge, score, or complete evaluation design.
- Representativeness is always scoped to a stated target distribution/use/risk rather than treated as an inherent dataset property.
- Versioning covers materially changed cases, labels/references, preprocessing, sampling, and scoring-relevant metadata.
- Held-out status is not assumed after repeated tuning/exposure, and contamination is not limited to exact duplicates.
- Human or synthetic labels/references are not treated as infallible ground truth.
- Dataset size is not presented as a sufficient proxy for coverage or evaluation quality.
- Concrete dataset identities, records, licenses, versions, and access details remain outside the reusable evaluation-dataset concept owner.
