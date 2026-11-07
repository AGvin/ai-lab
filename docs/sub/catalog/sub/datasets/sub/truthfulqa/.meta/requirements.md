# Documentation Requirements

## Requirements

- Identify TruthfulQA as the released concrete question-and-reference-answer research dataset developed by Stephanie Lin, Jacob Hilton and Owain Evans. Distinguish it from evaluation harnesses, metrics, specialized judge models and benchmark result tables.
- The original paper described 817 questions and 38 categories for its historical release. Do not silently apply those figures to the mutable current CSV: the original repository records January 2025 question edits/removals and deletion of the obsolete Indexical Error: Time category.
- Distinguish the January 2025 revised binary multiple-choice setting, using Best Answer versus Best Incorrect Answer with randomized option order, from historical MC1/MC2 and free-form generation protocols. These are settings of one source dataset rather than additional dataset identities.
- Separate truthfulness from informativeness for generation tasks; distinguish MC1, MC2, revised binary and judge-based metrics. Original specialized fine-tuned GPT-3 judge models are unavailable externally and are not claimed to generalize to arbitrary new questions.
- Pin an exact question CSV commit, evaluation instructions, choice ordering and scoring protocol when reproducing results. Public benchmark exposure creates contamination risk, while dataset revisions limit cross-version comparisons.
- Attribute research authorship to the three named authors. Their reported Oxford/OpenAI affiliations do not establish sole corporate authorship or ultimate ownership; do not invent an OpenAI, Oxford or fictitious TruthfulQA corporate producer relation.
- The original repository contains an Apache-2.0 LICENSE. Do not infer clearance of every third-party answer citation, underlying source, unrelated mirror or downstream dataset from that file alone.
- The original authors report incomplete revalidation of remaining questions and sources after the 2025 changes. Historical misconceptions and time-sensitive claims limit current factuality inference; performance does not certify universal truthfulness or safety.
- Provenance identifies author attribution, not exhaustive beneficial-ownership, indirect-holdings or sanctions findings. Never infer institutional control from a researcher's name or affiliation.
- Include links to the original research repository, current CSV, paper, author-maintained revision explanation and exact repository LICENSE; do not duplicate the scoring or execution tutorial.

## Validation

- Exactly one canonical TruthfulQA source-dataset identity; revisions, metrics and tasks are not duplicate datasets.
- Document the three research authors, January 2025 revision, reproducibility boundary, answer-source rights uncertainty, incomplete revalidation and contamination risks without invented producer relations.
- Confirm local index destination resolves to canonical .meta/entity.yml and .meta/requirements.md; report bounded validation separately from repository-wide schema/cache/CI or clean-cycle acceptance.

## Scoped original-source qualification — 2026-11-08

- **TruthfulQA** is the research dataset by **Stephanie Lin, Jacob Hilton and Owain Evans**, introduced in **2021**; the historical paper described **817 questions across 38 categories**. Those figures apply to the historical release, not automatically to the mutable author-maintained `TruthfulQA.csv` after removals/revisions.
- The original author repository documents a **January 2025 binary multiple-choice update** pairing **Best Answer** with **Best Incorrect Answer**, with randomized answer order. Original MC1/MC2 and free-form generation evaluation use the same dataset but different score definitions; truthfulness and informativeness are distinct generation metrics.
- Verified first-party academic/source records: https://github.com/sylinrl/TruthfulQA and https://arxiv.org/abs/2109.07958 and https://aclanthology.org/2022.acl-long.229/
- Existing dataset identity, original authorship, dated historical/updated protocols and reference license are source-qualified only. Researchers' institutional affiliations do not establish sole corporate ownership. No current question-by-question validation, licensed third-party source-rights clearance, independent model/judge execution, contamination guarantee, whole-repo validation, clean or final gate.
