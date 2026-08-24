# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale demand, supply, inventory, S&OP/IBP, capacity, allocation, replenishment, exception, and scenario-planning workflows where **time-series evidence, optimizer/planning constraints, service/cost trade-offs, planner approval, and executable plan feasibility** determine the AI route.
- Keep the scenario organization-scale. Finance/procurement transaction controls belong in `finance-risk-and-procurement/`; manufacturing inspection belongs in `manufacturing-quality-inspection/`; generic enterprise analytics belongs in `enterprise-data-analysis/` when planning is not the primary decision context.
- Do not turn this page into ERP/APS/SCM procurement guidance. It owns the model/agent route and acceptance boundary for planning decisions.

## Planning Systems Remain Authoritative

- Keep demand/supply planning systems, ERP, inventory, order, procurement, manufacturing, logistics, capacity, product/location hierarchies, calendars, lead times, policies, and optimizer outputs authoritative.
- Use generative models to explain, summarize, query, compare, hypothesize, and propose scenarios/actions; do not let model memory become the source of truth for demand, inventory, supply, capacity, lead time, cost, service level, or committed dates.
- Preserve planning area/version/run, product/location/customer identifiers, time bucket, scenario, optimizer/forecast version, and source data for material AI outputs.
- When systems or planning runs conflict, surface the exact versions and ownership rather than synthesizing a fictional current plan.

## Integrated Planning-Assistant Route

- Prefer an organization-approved planning-native assistant/agent when it operates directly on governed planning data and preserves model/run context, permissions, scenarios, and approval workflows.
- Current SAP Joule in Integrated Business Planning can explain supply-planning optimizer results, compare planning runs, identify unmet demand/inventory targets, and support planning workflows. Current SAP Planning Assistant adds exception management, inventory-driver assessment, what-if scenarios, and mitigation recommendations. Treat exact capability/entitlement/action availability as mutable.
- Current Dynamics 365 Supply Chain Management supports generative demand-plan analysis and is rolling out AI explanations/forecast enhancements in the 2026 release wave. Microsoft explicitly requires planners to review generated responses against actual demand-plan data before making modifications.
- Current Oracle Fusion Supply Chain Planning combines demand/supply/inventory planning with AI/agentic applications; treat product claims as route eligibility, not proof of organization-specific planning quality.
- Evaluate integrated assistants on the organization's actual forecast/planning hierarchy and constrained scenarios, not generic natural-language demos.

## Separate Forecasting, Optimization, and Explanation

- Keep **forecast generation**, **supply/inventory optimization**, **scenario simulation**, and **natural-language explanation** as separate evidence layers.
- A generative explanation of why demand changed does not replace the statistical forecast or causal/operational evidence.
- A forecast does not prove a feasible supply plan; capacity, lead times, sourcing, inventory, transportation, policy, and service constraints still apply.
- An optimizer output does not prove the business should accept the scenario; planners own assumptions, trade-offs, exceptions, and commitments.
- Record which underlying forecast/optimizer/scenario generated the values summarized by AI.

## Demand Forecasting

- Preserve historical demand, promotions/events, price/market inputs, new-product effects, lost sales/stockouts, returns, one-off anomalies, hierarchy, seasonality, and external signals as explicit modeling inputs where applicable.
- Evaluate forecast models against appropriate baselines and backtests by product/location/time horizon rather than aggregate accuracy alone.
- Use metrics suited to the business distribution and decision; avoid one metric that hides intermittent/low-volume/high-value errors.
- Keep forecast bias and asymmetric stockout/overstock cost visible.
- Treat generative AI explanations as interpretive aids; validate claimed drivers against actual data/features/events.
- Current Dynamics 365 Copilot can analyze shifts, trends, anomalies, and forecast accuracy; Microsoft documents limitations including truncated result lists and mandates human review, so do not treat the summary as exhaustive.

## Supply and Inventory Planning

- Keep inventory targets, safety stock, lead time, service targets, MOQ/lot sizes, sourcing rules, capacities, material constraints, allocation policy, shelf life, and transportation constraints explicit.
- Use deterministic optimization/planning engines to calculate feasible supply/inventory plans where the process requires them.
- AI can explain constraint violations, identify drivers, compare runs, and propose scenarios; it must not invent available capacity, supplier lead time, inventory, or replenishment policy.
- Current SAP IBP Joule can explain planning-run KPIs, unfulfilled demand, missed inventory targets, and compare runs; preserve the run/source as evidence.
- Do not accept a recommended mitigation until the planning engine or authoritative operational systems confirm feasibility.

## Exception Management

- Define material planning exceptions and thresholds deterministically where possible: stockout risk, excess inventory, unmet demand, capacity overload, late supply, service-level risk, forecast bias, supplier disruption, or another organization-specific condition.
- Use AI to cluster, prioritize, summarize, explain, and propose mitigations from the validated exception set.
- Avoid using model-generated urgency as the sole priority signal; include customer/service/financial/operational impact and confidence.
- Preserve exception ID/source/run and the recommendation/approval/action taken.
- Current SAP Planning Assistant supports exception monitoring, context creation, what-if scenarios, and plan-change recommendations; treat recommendation as planner decision support, not automatic authority.

## Scenario and What-If Planning

- Keep assumptions explicit: demand uplift/downside, supply disruption, lead-time change, capacity, price/cost, inventory target, sourcing change, promotion, weather/event input, or policy change.
- Run scenarios through the actual planning/optimization model where feasibility and downstream effects matter.
- Compare scenarios on service, inventory, cost, revenue/margin, capacity, risk, and other governed metrics rather than a generated narrative alone.
- Preserve baseline versus scenario and ensure the model does not present a hypothetical plan as current committed state.
- Require human/planner approval before promoting a scenario to an operational plan.

## Purchase-Order and Supply Changes

- Treat supplier/PO changes as transactional operational events with downstream inventory, production, customer commitment, and cash implications.
- Use AI impact analysis to surface affected demand/orders/locations/capacity where supported, while preserving deterministic source-system facts.
- Current Dynamics 365 2026 planning features include Procurement Agent impact analysis for downstream effects of PO changes; treat preview/availability state as mutable and verify exact behavior before production use.
- Do not autonomously modify PO quantities/dates/suppliers based solely on generated recommendations without the required procurement/planning approvals.

## Demand Signals and External Data

- Validate ownership, license, freshness, granularity, geographic/product mapping, lag, and data quality for external demand signals.
- Do not add social/search/weather/market signals simply because they are available; require measured forecast/planning improvement on relevant horizons.
- Prevent leakage from future information during backtesting.
- Keep external signals distinguishable from transactional demand so planners can inspect their influence.
- Revalidate when signal providers/methodology change.

## New Products and Sparse Demand

- Treat cold-start/new-product/intermittent-demand planning as a separate uncertainty class.
- Use analogs, attributes, market/research evidence, and expert input where statistically appropriate, but preserve assumption provenance.
- Do not let a generative model manufacture historical demand or false precision for products with little evidence.
- Use wider uncertainty/scenario ranges and stronger human review where evidence is sparse.

## Planning Hierarchies and Aggregation

- Preserve product, location, customer/channel, region, and time hierarchies and reconciliation rules.
- Verify whether AI explanations operate at the selected aggregation level and whether drivers survive drill-down.
- Do not infer item/location actions from an aggregate trend without checking local constraints.
- Reconcile top-down/bottom-up forecast/planning changes according to the planning system's governed method.

## Master Data and Data Quality

- Treat missing/wrong lead times, UOM conversions, calendars, product-location assignments, supplier constraints, inventory, historical demand, and master-data mappings as potential planning errors before blaming the model.
- Surface data-quality warnings with affected planning scope.
- Use deterministic validation for identifiers, units, dates, duplicate records, impossible values, and hierarchy consistency.
- Do not allow AI to silently repair authoritative master data; propose corrections with owner/review.

## Planner Approval and Decision Rights

- Define who can change forecasts, safety stock/inventory targets, supply plans, allocations, sourcing, production/capacity assumptions, and committed dates.
- Keep generated recommendations read/proposal-first until decision rights and downstream validation are explicit.
- Use approval workflows for material plan changes.
- Do not let the model interpret access to planning data as authorization to change operational plans.
- Preserve planner rationale for material overrides when audit/relearning requires it.

## Agentic Planning Actions

- Treat agents that modify planning inputs/targets, approve workflows, trigger optimization, create procurement/manufacturing/logistics actions, or communicate commitments as side-effecting systems.
- Define identity, tool scopes, permitted plan areas, thresholds, approvals, idempotency, retries, stop conditions, downstream verification, and audit.
- Keep deterministic constraints/optimizer checks in the loop before operational actions.
- Prevent untrusted supplier/customer/document/web content from expanding agent authority through prompt injection.
- Do not autonomously propagate a speculative scenario into ERP/fulfillment without explicit promotion/approval state.

## Evaluation Suite

- Build a versioned planning evaluation set across demand shift explanation, forecast-quality interpretation, constrained supply, inventory target, unmet demand, capacity bottleneck, supplier/PO change, external signal, new product, and scenario comparison.
- Include deliberately stale/wrong master data, conflicting runs, impossible mitigation, hidden stockout history, unit/calendar error, sparse demand, and a recommendation that must be rejected/escalated.
- Score source/run correctness, explanation support, forecast/optimizer interpretation, feasible recommendation rate, planner correction time, scenario quality, action safety, latency, and cost.
- Evaluate recommendations against actual planning-engine feasibility and subsequent outcomes where available.
- Re-run after forecast/optimizer/model/agent/master-data/policy changes.

## Concurrency and Planning Cycles

- Evaluate daily/weekly/monthly planning peaks, number of product-location combinations, scenario/optimization run duration, AI/model quotas, and planner concurrency.
- Measure end-to-end time from exception/question to validated scenario/decision, not just model response latency.
- Define degraded behavior when AI is unavailable; core deterministic planning must remain operable.
- Avoid an AI dependency that prevents planners from executing critical planning cycles.

## Observability and Audit

- Record model/assistant version, planning run/scenario, data cutoff, sources, generated recommendation/explanation, user approval/override, resulting plan/action, and errors for material workflows.
- Monitor repeated incorrect driver explanations, infeasible recommendations, override rates, stale-data usage, prompt-injection events, and model/provider outages.
- Distinguish model errors from data/master-data/forecast/optimizer errors.

## Cost per Accepted Planning Decision

- Compare **total cost per accepted planning decision/scenario**: AI/API seats, planning/optimizer compute, data ingestion, analyst/planner time, retries, scenario runs, integration/admin, inventory/service impact from bad decisions, and review burden.
- A planning-native assistant can be valuable when it reduces exception-analysis time while preserving exact run context.
- A stronger generative model does not solve poor forecast/master data/constraints and can add cost without improving accepted decisions.
- Measure planner productivity and downstream service/inventory/cost outcomes cautiously; do not attribute business improvement solely to the AI layer without appropriate evidence.

## Local/Private and Hybrid Route

- Use private/self-hosted inference when planning/business data cannot use managed AI or organization control/economics justify it.
- Keep forecast/optimization engines and authoritative SCM/ERP systems unchanged as computation/state owners.
- A hybrid route can keep planning datasets private while using hosted models only for approved public research/sanitized explanation tasks.
- Local inference does not remove data quality, optimization feasibility, decision-rights, audit, or action-safety requirements.
- Escalate shared model gateway/inference to `internal-ai-platform/` when it becomes organization infrastructure.

## Escalation Triggers

- Move to this scenario when demand/supply/inventory planning, optimization, and exception workflows become organization-scale AI use.
- Move to `finance-risk-and-procurement/` when procurement/payment/supplier transaction controls dominate.
- Move to `manufacturing-quality-inspection/` when production-line visual/sensor inspection dominates.
- Move to `enterprise-data-analysis/` when general governed analytical access rather than planning decisions dominates.
- Move to `enterprise-workflow-automation/` when planning agents coordinate broad cross-system actions beyond the planning domain.
- Move to regulated/high-security routes when supply-chain data/actions require stronger controls.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted inference target is selected and hardware materially constrains model/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared organization inference infrastructure.
- SCM/planning hardware procurement remains outside this scenario.

## Canonical Links

- Link finance/procurement, enterprise analytics, manufacturing, workflow-automation, and internal-platform concerns to their organization scenario owners.
- Link named SCM/planning services and exact models to canonical catalog owners when materialized.
- Do not duplicate forecast/optimizer product profiles here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party SAP Integrated Business Planning/Joule/Planning Assistant documentation, current Microsoft Dynamics 365 Demand Planning/Copilot and 2026 release-wave documentation, and current Oracle Fusion Cloud Supply Chain Planning/agentic SCM material.
- Current evidence establishes generative demand analysis, optimizer-run explanations, planning exception/scenario assistance, inventory/demand fulfillment recommendations, and emerging supply-chain agents. It also explicitly preserves planner review and deterministic planning-system context.
- Planning assistant features, preview/GA state, forecast inputs, models, entitlements, quotas, optimizer behavior, integrations, and product pricing are mutable; recheck them before rendering current guidance.
- Forecast/optimizer/planning systems, planner decision rights, and organization-specific backtests/scenarios remain the acceptance authority.

## Validation

- Forecasting, optimization, explanation, and scenario planning remain distinct evidence layers.
- AI explanations/recommendations remain tied to exact planning runs/data cutoffs rather than model memory.
- Master data and deterministic planning constraints are validated before action.
- Proposed mitigations are checked for optimizer/operational feasibility.
- Scenario recommendations remain hypothetical until planners promote/approve them.
- PO/supply plan changes are side-effecting actions with downstream impact/approval controls.
- Human review is explicitly required before AI-derived demand-plan changes.
- Cost is measured per accepted planning decision including optimizer/planner/downstream consequences.
- Internal-platform/workflow/regulated concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
