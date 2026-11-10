# Spider 2.0

**Spider 2.0** is the original [2024 enterprise text-to-SQL benchmark](https://arxiv.org/abs/2411.07763) from Fangyu Lei and collaborators. It evaluates models and agents handling multi-step SQL/database workflows in realistic enterprise-like environments, rather than a standalone SQL agent, trained model or database hosting service.

## Benchmark settings and source-count differences

The original [project README](https://github.com/xlang-ai/Spider2) currently identifies **547 Spider 2.0-Lite** examples involving BigQuery, Snowflake and SQLite, and **547 Spider 2.0-Snow** examples on Snowflake. These are separately evaluated configurations, not necessarily 1,094 unique independent questions. Source data, evaluation suites, execution environments, access costs and leaderboard conditions differ between settings.

**Spider 2.0-DBT** covers project-level database transformation and code-agent workflows with DuckDB/DBT. The first-party inventory is **internally inconsistent**: the top-level README reports **68 tasks**, the [DBT README](https://github.com/xlang-ai/Spider2/tree/main/spider2-dbt) states **69 examples**, and the current `spider2-dbt/examples/` directory contains **70 children**. A directory listing is not a scored-task list. Pin release and evaluation manifest before making exact DBT sample-count or cross-benchmark claims.

This canonical dataset record groups the original project's Lite, Snow and DBT settings while preserving their separate task/evaluation boundaries. Spider 1.0, [BIRD](https://bird-bench.github.io/), any `Spider-Agent` runner, warehouse service and external LLM under test are not additional Spider 2.0 datasets.

## Access, licensing and execution risks

The [root MIT license](https://github.com/xlang-ai/Spider2/blob/main/LICENSE) covers distributed repository software. It does **not** independently establish unrestricted reuse of every third-party database, cloud warehouse, sample table, executable, result, screenshot or other underlying payload. Verify the actual asset and provider agreement before commercial distribution or training.

The [publisher reported a Spider 2.0-Snow account suspension on August 12, 2026](https://github.com/xlang-ai/Spider2#-news); this historical notice is not proof the issue persists or was fixed. The [Snowflake MFA/access instructions](https://github.com/xlang-ai/Spider2/blob/main/assets/Snowflake_Guideline.md) require requested credentials; BigQuery execution and other hosted environments may incur costs or access restrictions. Never run benchmark queries against production data without appropriate access control, cost budgets and destructive-SQL safeguards.

The upstream [October 2025 evaluation fix notice](https://github.com/xlang-ai/Spider2#-news) also cautions that leaderboard results are mutable. AI Lab has not executed databases, reproduced publisher model scores, verified current Snowflake access, or audited data rights.

## Original resources

- [Spider 2.0 project and leaderboard](https://spider2-sql.github.io/)
- [Original paper (2024)](https://arxiv.org/abs/2411.07763)
- [Original repository and current benchmark overview](https://github.com/xlang-ai/Spider2)
- [Spider 2.0-Lite questions and evaluator](https://github.com/xlang-ai/Spider2/tree/main/spider2-lite)
- [Spider 2.0-Snow questions and evaluator](https://github.com/xlang-ai/Spider2/tree/main/spider2-snow)
- [Spider 2.0-DBT tasks and contradictory inventory](https://github.com/xlang-ai/Spider2/tree/main/spider2-dbt)
- [Repository license and Snowflake access guidance](https://github.com/xlang-ai/Spider2/blob/main/LICENSE)
