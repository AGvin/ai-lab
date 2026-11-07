# Documentation Requirements

## Requirements

- Identify **Qasper** as Ai2's independently published **2021** long-document scientific-paper question-answering dataset: **5,049 questions on 1,585 original NLP papers**, distinct from DROP, OpenBookQA, ARC, SCROLLS aggregation, baseline model and evaluator.
- A question writer saw only title and abstract; a separate NLP practitioner answered from full text and selected supporting evidence. Extractive, free-form, yes/no and unanswerable forms are represented, not only span retrieval or closed-book factoids.
- Preserve **paper rows** versus nested **question counts**. Original publisher dataset_infos for builder **0.3.0** has **888 training, 281 validation and 416 test paper records** (1,585 total); these must not be called 1,585 questions. Pin dataset/split/revision and exact answer/evidence scoring when comparing model performance.
- Publisher-managed dataset card declares **CC BY 4.0**, but underlying scientific paper text comes from **S2ORC**. Do not treat that declaration as an independent blanket clearance of third-party papers, figures/tables, source licenses, full-text rehosting or commercial reproduction. Check file-level rights and attribution before downstream data use.
- Published annotation schema includes pseudonymous worker IDs, expertise background and evidence metadata. Apply proportionate privacy review before copying raw records and never state a privacy certification that was not performed.
- Differentiate original published dataset, borrowed research-paper source corpus, implementation/model/evaluation software, historical results, and later suites such as SCROLLS; do not add unverified leaderboard performance or independent runtime claims.
- Cite current Ai2 original open-data portfolio, publisher Hub dataset card and builder metadata, original NAACL 2021 paper, and Ai2 baseline code only for implementation boundary.
- Reuse existing `catalog/producers/a/ai2`, add one exact `Qasper produced-by Ai2` ↔ `Ai2 produces Qasper` inverse pair; preserve the earlier ARC/OpenBookQA/DROP pairs with zero duplicate producer acceptance.
- Include source-rights caveat and exact public dataset scope in reader; update dataset index and existing Ai2 entity/requirements/reader, reviewing decision-support impacts without unrelated changes.

## Validation

- One canonical `catalog/datasets/qasper` node with three new authored files; datasets index has one entry.
- Ai2 remains one producer with four exact reciprocal dataset links.
- Seven-file scoped authoring/readback is not global schema/cache/CI, final renderer, full eight-root clean cycle, model execution, or complete data-rights assessment.

## Scoped original-source qualification — 2026-11-08

- **Qasper** is Ai2's 2021 NAACL scientific-paper QA benchmark, consisting of **5,049 questions across 1,585 research papers**. A writer works from title and abstract; a separate annotator supplies answers and evidence after reading full text. The 0.3.0 dataset builder's **888/281/416** train/validation/test numbers count *papers*, not individual questions.
- The original Hub card declares **CC BY 4.0** for the dataset, but source article full text derives from **S2ORC** and is not independently licensed for universal redistribution under that declaration. Baseline LED implementation, full text, answer grading, question set and later suite/leaderboard packaging remain distinct.
- First-party sources: https://huggingface.co/datasets/allenai/qasper ; https://github.com/allenai/qasper-led-baseline ; https://aclanthology.org/2021.naacl-main.365/
- Scoped acceptance concerns an existing published corpus's provenance, question/paper count and bounded license declaration, **not** third-party full-text rights, privacy checks, model runs, global schema/cache/CI/render, clean or final acceptance.
