# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale governed analysis across data warehouses, lakehouses, databases, semantic/metric layers, BI systems, and shared datasets where **trusted definitions, access controls, lineage, concurrency, cost, audit, and reproducibility** determine the AI route.
- Keep the scenario organization-scale. Individual analytical work belongs in `professionals/data-analyst-or-data-scientist/`; a bounded shared analyst team belongs in `teams/data-analysis-team/`.
- Distinguish it from `business-knowledge-assistant/`: enterprise data analysis operates on structured governed data and executable queries/models, not primarily document retrieval/synthesis.
- Do not turn this page into a data-platform procurement guide. It owns the model/conversational-analysis route and its acceptance boundary.

## Deterministic Data Platform Remains Authoritative

- Keep warehouses/databases/lakehouses, SQL engines, semantic layers, transformation pipelines, notebooks, BI systems, and statistical runtimes as the computation/source-of-truth layer.
- Treat the model as natural-language interface, query/code author, semantic navigator, analyst/reviewer, and agent—not the arithmetic/data system of record.
- Require material results to correspond to executed queries/code against the intended governed dataset and definition version.
- Preserve query/code, metric definition, filters, parameters, dataset/table/model identity, time window, and output provenance for decisions/reports.
- Do not accept prose-only calculations or model-memory business metrics as enterprise analysis.

## Semantic Layer and Business Definitions

- Define canonical metrics/entities/dimensions through the organization's semantic/metric/catalog layer or explicit authoritative definitions.
- Current BigQuery/Google data-platform direction explicitly emphasizes semantic context and governed metadata for conversational/data agents; treat this as evidence that enterprise AI analysis requires more than schema names.
- The model must not infer `revenue`, `active customer`, `churn`, `margin`, `conversion`, or similar business terms from generic knowledge when a governed definition exists.
- Preserve metric version/effective date, grain, filters, attribution, currency/timezone, and ownership where material.
- When definitions conflict or are absent, ask/escalate rather than generating a plausible enterprise definition.

## Default Governed Conversational-Analytics Route

- Prefer an organization-approved conversational-analytics assistant integrated with the governed data platform when it can preserve access controls, semantic context, query visibility, lineage, and operational controls.
- Current BigQuery Conversational Analytics is GA and provides natural-language multi-step analysis/visual reports on governed BigQuery data; current Gemini in BigQuery supports AI-assisted SQL/Python and is governed by product-specific security/privacy controls. Treat exact feature/model/region/plan behavior as mutable.
- Evaluate an integrated route using the organization's real metrics, permission personas, data volume, complex joins, historical definitions, and adversarial cases.
- Keep generated queries/analysis steps inspectable and retain the ability to reproduce results outside the chat surface.
- Do not infer enterprise correctness from `conversational analytics` branding or provider claims.

## Access Control and Data Governance

- Preserve IAM/RBAC/ABAC, row/column policies, authorized views, masking/tokenization, data classifications, project/dataset boundaries, and source-system controls.
- A conversational layer must not broaden access because the model can formulate a query the user could not author manually.
- Test negative permissions, cross-department boundaries, sensitive columns, row filters, contractors/guests, offboarded users, and service accounts.
- Treat schema/metadata as sensitive when names/descriptions reveal confidential business/customer information.
- Do not rely on natural-language policy alone where deterministic IAM/policy controls can enforce the boundary.

## Data Residency, Privacy, and AI-Service Boundary

- Verify the exact AI feature's processing, retention, residency, logging, and training terms separately from the underlying warehouse/storage service.
- Current Gemini in BigQuery documentation states that GA features preserve BigQuery data-at-rest location and do not use prompts/responses/schema information for model training without permission; treat exact feature/region coverage as mutable.
- Do not assume preview/agent/connector features inherit every GA control automatically.
- Include model gateways, external BI assistants, observability proxies, and connected tools in the provider/data chain.
- Route regulated/high-security datasets to stronger organization scenarios when required.

## Query Generation and Safety

- Make generated SQL/query/code visible to the analyst/reviewer where practical.
- Review joins/cardinality, filters, date boundaries, window frames, aggregations, nulls, dialect functions, data source, and estimated scan/compute before material execution.
- Separate read-only analysis from DDL/DML/export/schedule/write operations.
- Use query plan/dry-run/cost-estimation/quotas/limits where available for expensive or agent-generated queries.
- Require deterministic checks/approval for CREATE/REPLACE/UPDATE/DELETE/export, scheduled pipelines, grants, or other state-changing actions.

## Cost Governance

- Track model/API/assistant cost and data-platform scan/compute cost separately, then combine them at accepted-result level.
- Bound query bytes/compute, agent retries, parallel exploration, long-running jobs, and generated reports.
- Do not let an agent repeatedly rerun expensive queries because it failed to interpret results.
- Prefer cached/materialized/approved aggregates when they satisfy the question and reduce cost without sacrificing freshness/correctness.
- Measure cost per accepted analysis/decision rather than token or warehouse-query cost alone.

## Data Quality and Lineage

- Surface dataset freshness, pipeline status, quality checks, late arrivals, backfills, nulls, duplicates, schema changes, and ownership where they affect interpretation.
- Preserve lineage from reported metric/result to the executed query and source datasets/models.
- Do not let AI hide data-quality uncertainty behind a polished narrative.
- When data is incomplete/stale, state the limitation and avoid definitive business conclusions.
- Keep data-quality remediation outside model free-form authority unless a governed deterministic workflow owns changes.

## Shared Metrics and BI

- Preserve one canonical definition for recurring metrics across conversational answers, dashboards, reports, and downstream agents.
- Do not allow a model to create a second shadow metric in a prompt or generated query that conflicts with the semantic layer.
- For executive/operational reporting, include source/time window/definition and separate actuals from forecasts/estimates.
- Verify generated visualizations against query output, units, scale, aggregation, filters, and denominator.
- Keep published dashboard/report changes behind normal review/approval.

## Statistical, Experiment, and Predictive Analysis

- Use deterministic statistical/modeling runtimes for experiments, forecasting, predictive modeling, simulation, and inference.
- Preserve assumptions, sample/population, missing-data treatment, weighting, baselines, train/validation/test, leakage controls, seeds, backtesting, and uncertainty.
- Do not allow conversational agents to convert correlation or model feature importance into causal conclusions.
- Route specialized model-building methodology to governed data-science processes; this scenario focuses on enterprise AI-assisted analysis access.
- Require stronger methodological/domain review for high-consequence decisions.

## Enterprise Data Agents

- Treat agents that query data continuously, monitor metrics, generate reports, create tables, trigger workflows, or act from analytical findings as a higher tier than conversational analysis.
- Separate read/query reasoning from business-system actions.
- Use least privilege, explicit tool sets, query/spend limits, semantic/metric policy, deterministic action checks, approval gates, and audit logs.
- Current Google semantic-governance preview explicitly positions natural-language agent policy as a complementary layer to IAM/rate/network controls and warns that LLM verdicts may be inaccurate; preserve deterministic baseline controls.
- Do not let an agent autonomously change operational/financial/customer state solely because an analytical pattern crosses a model-generated threshold.

## Multi-Source and Cross-Cloud Analysis

- Treat cross-source/cross-cloud federation as a data-governance boundary, not only a retrieval convenience.
- Preserve source identities, authorization, schemas, units, freshness, transfer/egress, and semantic compatibility.
- Do not merge metrics from multiple warehouses/BI systems until definitions and time/grain semantics are reconciled.
- Track which data moved, which engine executed the query, and where AI processing occurred when residency/cost/audit matters.

## Concurrency and Scale

- Evaluate realistic employee/analyst concurrency, query volume, dashboard/report workloads, peak periods, model rate limits, warehouse queues, and shared semantic-service capacity.
- Measure end-to-end p50/p95 latency and accepted-result success rather than model response latency alone.
- Define behavior for warehouse/model/connector failure, rate limiting, stale catalog, and partial-source availability.
- Monitor repeated query failures, semantic mismatches, cost spikes, access denials, and analyst corrections as production quality signals.

## Evaluation Suite

- Build a versioned enterprise evaluation set covering canonical metrics, cross-table joins, semantic synonyms, historical definition changes, timezones/currencies, restricted data, expensive query, no-data/ambiguous case, conflicting definitions, visualization, and one agent/action scenario where applicable.
- Evaluate across user/permission personas and business domains.
- Score semantic/metric correctness, query correctness, data access, reproducibility, lineage, cost, latency, no-answer/escalation, permission leakage, and human correction effort.
- Include adversarial natural-language prompts that request unauthorized or semantically invalid analysis.
- Re-run regression tests after model, semantic layer, schema, catalog, access-policy, or prompt/agent changes.

## Local/Private Model Route

- Use private/self-hosted models when the data boundary prohibits managed AI processing or organization economics/control justify the operations.
- Keep data execution in the governed platform and send only approved schema/query/result context to the local model.
- Evaluate exact model/runtime/hardware/concurrency on SQL/code/semantic tasks; do not preserve a static local-model ranking here.
- Local inference does not remove warehouse IAM, semantic correctness, prompt injection, endpoint security, audit, or operational requirements.
- Escalate shared model routing/infrastructure to `internal-ai-platform/` when it becomes cross-organization infrastructure.

## Cost per Accepted Enterprise Analysis

- Compare **total cost per accepted enterprise analytical outcome**: AI seats/API, warehouse/lakehouse compute, semantic/catalog services, data transfer, integration, governance/admin, analyst review, failed queries, audit, local infrastructure, and wrong-decision risk.
- A native conversational layer can be economically strong when it preserves governance and reduces analyst backlog/context switching.
- A custom/general assistant can be cheaper nominally but expensive if semantic mistakes, data movement, or review burden are high.
- A stronger model is wasted cost when metric definitions/data quality/access are the bottleneck.

## Escalation Triggers

- Move from team analytics to this scenario when governed enterprise metrics/data, multiple teams, large concurrency, centralized semantics, or organization-wide analysis access becomes first-order.
- Move to `internal-ai-platform/` when centralized model/provider routing, budgets, common agent runtime, or AI observability becomes the primary concern.
- Move to regulated/high-security routes when data classes require stronger isolation/compliance controls.
- Move toward `enterprise-workflow-automation/` when analytical agents increasingly act across business systems rather than answer/analyze.
- Stop/narrow conversational access where semantic/access/audit requirements cannot meet the needed threshold.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted inference target is selected and hardware materially constrains model choice.
- Use `../../../hardware/sub/servers/` for shared inference infrastructure.
- Data-platform hardware procurement remains outside this model-selection scenario.

## Canonical Links

- Link team analysis to `decision-support/scenarios/teams/data-analysis-team` for bounded team context.
- Link centralized AI platform concerns to `decision-support/scenarios/organizations/internal-ai-platform`.
- Link managed data/BI services and exact models to canonical owners when named/materialized.
- Do not duplicate warehouse/semantic/catalog product profiles here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party BigQuery Conversational Analytics GA documentation, current Gemini in BigQuery security/privacy/compliance documentation, current BigQuery governance/semantic-platform material, and current semantic-governance agent policy documentation.
- Current evidence establishes organization-scale conversational analysis over governed data, AI-assisted SQL/Python, semantic/governance emphasis, data-location/training controls for specified GA features, and emerging policy layers for data agents. None of this establishes semantic/query correctness for the organization's metrics.
- AI/data-platform features, preview/GA state, models, semantic capabilities, security/residency coverage, query pricing, quotas, and agent-policy behavior are mutable; recheck them before rendering current guidance.
- Executed governed queries, canonical definitions, and enterprise evaluation remain the acceptance authority.

## Validation

- Governed structured data and semantic definitions distinguish this route from document knowledge assistance.
- Deterministic warehouse/notebook/statistical execution remains the computation source of truth.
- User/data permissions and negative-access tests remain enforced through the conversational layer.
- Semantic layer/metric definitions are not inferred ad hoc from schema names.
- Query cost and state-changing operations have deterministic limits/approval.
- Enterprise data agents add policy/intent checks without replacing IAM and other baseline controls.
- Reproducibility, lineage, data quality, concurrency, and audit are first-class acceptance criteria.
- Internal-platform/workflow automation concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
