# Documentation Requirements

## Requirements

- Identify FrontierMath as Epoch AI's released mathematical-reasoning benchmark program with original unpublished expert-crafted mathematics problems, mathematically verifiable outcomes and model-evaluation methodology.
- Separate the **Tiers 1–3** and research-level **Tier 4** assessments and versioned public/private splits; the June 12, 2026 **v2** release revised the benchmark to 338 validated problems (295 in Tiers 1–3 and 43 in Tier 4), correcting substantial errors from earlier versions. Scores from original v1 and v2 are not directly interchangeable.
- Keep the smaller *public examples* distinct from the privately administered full scored problem sets; third-party users cannot reproduce private-tier scoring merely from the public samples. Respect official access and licensing boundaries.
- Distinguish FrontierMath Tiers 1–4 from the separate FrontierMath Open Problems program and the formalized FrontierMath Erdős problem set. They are related evaluated collections with different proof/verification methodology and access; do not claim that ordinary numeric-answer grading applies to all.
- Preserve sponsorship disclosure: OpenAI funded some development and obtained special access to subsets, but Epoch AI is the benchmark producer. Contamination and privileged-access risk must be considered in interpreting evaluation results.
- Scope reported accuracy to precise benchmark version/split, model version, tool access, sampling and pass@k/retry rules, answer-verification strategy and compute constraints. Avoid quoting vendor leaderboard ranks as independently replicated facts.
- Maintain Epoch AI producer provenance and reciprocal relation.

## Validation

- Exact public/private v2 status and task counts are sourced from the benchmark operator, not inferred from unrelated leaderboards.
- Private evaluation problem sets are not falsely represented as public downloads.
- FrontierMath benchmark does not conflate v1/v2, math tier variants, research open problems or the Erdős formal proof track.
- Reciprocal Epoch AI provenance resolves correctly.

## Scoped original-source qualification — 2026-11-08

- **FrontierMath** is the **Epoch AI** expert-authored mathematics benchmark program. Its **2026-06-12 V2** release corrected defects in earlier items and now describes **338 problems**, comprising **295** in Tiers **1–3** and **43** in research-level **Tier 4**. The publisher made **12 examples public**, while ordinary leaderboard evaluations operate on **private** benchmark sets. Those V2 counts cannot be applied to the original V1 or independent FrontierMath Open Problems / Erdős collections.
- Epoch AI discloses **OpenAI funding and special access to a subset**; this is an evaluation fairness/contamination concern, not proof OpenAI produced or owns the benchmark. The authors' internal model leaderboard measurements, selected private questions, tool access, sampling and answer-checking remain independent of the canonical dataset source identity.
- Verified original publisher sources: https://epoch.ai/frontiermath ; https://epoch.ai/benchmarks/frontiermath-tiers-1-3-v2 ; https://epoch.ai/benchmarks/frontiermath-tier-4-v2
- Qualification covers existing Epoch AI ownership, current source-described V2 task/release/access boundaries and method only. No private item access, independent arithmetic/proof verification, model benchmark run, full source-rights/legal/security/privacy review, repository-wide schema/cache/CI/render, clean or final gate.
