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

- Preserve the explicit original-to-derived dataset lineage with one `has-derivative` relation to `catalog/datasets/simpleqa-verified` and the inverse `derived-from` edge; Google DeepMind's curated 1,000-question revision is a separate publisher-and-selection identity, not a new variant of the original full dataset.

## Validation

- One canonical source identity `catalog/datasets/simpleqa`; no duplicate data or software identity.
- Both producer-dataset inverse relations, index link and metadata paths resolve to canonical owner nodes.
- This is a six-path scoped research addition, not a complete eight-root audit, final render, global cache/CI/schema verification or completed clean pass.

## Scoped original-source qualification — 2026-11-08

- **SimpleQA** is OpenAI's original **2024-10-30** short-answer factuality question benchmark with **4,326** published question/answer cases, evaluated with correct/incorrect/not-attempted labels. Publisher documentation explains selection and the limited independent question-spot-check process; this is not an assurance that every answer remains current or that a SimpleQA score proves general factual reliability.
- The dataset identity is distinct from the `simple-evals` software, grader or model-result tables. The **July 2025 discontinuation of new `simple-evals` result updates** does not withdraw the historical benchmark. The independently curated **2025 SimpleQA Verified** derivative by Google DeepMind/Google Research is a separate selection, not a renamed 4,326-question OpenAI release.
- Verified first-party sources: https://openai.com/index/introducing-simpleqa/ and https://github.com/openai/simple-evals and https://arxiv.org/abs/2411.04368
- Existing original dataset/release and official evaluator/derivative boundaries qualified only; no question-level fact checking, independent model grading, third-party answer source-rights audit, contamination proof, complete legal/privacy/security/CI/render, clean or final gate.
