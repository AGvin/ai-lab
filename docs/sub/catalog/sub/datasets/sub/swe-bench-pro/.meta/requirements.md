# Documentation Requirements

## Requirements

- Identify SWE-bench Pro as Scale AI's independently released long-horizon software-engineering agent evaluation benchmark, with code-repository issues and environment-based tests, distinct from the original SWE-bench dataset and its verified subset.
- Preserve version boundaries: the public V2 dataset released September 2026 includes 642 validated tasks in Harbor format, a HARD-51 subset and locked-protocol offline agent evaluation with fresh-sandbox re-grading. The earlier v1 dataset and harness are separate historical versions, not comparable by default.
- Distinguish the public open dataset from Scale's privately evaluated submissions and any hidden benchmark tasks; a public GitHub repository does not establish access to private evaluation datasets.
- Keep the individual V2 tasks, reference patches, agent execution containers, scenario selection and evaluation tooling as parts of the benchmark rather than independent benchmark products.
- Treat dataset revisions, task counts, repository coverage, failure-repair criteria, scoring protocol, evaluation time budgets, agent capabilities, test isolation and contamination checks as freshness-sensitive.
- Do not equate scores produced with legacy v1 evaluator and scores with locked-protocol V2. Model/agent benchmark performance is tied to harness, environment and exact revision.
- Preserve Scale AI as canonical producer; maintain reciprocal provenance.

## Validation

- SWE-bench Pro is not conflated with original SWE-bench or unrelated code benchmark leaders.
- V1/V2/HARD-51 version, split and evaluator boundaries are explicit and source-backed.
- Benchmark score comparisons are scoped to exact evaluation protocol and revision.
- The `produced-by` relation and producer inverse `produces` are reciprocal.
