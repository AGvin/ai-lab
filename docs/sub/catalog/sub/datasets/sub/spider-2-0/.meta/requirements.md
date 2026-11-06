# Documentation Requirements

## Requirements

- Identify the original independently published **Spider 2.0** enterprise text-to-SQL and data-workflow benchmark introduced with the 2024 paper, rather than Spider 1.0, BIRD, a SQL-trained model, a generic SQL agent, a database platform or leaderboard.
- Keep **Spider 2.0-Lite** (BigQuery, Snowflake, SQLite), **Spider 2.0-Snow** (Snowflake) and **Spider 2.0-DBT** (repository-based DuckDB/DBT transformations) as scoped evaluation settings under one original benchmark, not automatically three independent publisher/producer/dataset credits.
- The top-level publisher README currently reports **547 Lite / 547 Snow** examples. These are overlapping or corresponding benchmark configurations, not evidence of 1,094 independent queries. DBT count is **source-conflicted**: root README says **68 tasks**, DBT child README **69 examples**, and the current examples directory has **70 children**. Preserve discrepancy and require a pinned evaluation set before quoting exact scored DBT totals.
- Separate question JSONL, warehouse tables, evaluation suite, Docker or tool-call-based Spider-Agent, leaderboard scores, original BIRD/Spider benchmarks and DBT source projects. Code and dataset rights are not necessarily identical.
- The repository's MIT LICENSE is a source-code grant (copyright `bird_sql`); do not infer third-party SQL database/table rights, Snowflake-hosted data, Google BigQuery sample data, commercial redistribution rights, or an all-payload commercial clearance.
- The publisher's 2026-08-12 Snow notice reports an account suspension/disruption; documentation and MFA access guidance are not proof that service access has been restored as of this review. BigQuery and/or Snowflake may involve credentials, quotas, availability, cloud billing and query costs.
- Published benchmark scores are version-, dataset-, grading-, warehouse-, language-model- and runtime-dependent. Publisher 2025 evaluation fixes and mutable leaderboards invalidate silent comparisons to older scores.
- The original paper credits Fangyu Lei and collaborators; the GitHub organization or copyright string does not establish a separate verified legal producer. Do not invent an organizational producer identity.
- Preserve data privacy, SQL execution, destructive query, credential and network risks when documenting evaluation setup. Do not run third-party queries or supply credentials during catalog intake.
- Final generated reader/cache/schema/CI checks remain downstream of two complete clean research passes.

## Validation

- One new canonical dataset triad with one direct `datasets/README.md` navigation entry; no duplicate alias or platform/agent entity.
- Exact first-party source URLs, conflicting DBT counts, version/setting separation and license/access warnings.
- Scoped write/diff/readback only; no full eight-root clean cycle, global schema/cache/CI/render or executed database evaluation.
