# Documentation Requirements

## Scenario Fit

- Present this scenario for a multi-person customer-success/support team sharing tickets/conversations, account context, product/support knowledge, summaries, response assistance, triage, follow-up, and human escalation.
- Keep the scenario team-scoped. One professional drafting customer replies can remain in `general-knowledge-worker/`; organization-scale high-concurrency voice/digital contact-center infrastructure belongs in `organizations/customer-service-and-contact-center/` when that becomes the primary constraint.
- Distinguish this scenario from `small-business-team/`: here **customer conversation state, knowledge grounding, resolution quality, escalation, case ownership, customer data, and controlled support actions** determine the model route.
- Do not turn the page into helpdesk vendor selection. It owns AI model/assistant/agent routing and acceptance for a bounded support/success team.

## Preserve Customer-Support Sources of Truth

- Identify authoritative systems for customer/account identity, entitlements/subscriptions, tickets/conversations, CRM fields, product/service status, orders, support policies, knowledge articles, runbooks, incident notices, and customer commitments.
- Use AI to search, summarize, draft, classify, troubleshoot, and propose actions; do not let assistant memory become the only record of customer status, entitlement, promised follow-up, refund, cancellation, SLA, or case resolution.
- Preserve conversation/case/account IDs and source links in internal summaries where useful.
- When sources conflict, surface the discrepancy and authoritative owner rather than selecting a plausible customer-facing answer.
- Keep approved support knowledge and current product/system state distinct from generated response wording.

## Default Support-Integrated AI Route

- Prefer an organization-approved AI capability integrated with the team's support/helpdesk/knowledge workflow when it preserves access control, conversation state, routing, and handoff while reducing copy/paste.
- Current Intercom/Fin is an example of a support-integrated route: current documentation describes AI responses across channels, workflow-based configuration, audience targeting, human handoff/escalation, conversation status visibility, and integration with external helpdesks. Treat exact capabilities, channels, pricing/outcome definitions, and rollout state as mutable.
- Evaluate support AI on the team's real top contact reasons rather than generic assistant benchmarks.
- Start with response assistance or bounded autonomous resolution for well-grounded low-risk intents before expanding to actions or high-consequence cases.
- Keep the ability for customers/agents to reach a human when the automation cannot resolve safely or accurately.

## Knowledge Grounding

- Use approved support/product knowledge as the primary answer source for product behavior, policies, procedures, eligibility, troubleshooting, and known limitations.
- Preserve article/document audience permissions and visibility. Current Fin documentation, for example, states that it respects audience targeting on Intercom Articles; treat this as product-specific evidence, not a universal RAG guarantee.
- Keep source links/identities available to support reviewers for important answers.
- Distinguish published support policy from internal draft notes, historical docs, community suggestions, and generated text.
- Detect stale or conflicting knowledge and route it to knowledge owners rather than letting the model normalize contradictions.
- RAG/knowledge grounding reduces unsupported answering risk but does not guarantee source correctness, completeness, freshness, or correct interpretation.

## Customer Context and Personalization

- Use only customer/account attributes that the support workflow is permitted to access and that materially improve resolution.
- Keep identity verification/authorization separate from conversational recognition. Knowing an account email/name does not authorize disclosure or account-changing actions.
- Do not infer customer plan, entitlement, purchase, identity, region, health/financial status, or other sensitive attribute when it is not present in an authoritative source.
- Minimize unnecessary customer data passed to the model and connected providers.
- Preserve account/ticket separation so one customer's information cannot leak into another conversation or reusable prompt/memory.

## Response Assistance

- Use AI to summarize context, draft/rewrite responses, suggest troubleshooting steps, translate, retrieve sources, and identify missing information.
- Require human review for customer-facing drafts when the use case is new, poorly measured, high-risk, or contains commitments/financial/legal/security implications.
- Verify names, product/account facts, links, prices, dates, policy language, instructions, and promises before sending.
- Do not fabricate troubleshooting outcomes, refunds, credits, availability, delivery dates, incident resolution, or engineering status.
- Preserve the sent response and final case state in the helpdesk rather than chat history.

## Autonomous Resolution Boundary

- Permit autonomous resolution only for intents with a defined knowledge source, acceptance criteria, safe response/action boundary, measurable handoff path, and low enough failure severity.
- A model response should not close a case merely because it sounded complete; define how resolution is confirmed/assumed and how reopened/follow-up conversations are handled.
- Current Fin documentation exposes resolved, escalated/handoff, pending, and negative-experience views and defines configurable resolution/handoff behavior; use such product states as evidence inputs rather than universal definitions.
- Maintain a sampled QA process for autonomous resolutions, especially after model/knowledge/workflow changes.
- Narrow or disable autonomous resolution for intents with repeated hallucination, high reopen/escalation, low customer satisfaction, or unacceptable business risk.

## Human Handoff and Escalation

- Define explicit handoff triggers: customer asks for a human, repeated failure/no progress, negative/frustrated interaction, unsupported intent, high-risk topic, missing authorization, policy exception, sensitive account action, incident/severity threshold, or another team-specific rule.
- Current Fin documentation supports configurable escalation rules/guidance/workflows and automatic handoff in selected high-risk situations; treat exact default behavior as mutable product evidence.
- Before handoff, collect only the additional information needed to help the receiving human when policy permits.
- Pass the full relevant conversation/context/source trail to the teammate so the customer does not have to repeat the issue unnecessarily.
- Do not allow automation to trap a customer in repeated AI responses when escalation conditions are met.
- Track handoff reason so the team can improve knowledge, routing, product, or AI policy.

## Triage and Routing

- Use AI to classify contact reason, product area, sentiment/urgency cues, language, likely required expertise, and candidate next queue when those labels are validated.
- Preserve deterministic routing for contractual SLA, paid-tier entitlement, geography, language coverage, security/privacy cases, regulated workflows, and other rule-driven conditions where correctness matters.
- Validate automated triage against a manually labeled sample and monitor drift as products/contact reasons change.
- Do not infer severity solely from emotion or message length.
- Require human or deterministic checks for emergency/security/abuse/legal/medical/financial/high-value-account escalation where applicable.

## Troubleshooting and Technical Support

- Use AI to guide evidence collection, suggest known troubleshooting steps, summarize logs/error messages, and link verified docs/runbooks.
- Keep product version, OS/device/environment, account/feature flag, error code, steps already tried, and current incident status explicit.
- Do not ask customers to run destructive commands, expose secrets, disable security, or change production/account state without appropriate verified procedure and warnings.
- Route software-engineering/debugging work to the appropriate engineering team when support evidence shows a product defect rather than endlessly improvising customer steps.
- Preserve reproduction evidence and exact observed outcome for escalated bugs.

## Knowledge Maintenance

- Use unresolved/escalated conversations and repeated human corrections as signals for missing/stale knowledge, not as permission for the model to edit the knowledge base automatically.
- Propose article/runbook changes with links to representative cases and product/source evidence.
- Require knowledge-owner review before publishing support-policy/procedure changes.
- Track article effective dates/versions where product behavior changes rapidly.
- Separate internal troubleshooting notes from customer-facing published guidance.

## Customer Success Work

- Use AI to prepare account summaries, meeting briefs, adoption/usage questions, follow-up drafts, renewal-risk hypotheses, and success-plan updates from approved CRM/product/customer context.
- Treat health/risk/propensity scores as governed analytical outputs, not model intuition.
- Do not invent customer goals, blockers, executive sentiment, renewal probability, or commitments from sparse notes.
- Preserve success-plan/customer commitments in CRM/account systems.
- Require review before external messages or commercial/renewal/contract commitments.

## Actions and Procedures

- Separate informational response from actions such as updating account fields, issuing credits/refunds, changing subscriptions, cancelling service, modifying orders, scheduling, creating tickets, resetting access, or triggering workflows.
- Current support AI products can execute configured procedures/actions and hand off to workflows; treat action capability as a higher-risk tier than answering.
- Define allowed actions, required fields, customer authorization, limits, preconditions, confirmation, idempotency, downstream verification, and rollback/reconciliation.
- Use deterministic policy for financial/account/security-sensitive eligibility where possible; do not let the model invent exceptions.
- Require human approval for high-impact or exceptional actions unless a separately governed deterministic procedure explicitly authorizes automation.

## Customer Authentication and Security

- Do not disclose account-specific/private information until the support system has established the required customer identity/authorization level.
- Keep authentication secrets, passwords, MFA/recovery codes, private keys, and full payment credentials out of model context.
- Treat requests to disable security, change account ownership/access, reveal sensitive records, or bypass normal verification as high-risk.
- Customer messages/attachments/linked pages can contain prompt-injection instructions; they must not override support-system policy or agent permissions.
- Ensure an agent cannot use customer-supplied text to expand its tool scopes or access another account.

## Sensitive and High-Stakes Topics

- Define topics that must escalate or receive stronger review, such as security incidents/account takeover, privacy/data requests, legal threats, medical/health guidance, financial decisions, self-harm/safety, minors, fraud/abuse, regulatory complaints, or major contractual disputes as applicable.
- Use the AI to route, summarize, and collect bounded context—not to make qualified legal/medical/security/compliance decisions outside the approved support role.
- Preserve official emergency/security/privacy/legal response procedures.
- Escalate to `sensitive-data-professional`, regulated, or high-security organization scenarios when such data/workflows are a routine core workload rather than occasional escalation.

## Multilingual Support

- Evaluate supported languages on actual support intents, terminology, brand tone, troubleshooting accuracy, and escalation—not general translation benchmarks alone.
- Preserve product names, error messages, legal/policy terms, URLs, and structured values during translation.
- Use qualified/native review for languages/markets where incorrect guidance has material consequence or the model has not passed the team's acceptance suite.
- Keep customer language preference and available human-language coverage in routing logic where useful.
- Do not promise identical support coverage merely because the AI can converse in a language.

## Channel Differences

- Evaluate chat, email, phone/voice, social/community, and messaging channels separately where used.
- Voice adds speech recognition, speech generation, latency, interruption, identity, background-noise, and call-transfer constraints beyond text support.
- Email allows longer context but can include attachments, quoted histories, phishing/prompt-injection content, and external recipients.
- Social/community channels have publication/privacy boundaries different from private tickets.
- Preserve channel-appropriate human handoff and audit/history.

## QA and Evaluation Suite

- Maintain a versioned test set of representative intents from real, permitted support cases or sanitized/synthetic equivalents.
- Include top-volume intents, long-tail difficult cases, ambiguous questions, missing knowledge, conflicting articles, unsupported requests, multilingual cases, customer frustration, and cases that must hand off.
- Score answer correctness/source support, policy adherence, resolution, escalation appropriateness, hallucination/unsupported claims, customer effort, response latency, human correction time, and action safety.
- For autonomous resolution, sample production conversations and monitor reopen/recontact, negative feedback, escalation, and hidden failure patterns.
- Do not use vendor-reported resolution rate as proof of fit for the team's products/customers; measure the team's own accepted outcomes.

## Outcome and Resolution Metrics

- Define what `resolved`, `contained`, `deflected`, `handoff`, `reopen`, `repeat contact`, `CSAT/CX`, and `time to resolution` mean for the team before comparing tools.
- Current providers can price or report AI work by `resolution`/outcome; do not assume their billing metric equals the team's customer-success definition.
- Track false-positive resolutions where the system closes/marks success but the customer remains unresolved.
- Separate AI-handled volume from quality/customer outcome and downstream human rework.
- Use deterministic reporting/analytics for metric calculations.

## Local and Hybrid Route

- Use local/private inference when customer/account data cannot use hosted processing or repeated private assistance justifies local operations and the exact model/runtime passes support-quality tests.
- Keep authoritative support knowledge/tickets in their source systems regardless of model location.
- A hybrid route can keep sensitive account context local while using hosted models for public product documentation or sanitized language tasks under an explicit routing rule.
- Local RAG does not guarantee accurate support answers, freshness, customer authorization, or prompt-injection safety.
- Shared local support inference must include authentication, isolation, concurrency, monitoring, updates, logging, and failure/handoff behavior.
- Escalate infrastructure to internal-platform/hardware owners when operation becomes a shared service concern.

## Direct API and Custom Support Agents

- Use direct APIs/custom agents when the team needs a helpdesk integration, structured triage, custom retrieval/action policy, batch summarization, or channel behavior not provided by the managed support product.
- Define tool schema, retrieval sources, customer identity boundary, conversation state, retry/stopping behavior, action policy, handoff, observability, cost limits, and failure modes.
- Keep customer-facing autonomous deployment behind a staged evaluation/pilot rather than moving directly from prompt testing to full traffic.
- Protect API credentials and limit downstream system permissions.
- Do not allow a custom agent to silently switch providers/data boundaries on failure.

## Team Data Boundary

- Classify tickets, customer identifiers, account usage, contracts, billing, order/payment details, support attachments, logs, health/security information, employee notes, and CRM data before model use.
- Use approved provider/accounts and preserve source-system permissions.
- Minimize data and connector scope to the support objective.
- Verify provider/intermediary/helpdesk/tool chain for sensitive customer data.
- Keep secrets/authentication/payment credentials out of model prompts and knowledge sources.

## Cost per Accepted Customer Outcome

- Compare **total cost per accepted support/success outcome**: AI seats/outcome/API charges, helpdesk integration, knowledge maintenance, failed resolutions, repeat contacts, human handoff/rework, QA/review, local infrastructure, and customer/contract risk.
- A support-native AI agent can be economical when it resolves eligible intents accurately and hands off the rest with useful context.
- A low-cost general model can be expensive if unsupported answers create repeat contacts or damage customer trust.
- Measure cost alongside quality and resolution; do not optimize solely for containment/deflection.
- Include the value/cost of escalation latency and customer effort.

## Escalation Triggers

- Move from general team use to this scenario when shared customer conversations/knowledge/triage/handoff become first-order concerns.
- Move to `organizations/customer-service-and-contact-center/` when high concurrency, omnichannel/voice infrastructure, workforce/contact-center operations, enterprise CRM integration, centralized QA/routing, or organization-scale autonomous resolution dominates.
- Move to `data-analysis-team/` when support analytics becomes the primary workload.
- Move to `research-and-insights-team/` when customer-feedback research rather than live service dominates.
- Move to sensitive/regulated/high-security routes when customer data/workflow obligations require stronger controls.
- Narrow or stop autonomous resolution/actions when quality, escalation, authorization, or auditability cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only when a fixed local/shared inference target materially constrains support model selection.
- Use `../../../hardware/sub/servers/` for a dedicated shared support inference host and `../../../hardware/sub/computers/` for a bounded workstation route.
- Hardware purchasing remains outside this scenario; managed support/API/hybrid routes remain valid alternatives.

## Canonical Links

- Link organization-scale contact-center concerns to `decision-support/scenarios/organizations/customer-service-and-contact-center`.
- Link customer-feedback research to `decision-support/scenarios/teams/research-and-insights-team` and analytics to `decision-support/scenarios/teams/data-analysis-team`.
- Link managed support services and exact local models to their canonical catalog owners only when named/materialized.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Intercom/Fin AI Agent documentation for support channels, knowledge/audience behavior, workflows, handoff/escalation, conversation states, outcome measurement, and external-helpdesk integration, plus current Salesforce Agentforce Contact Center evidence for the organization-scale boundary.
- Current evidence establishes support-native AI routes with configurable autonomous responses, workflow/actions, human escalation, customer/channel targeting, and outcome tracking. These product capabilities do not establish correct answers, customer authorization, or acceptable resolution quality for the target business.
- Support-agent behavior, default escalation, channels, actions/procedures, helpdesk integrations, knowledge sources, pricing/outcome definitions, model/provider chain, and plan limits are mutable; recheck them before rendering current guidance.
- Team-specific knowledge, authorization, QA, and measured customer outcomes remain the acceptance authority.

## Validation

- Helpdesk/CRM/knowledge systems remain authoritative for customer identity, entitlement, case state, policies, and commitments.
- Knowledge grounding preserves source permission/freshness and is not treated as a correctness guarantee.
- Response assistance, autonomous resolution, triage, handoff, and side-effecting procedures remain distinct risk tiers.
- Customers can reach humans under explicit escalation/handoff rules and are not trapped in repeated AI failure.
- Account-specific disclosures/actions require the appropriate authentication/authorization boundary.
- Support QA uses representative team cases and measured accepted customer outcomes rather than vendor resolution claims alone.
- Outcome billing/metrics are not confused with the team's own resolution/quality definitions.
- Organization-scale contact-center architecture is delegated upward.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
