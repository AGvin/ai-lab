# Documentation Requirements

## Requirements

- Identify LiveCodeBench as a continuously updated coding benchmark/dataset family with explicit versioned releases rather than one timeless fixed question set.
- Preserve the distinction among code-generation, code-execution, test-output-prediction, self-repair, and other upstream scenarios when results or dataset slices differ.
- Keep dataset releases distinct from the LiveCodeBench runner/evaluation implementation, leaderboards, model adapters, and generic code-evaluation concepts.
- Preserve the project's contamination-mitigation goal and time-window semantics without claiming that recency alone proves a model is contamination-free.
- Treat release membership, task counts, default release aliases, evaluation timeouts, supported model adapters, and leaderboard results as mutable/version-sensitive facts.

## Validation

- Results identify the applicable LiveCodeBench release and scenario when those conditions matter.
- The benchmark family is not reduced to one historical release snapshot.
- Runner implementation details are not presented as intrinsic dataset identity facts.

## Scoped original-source qualification — 2026-11-08

- **LiveCodeBench** is the continuously updated contest-derived **coding benchmark family**, not one immutable 400-problem test or a serving product. Publisher-documented scenarios include code generation, code execution, test output prediction and self-repair, with release-date task-window distinctions.
- Its original `release_v1` comprised **400 tasks (May 2023–March 2024)**, whereas the historically listed `release_v6` comprised **1,055 tasks through April 2025**. Those are version-specific facts, **not a claim that release_v6 is the latest in November 2026**, nor that scores from different releases are directly comparable. Competition-origin problem data can have rights requirements beyond the GitHub evaluator's repository license.
- First-party sources: https://github.com/LiveCodeBench/LiveCodeBench ; https://livecodebench.github.io/ ; https://huggingface.co/livecodebench/
- Bounded original-source acceptance covers identity, released version/scenario boundaries and provenance. No copied competition questions, rights clearance, generated-code execution, current leaderboard/freshness audit, root-wide CI/render, clean or final credit.
