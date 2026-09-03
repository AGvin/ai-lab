# Documentation Requirements

## Scenario Fit

- Present this scenario for one data analyst, analytics engineer, data scientist, or adjacent professional whose recurring AI-assisted work centers on **structured-data understanding, SQL/Python/R/notebook work, statistics, visualization, forecasting/modeling support, and reproducible analytical outputs**.
- Keep the scenario individual-professional in scope. Shared enterprise metrics, centralized semantic layers, organization-wide governed analytics, concurrency, platform ownership, and production decision infrastructure belong in team/organization routes when those become first-order constraints.
- Distinguish this scenario from `personal-data-analysis/`: this route assumes employer/client datasets, workplace access controls, shared definitions, professional review, reproducibility, and potentially production data systems.
- Distinguish it from `general-knowledge-worker/`: calculations, queries, transformations, schemas, statistical assumptions, code execution, and reproducibility materially change the useful model/tool contract.
- Do not turn the scenario into a data-platform product comparison. It owns model-route selection for the professional, while warehouses, notebooks, BI tools, databases, and pipelines remain authoritative execution/data systems.

## Deterministic Execution Is the Core Boundary

- Treat the language model primarily as a **natural-language interface, code/query author, explainer, reviewer, and hypothesis assistant**. SQL engines, Python/R runtimes, spreadsheet formulas, statistical libraries, notebooks, and data warehouses remain the computation source of truth.
- Require important totals, transformations, aggregations, joins, statistical metrics, forecasts, and charts to be reproducible from executable code/query/formulas rather than prose-only reasoning.
- Preserve source data, query/code, parameters, filters, environment/package versions when material, and the resulting output so another analyst can rerun or review the result.
- A fluent narrative about data is not evidence that the underlying rows, joins, denominators, time windows, or statistical assumptions are correct.
- If the model cannot execute or inspect the real computation path, label the result as a proposed analysis/query rather than a verified analytical result.

## Separate the Analytical Workloads

- Classify recurring work before selecting one assistant/model:
  - schema and unfamiliar-dataset exploration;
  - SQL generation, explanation, optimization, and debugging;
  - Python/R/notebook code generation and repair;
  - data cleaning, normalization, joining, and reshaping;
  - descriptive statistics and exploratory analysis;
  - visualization and dashboard-support work;
  - anomaly/outlier investigation;
  - forecasting and predictive-modeling support;
  - experiment/A-B analysis and causal-design support;
  - text/image/unstructured-data enrichment inside analytical pipelines;
  - documentation, metric definitions, and stakeholder explanations;
  - repetitive analytical automation or agentic data workflows.
- Do not force every workload into one chat surface. A warehouse-native assistant, notebook assistant, managed file-analysis workspace, IDE agent, direct API model, local model, and deterministic data tools can each own different parts of the loop.

## Default Managed Code-Backed Route

- Use an organization-approved managed assistant with inspectable code-backed analysis as the default low-administration route for bounded files or extracted datasets when hosted processing satisfies the data boundary.
- Current ChatGPT data analysis can inspect common structured files, create tables/charts, and execute Python calculations, transformations, and statistics in a stateful Jupyter environment for applicable tasks. Current OpenAI guidance explicitly instructs users to review generated code, outputs, source data, and assumptions before relying on the result.
- Treat managed file analysis as a **bounded workspace**, not a substitute for the governed warehouse/notebook/pipeline when the authoritative dataset is larger, live, permissioned, or shared.
- Evaluate a managed assistant using real accepted tasks: correctly interpret schema, reproduce a known metric, clean a sample dataset, generate and execute a query/code path, produce a chart, explain assumptions, and survive one deliberately misleading column/type case.
- Treat file limits, runtime libraries, connected-source access, model aliases, session persistence, plan eligibility, and data-handling terms as mutable product facts.

## Warehouse-Native and Notebook-Native Route

- Prefer AI assistance inside the user's approved warehouse/notebook environment when the authoritative data already resides there and moving extracts into a separate chat would weaken freshness, permissions, lineage, or reproducibility.
- Current Gemini in BigQuery can help analysts generate/explain SQL and Python and supports guided analysis workflows; treat it as an example of a warehouse-native model surface rather than a universal recommendation.
- Preserve warehouse permissions and query governance. AI assistance must not become a shortcut around dataset/table/row/column authorization.
- Keep generated SQL visible and reviewable before execution when it can scan expensive data, create/replace tables, mutate state, or expose sensitive fields.
- Use dry-run/query-plan/cost-preview mechanisms when the platform provides them before running potentially expensive generated queries.
- In notebook environments, keep code cells and outputs versioned or otherwise recoverable. Re-run the relevant pipeline after the model changes code; do not trust stale state from earlier cells.

## Schema and Semantic Correctness

- Require the model to establish table/column meaning before analysis. Names alone may not reveal business semantics, units, grain, effective dates, status definitions, or slowly changing dimensions.
- Preserve the distinction between physical schema and semantic definitions. A warehouse column called `revenue`, `customer`, `active`, or `conversion` may not match the organization's canonical metric definition.
- When a data catalog, metric layer, dbt model, semantic layer, schema documentation, or source owner exists, use it as evidence rather than letting the model infer business meaning from values.
- Verify grain before aggregation and join cardinality before joins. Explicitly inspect one-to-one, one-to-many, many-to-one, and many-to-many behavior.
- Check unmatched rows, duplicate keys, nulls, late-arriving data, backfills, snapshot semantics, partitions, and timezone/effective-date rules when material.
- Do not silently coerce IDs into measures, percentages into decimals, local time into UTC, or strings into categories without preserving the intended semantics.

## SQL Generation and Review

- Use the model to draft, explain, refactor, and debug SQL, but review identifiers, joins, filters, window frames, date boundaries, aggregation grain, null handling, ordering, and dialect-specific functions before accepting the query.
- Require a small known-answer test or comparison against an existing trusted query for important metrics.
- Separate read-only analytical queries from DDL/DML and other state-changing SQL. Authorization to inspect data does not imply authorization to create, overwrite, delete, update, grant, export, or schedule resources.
- For generated optimization advice, validate the actual warehouse query plan/cost/runtime. A model's generic indexing/partition advice can be wrong for the target engine.
- Preserve query text and warehouse/dataset/version context for results used in reports or decisions.

## Python, R, and Notebook Work

- Use code execution for data cleaning, statistics, visualization, feature engineering, model evaluation, and repeatable transformations rather than asking the LLM to calculate values mentally.
- Review package/function selection, dtype conversion, missing-value treatment, random seeds, train/test leakage, grouping, indexing, and plotting transformations.
- Pin or record package/runtime versions when changes could materially affect reproducibility.
- Make hidden state visible: notebook execution order, mutated DataFrames, cached variables, changed files, and random-state reuse can cause outputs that no longer correspond to the displayed code.
- Prefer functions/scripts/pipelines that can rerun from raw input to result for recurring analyses rather than long chains of manual conversational edits.

## Statistics and Experimental Analysis

- Require explicit hypotheses, outcome metrics, population/sample definitions, inclusion/exclusion criteria, missing-data treatment, weighting, confidence level, and test/model assumptions when they affect the conclusion.
- Do not let the assistant convert correlation, feature importance, clustering, anomaly score, or model explanation into causal claims without an appropriate identification/design argument.
- For experiments, verify randomization unit, exposure, sample-ratio mismatch, pre-period effects, multiple testing, guardrail metrics, novelty/seasonality, and stopping behavior where material.
- For forecasting, preserve training window, horizon, backtesting scheme, baseline comparison, exogenous variables, leakage controls, and uncertainty intervals.
- Treat model-generated statistical methodology as a proposal to validate, not as automatically correct because the code runs.

## Data Science and Predictive Modeling

- Use the assistant to accelerate feature ideas, code scaffolding, experiment design, model diagnostics, documentation, and error analysis, while keeping the actual training/evaluation pipeline deterministic and reviewable.
- Compare against simple baselines before escalating model complexity.
- Preserve train/validation/test boundaries and avoid allowing the LLM to optimize repeatedly against a held-out test set through conversational iteration.
- Record dataset/version, feature pipeline, random seed, hyperparameters, metrics, evaluation slices, and model artifact when the output may be reused.
- For high-consequence predictive use, require domain/organizational review beyond model-selection guidance; this scenario does not approve deployment into production decisions.

## Visualization and Communication

- Select charts from the analytical question and data shape, not from visual novelty.
- Verify axis scales, units, aggregation, sorting, missing periods, denominators, sampling, labels, color/category encodings, and transformations before accepting a chart.
- Separate observed data from forecast/model output and label uncertainty where material.
- Keep stakeholder narrative traceable to the actual query/code output. The assistant may improve explanation, but it must not invent causes, caveats, or business context absent from evidence.
- Preserve the canonical metric/query definition alongside recurring charts or reports so generated prose does not become the only documentation.

## Professional Data Boundary

- Classify datasets before using a hosted model: public, internal, confidential, client-owned, personal data, regulated, security-sensitive, production-derived, or another organization-defined class.
- Follow employer/client policy and the approved provider/account boundary. A consumer assistant or personal API key is not automatically acceptable for workplace datasets.
- Minimize extracts sent to a model: select required columns/rows, aggregate or tokenize identifiers, redact free-text secrets/PII, and use synthetic or representative samples when they preserve the debugging/analysis objective.
- Treat schema names, row samples, query text, notebooks, dashboards, logs, and error messages as potentially sensitive even when raw tables are not uploaded.
- Keep credentials, database connection strings, tokens, private keys, signed URLs, and production secrets out of prompts/notebooks/chat history unless explicitly required and safely managed.
- When a connected warehouse/source is used, verify identity, scopes, permission inheritance, data residency/retention, logging, and revocation behavior.

## Provider and Tool Chain

- Trace the complete analytical path: IDE/notebook/BI client → assistant or gateway → model provider → connected warehouse/files → execution runtime → logs/telemetry/cache.
- A local notebook plus hosted model is still a hosted data-processing route if schema/data snippets leave the machine.
- A warehouse-native assistant may preserve data locality better than exporting data, but its AI service can have a different compliance/security boundary from the warehouse itself; verify the exact product terms/configuration.
- If an intermediary model router/observability layer receives prompts or query results, include it in the data-boundary and retention review.

## Local and Self-Hosted Model Route

- Use a local model when confidentiality, offline work, provider independence, or repeated private code/query assistance justifies local setup and the exact hardware/runtime is verified.
- Keep the deterministic analytical engine local regardless of model choice. Python/R/SQL/DuckDB/SQLite/notebook/warehouse execution remains the source of truth; the local LLM assists with query/code generation, explanation, schema navigation, and review.
- `Qwen3 8B` is a current compact local text/reasoning candidate for bounded SQL/Python/help workflows when its exact task quality and hardware fit are measured. Coding-specific local candidates can be consumed from the software-development decision guide when code generation dominates.
- Do not treat local model output as numerically reliable without executing the generated query/code.
- A local route still requires endpoint security, access control, model/cache/history protection, and safe tooling permissions.

## Direct API and Custom Analytical Agents

- Use direct APIs/custom agents only when the analyst needs repeatable integration, programmatic batch generation/review, internal tooling, or tool orchestration not provided by the managed workspace.
- Keep query execution and write permissions narrow. An agent that can issue SQL, modify notebooks, update dashboards, or write tables is side-effecting.
- Separate read-only exploration from state-changing actions. Require explicit approval or deterministic policy for CREATE/REPLACE/UPDATE/DELETE/export/scheduled-job actions and high-cost queries.
- Bound loops, retries, spend, query scan cost, and runtime. A model should not repeatedly rerun an expensive query because it failed to interpret the result.
- Require observable completion evidence: executed query/code, validation checks, expected row counts/schema, tests or reconciliations, and final artifact review.

## Cost per Accepted Analytical Result

- Compare **total cost per accepted analytical result**: assistant/API spend, warehouse scan/compute cost, notebook/runtime cost, data transfer, local compute, retries, correction/review time, reproducibility work, and the consequence of an incorrect decision.
- A higher-priced managed/warehouse-native assistant can be cheaper when it reduces data movement, preserves permissions/lineage, and shortens debugging/review.
- A local model can lower provider spend for repetitive private query/code help but can be more expensive if model maintenance or lower quality increases analyst correction time.
- Do not optimize model selection on token price while ignoring warehouse query cost or human verification time.

## Escalation Triggers

- Move from generic managed file analysis to warehouse/notebook-native assistance when freshness, data volume, permissions, lineage, or reproducibility make extracts impractical.
- Move to a stronger/specialized model when SQL/code quality or complex reasoning repeatedly fails the accepted test suite and the additional cost reduces total correction effort.
- Move to local/self-hosted assistance when data egress is not permitted and the exact local route passes quality/latency acceptance.
- Move to `researcher/` when evidence/literature synthesis rather than structured-data analysis becomes dominant.
- Move to team/organization data-analysis scenarios when shared metrics, centralized governance, production BI, concurrency, semantic layers, platform ownership, or multi-user workflows dominate.
- Escalate to qualified domain/statistical review when health, finance, legal, safety, policy, or another high-consequence decision exceeds ordinary analytical support.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when local model inference or local accelerated data/model workloads materially constrain the AI route.
- Use `../../../hardware/sub/computers/` for a professional workstation/laptop and the applicable accelerator specialization where known.
- Keep data-processing hardware/platform sizing and hardware purchasing outside this scenario; the model route can remain managed, warehouse-native, hosted, or hybrid.

## Canonical Links

- Link managed assistant examples to their canonical service owners when named.
- Link `Qwen3 8B` to `catalog/models/alibaba/qwen/qwen3/models/qwen3-8b` when named.
- Link coding-specific candidates through `decision-support/selection/models/decision-guides/software-development` rather than duplicating their ranking here.
- Link personal structured-data analysis to the sibling `personal-data-analysis/` owner only for boundary navigation, not duplicated content.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI code-backed data-analysis documentation, current Google Gemini in BigQuery SQL/Python/data-analysis documentation, and canonical AI Lab model/service owners.
- Current OpenAI evidence establishes uploaded structured-data analysis with Python/Jupyter-backed execution and explicit code/output/assumption review. Current BigQuery evidence establishes AI-assisted SQL/Python generation and data analysis within a governed warehouse surface. These are product-capability facts, not proof of analytical correctness.
- Current BigQuery documentation also demonstrates that AI-assistance security/compliance boundaries can differ from the underlying BigQuery service; verify the exact product/account/data requirements rather than assuming warehouse locality implies identical AI controls.
- Model aliases, assistant/warehouse features, preview status, supported languages, file/query limits, runtime packages, data terms, retention, and pricing are mutable; recheck them before rendering current guidance.
- Provider claims never replace reproducible queries/code and dataset-specific validation.

## Validation

- Deterministic SQL/Python/R/formula execution remains the computation source of truth.
- Professional schema/metric semantics, grain, joins, timezones, missingness, permissions, and lineage are explicit parts of model-route evaluation.
- Managed file analysis, warehouse-native assistance, notebook assistance, local models, and direct API/agents remain distinct route classes.
- Generated SQL/code is inspectable and state-changing or expensive operations have stronger controls than read-only analysis.
- Statistical and predictive conclusions preserve assumptions, baselines, uncertainty, leakage/causal boundaries, and reproducibility.
- Workplace data is not moved to consumer or unapproved model routes by convenience.
- Local models assist analytical work but do not replace deterministic computation or endpoint/tool security.
- Team/enterprise analytics architecture remains outside this individual-professional scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
