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
