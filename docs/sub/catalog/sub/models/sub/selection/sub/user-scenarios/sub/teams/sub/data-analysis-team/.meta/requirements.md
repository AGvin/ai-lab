# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person analytics/data-science team sharing datasets, metric definitions, notebooks/queries, dashboards/reports, review responsibilities, and access boundaries.
- Keep the scenario team-scoped. One analyst/data scientist belongs in `professionals/data-analyst-or-data-scientist/`; organization-wide data platform, centrally governed semantic layers, high-concurrency BI infrastructure, or enterprise model gateways belong in organization routes when they dominate.
- Distinguish this scenario from `small-business-team/`: here analytical correctness, shared definitions, reproducibility, peer review, and data-access boundaries are the primary AI-selection constraints.
- Do not turn the page into warehouse/BI platform architecture. It owns the model/assistant route for the team's analytical workflow.

## Deterministic Shared Execution Layer

- Keep SQL engines, warehouses, Python/R runtimes, notebooks, transformation frameworks, spreadsheets where appropriate, statistical libraries, and BI tools as the computation source of truth.
- Treat the language model as query/code author, explainer, reviewer, schema navigator, hypothesis assistant, and workflow interface—not the arithmetic engine of record.
- Require material results to be reproducible from shared code/query/formulas and versioned data/definitions.
- Store reusable queries, notebooks, scripts, metric definitions, tests, and analytical documentation in team-owned systems rather than individual assistant memory.
- A conversational answer becomes accepted analysis only after the underlying computation and source data are verified.

## Shared Metric and Semantic Boundary

- Define where canonical business/analytical meaning lives: metric layer, dbt/model documentation, warehouse views, data catalog, BI semantic layer, specification, or named data owner.
- The model must retrieve/use that definition rather than infer terms such as `active user`, `revenue`, `retention`, `conversion`, `customer`, or `churn` from generic knowledge or column names.
- Preserve grain, filters, exclusions, attribution rules, effective dates, currency/timezone, and source systems for each shared metric.
- When definitions conflict, surface the conflict and source owners instead of selecting the most plausible definition.
- Do not let generated query convenience create a second hidden semantic layer in prompts or chat history.

## Default Warehouse/Notebook-Native Route

- Prefer an organization-approved warehouse/notebook-native assistant when the authoritative data already resides there and this route preserves permissions, freshness, lineage, and reproducibility better than exporting datasets to a separate chat.
- Current Gemini in BigQuery is a current example of AI-assisted SQL/Python and data-analysis workflows inside a governed warehouse surface. Treat exact features, preview status, supported models, security boundaries, and pricing as mutable.
- Evaluate any warehouse-native assistant on team tasks: reproduce known metrics, generate/debug queries, explain schemas, perform a controlled exploratory analysis, and recover from deliberately ambiguous/incorrect column semantics.
- Keep generated SQL/code visible. Use query plan/dry run/cost estimation, read-only defaults, or comparable controls where the platform provides them.
- Do not assume the AI feature has identical compliance/security/residency behavior to the underlying warehouse; verify the exact generative-AI service boundary.

## Managed File/Code-Backed Analysis Route

- Use an approved managed file-analysis workspace for bounded extracts, ad hoc exploration, stakeholder files, or collaborative analyses when data movement is permitted.
- Current ChatGPT data analysis is an example of Python/Jupyter-backed structured-data analysis with visible generated code and output. Treat plan/file/runtime limits and connected-source behavior as mutable.
- Require analysts to inspect generated code, source data, transformations, and assumptions before accepting results.
- Do not move large/live/shared authoritative datasets into file uploads merely because the chat interface is easier; use a warehouse/notebook route when freshness/access/scale make extracts misleading.

## Team Data Access and Least Privilege

- Preserve warehouse/source permissions for every team member and AI integration.
- Do not create a broad service account or model connector that can read more data than the requesting user/workflow needs unless an explicitly governed team service requires it.
- Treat row/column policies, sensitive views, PII masking, data labels, and client/project boundaries as part of AI access, not separate afterthoughts.
- Verify what schema metadata, query text, row samples, notebook outputs, and error logs leave the source system through the AI feature/provider.
- Keep credentials, signed URLs, connection strings, private keys, and production tokens out of prompts and shared notebooks.

## Shared Query and Code Review

- Require review proportional to consequence for generated SQL/Python/R.
- Review joins/cardinality, filters, date windows, window functions, null behavior, aggregation grain, deduplication, partitions, dialect functions, and state-changing statements.
- Separate SELECT/read-only exploration from DDL/DML/export/scheduled-job actions.
- For important recurring metrics, compare AI-generated queries against a known-good query/test or metric definition before adoption.
- Preserve query/code changes in normal version control/review where the team uses it, so generated changes have authorship, diff, and rollback.

## Data Quality and Transformation

- Make assumptions about missingness, duplicates, late-arriving data, backfills, snapshots, timezones, currency, units, and identifiers explicit.
- Use data-quality tests and before/after row/null/key checks for material cleaning and joins.
- Preserve raw/staged sources and traceability from transformed rows/metrics back to source records where appropriate.
- Do not let different team members accept different model-generated cleaning rules for the same shared dataset without reconciling them into a canonical transformation.
- When the AI identifies an anomaly, distinguish data-quality defect, pipeline incident, real business event, and statistical outlier before escalation.

## Shared Notebooks and Reproducibility

- Keep notebook execution state reviewable and rerunnable from a defined starting point.
- Re-run affected cells/pipelines after AI code edits; do not trust stale outputs from prior state.
- Record package/runtime versions, seeds, parameters, data snapshots, and model/service version where material to repeatability.
- Prefer reusable functions/pipelines over repeated manual conversational transformations.
- Define a team convention for where accepted AI-generated queries/code and explanations are stored so useful work is not lost in personal chats.

## Statistics and Experiment Analysis

- Use explicit hypotheses, sample/population definitions, outcome metrics, missing-data treatment, weighting, confidence assumptions, and test/model assumptions.
- For A/B experiments, verify randomization unit, exposure, sample-ratio mismatch, pre-period effects, multiple testing, novelty/seasonality, guardrail metrics, and stopping rules where material.
- Do not allow model-generated narrative to turn correlation or post-hoc segmentation into causal evidence.
- Require peer/methodological review for high-impact experimental conclusions.
- Keep exploratory analysis visibly distinct from confirmatory/pre-registered analysis when the team's methodology requires it.

## Predictive and Data-Science Work

- Use AI to accelerate code scaffolding, feature ideas, model diagnostics, experiment design, documentation, and error analysis while preserving deterministic training/evaluation pipelines.
- Maintain train/validation/test boundaries, leakage controls, baselines, seeds, features, hyperparameters, evaluation slices, and model artifacts.
- Do not repeatedly expose a held-out test set to model-assisted iteration in a way that invalidates it.
- For production ML, deployment/monitoring/fairness/governance can exceed this team model-selection scope; escalate to organization/platform owners when those become central.

## Visualization and Recurring Reporting

- Verify chart axes, scales, units, aggregation, missing periods, denominator, filters, sorting, sampling, and labels.
- Keep observed data separate from forecasts/estimates.
- Store recurring report definitions/queries in team-owned systems; the assistant can draft commentary but should not redefine the metric between runs.
- Compare generated narrative to the actual computed output and flag unsupported causal explanations.
- For scheduled reporting agents, require deterministic data refresh, report validation, destination/recipient controls, and failure visibility before delivery.

## Analytical Agents and Side Effects

- Treat an agent that can execute queries, edit notebooks, modify dashboards, create tables, schedule jobs, or send reports as side-effecting.
- Grant read-only access by default where the workflow permits.
- Require explicit approval or deterministic policies for CREATE/REPLACE/UPDATE/DELETE, exports, scheduled jobs, dashboard publication, permission changes, and expensive scans.
- Bound retries and query/compute spend; an agent must not repeatedly run an expensive query because it misunderstood the output.
- Log which queries/actions actually executed and retain enough audit evidence for consequential workflows.

## Team Evaluation Suite

- Build a versioned evaluation set from representative approved datasets and tasks across the team's real tools.
- Include: a known metric reproduction, schema interpretation, multi-table join, cleaning task, statistical analysis, chart/report, query debugging case, and an ambiguous case that should ask/escalate.
- Score numerical/query correctness, metric-definition adherence, data lineage/provenance, code quality, reproducibility, correction/review time, latency, access-policy fit, and total cost.
- Include adversarial cases such as similarly named columns, wrong grain, duplicated joins, timezone boundary, stale table, null-vs-zero, and hidden PII.
- Use provider benchmarks only to identify candidates, not as team acceptance evidence.

## Multiple Models and Routing

- Use a primary approved route for common analysis to reduce tool/context fragmentation.
- Add a stronger/specialized model only when it measurably improves complex SQL/code, statistical reasoning, long-document/data work, or review enough to justify extra cost/data path.
- Use smaller/lower-cost models for bounded classification/documentation/explanation where they pass acceptance.
- Keep fallback behavior explicit; never silently route sensitive datasets to a different provider when the preferred model is unavailable.

## Local and Private Model Route

- Use local/self-hosted models when data egress is prohibited or repeated private code/query assistance justifies the operational burden.
- Keep deterministic SQL/Python/R execution as the source of truth even when the model is local.
- Shared local inference must be evaluated under team concurrency: queue time, context/KV memory, accelerator utilization, isolation, auth, logs, uptime, updates, and accepted-result quality.
- A local endpoint does not prove the analyst client/editor/notebook path is local if hosted embeddings, telemetry, or fallback models remain enabled.
- If operating shared inference evolves into cross-team platform work, move to `organizations/internal-ai-platform/`.

## Provider and Processing Chain

- Trace notebook/IDE/BI client → assistant/gateway → model provider → warehouse/files → code execution → logs/telemetry/cache.
- Treat intermediaries and observability systems as data recipients when they receive prompts, schema, data samples, query output, or code.
- Recheck provider data/retention/residency terms for sensitive data classes.
- Do not assume one approved AI route is valid for every dataset in the team's warehouse.

## Cost per Accepted Team Analysis

- Compare **total cost per accepted analytical result/report**: AI seats/API, warehouse scans/compute, notebook runtime, data transfer, local infrastructure, reruns, correction/review, data-quality work, and the consequence of wrong metrics.
- A warehouse-native route can be economical even with premium AI pricing when it avoids data movement and preserves lineage/permissions.
- A local model can reduce provider spend but lose value if lower quality increases analyst review or shared infrastructure operations.
- Track expensive query generation and repeated failed agent runs separately from model token cost.

## Escalation Triggers

- Move from individual analyst use to this scenario when shared datasets/metrics/notebooks/review become first-order constraints.
- Move to organization-scale enterprise-data-analysis when governed semantic layers, production BI, large concurrency, centralized access/data policy, multiple teams, or organization-wide analytics infrastructure dominate.
- Move to internal-platform when centralized model/provider gateway, budgets, shared agent platform, or AI observability becomes the main problem.
- Move to regulated/high-security routes when data classification requires stronger controls.
- Narrow or stop agentic execution when write/compute risk or verification burden exceeds team acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared inference target materially constrains the model route.
- Use `../../../hardware/sub/servers/` for a dedicated shared inference server or `../../../hardware/sub/computers/` for a team workstation where appropriate.
- Data warehouse/compute hardware purchasing remains outside this scenario.

## Canonical Links

- Link individual analytical workflow details to `catalog/models/selection/user-scenarios/professionals/data-analyst-or-data-scientist` where needed.
- Link managed assistant/warehouse products to their canonical service/software owners when named.
- Link exact local model candidates only through canonical Model Reference owners when current evidence justifies them.
- Link organization-scale analytics to `catalog/models/selection/user-scenarios/organizations/enterprise-data-analysis` rather than duplicating platform concerns.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party OpenAI code-backed data-analysis documentation, current Google Gemini in BigQuery SQL/Python/data-analysis documentation, and canonical AI Lab analytical model/service owners.
- Current evidence establishes inspectable code-backed managed analysis and warehouse-native AI-assisted SQL/Python workflows, but not correctness for team datasets or identical security boundaries across the warehouse and AI feature.
- Warehouse AI features, model aliases, notebook/file limits, query cost controls, data policies, preview status, retention, and pricing are mutable; recheck them before rendering current guidance.
- Provider capability claims do not replace shared metric definitions, deterministic execution, peer review, or reproducibility.

## Validation

- Shared metric definitions, datasets, queries/notebooks, permissions, and peer review distinguish the team route from individual analysis.
- SQL/Python/R/warehouse execution remains the computation source of truth.
- Warehouse-native and managed file-analysis routes remain distinct and data movement is explicit.
- Generated queries/code preserve grain, semantic definitions, access policies, and state-changing/cost controls.
- Statistical/predictive conclusions preserve assumptions and reproducibility.
- Team-owned code/definitions replace personal assistant memory as durable state.
- Local/shared models include concurrency/operations and do not imply complete locality.
- Organization-scale analytics/platform concerns are delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
