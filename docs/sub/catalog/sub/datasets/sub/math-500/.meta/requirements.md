# Documentation Requirements

## Requirements

- Identify MATH-500 as the concrete 500-problem held-out MATH evaluation subset chosen and released by OpenAI with *Let's Verify Step by Step*, not the original full MATH dataset or PRM800K's 800,000 process-supervision step labels.
- Attribute the underlying competition-math questions and original MATH research to the Hendrycks et al. research authors; OpenAI is responsible for selecting/publishing this 500-problem evaluation split, not for originating every MATH question. Hugging Face H4 is a republisher of the subset, not a new source-data producer.
- The OpenAI PRM800K repository explains that 4,500 of the prior MATH test problems were added to training and 500 were selected uniformly at random for evaluation. Preserve this historically described split context without implying 500 further independent questions or a general new MATH version.
- Source identity is the original OpenAI `prm800k/math_splits/test.jsonl` Git LFS file. Pin the exact Git/LFS object and compare materialized H4 exports before asserting byte-identical data; the H4 card links to the original but an exact content digest was not verified in this intake.
- Treat evaluator implementation, sampling, grading, exact-answer normalization, prompt settings and model results as separate evaluation contracts. The publisher explicitly warns that math answer-equivalence grading can reject correct or accept incorrect answers. No verified benchmark score or inference was produced.
- The H4 MATH-500 card inspected in this intake supplies no explicit dataset license. Original OpenAI PRM800K and Hendrycks MATH repositories contain MIT software/documentation LICENSE files, but those do not independently prove all rights in the underlying competition questions or redistribute them under an unqualified MIT data grant.
- Do not copy or redistribute test questions under the assumption that repository code licenses settle original data rights; obtain appropriate source rights and comply with applicable attribution/conditions. No legal opinion or third-party rights audit is implied.
- Preserve released historical availability while noting that the original PRM800K repository is archived; no current maintenance guarantee is established.
- Producer `catalog/producers/o/openai` refers only to OpenAI's curated subset and release. It must not imply OpenAI authorship/ownership of the full MATH corpus or unqualified rights to all original questions. Keep an exact inverse `produces` relation.
- Provenance is attributed from first-party publications, not a complete beneficial-ownership, current indirect-holdings or sanctions investigation. No current Russian ownership/control inference is supported by this review.
- Render original PRM800K selection/split, H4 distributor card, original Hendrycks MATH repository and both exact MIT repository LICENSE locations as separate official resources.

- Relate the subset to the now-canonical original MATH dataset through `derived-from catalog/datasets/math` and its reciprocal `has-derivative` without transferring original author rights or mistaking this for a learned model derivative.

## Validation

- Exactly one source-backed canonical MATH-500 subset record; the full MATH, PRM800K labels, evaluator, mirrors or score variants are not silently conflated or given duplicate intake credit.
- Reciprocal OpenAI produced-by/produces relations have exact canonical IDs; source-data versus subset-curation authorship is explicit.
- Index, source profile and OpenAI producer reader links have canonical targets; bounded checks do not establish complete JSON Schema, cache/CI, final renderer or two whole-catalog clean passes.

## Scoped original-source qualification — 2026-11-08

- **MATH-500** is the original **500-problem held-out selection** from the larger **Hendrycks MATH** corpus made and distributed by OpenAI with its **2023 PRM800K / Let's Verify Step by Step** research. The original `openai/prm800k` repository preserves the 500-item `prm800k/math_splits/test.jsonl` Git LFS test split, distinct from the **800,000 process-supervision correctness labels** and the rest of the original MATH dataset.
- The OpenAI repo explains moving 4,500 prior MATH test questions to training and preserving 500 as held-out; OpenAI is the **subset curator**, not author of every original competition math question. Hugging Face H4's MATH-500 is a redistribution of this selection, not a new independent source corpus. Verify exact LFS/dataset revisions and grader answer-equivalence behavior before comparing reported scores.
- Verified publisher sources: https://github.com/openai/prm800k and https://github.com/openai/prm800k/blob/main/prm800k/math_splits/test.jsonl and https://github.com/hendrycks/math and https://huggingface.co/datasets/HuggingFaceH4/MATH-500
- Original released subset and derived-from boundary source-qualified only. No byte-for-byte H4-to-LFS equivalence, rights clearance for all third-party competition questions, math model execution, independent grader/score audit, complete security/legal/privacy/CI/render, clean or final credit.
