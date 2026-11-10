# Documentation Requirements

## Requirements

- Identify SWE-bench as the concrete dataset family built from real-world software repository issues and repository states for evaluating systems that generate patches intended to resolve those issues.
- Keep dataset/task identities distinct from the SWE-bench evaluation harness, Docker execution environment, leaderboard/service surfaces, scoring/reporting procedure, and generic software-engineering benchmark concepts.
- Preserve major dataset variants only as source-backed variant identities. Current upstream material includes full SWE-bench plus variants such as Lite, Verified, Multimodal, and Multilingual; do not compare results across variants as though they were the same test set.
- Preserve the specific Verified boundary when discussed: it is a curated subset whose instances were reviewed by software engineers for solvability, not a claim that every benchmark instance or every future task is unambiguous.
- The independently materialized Verified subset is unsuitable for unqualified frontier benchmark tracking per the February 2026 OpenAI audit. A July 2026 audit retracted the earlier Pro recommendation following problems in Pro V1; later V2 has a distinct release boundary.
- Treat task repositories, issue/commit snapshots, container images, harness versions, dataset revisions, supported architectures, execution resources, and leaderboard policies as mutable/version-sensitive facts.
- Preserve contamination and patch-leakage risk for public repository-derived tasks and do not assume every evaluated model or agent is independent of public benchmark/repository history.
- Keep repository-level software-engineering scope distinct from function-completion datasets such as HumanEval and from broad knowledge tests such as MMLU.
- Include current upstream repository, documentation, and dataset-card references.

## Validation

- The page profiles the SWE-bench dataset family and does not collapse it with the evaluation harness or one leaderboard snapshot.
- Results from different SWE-bench variants or harness conditions are not directly compared without matching conditions.
- Verified is described as a curated solvability-reviewed subset rather than a generic quality label applied to the whole family.
- Current resource and architecture requirements are not presented as timeless characteristics of the dataset itself.

## Scoped original-source qualification — 2026-11-08

- **SWE-bench** is the original **Princeton-led ICLR 2024** software-issue-to-patch evaluation dataset family by **Jimenez et al.**. Each issue is paired with a specific open-source repository snapshot and a proposed code patch is tested against a versioned test suite. The current first-party `SWE-bench/SWE-bench` repository tracks several **distinct** subsets and variants (full, Lite, Verified, Multimodal, Multilingual); a current harness command or leaderboard view is not an immutable dataset revision.
- The original public-issue data and environment are different from the accompanying Docker harness, model/agent scaffold, result leaderboard and product-specific submissions. Treat Verified as separately curated and historically assessed; the February 2026 OpenAI Verified deprecation and July 2026 revision of its Pro recommendation do not retroactively erase the original SWE-bench research release.
- Verified original publisher sources: https://github.com/SWE-bench/SWE-bench and https://swebench.com/SWE-bench/ and https://arxiv.org/abs/2310.06770
- Source acceptance covers the existing original family and first-party dataset/evaluation boundary only. No Docker evaluation, current leaderboard/rank certification, licensing of every third-party GitHub issue/code/test, independent model performance/contamination audit, whole-repo schema/cache/CI/render, clean or final credit.
