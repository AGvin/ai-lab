# Documentation Requirements

## Requirements

- Identify **SciFact** as original Ai2 **2020** scientific claim verification data: approximately **1.4K expert-written claims** with science-paper abstract evidence, support/refute labels and rationale spans, distinct from Qasper full-document QA, DROP paragraph operations, ARC/OpenBookQA question-choice datasets, a fact-checker model, evaluation harness or downstream BEIR/SCIVER packaging.
- Describe original claim `claims_train.jsonl`, `claims_dev.jsonl`, unlabeled-for-gold `claims_test.jsonl` and `corpus.jsonl` evidence abstract data. Original repository explicitly states **test gold evidence and labels are not publicly available** for local scoring.
- Preserve the original EMNLP 2020 paper's roughly **1.4K claims** separately from current publisher Hub builder **1.0.0**, which reports **1,261 train / 450 validation / 300 test claim examples** and a separate **5,183-abstract corpus**. The original and builder release/split packaging must not be silently normalized or scored interchangeably; the exact difference was not item-level audited.
- Material source-rights caveat is mandatory. Original first-party `allenai/scifact/LICENSE.md` grants **CC BY 4.0** for claims/evidence annotations, **ODC-By 1.0** for S2ORC-origin abstracts, **Apache-2.0** for code. Publisher-managed `allenai/scifact` Hub card instead marks the complete dataset **CC BY-NC 2.0**. Do not declare all files commercially reusable, noncommercial-only, or fully third-party rights-cleared without pinning the exact distribution and resolving the conflicting terms.
- Original claims and underlying scientific abstracts differ in ownership; source-abstract third-party copyrights/licensing and derivative data terms require separate review. Respect evidence labels, article identifiers and benchmark release when making operational claims.
- Historical baseline, COVID demo, SCIVER task, BEIR mirror and live leaderboard are separate software/aggregation/usage surfaces, not extra original SciFact datasets or currently verified model rankings.
- Cite original Ai2 published repository, original component `LICENSE.md`, EMNLP 2020 original paper, current Ai2 open-data listing, publisher Hub dataset card and builder metadata.
- Reuse `catalog/producers/a/ai2` with one new reciprocal `produced-by` / `produces` pair; preserve accepted ARC/OpenBookQA/DROP/Qasper producer relations without new producer or producer-gate credit.
- Keep license source contradiction and original hidden-test limitations visible in reader; review decision-support impact without unverified practical rankings.

## Validation

- One original `catalog/datasets/scifact` identity; three new authored files, one datasets-index link and three producer current-source updates.
- Ai2's resulting five data producer relations are exact reciprocals, no duplicate Ai2 entity.
- Seven-path scoped validation is not whole-catalog schema/cache/CI, final render, complete eight-root clean cycle, runtime benchmark evaluation or comprehensive legal audit.

## Scoped original-source qualification — 2026-11-08

- **SciFact** is the 2020 EMNLP Ai2 scientific-claim verification benchmark originally described as **~1,400 expert-written claims** with research-abstract evidence and SUPPORT/CONTRADICT rationales. The original code and data release expressly withheld gold test labels/evidence; later publisher Hub builder counts (1,261 train / 450 validation / 300 test claim rows and 5,183 abstracts) reflect a separately defined distribution/revision.
- A material **publisher license discrepancy remains open**: original `allenai/scifact/LICENSE.md` says **CC BY 4.0** for claims/annotations, **ODC-By 1.0** for S2ORC abstracts, **Apache-2.0** for code; Ai2 Hub marks the whole distribution **CC BY-NC 2.0**. Do not infer commercial-use approval or a single all-content grant from either source.
- First-party sources: https://github.com/allenai/scifact ; https://github.com/allenai/scifact/blob/master/LICENSE.md ; https://huggingface.co/datasets/allenai/scifact ; https://aclanthology.org/2020.emnlp-main.609/
- Acceptance is a scoped first-party qualification of this existing dataset's published identity and limitations, **not** raw source-rights clearance, hidden-label recovery, executed tests, security/privacy/legal review, whole-repository schema/cache/CI/render, clean or final gate.
