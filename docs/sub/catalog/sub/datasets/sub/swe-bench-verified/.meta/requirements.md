# Documentation Requirements

## Requirements

- Identify SWE-bench Verified as a released 500-instance curated SWE-bench test subset created by OpenAI jointly with the original SWE-bench authors, not an unrelated standalone issue corpus, evaluation harness or SWE-bench Pro.
- Original August 2024 screening used 93 developers, 1,699 candidate samples and three independent reviewers per sample. Selection did not guarantee every retained task was unambiguous or every test correct.
- Prominently state OpenAI stopped reporting Verified for frontier coding capability in February 2026 due to residual test defects and training-data contamination.
- The 59.4% finding is strictly from 138 selectively audited hard-to-solve instances, not a prevalence estimate over all 500 tasks.
- Preserve dated recommendation history: OpenAI recommended Pro in February 2026, then retracted that recommendation in July 2026 after auditing the 731-task Pro V1 public split. Do not extrapolate that audit directly to September 2026 Pro V2 without independent V2 evidence.
- Distinguish source SWE-bench family, Verified subset, Lite/Multimodal variants, independent Pro V1/V2, harness software, test containers, leaderboards and scores; do not treat those as interchangeable result contracts.
- Require pinned data revision, issue/base commit, model/agent/scaffold, prompts, verifier, harness and runtime environment for reproductions. Historical accessibility does not imply an uncontaminated contemporary benchmark.
- The SWE-bench source MIT repository LICENSE is not complete clearance for third-party code, original GitHub issues, patches and tests. Current source-review did not establish all dataset redistribution rights.
- OpenAI's producer relation reflects joint curation of Verified only, not exclusive authorship of original SWE-bench data. Reconcile its exact reciprocal `produces` with one family `derived-from` / `has-derivative` pair.
- Render official release, maintained Hub dataset, two dated 2026 audits, original source repository and exact code LICENSE. No model execution, scoring, full rights audit or beneficial ownership review was performed.

## Validation

- One canonical curated subset identity without source/harness duplication.
- Both inverse provenance relations and local reader/index links resolve.
- February and July 2026 scopes are distinguished and do not endorse Pro V2 without a V2 audit.
- Scoped content checks are not current-head full schema, CI, final rendering or clean research pass.

## Scoped original-source qualification — 2026-11-08

- **SWE-bench Verified** is the distinct human-reviewed **500-issue subset** of original SWE-bench, curated by OpenAI together with the SWE-bench authors in **August 2024**. OpenAI's first-party retrospective documents **93 professional developers** screening **1,699 candidate samples** and retaining 500 judged feasible under their evaluation rubric; this is not a guarantee that every accepted test is complete or every task still cleanly differentiates models.
- In **February 2026** OpenAI stopped reporting Verified as an informative frontier coding benchmark because of contamination and narrow/incorrect tests. Its **59.4% material-defect finding applies to a selectively audited set of 138 difficult tasks, not all 500**. A later July 2026 Pro V1 audit also changed OpenAI's comparative recommendation; these are dated suitability reviews, not new dataset families or source gate identities.
- Verified first-party sources: https://openai.com/index/introducing-swe-bench-verified/ and https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ and https://www.swebench.com/verified and https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified
- Original curated subset lineage and historical/current first-party evaluation limits are accepted, not full rights to original third-party GitHub issue/test contents, live agent scoring, independent benchmark contamination or legal/security audit, schema/cache/CI/render, clean or final credit.
