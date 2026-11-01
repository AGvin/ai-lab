# Documentation Requirements

## Requirements

- Identify original SimpleQA as OpenAI's released October 30, 2024 source dataset with 4,326 short-form factual questions and answers selected by agreement between independent AI trainers.
- Preserve the short-answer, single-reference factuality purpose. Do not infer broad model safety, real-world truthfulness, long-form fact-checking or browsing competence from a score.
- Distinguish this dataset from the `simple-evals` evaluator, grader model, hosted evaluations, mirrors and model-results tables.
- Distinguish original SimpleQA from Google DeepMind and Google Research's published 2025 SimpleQA Verified, a separately curated 1,000-question derivative; do not combine publisher, size, sampling or results.
- The evaluation labels responses correct, incorrect or not attempted; preserve the dataset revision, prompted grader/rubric, abstention treatment, model setup and available tools when comparing runs.
- OpenAI's third-trainer spot check of 1,000 questions estimated an approximately 3% inherent question error rate after disagreement adjudication. Do not imply every answer is valid or immutable; consider source ambiguity, revisions, topical bias, public exposure and contamination.
- The original `simple-evals` repository announced in July 2025 that it would stop updating new model results while retaining benchmark implementations. This does not withdraw the historical SimpleQA dataset.
- The original repository is MIT-licensed and the README labels SimpleQA MIT, but this does not independently clear every cited external factual source or downstream repackaging.
- One reciprocal `produced-by` SimpleQA / `produces` OpenAI pair; the Google-derived benchmark must not be attributed exclusively to the OpenAI original producer.
- Include original OpenAI release, original research paper, official evaluator, license, and derivative research reference. Do not claim runtime benchmark execution or complete content-rights clearance.

## Validation

- One canonical source identity `catalog/datasets/simpleqa`; no duplicate data or software identity.
- Both producer-dataset inverse relations, index link and metadata paths resolve to canonical owner nodes.
- This is a six-path scoped research addition, not a complete eight-root audit, final render, global cache/CI/schema verification or completed clean pass.
