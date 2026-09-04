# Documentation Requirements

## Scenario Fit

- Present this scenario for a small multi-role business team—typically a limited number of people sharing customers, documents, schedules, operations, marketing, sales, finance/admin, or support work—where AI must work across **shared state, shared budgets, shared tools, and basic administration** without assuming an enterprise AI platform team.
- Keep the scenario team-scoped. One person's work belongs in the relevant professional scenario; organization-wide model gateways, formal centralized governance, multi-business-unit deployment, or dedicated platform operations belong in organization routes.
- Distinguish this scenario from role-specific team scenarios: use it when the business is small enough that several roles share one practical AI/workspace decision rather than each function requiring its own specialized model route.
- Do not turn this page into small-business software procurement. It owns the model/workspace route and when the team should split into specialist workflows.

## Start With Shared Work, Not Individual Chat

- Identify which work must actually be shared: company documents, customer information, email/calendar, meeting notes, proposals, marketing assets, product/service knowledge, tasks, recurring reports, spreadsheets, support history, or internal procedures.
- Separate personal/private employee use from business workspace use. Shared business context should live in organization-approved systems rather than one employee's personal chat history or memory.
- Define the authoritative system for each shared state: drive/document store, CRM, calendar, ticketing, accounting system, project tracker, website/CMS, or another source.
- Treat the assistant as a reasoning/search/action surface over those systems, not as the sole record for customer commitments, invoices, deadlines, permissions, or business procedures.
- Avoid building custom infrastructure until repeated accepted workflows justify the operational burden.

## Default Managed Team Workspace Route

- Prefer one organization-owned managed AI workspace when it covers most routine team needs and its data terms fit the business. This minimizes account sprawl, duplicated subscriptions, disconnected chat histories, and uncontrolled personal-tool use.
- Current ChatGPT Business is an example of a collaborative business workspace whose data is excluded from model training by default and where each user retains their own conversation history unless they choose to share specific content. Treat exact plan features, limits, apps/plugins, Codex access, retention, and pricing as mutable.
- Current Google Workspace with Gemini is an example of AI embedded into an existing productivity suite; current Workspace protections and user/source permissions carry into supported Gemini features, while administrators can restrict AI access and specific data sources.
- Evaluate the workspace on the team's real recurring workflows rather than model reputation alone: shared source retrieval, drafting, meeting follow-up, spreadsheet/report work, customer response assistance, research, and one or two bounded action workflows.
- Add a second managed provider only when it repeatedly delivers a distinct accepted-result or ecosystem advantage worth the extra account, policy, billing, and context fragmentation.

## Accounts, Roles, and Administration

- Give each person an individual managed account. Do not solve collaboration by sharing one login.
- Assign at least one clearly responsible workspace owner/admin and a backup owner where the product/business size makes this practical.
- Review member lifecycle: invite, role change, offboarding, lost device/account recovery, shared-link access, and ownership of reusable company artifacts.
- Distinguish user-level permissions from workspace-level feature/app permissions. A person may have access to an AI workspace while a particular connector/app remains disabled by the administrator.
- Current ChatGPT Business app/plugin controls allow administrators to manage enabled integrations; current Google Workspace admin controls can restrict Gemini/features/data access. Treat exact control granularity as product-specific and mutable.
- Keep personal workspaces/accounts separate from company-owned workspaces so business data does not remain tied to an employee's personal subscription after departure.

## Shared Knowledge and Documents

- Use connected/shared sources when they materially reduce repeated uploading and improve freshness, but preserve the source system as authoritative.
- Verify that the assistant respects source permissions and that the connected integration does not broaden access beyond what the user can legitimately see.
- Current Google Workspace documentation states that Gemini can only use Workspace data the user has access to and that administrator/content-owner restrictions can further block access. Current ChatGPT synced-app/business controls similarly support admin-managed source connections; verify the exact configuration used.
- Prefer a bounded company folder/site/library over broad all-drive/all-mail indexing when it satisfies the use case.
- Keep provenance visible: important answers should identify the underlying document/message/record, and stale/conflicting sources should not be silently merged into one confident answer.
- When the primary problem becomes a durable organization-wide knowledge architecture, route to the business-knowledge-assistant organization scenario rather than growing this page into a RAG platform design.

## Common Team Workloads

- Evaluate at least the recurring categories that matter to this business:
  - drafting/reviewing customer and vendor communications;
  - proposals, estimates, statements of work, or internal documents;
  - meeting preparation, summaries, and follow-up;
  - current web/market/vendor research;
  - spreadsheet/data summaries and recurring reports;
  - marketing copy/creative ideation;
  - support/customer-success response assistance;
  - internal procedure/knowledge lookup;
  - calendar/task/project coordination;
  - bounded workflow automation.
- Route sustained specialist needs to the appropriate team scenario instead of forcing a general workspace to be the best coding, analytics, research, creative, or support model for every role.

## Customer and Business Data Boundary

- Classify business data before enabling hosted processing: public marketing material, ordinary internal content, customer contact data, confidential contracts/pricing, payment/financial data, employee data, credentials, regulated records, or other sensitive classes.
- Do not allow a managed workspace approval to become blanket approval for every connected source or data class.
- Minimize sensitive data in prompts and uploads where the full record is unnecessary.
- Keep passwords, API keys, private keys, payment-card data, recovery codes, and other authentication secrets out of general assistant context.
- If regulated/high-sensitivity data becomes routine, route to the applicable sensitive professional or regulated-organization workflow rather than relying on a small-business general setup.

## Apps, Plugins, and Connected Tools

- Treat every integration as a new data/tool boundary. Review what it can read, what it can write, which account authenticates, which workspace members can use it, and how access is revoked.
- Current ChatGPT Business documentation distinguishes plugin installation from underlying app permissions and lets admins manage both; treat exact available apps/actions as mutable.
- Enable the minimum set of connectors that support proven workflows. Do not connect mail, drive, CRM, accounting, calendar, or project systems merely because a connector exists.
- Re-review permissions when the provider adds write/actions to a previously read-oriented integration.
- Preserve source-system access controls; the AI integration must not become a shortcut around folder, mailbox, CRM, calendar, or project permissions.

## Read-Only Assistance vs Actions

- Separate read/search/summarize workflows from actions that modify external state.
- Low-risk examples can include drafting an unsent response, summarizing a meeting, suggesting task wording, or preparing a proposed calendar entry.
- Require confirmation or deterministic policy for sending external messages, scheduling/inviting third parties, editing shared files, updating CRM/customer status, publishing content, changing permissions, deleting records, purchasing, or making financial commitments.
- Verify account, recipient/customer, destination, amount/date/timezone, and attachment/context before a consequential action.
- Do not let a broad natural-language request such as `handle this customer` authorize multiple side effects implicitly.

## Sales, Marketing, and Customer Communication

- Preserve customer facts, prices, product/service claims, contract terms, availability, and commitments in authoritative systems/source material.
- Use the model to draft/segment/summarize/brainstorm, but verify externally sent facts and promises before delivery.
- Do not fabricate testimonials, customer outcomes, product capabilities, discounts, inventory, or deadlines.
- For personalized outreach, ensure the source and use of customer/prospect data is permitted and keep opt-out/marketing-law obligations outside model judgment where deterministic systems should enforce them.
- Route high-volume or organization-scale sales/support automation to the dedicated organization scenarios.

## Spreadsheet and Financial/Admin Work

- Use code/formula-backed calculation for budgets, forecasts, invoices, reconciliations, payroll-related summaries, tax-support calculations, or other material arithmetic.
- Preserve source spreadsheets/accounting exports and verify totals against the authoritative system.
- AI can help categorize, explain, find anomalies, or draft narratives, but should not autonomously authorize payments, move money, submit taxes, change payroll, or alter accounting records from free-form model judgment.
- For complex recurring analytics, route to `data-analysis-team/` or an organization data-analysis scenario.

## Research and Current Information

- Use source-grounded web/deep research for current vendor comparisons, market facts, regulations, product capabilities, pricing, or local business information.
- Prefer primary/authoritative sources for claims used in proposals, customer communication, procurement, or policy.
- Citation presence is not sufficient; verify that the source actually supports the material claim.
- Record dates/effective periods when a business decision depends on mutable prices, terms, laws, schedules, or product capabilities.

## Local and Hybrid Route

- Use local inference when business confidentiality, offline work, repeated private workloads, or provider independence justifies endpoint/runtime administration and exact hardware fit is validated.
- Keep local models as bounded helpers unless they pass the same accepted-result tests as managed alternatives. Small teams should not inherit a homegrown inference stack merely to avoid one subscription.
- A hybrid route can keep selected private documents or preprocessing local while using an approved hosted workspace for public/sanitized reasoning under an explicit routing rule.
- Local inference does not remove endpoint security, user separation, backups, update, logging, malware, or access-control responsibilities.
- If running the model service becomes a real shared infrastructure job, route to internal-platform/server/hardware ownership rather than treating it as a simple small-team tool.

## Direct API and Bounded Automation

- Use direct APIs only for a concrete repeatable workflow that a managed workspace cannot express well: batch classification, structured extraction, custom internal UI, templated content generation, or a carefully bounded system integration.
- Protect API keys, apply project-level budget/rate limits, validate structured outputs, and make retries/idempotency explicit.
- For customer-facing or financial/operational automation, use deterministic validation and human approval proportional to consequence.
- Track provider/intermediary/tool chain and logging because automation can copy business/customer data into additional systems.
- Do not build a custom AI platform simply because an API exists; include development, maintenance, monitoring, security, and incident cost in the route decision.

## Shared Quality and Operating Method

- Build a small team acceptance set from real recurring tasks and approved data: one document workflow, one current-research task, one spreadsheet/report task, one customer communication task, and any high-value specialist workflow.
- Measure accepted-result quality, correction/review time, source support, latency, team usability, permission friction, and total cost.
- Define a lightweight shared usage rule: permitted data classes, approved workspace/account, required review for external outputs, prohibited secrets/actions, and escalation owner.
- Keep reusable prompts/templates/workflows in company-owned shared storage rather than one employee's private history.
- Review the setup when models, plans, connected apps, staff, or business data sensitivity materially change.

## Cost per Accepted Team Outcome

- Compare **total cost per accepted team outcome**: seats/subscriptions, API usage, credits, duplicate providers, admin time, onboarding/training, connector setup, correction/review, local infrastructure, and error/incident burden.
- A single integrated workspace can be cheaper than a nominally cheaper mix of personal tools when it reduces policy, account, source, and collaboration fragmentation.
- Do not buy every employee the same premium capability if only certain roles need it; use the product's supported licensing/access model and measured workload needs.
- Conversely, do not optimize seat cost by sharing accounts or moving business data into personal/free tools.

## Escalation Triggers

- Move from individual professional use to this scenario when multiple people share company context, sources, budgets, or workflows.
- Move to a specialist team scenario when software development, analytics, research, product, marketing, creative, operations, or customer-support work has distinct model/evaluation needs.
- Move to an organization/internal-platform route when centralized model access, multi-department governance, advanced RBAC/DLP/residency, shared agent infrastructure, observability, or significant scale becomes the real problem.
- Move to a regulated/high-security route when business data requires materially stronger legal/security/isolation controls.
- Move to local/private processing only when the complete operational burden is justified and approved.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when the team already uses a fixed local inference host/workstation and exact hardware materially constrains model selection.
- Use `../../../hardware/sub/computers/` for a shared workstation route and `../../../hardware/sub/servers/` for a dedicated inference host.
- Hardware purchasing remains outside this scenario; managed workspace/API/hybrid routes remain valid when no suitable shared hardware exists.

## Canonical Links

- Link named managed workspaces/services to their canonical service owners when materialized.
- Link role-specific needs to the applicable professional/team scenario or decision guide instead of duplicating specialized contracts.
- Link exact local model candidates only when current evidence justifies them and their canonical Model Reference owners exist.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party ChatGPT Business workspace/privacy/app-admin documentation, current Google Workspace with Gemini enterprise-data/access-control/DLP documentation, and canonical AI Lab service/model owners.
- Current evidence establishes that managed small-team workspaces provide individual accounts, organization data protections, administrator controls, and permission-aware connected-source behavior, while exact app/action access differs by product/configuration.
- Current Google Workspace evidence also demonstrates that AI-specific DLP coverage can be feature/source specific; do not assume one control covers every Gemini surface or data type.
- Workspace features, plugin/app catalogs, write actions, DLP/admin controls, retention, plans, seat rules, model aliases, and pricing are mutable; recheck them before rendering current guidance.
- Provider controls support the team's governance; they do not replace business policy, source correctness, or human review.

## Validation

- Shared workspace/state—not generic individual use—defines the scenario.
- Individual managed accounts are used instead of shared credentials.
- Authoritative business systems remain sources of truth for customers, money, deadlines, and shared records.
- Connected apps preserve source permissions and have explicit read/write boundaries.
- External/customer/financial actions have stronger confirmation and deterministic controls than read-only assistance.
- The small team does not inherit unnecessary enterprise/self-hosted infrastructure.
- Specialized functions can route to their dedicated scenario instead of being flattened into one general workspace.
- Consumer/free convenience does not override business data policy.
- Cost is measured per accepted team outcome including administration and review.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
