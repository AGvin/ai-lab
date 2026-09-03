# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale sales/revenue operations spanning lead/account research, qualification, CRM context, opportunity/deal assistance, outreach/nurture, forecasting support, quote/proposal preparation, seller coaching, and governed revenue-process automation.
- Keep the scenario organization-scale. A small marketing/growth team belongs in its team route; a single consultant/seller belongs in the appropriate professional route.
- The defining constraints are **CRM truth, customer/prospect data, lead/account eligibility, external communication, pricing/quote authority, pipeline/forecast semantics, attribution, side-effecting CRM actions, and revenue-risk controls**.
- Do not turn this page into CRM or sales methodology procurement guidance. It owns the AI model/agent route and acceptance boundary.

## CRM and Revenue Systems Remain Authoritative

- Keep CRM, CPQ/pricing, contracts, billing, product catalog, entitlement, account hierarchy, consent/preferences, activity, opportunity, quote/order, and forecasting systems authoritative.
- Use models to research, summarize, draft, classify, recommend, coach, and perform only approved actions.
- Do not let assistant memory become the source of truth for customer status, pipeline stage, deal amount, discount, price, contract term, next step, or forecast category.
- Preserve lead/contact/account/opportunity/quote/activity IDs and source references for material AI outputs/actions.
- When sources conflict, route to deterministic system/owner rather than model plausibility.

## Integrated CRM Agent Route

- Prefer an organization-approved CRM/revenue-integrated AI route when it can use governed customer/account data, sales workflow state, permissions, actions, and audit without copying sensitive context into disconnected personal tools.
- Current Agentforce Sales is a current example: Salesforce documents prospecting/account research, lead nurturing, meeting booking, seller preparation/coaching, next-best actions, and quote-oriented workflows. Treat exact agent catalog, GA state, actions, pricing, data sources, and release behavior as mutable.
- Evaluate integrated sales agents on the organization's real funnel, customer segments, product complexity, account data quality, sales cycle, permissions, and approval rules.
- Start with read/research/draft/assist workflows before authorizing autonomous external communication or commercial actions.

## Lead and Account Research

- Use current public/internal sources to research accounts/contacts only when collection/use complies with organization policy and applicable data/marketing rules.
- Prefer authoritative company/CRM/current sources for material facts and record freshness/source.
- Distinguish verified facts from inferred intent/fit/priority.
- Do not invent headcount, budget, technology stack, pain, buying intent, relationship, or decision authority from sparse signals.
- Treat third-party enrichment sources as separate data providers with their own accuracy, license, and privacy boundaries.

## Qualification and Scoring

- Keep deterministic qualification requirements explicit where the organization has them: territory, product fit, customer type, budget/authority/need/timing criteria, eligibility, compliance, or another governed rule.
- Use AI scores/ranks as decision support only after validation against outcomes and bias/error analysis.
- Do not let a model-generated `hot lead` label become a factual customer attribute.
- Preserve reasons/evidence for ranking so sellers/revops can challenge incorrect signals.
- Re-evaluate scoring after product/market/territory/CRM schema changes.

## Prospecting and Outbound Communication

- Treat sending email/messages, booking meetings, updating CRM, adding contacts, or enrolling nurture sequences as side-effecting actions.
- Preserve consent/opt-out/suppression, regional marketing rules, customer status, contact ownership, and company policy in deterministic systems.
- Require review/approval appropriate to scale and risk before agents send external messages.
- Verify recipient/company, product/offer, claims, links, time/date/timezone, personalization facts, and sender identity.
- Do not fabricate mutual connections, customer references, company initiatives, urgency, availability, or personalized facts.
- Avoid uncontrolled volume optimization that damages sender reputation/customer trust or violates policy.

## CRM Write Actions

- Separate read/search/summarize from state changes such as creating/updating leads/contacts/accounts/opportunities/activities/tasks/forecast fields.
- Define field-level allowed actions, validation, ownership, stage transition rules, required evidence, idempotency, audit, and rollback/reconciliation.
- Do not allow free-form model judgment to close opportunities, mark legal/technical/security approval, change contractual status, or overwrite seller notes without an approved workflow.
- Preserve human ownership for ambiguous/high-value pipeline changes.
- Monitor bulk-change and duplicate-record failure modes.

## Opportunity and Deal Assistance

- Use AI to summarize account/deal history, identify missing information, prepare meetings, surface risks/questions, compare source documents, and draft next-step suggestions.
- Keep opportunity stage, amount, probability/forecast category, close date, competitors, contacts, commitments, and blockers grounded in CRM/source evidence.
- Do not infer deal probability or buyer intent as fact from conversational tone.
- Separate model recommendations from seller/manager decisions.
- Route contract/legal/security/product-feasibility claims to their authoritative owners rather than model memory.

## Pricing, Quotes, Discounts, and Commercial Terms

- Use deterministic product catalog/CPQ/pricing/approval systems for prices, bundles, eligibility, taxes/fees, discount thresholds, and contractual terms.
- AI may help configure/draft/explain a quote, but exact commercial values must be generated/validated by authoritative systems.
- Do not let a model invent a discount, exception, payment term, SLA, availability, or contractual promise.
- Require approval according to discount/value/exception thresholds.
- Preserve quote/version/approval IDs and final customer-facing artifact.

## Forecasting and Pipeline Analysis

- Use deterministic analytical models/SQL/BI for pipeline totals, conversion, velocity, coverage, forecast rollups, and historical performance.
- Define stage/probability/forecast-category semantics and time windows explicitly.
- AI can explain anomalies, generate questions, summarize pipeline, and propose risk factors; executed data owns numeric results.
- Do not turn correlation in activity/engagement data into guaranteed revenue outcome.
- Route organization-wide data semantics/analytics to `enterprise-data-analysis/` when central governance dominates.

## Seller Coaching

- Use AI for role play, call/deal review, objection practice, product/competitive preparation, and communication feedback from approved context.
- Current Agentforce Sales Coach is an example of CRM-contextual coaching; treat provider behavior as current capability evidence, not proof of seller improvement.
- Do not let model coaching fabricate customer objections/competitor facts or become employee performance evidence without appropriate human review.
- Separate training/simulation feedback from managerial performance assessment.

## Customer and Prospect Data Boundary

- Classify CRM/customer/prospect/contact, communication, contract, commercial, support, billing, and usage data before AI use.
- Use approved enterprise accounts/services and preserve source permissions.
- Minimize the fields/context sent to models and external enrichment providers.
- Keep credentials, payment secrets, private keys, authentication tokens, and unnecessary sensitive attributes out of prompts.
- Escalate regulated/high-security customer data to appropriate stronger-control scenarios.

## Sensitive Attributes and Fairness

- Do not infer or use protected/sensitive traits or proxies for targeting, qualification, priority, or treatment unless there is a clearly lawful/approved business use with appropriate controls.
- Validate scoring/routing across relevant groups/regions/customer types for systematic error or exclusion.
- Keep human review for edge/high-value decisions where model ranking can materially affect opportunity access.
- Do not use conversational style or accent as a proxy for value, intent, or risk.

## Revenue Agents and Automation

- Treat multi-step agents that research, send outreach, book meetings, create tasks, update CRM, generate quotes, or trigger downstream workflows as high-impact automation.
- Define identity, tools/scopes, eligible records, action limits, approvals, schedule/trigger, retries, idempotency, stop conditions, and audit.
- Bound autonomous outreach volume and commercial-action authority.
- Do not allow agent reasoning alone to bypass pricing, legal, privacy, security, or credit approval systems.
- Treat inbound email/web/CRM notes as untrusted prompt-injection sources when agents can act.

## Evaluation Suite

- Build a versioned evaluation set across prospect research, qualification, account briefing, meeting prep, outbound draft, opportunity summary, CRM update proposal, forecast explanation, quote configuration, and a scenario that must escalate.
- Include stale CRM data, duplicate accounts, conflicting source facts, missing consent, restricted contact, unsupported discount, ambiguous stage, prompt-injected email, and high-risk customer data.
- Score factual/source accuracy, CRM-field correctness, action safety, communication quality, policy adherence, seller correction time, downstream conversion/rework where meaningful, latency, and cost.
- Test agents end-to-end rather than isolated text generation.
- Re-run after model/agent/policy/CRM/product/pricing changes.

## Observability and Revenue Accountability

- Record agent/model/workflow version, records read/changed, sources, messages sent, meetings booked, actions/approvals, errors, and final outcomes where permitted.
- Monitor false qualification, bad personalization, duplicate/wrong-account changes, failed meetings, inappropriate outreach, discount/quote errors, CRM drift, complaints/opt-outs, and prompt-injection events.
- Distinguish AI-generated activity volume from actual accepted revenue outcomes.
- Preserve enough trace to investigate commercial commitments and record mutations.

## Cost per Accepted Revenue Outcome

- Compare **total cost per accepted revenue-operation outcome**: seats/API/agent charges, enrichment data, CRM/CPQ, research, retries, seller review/correction, admin/integration, bad outreach, sales-time waste, and commercial/customer risk.
- Do not optimize on messages sent, leads touched, or meetings booked alone.
- Measure qualified accepted opportunities/actions and downstream seller/customer outcomes where attribution is credible.
- A stronger/more expensive model can be economical if it materially reduces false research/personalization/CRM edits; a cheaper model can be better for bounded deterministic classification.

## Local/Private and Hybrid Route

- Use private/self-hosted inference when customer/commercial data cannot use hosted processing or organization economics/control justify it.
- Keep CRM/CPQ/pricing/authorization systems authoritative regardless of model location.
- Hybrid routes can keep sensitive account/deal context private while using hosted models for public account research under explicit routing rules.
- Local inference does not remove outreach/action authorization, prompt injection, data quality, audit, or evaluation requirements.
- Escalate shared model gateway/inference to `internal-ai-platform/` when it becomes central infrastructure.

## Escalation Triggers

- Move to this scenario when CRM-integrated sales/revops research, scoring, outreach, pipeline, quotes, or automation becomes organization-scale.
- Move to `enterprise-data-analysis/` when governed revenue analytics/semantic metrics dominate.
- Move to `enterprise-workflow-automation/` when agents coordinate broadly across finance/procurement/fulfillment/other back-office systems.
- Move to `internal-ai-platform/` when central model routing/contracts/budgets/agent runtime become primary.
- Move to regulated/high-security routes when customer/commercial data or actions require stronger controls.
- Narrow/stop autonomy where external communication, CRM mutation, pricing, or authorization cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted inference target is selected and hardware materially constrains model/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared organization sales/revenue inference infrastructure.
- Sales/CRM infrastructure procurement remains outside this scenario.

## Canonical Links

- Link marketing/growth team context to `decision-support/scenarios/teams/marketing-and-growth-team` where relevant.
- Link enterprise analytics/platform/automation concerns to their organization scenario owners.
- Link named CRM/sales services and exact models to canonical catalog owners when materialized.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Salesforce Agentforce Sales release/announcement and Sales Coach documentation plus canonical AI Lab managed-workspace/agent owners.
- Current evidence establishes CRM-integrated agents for prospecting/account research, lead nurturing/qualification, seller coaching, meeting booking, next-best actions, and quote-oriented workflows. These capabilities do not establish factual prospect intent, correct commercial authority, or organization-specific revenue lift.
- Sales agent catalogs, actions, CRM/data integrations, pricing, releases, enrichment sources, privacy/marketing rules, and product behavior are mutable; recheck them before rendering current guidance.
- CRM/CPQ/approved business systems, deterministic policy, sellers/managers, and measured revenue outcomes remain the acceptance authority.

## Validation

- CRM/CPQ/pricing systems remain authoritative for customer, opportunity, commercial, and forecast state.
- Research/qualification scores preserve source/evidence and do not become hidden customer facts.
- External outreach and CRM/quote changes are side-effecting actions with explicit policy/approval.
- Deterministic consent/suppression/pricing/legal/security rules are not replaced by model judgment.
- Seller coaching remains assistance and is not automatically employee-performance evidence.
- Evaluation measures accepted commercial actions/outcomes rather than activity volume alone.
- Internal-platform/enterprise-automation/regulated concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
