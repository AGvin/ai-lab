# Documentation Requirements

## Requirements

- Identify SWE-bench as the concrete dataset family built from real-world software repository issues and repository states for evaluating systems that generate patches intended to resolve those issues.
- Keep dataset/task identities distinct from the SWE-bench evaluation harness, Docker execution environment, leaderboard/service surfaces, scoring/reporting procedure, and generic software-engineering benchmark concepts.
- Preserve major dataset variants only as source-backed variant identities. Current upstream material includes full SWE-bench plus variants such as Lite, Verified, Multimodal, and Multilingual; do not compare results across variants as though they were the same test set.
- Preserve the specific Verified boundary when discussed: it is a curated subset whose instances were reviewed by software engineers for solvability, not a claim that every benchmark instance or every future task is unambiguous.
- Treat task repositories, issue/commit snapshots, container images, harness versions, dataset revisions, supported architectures, execution resources, and leaderboard policies as mutable/version-sensitive facts.
- Preserve contamination and patch-leakage risk for public repository-derived tasks and do not assume every evaluated model or agent is independent of public benchmark/repository history.
- Keep repository-level software-engineering scope distinct from function-completion datasets such as HumanEval and from broad knowledge tests such as MMLU.
- Include current upstream repository, documentation, and dataset-card references.

## Validation

- The page profiles the SWE-bench dataset family and does not collapse it with the evaluation harness or one leaderboard snapshot.
- Results from different SWE-bench variants or harness conditions are not directly compared without matching conditions.
- Verified is described as a curated solvability-reviewed subset rather than a generic quality label applied to the whole family.
- Current resource and architecture requirements are not presented as timeless characteristics of the dataset itself.
