# Documentation Requirements

## Scenario Fit

- Present this scenario for a product-management team that repeatedly combines user/customer feedback, research, requirements, product/usage metrics, experiments, roadmap context, launch material, and cross-functional input to make product decisions.
- Keep the scenario team-scoped. One general knowledge worker belongs in the professional route; organization-wide portfolio/governance/data-platform/enterprise-knowledge architecture belongs in organization routes when it dominates.
- Distinguish this scenario from `research-and-insights-team/`: research is an input, but here **requirements, prioritization, decision traceability, product metrics, cross-team context, and lifecycle delivery** determine the AI route.
- Distinguish it from `project-and-operations-team/`: project execution/status/risk can be related, but this route is centered on product problem/solution/evidence decisions and roadmap/launch state.
- Do not let the page become a product-management methodology guide. It owns model/workspace selection for the team's decision workflow.

## Preserve Product Sources of Truth

- Identify the authoritative system for each product object: product brief/PRD, issue tracker, roadmap, experiment system, analytics, research repository, feedback/support system, design files, release notes, and decision log.
- Use the assistant to retrieve, synthesize, draft, compare, and propose changes; do not let chat memory become the only record of approved requirements, roadmap commitments, experiment results, or launch decisions.
- Preserve object IDs/links and version/effective dates for material product decisions.
- When sources conflict, surface the conflict and owner rather than silently merging them into one generated narrative.
- Keep generated summaries derived from authoritative objects so later changes can be traced and refreshed.

## Default Managed Connected-Workspace Route

- Prefer an organization-approved managed workspace with permission-aware connected sources when the team's core data lives across documents, mail/chat, files, calendars, research, and product systems and hosted processing is permitted.
- Current managed workspaces can connect to supported internal sources and apps while administrators control app/source access. Treat exact connector catalogs, actions, indexing/sync behavior, retention, and model aliases as mutable.
- Evaluate the workspace on real product tasks: synthesize one research/feedback set, compare a requirement against current product docs, draft a decision brief, analyze a bounded experiment table, prepare launch/risk questions, and identify source conflicts.
- Prefer one primary workspace for shared product context to reduce duplicated project memories and inconsistent source connections.
- Add a specialist research/data/coding route only when it materially improves a recurring product workflow and the data boundary remains acceptable.

## User and Customer Feedback

- Treat feedback sources separately: interviews, surveys, support tickets, app reviews, sales calls, community posts, NPS/free text, usability studies, and usage telemetry have different sampling and evidence properties.
- Use AI to extract/categorize/code/theme feedback only after the team defines the intended coding taxonomy and validation approach.
- Validate automated qualitative coding against manually reviewed samples and periodically recheck drift when categories/prompts/models change.
- Do not equate mention frequency with prevalence, severity, revenue impact, or roadmap priority without appropriate sampling/context.
- Preserve minority/negative/outlier feedback that materially challenges the dominant theme.
- Keep customer quotes traceable to source and redact/obtain permission before broader sharing as required.

## Requirements and PRD Drafting

- Use the model to structure problem statements, requirements, acceptance criteria, alternatives, risks, open questions, and edge cases from verified source material.
- Require every factual/product claim in a requirement to trace to an authoritative source or explicit owner decision.
- Separate observed user/problem evidence from proposed solution/design.
- Do not let the model invent technical feasibility, delivery dates, legal constraints, customer commitments, or dependency status because they sound plausible.
- Keep final approved requirements in the team's canonical product/issue system and retain human ownership/review.
- Ask the model to identify ambiguous terms, missing acceptance criteria, conflicting requirements, and hidden assumptions before approval.

## Prioritization and Roadmap Support

- Use AI to organize evidence and compare alternatives, but keep prioritization criteria explicit: strategic fit, user/customer impact, revenue/cost, risk, effort/capacity, dependencies, learning value, urgency, and confidence as applicable.
- Do not let model-generated numeric scores create false precision. If the team uses a scoring framework, preserve input sources/assumptions and let humans own weights/decisions.
- Distinguish committed roadmap items from candidates/hypotheses/ideas.
- Treat dates and delivery confidence as owned by the relevant product/engineering/business process, not by model estimation alone.
- Preserve the reasoning and evidence for material priority changes in a decision record rather than only a chat summary.

## Experiment and Product-Metric Analysis

- Use deterministic analytics systems/SQL/Python/statistical tools for experiment and usage calculations.
- Route sustained analytics to `data-analysis-team/` and link its verified results into product decisions.
- Require canonical metric definitions, population/sample boundaries, date windows, variants, guardrails, and statistical assumptions before interpreting an experiment.
- Do not let the model convert correlation, segment differences, or post-hoc analysis into causal claims without an appropriate design.
- Verify sample-ratio mismatch, exposure, novelty/seasonality, multiple testing, stopping behavior, and data-quality issues where material.
- Keep narrative interpretation traceable to executed queries/experiment reports.

## Research and Competitive Context

- Use current source-grounded research for competitor capabilities, market changes, standards, policy, technology, and customer alternatives.
- Route deep research methodology to `research-and-insights-team/` when evidence coverage/review becomes substantial.
- Prefer primary/authoritative sources for material competitor/product facts and record dates/release status.
- Do not infer competitor strategy, adoption, customer satisfaction, or future plans as fact from generic model memory.
- Distinguish announced/preview/GA/discontinued capabilities in product comparisons.

## Cross-Functional Context

- Product teams often consume engineering, design, sales, support, marketing, legal/security, analytics, and leadership inputs. Preserve each source's ownership and permission boundary.
- Do not flatten disagreement between functions into a generated `consensus` unless the team actually made a decision.
- Keep confidential personnel/customer/legal/security material out of broadly shared product workspaces when not needed.
- When summarizing meetings/channels, retain action owner, due date, decision status, and source link rather than converting all conversation into requirements.
- Verify which account/workspace/source is active before an assistant searches across multiple internal systems.

## Decision Records

- For material decisions, preserve: question, options, evidence, assumptions, constraints, decision owner, decision/date, rejected alternatives where still useful, and re-evaluation trigger.
- Use the model to draft/compare a decision record, but require humans to approve the actual decision.
- Link decisions to requirements/experiments/research rather than copying evidence into many documents.
- Revisit model-generated summaries when an underlying source changes; do not preserve stale AI synthesis as a permanent product fact.

## Backlog and Issue Management

- Use AI for deduplication suggestions, issue classification, requirement clarification, acceptance-criteria drafting, and dependency discovery when the tracker remains authoritative.
- Do not allow automated deduplication to close/delete issues solely from semantic similarity; superficially similar reports can have different causes/contexts.
- Keep status, owner, priority, milestone, and dependency changes explicit and auditable.
- Require confirmation for bulk issue creation, reassignment, closure, priority changes, or external customer updates unless a deterministic approved rule owns the action.
- Prevent a model from treating old issue discussion or rejected proposals as current requirements without checking current state.

## Launch and Release Support

- Use AI to prepare launch checklists, release notes, FAQs, support material, stakeholder summaries, risk questions, and source-backed communication.
- Preserve actual shipped scope/version, flags, availability, pricing, regional state, support status, and known limitations from authoritative release/product systems.
- Do not announce or promise unshipped capabilities, dates, compatibility, or availability from draft plans.
- Require review for external claims, legal copy, pricing, security/privacy claims, customer commitments, and localization.
- Separate internal launch readiness from public launch messaging.

## Product Agents and Side Effects

- Treat agents that update issue trackers, roadmaps, docs, calendars, CRM, support systems, or release systems as side-effecting.
- Start with read/search/draft workflows; add write actions only when a repeated bottleneck justifies them.
- Use least privilege, explicit destinations, bounded scope, deterministic checks, and human confirmation for consequential changes.
- Do not let free-form model judgment automatically alter roadmap priority, close customer issues, send stakeholder/customer communication, or publish release material.
- Keep auditability and rollback/reconciliation for recurring automated changes.

## Product Data and Confidentiality

- Classify roadmap, unreleased designs, customer feedback, revenue/opportunity data, contracts, experiments, security findings, employee data, and research before hosted AI use.
- Use organization-approved accounts/sources and preserve source permissions.
- Minimize uploaded context and connect only sources needed by the workflow.
- Keep secrets/API keys/authentication material out of product prompts/documents.
- Escalate to sensitive/regulated/high-security routes when the data class requires stronger controls.

## Local and Hybrid Route

- Use local/private inference when unreleased/confidential product material cannot use hosted services or repeated private workflows justify local operation.
- Keep local models as bounded drafting/extraction/synthesis helpers unless they pass the team's product acceptance tasks.
- A hybrid route can keep private roadmap/customer context local while using hosted deep research for public market/competitor evidence under explicit routing rules.
- Local RAG does not guarantee freshness, source correctness, permissions, or prompt-injection resistance.
- Escalate shared local infrastructure to internal-platform/hardware owners when it becomes operationally significant.

## Team Evaluation Suite

- Maintain representative tasks: feedback synthesis, requirement drafting, current competitor research, experiment interpretation, decision brief, issue/backlog triage, and launch-summary preparation.
- Include cases with conflicting sources, stale roadmap information, ambiguous requirements, duplicate-looking issues, missing experiment assumptions, and confidential context that should not be exposed.
- Score source traceability, requirement accuracy, omission, decision usefulness, analytical correctness, correction/review time, permission fit, latency, and cost.
- Compare assistants/configurations against the same source set where practical.
- Do not use general writing/reasoning benchmarks as a substitute for product-team acceptance.

## Cost per Accepted Product Decision/Artifact

- Compare **total cost per accepted product artifact/decision-support outcome**: seats/API/research credits, connector setup, analyst/research effort, duplicate tools, correction/review, admin, and the cost of stale/wrong product information.
- A connected managed workspace can be economically strong when it reduces source gathering and preserves team context.
- Specialist research/data models can be justified when they materially reduce review or improve evidence quality on recurring high-value decisions.
- Do not measure value by number of generated PRDs/issues; measure accepted useful artifacts and reduced decision/work cycle time.

## Escalation Triggers

- Move from general team use to this scenario when product evidence/requirements/roadmap/experiment workflows become recurring shared work.
- Move to `research-and-insights-team/` when source discovery/evidence synthesis dominates.
- Move to `data-analysis-team/` when structured analytics/experimentation dominates.
- Move to `project-and-operations-team/` when execution/status/risk/coordination becomes the primary problem.
- Move to organization-scale knowledge/data/internal-platform routes when cross-team central infrastructure/governance becomes first-order.
- Narrow or stop agentic writes when review/rollback/authorization cannot be bounded safely.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared inference target materially constrains the team's route.
- Use `../../../hardware/sub/servers/` or `../../../hardware/sub/computers/` according to the existing target.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link research workflow to `decision-support/scenarios/teams/research-and-insights-team`.
- Link structured analysis to `decision-support/scenarios/teams/data-analysis-team`.
- Link managed workspace/services to canonical service owners when named.
- Link organization-scale knowledge/data/platform concerns to their organization scenario owners instead of duplicating them here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current managed-workspace connected-source/app/permission documentation, current ChatGPT/Gemini deep-research evidence, current code-backed/warehouse analytical evidence, and canonical AI Lab research/data owners.
- Current evidence supports permission-aware connected-source retrieval, source-grounded research, code-backed analysis, and increasingly action-capable workspace integrations. These product capabilities do not establish product-domain correctness or authorization to change roadmaps/issues.
- Connector catalogs/actions, deep-research behavior, model aliases, workspace sharing, analytics tools, plans, pricing, and internal product data are mutable; recheck them before rendering current guidance.
- Product decisions remain human-owned and source-backed.

## Validation

- Product source systems remain authoritative for requirements, roadmap, experiments, releases, and issues.
- User feedback synthesis preserves sampling/context and does not equate frequency with priority.
- Prioritization scores do not become model-generated false precision.
- Experiment/product metrics use deterministic analytical evidence.
- Competitor/current claims are source/date aware.
- Cross-functional disagreements remain visible until humans decide.
- Agent write actions have stronger controls than read/draft workflows.
- Team-owned decision records preserve source traceability outside chat memory.
- Organization-wide platform/governance remains delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
