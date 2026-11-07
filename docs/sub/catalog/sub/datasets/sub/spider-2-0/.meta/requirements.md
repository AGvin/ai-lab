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

## Scoped original-source qualification — 2026-11-08

- **Spider 2.0** is the original **2024 enterprise text-to-SQL and database-workflow benchmark** maintained by `xlang-ai/Spider2`, not Spider 1.0, BIRD, a database engine, or an independent canonical dataset for each task configuration. Its first-party overview lists **547 Lite** and **547 Snow** tasks as separate evaluation settings, which must not be summed into 1,094 independently authored benchmark questions.
- The published **DBT** setting has a documented inventory inconsistency: the root source counts **68 tasks**, its dedicated README mentions **69 examples**, and an observed examples directory has **70 entries**. The exact scored subset must be pinned before asserting a definitive count. An **2026-08-12 publisher notice** reports suspended/disrupted Snowflake access; no subsequent restoration was verified, and reproducibility requires authorized cloud credentials, quotas, task revisions, pinned evaluation suite, and billing/privacy safeguards.
- Source repository **MIT software licensing** does not grant separate rights to all third-party warehouse tables, hosted SQL data, or evaluation content. Published leaderboard measurements and raw ground-truth tables differ from the benchmark identity.
- Original first-party sources: https://github.com/xlang-ai/Spider2 ; https://github.com/xlang-ai/Spider2/tree/main/spider2-lite ; https://github.com/xlang-ai/Spider2/tree/main/spider2-snow ; original paper https://arxiv.org/abs/2411.07763
- Source gate qualifies only the existing original dataset identity, public publisher-described settings, dated access issues and data-rights uncertainty. No Snowflake connection, query execution, reconciliation of every DBT directory, independent evaluation, legal/privacy/security audit, whole-repository schema/cache/CI/render, clean or final credit.
