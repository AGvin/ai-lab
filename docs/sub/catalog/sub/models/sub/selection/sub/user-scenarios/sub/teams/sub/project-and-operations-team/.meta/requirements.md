# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person project/operations team coordinating requirements, work items, meetings, schedules, dependencies, risks, recurring processes, status, operational documents, and stakeholder reporting.
- Keep the scenario team-scoped. One general knowledge worker belongs in the professional route; product problem/roadmap decisions belong in `product-management-team/`; organization-wide workflow automation/platform governance belongs in organization routes when it dominates.
- Distinguish this scenario from `small-business-team/`: here the primary AI-selection constraint is **shared execution state, ownership, deadlines, dependencies, recurring processes, risk, and controlled updates to work systems**.
- Do not turn the page into project-management methodology or a Jira/Asana/etc. product comparison. It owns the model/workspace route and action-safety contract for shared project/operations work.

## Authoritative Work Systems

- Identify the authoritative systems for work items, project plans, requirements, meeting records, schedules, runbooks/SOPs, risks/issues, approvals, calendars, and reports.
- Use AI to search, summarize, draft, compare, classify, and propose updates; do not let assistant memory become the only record of owner, status, priority, due date, dependency, commitment, or decision.
- Preserve work-item/page/project IDs and source links in material summaries so people can verify current state.
- When sources disagree, surface the conflict and authoritative owner rather than synthesizing a fictional `latest state`.
- Treat generated status reports as derived views that must be refreshable from current source systems.

## Default Work-Management-Native Route

- Prefer an organization-approved assistant/agent integrated with the team's work-management and knowledge systems when it preserves permissions and reduces copy/paste without adding unnecessary infrastructure.
- Current Atlassian Rovo is an example of a work-management-native route: current Jira/Confluence/Rovo features support permission-aware search/chat, content generation, work-item/page actions, configurable agents, and automation-triggered agents. Treat exact plan/access/action catalogs and rollout state as mutable.
- Evaluate an integrated route on actual team workflows: find current project state, summarize blockers, draft a status update, prepare a meeting brief, clarify a work item, identify stale/contradictory information, and propose one bounded update.
- Do not assume the work-management-native model is best for every research/writing/analysis task; add specialist routes only where a recurring accepted-result advantage justifies context/provider complexity.

## Search, Context, and Permission Inheritance

- Use permission-aware retrieval over project/knowledge sources when available; the assistant must not expose work items/pages/files the requesting user cannot access.
- Current Rovo documentation states that search/chat use only content the user has permission to access across Atlassian and connected sources. Treat this as product-specific behavior to verify, not a universal connector guarantee.
- Keep source identity visible in answers and status summaries.
- Prefer scoped projects/spaces/folders to broad organization-wide sources when that reduces irrelevant or sensitive context.
- Treat connected third-party sources as additional data paths whose access, indexing, retention, and permissions must be reviewed.

## Requirements and Work-Item Quality

- Use AI to draft/rewrite descriptions, acceptance criteria, checklists, dependencies, questions, and summaries from verified source context.
- Do not allow the model to invent scope, business priority, technical feasibility, assignee, estimate, due date, or acceptance criteria that the team has not approved.
- Ask the model to identify ambiguity, missing owner, missing acceptance evidence, conflicting requirements, dependency uncertainty, and stale references.
- Keep final approved work-item state in the tracker.
- For implementation/engineering work, route detailed coding-agent/model questions to the software-development team/decision owners rather than duplicating them here.

## Ownership, Status, and Deadlines

- Treat owner, assignee, status, milestone, due date, priority, and dependency as controlled project state.
- Do not infer that a person owns a task merely because they were mentioned in a meeting or document.
- Verify dates/timezones and distinguish target/forecast/commitment/deadline where the team uses different meanings.
- Use deterministic overdue/status/dependency rules where possible rather than free-form model judgment.
- Require explicit review for bulk reassignment, priority changes, milestone moves, closure, cancellation, or deadline changes.

## Meetings and Follow-Up

- Use AI to prepare agendas, gather current project context, summarize notes/transcripts, extract candidate actions/decisions, and draft follow-up.
- Preserve the original meeting notes/recording/transcript where policy permits and the team requires traceability.
- Treat extracted actions as proposals until owner, due date, destination project, and wording are confirmed.
- Distinguish a discussion point, tentative suggestion, decision, action item, risk, and blocker rather than flattening them into one list.
- Do not let a meeting summary overwrite more recent tracker state without checking timestamps/owners.

## Status and Executive Reporting

- Generate status from authoritative work systems and named source documents rather than from conversational memory.
- Define the report's scope/time window and required dimensions: completed, in progress, next, blockers, risks, decisions, schedule, budget/capacity, and dependencies as applicable.
- Separate observed status from model interpretation or forecast.
- Verify counts, dates, owners, milestones, and key metrics deterministically before circulation.
- Flag missing/stale inputs rather than inventing a green/amber/red assessment.
- Keep source links available for important claims in the status report.

## Risks, Issues, and Dependencies

- Use AI to surface candidate risks, contradictions, dependency chains, stale items, and missing mitigations, but keep risk acceptance/priority human-owned.
- Preserve distinction between a risk (possible future event), issue/blocker (current condition), dependency, assumption, and decision.
- Require source evidence for `blocked` or `at risk` status when the team uses those states operationally.
- Current Atlassian Rovo includes agents/automation patterns for readiness/blocker checking; treat such outputs as decision support unless a deterministic approved rule owns the status transition.
- Do not allow semantic similarity alone to establish or remove a dependency.

## SOPs, Runbooks, and Operational Knowledge

- Use AI to retrieve, explain, compare, and draft procedures while keeping approved SOP/runbook content authoritative.
- Preserve owner/effective date/version and escalation path for procedures used operationally.
- Do not let the model silently blend old and new procedure versions.
- For safety/security/financial/production-sensitive procedures, require exact source verification and deterministic checks appropriate to consequence.
- Route incident/security-specific automation to the applicable organization/security route when the workflow exceeds general operations.

## Read-Only vs Write-Capable Agents

- Separate search/read/summarize/draft capabilities from tools that create or mutate work state.
- Current Rovo agent tools can create/update Jira work items, create/edit Confluence pages, raise service requests, and perform other actions while respecting user permissions and requesting confirmation for consequential tools. Treat exact tool behavior/limits as mutable.
- Start new agent workflows read-only or proposal-first where practical.
- Add write actions only for a repeated, well-bounded workflow with clear fields, destination, owner, validation, and rollback/reconciliation.
- Authorization to read a project does not imply authorization to edit all of its work items/pages.

## Automation and Autonomous Triggers

- Treat event/schedule-triggered agents as a higher operational tier than interactive assistance.
- Current Atlassian automation can invoke Rovo agents under admin-managed rules; in that automation context the agent response can feed subsequent deterministic automation actions. Treat trigger/action behavior as exact-product evidence only.
- Define trigger, eligible scope, inputs, model instruction, output schema, downstream action, idempotency/deduplication, retry limit, failure path, and owner before activation.
- Avoid unbounded loops where model-generated text retriggers the same workflow.
- Preserve logs sufficient to know what triggered, what context was used, what the model returned, and what downstream action actually occurred.

## Change and Approval Boundaries

- Require stronger approval for changes to deadlines, priorities, ownership, external commitments, access/permissions, production/operational procedures, financial state, customer communication, or irreversible records.
- Use native workflow approvals and deterministic permission checks where available; do not replace them with a model asking itself whether an action is safe.
- Keep external stakeholders/clients/vendors as separate communication boundaries.
- Verify recipient, project, record, date, and attachments before sending a consequential update.

## Project and Operations Data Boundary

- Classify project data: public, ordinary internal, customer/client, confidential strategy, employee/personnel, contract/pricing, security/incident, production, financial, or regulated.
- Use organization-approved workspaces/accounts and preserve source permissions.
- Minimize broad connector scope and uploaded context.
- Keep secrets, API keys, credentials, recovery codes, private keys, and unnecessary customer/personnel data out of prompts/project docs.
- Escalate to sensitive/regulated/high-security routes when data class or failure severity requires stronger controls.

## Prompt Injection and Untrusted Work Content

- Treat issue descriptions, comments, emails, pasted customer/vendor text, uploaded documents, web pages, and connected-source content as potentially untrusted instructions when an agent can act.
- Retrieved content must not override system/team policy or expand tool permissions.
- Require bounded tools and confirmation for consequential actions even when a work item tells the agent to perform them.
- Avoid exposing sensitive secrets to an agent merely because an untrusted item requests them.

## Deterministic Calculations and Metrics

- Use spreadsheets/SQL/Python/reporting systems for schedule math, counts, SLA metrics, budgets, capacity, throughput, forecast calculations, and other material arithmetic.
- The assistant can generate/explain formulas/queries, but the executed deterministic output owns the number.
- Preserve metric definitions and time windows in recurring reports.
- Route sustained analytics to `data-analysis-team/` rather than duplicating its full analytical contract.

## Local and Hybrid Route

- Use local/private inference when project/client/operational data cannot leave the endpoint or repeated private workflows justify local operations.
- Keep the work tracker/knowledge source authoritative regardless of model location.
- A hybrid route can keep sensitive internal content local while using hosted models for public research or sanitized drafting under an explicit routing rule.
- Local inference does not remove user separation, authentication, backups, logging, prompt-injection, or action-permission requirements.
- Escalate shared local infrastructure to internal-platform/hardware owners when it becomes a service.

## Team Evaluation Suite

- Maintain representative tasks: current-state retrieval, meeting-to-actions, work-item clarification, blocker/risk summary, status report, SOP lookup, and one proposed/write action.
- Include adversarial cases: stale page vs current tracker, conflicting due dates, ambiguous owner, duplicate-looking issue, untrusted instruction inside a comment, missing source, and an action that should require confirmation.
- Score source/state accuracy, omission, update safety, ownership/deadline correctness, permission fit, correction/review time, latency, and cost.
- Compare agent/model configurations under the same project/source state where practical.
- Provider work-management demos are eligibility evidence, not team acceptance.

## Cost per Accepted Operations Outcome

- Compare **total cost per accepted coordination/operations outcome**: seats/API, connector setup, automation usage, failed actions, duplicate work, correction/review, admin, incident/error risk, and time saved finding/updating state.
- An integrated work-management agent can be economical when it reduces context gathering and safely writes back to the authoritative system.
- A stronger general model may be worth extra cost for difficult synthesis but can lose value if it cannot preserve/update project state safely.
- Measure accepted status/action/workflow outcomes, not generated summaries alone.

## Escalation Triggers

- Move from generic team use to this scenario when ownership/status/dependencies/meetings/recurring operations become shared AI workflows.
- Move to `product-management-team/` when product evidence/requirements/roadmap decisions dominate.
- Move to `data-analysis-team/` when structured operations analytics dominates.
- Move to organization workflow-automation/internal-platform routes when AI agents operate across many departments/systems with centralized identity, policy, observability, or high action volume.
- Move to high-security/regulated routes when operational data or actions require stronger controls.
- Narrow or stop write-capable automation when ownership, rollback, verification, or failure handling cannot be made reliable.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared inference target materially constrains the route.
- Use `../../../hardware/sub/servers/` for a dedicated operations/assistant host and `../../../hardware/sub/computers/` for a bounded team workstation route.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link product decisions to `catalog/models/selection/user-scenarios/teams/product-management-team` when appropriate.
- Link structured analysis to `catalog/models/selection/user-scenarios/teams/data-analysis-team`.
- Link work-management/services to their canonical software/service owners when materialized.
- Link organization-scale agent automation to its organization scenario rather than duplicating platform concerns.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Atlassian Rovo/Jira/Confluence search, agent, tool/action, and automation documentation plus canonical AI Lab managed-workspace owners.
- Current evidence establishes permission-aware multi-source search, work-context generation, configurable agents, work-item/page tools, confirmation for consequential tools, and admin-controlled automation-triggered agents. These features do not establish correct project state or authorization to make every operational change.
- Agent/tool catalogs, plan access, rollout state, automation behavior, permissions, connector coverage, model/reasoning tiers, pricing/credits, and work-system data are mutable; recheck them before rendering current guidance.
- Authoritative tracker/knowledge state and human/approved workflow controls remain the acceptance authority.

## Validation

- Work trackers/knowledge systems remain authoritative for ownership, status, dates, dependencies, procedures, and decisions.
- Search/read/draft and state-changing actions remain separate risk classes.
- Meeting-derived actions require confirmation of owner/date/destination before becoming authoritative state.
- Status/risk reports remain source-linked and do not invent missing/stale state.
- Agent automation has explicit trigger/scope/idempotency/retry/failure/ownership rules.
- Untrusted work content cannot silently expand agent authority.
- Deterministic calculations remain outside prose-only model reasoning.
- Organization-scale workflow/platform concerns are delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
