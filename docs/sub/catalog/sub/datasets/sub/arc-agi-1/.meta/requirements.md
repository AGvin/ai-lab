# Documentation Requirements

## Requirements

- Identify ARC-AGI-1 as François Chollet's original released Abstraction and Reasoning Corpus, a static grid-based abstract-reasoning benchmark introduced in 2019.
- Preserve the original task dataset and public training/evaluation sets, distinct from later semi-private/private competition holdouts. Track exact public-data revisions and benchmark scoring rules before comparing reported results.
- Keep ARC-AGI-1 distinct from the successor ARC-AGI-2 and interactive ARC-AGI-3; shared grid/puzzle terminology does not make their test sets or protocols interchangeable.
- Attribute original creation to François Chollet while treating subsequent ARC Prize Foundation competitions and governance as stewardship, not duplicate authorship.
- Keep contamination/leakage, evaluation protocol, repeated-trial rules, model version and compute budget explicit in scored comparisons.
- Do not duplicate interactive toolkit/benchmarking harness software, independent ARC Prize competitions, or derivative leaderboard pages as datasets.

## Validation

- Canonical identity and data access references describe the released ARC-AGI-1 benchmark.
- Original creator provenance and reciprocal producer relation are correct.
- ARC-AGI-1, ARC-AGI-2 and ARC-AGI-3 remain distinct identities.
- Benchmark scoring claims are qualified to the evaluated revision and compute protocol.

## Scoped original-source qualification — 2026-11-08

- **ARC-AGI-1** is the released **2019 Abstraction and Reasoning Corpus** created by François Chollet. The original first-party `fchollet/ARC-AGI` repository explicitly labels the version **v1**, and describes **400 public training plus 400 public evaluation** JSON grid-transformation tasks, with input/output example pairs, tests and exact grid correctness.
- The original public training/evaluation sets do not imply access to later ARC Prize semi-private/private contest holdouts. ARC-AGI-2 and the interactive ARC-AGI-3 are separate benchmark identities and evaluation protocols; model-score comparisons must specify dataset revision, trials, task exposure and compute/cost policies.
- Verified first-party original source: https://github.com/fchollet/ARC-AGI ; benchmark stewardship and rules: https://arcprize.org/arc-agi/1
- Scope accepted: existing dataset identity, original creator/release, public task format/splits and official lineage only. No benchmark task execution, verification of all individual examples, access to private holdouts, data reuse rights beyond published terms, independent model scores, full privacy/security/legal audit, repository-wide schema/cache/CI/render, clean or final gate.
