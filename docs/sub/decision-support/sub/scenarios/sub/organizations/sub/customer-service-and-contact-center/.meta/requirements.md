# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale customer service/contact-center operations with high interaction volume, multiple digital/voice channels, CRM/account context, automated resolution, human-agent assistance, routing, quality management, and operational service levels.
- Keep the scenario organization-scale. A bounded support/customer-success team belongs in `teams/customer-success-and-support-team/`.
- The defining constraints are **high concurrency, omnichannel/voice latency, customer identity/authorization, grounded service knowledge, routing/handoff, side-effecting procedures, QA, service reliability, workforce integration, and cost per accepted resolution**.
- Do not turn the page into CCaaS/helpdesk vendor procurement. It owns the model/agent route and acceptance/evidence needed for enterprise customer service.

## Preserve Customer and Service Systems of Record

- Keep CRM/account/order/subscription/billing/entitlement/case/incident/knowledge systems authoritative for customer identity, state, permissions, commitments, policies, and transactions.
- Use models to retrieve, summarize, reason, converse, classify, propose, and execute only bounded authorized actions.
- Do not let conversation memory become the source of truth for customer balance, plan, order state, refund, case status, SLA, or prior commitment.
- Preserve interaction/case/account/action IDs and source references for audit and handoff.
- When system sources conflict, surface the discrepancy and use deterministic owner/system policy rather than model plausibility.

## Integrated Contact-Center Route

- Prefer an organization-approved contact-center/CRM-integrated AI route when it can combine channels, customer context, service knowledge, identity, routing, human handoff, actions, observability, and enterprise controls without requiring the organization to assemble every component itself.
- Current Salesforce Agentforce Contact Center is a current example of an integrated organization route joining voice/digital channels, CRM context, AI agents, human handoff, and operational visibility. Treat exact products/features/channels/pricing/availability as mutable.
- Current Intercom/Fin also demonstrates support-native AI across chat/email/voice with configured resolution/handoff and external-helpdesk integration; use it as evidence of current route capabilities, not universal contact-center architecture.
- Evaluate integrated platforms on the organization's actual contact reasons, channels, data permissions, languages, actions, concurrency, and SLA rather than vendor reported resolution alone.

## Separate AI Roles

- Distinguish at least:
  - customer-facing autonomous self-service;
  - human-agent copilot/assist;
  - triage/classification/routing;
  - knowledge retrieval/answer grounding;
  - conversation/case summarization;
  - post-contact QA/coaching/analytics;
  - workflow/procedure actions;
  - outbound/proactive service where explicitly authorized.
- A model/configuration acceptable for summarization is not automatically safe for autonomous account actions.
- Use the least autonomous route that meets the business objective and only expand after measured acceptance.

## Knowledge Grounding and Current Service State

- Ground policy, product behavior, troubleshooting, eligibility, terms, and procedures in approved current support knowledge.
- Preserve source permissions, article audience, version/effective date, and citations/source identity for material answers.
- Use deterministic systems/APIs for live transactional/account state rather than stale document RAG where possible.
- Do not let model memory fill missing product/account facts.
- Monitor stale/conflicting knowledge and route corrections to knowledge owners rather than automatic model edits.

## Customer Identity and Authorization

- Define what level of identity verification is required before accessing/disclosing account-specific information or executing each action class.
- Separate channel/session recognition from authenticated authorization.
- Do not disclose private account data or perform sensitive actions because the customer states a name/email/order number that has not met the required verification policy.
- Keep passwords, MFA/recovery codes, private keys, and full payment credentials outside model context.
- Apply deterministic authorization limits for account ownership, payments/refunds, security changes, regulated records, and other sensitive actions.

## Autonomous Resolution Boundary

- Define eligible intents for autonomous resolution from knowledge quality, action complexity, customer authorization, error severity, reversibility, and measured accuracy.
- Maintain explicit non-eligible intents that always hand off or require human confirmation.
- Do not mark a conversation resolved merely because the model produced a final response; define resolution semantics and monitor reopen/recontact/customer confirmation according to channel/workflow.
- Sample high-confidence autonomous resolutions and review after model/knowledge/workflow changes.
- Narrow or disable autonomy when hidden failure/recontact/negative outcome rates exceed acceptance.

## Human Agent Assist

- Use models to prepare case/account summaries, retrieve sources, suggest replies/actions, explain policy, translate, and surface next questions while preserving human agent control.
- Show source/context used for material suggestions where feasible.
- Do not hide uncertainty or unsupported suggestions behind polished response text.
- Keep final customer-facing commitments and high-impact actions reviewable by the human agent unless explicitly automated under approved policy.
- Measure whether assist reduces handling/review time without increasing error or customer effort.

## Handoff and Escalation

- Define triggers for customer-requested human help, repeated no-progress, negative experience, unsupported intent, low/ambiguous confidence, high-value customer policy, sensitive topic, authorization failure, incident/severity, fraud/security, and other organization rules.
- Current support products expose configurable escalation/handoff and conversation states; treat exact defaults as product-specific.
- Pass relevant conversation history, retrieved sources, customer/account context, actions already attempted, and reason for handoff to the receiving agent.
- Do not make customers repeat sensitive information unnecessarily after handoff.
- Track handoff reasons and post-handoff outcomes to improve routing/knowledge/model policy.

## Routing and Queueing

- Use AI classification only after validating contact reason, product, language, sentiment/urgency cues, and expertise routing on representative labeled data.
- Preserve deterministic routing for contractual SLA, geography, language availability, customer tier, regulated/sensitive case types, security/fraud, and other rule-driven requirements.
- Do not infer severity solely from emotional language.
- Define fallback routing when model/CRM/knowledge systems are unavailable.
- Include queue capacity and workforce availability in routing design rather than treating model classification as the whole problem.

## Voice and Real-Time Interaction

- Evaluate voice as a distinct end-to-end pipeline: telephony/channel transport, ASR, turn detection/interruption, model reasoning, tool calls/retrieval, TTS, latency, transfer, recording/transcript, and accessibility.
- Measure time to first response and turn latency under real concurrent load.
- Test accents/languages, noisy environments, poor connections, names/numbers/account IDs, interruption/barge-in, silence, cross-talk, and transfer.
- Require confirmation/readback for critical numbers, dates, addresses, financial values, account identifiers, or commitments where ASR/TTS errors matter.
- Do not treat voice recognition as identity authorization.

## Multichannel State

- Preserve customer/case continuity when interactions move between chat, email, phone, social/messaging, or human agents.
- Define which channel is authoritative for consent, identity, attachments, and sensitive disclosures.
- Avoid duplicating cases/actions when the same customer contacts through several channels.
- Keep per-channel history and source data available for audit while minimizing unnecessary model context.
- Test handoff/channel-switch state continuity explicitly.

## Procedures and Side-Effecting Actions

- Separate answering from procedures that modify CRM/account/order/subscription/payment/fulfillment/appointments/returns/refunds/security or other systems.
- Define each action's authorization, required fields, limits, preconditions, confirmation, idempotency, downstream verification, rollback/reconciliation, and audit.
- Use deterministic business policy for refund/credit/eligibility/financial/security limits where possible.
- Do not let the model invent policy exceptions or chain multiple high-impact actions from a vague request.
- Keep human approval for exceptional, irreversible, high-value, regulated, security-sensitive, or ambiguous actions unless a deterministic approved workflow permits automation.

## Fraud, Abuse, Security, and Prompt Injection

- Treat customer text, attachments, emails, links, websites, tickets, and retrieved content as untrusted instructions.
- Customer-provided instructions must not expand tool scopes, expose secrets, override policy, or access another account.
- Route account takeover/fraud/security incident cases through appropriate verified procedures and specialist teams.
- Prevent a model from revealing internal security logic or restricted customer/account data in response to social-engineering prompts.
- Include prompt-injection and tool-manipulation cases in production evaluation.

## Sensitive and Regulated Service

- Classify health, financial, legal, minors, privacy rights, security, regulated complaints, self-harm/safety, and other high-consequence service topics.
- Use models for triage, source retrieval, summarization, and bounded assistance under the applicable policy; preserve qualified/human review where required.
- Do not let customer-service models substitute for medical/legal/financial/security specialists or official emergency procedures.
- Escalate the organization architecture to regulated/high-security scenarios where such data/workflows are central.

## QA, Coaching, and Compliance Review

- Use models to sample/classify interactions, identify policy adherence, summarize reasons for escalation, or propose coaching only after a human-validated QA rubric exists.
- Do not treat a model-generated QA score as a disciplinary/performance fact without appropriate review and employment-policy controls.
- Keep exact evidence snippets/source interaction IDs for material QA findings.
- Validate bias/consistency across channels, languages, teams, customer segments, and case types.
- Use deterministic rules for mandatory compliance statements where feasible.

## Evaluation Suite

- Maintain versioned contact-center evaluations representing volume mix, high-value intents, long-tail cases, unsupported questions, ambiguous identity, sensitive topics, multilingual/voice cases, knowledge conflict, system outage, action workflows, and mandatory handoff.
- Score grounded-answer correctness, customer authorization, resolution, handoff appropriateness, action correctness, hallucination/unsupported claims, latency, containment/recontact, human correction, customer effort, and cost.
- Test full end-to-end workflows rather than isolated prompt answers.
- Include negative-permission/account-isolation cases and prompt injection.
- Re-run regression after model, knowledge, action, routing, channel, or policy changes.

## Concurrency, Reliability, and SLA

- Measure peak concurrent conversations/calls, channel volume, model/provider quotas, CRM/tool latency, retrieval latency, queue depth, autoscaling/warmup, provider failure, and human-transfer capacity.
- Define degraded modes when model/retrieval/tool services fail: human queue, limited read-only flow, retry, fallback provider/model where approved, or explicit outage message.
- Do not silently degrade to an unapproved provider or answer from stale/incomplete context.
- Track p50/p95/p99 latency, timeout, action failure, transfer failure, and abandoned interactions.
- Align AI SLA with contact-center/business SLA rather than model endpoint availability alone.

## Observability and Audit

- Record model/agent/workflow version, source knowledge, customer/case IDs where permitted, tool/action attempts, authorization/confirmation, result, handoff, error, and final resolution state.
- Apply data-minimizing retention and protect transcripts/logs as customer records.
- Monitor hallucinations, action errors, repeated handoffs, hidden recontacts, policy exceptions, prompt-injection events, latency, and cost spikes.
- Preserve enough trace to reconstruct consequential actions and customer commitments.

## Outcome Metrics and Economics

- Define `resolution`, `containment`, `deflection`, `handoff`, `recontact`, `reopen`, `CSAT/CX`, `average handling time`, `first contact resolution`, and other metrics before comparing routes.
- Do not equate a vendor's billable resolution/outcome with the organization's quality definition.
- Monitor false-positive resolution and downstream human rework.
- Compare **total cost per accepted customer outcome**: model/agent charges, telephony/channel, CRM/helpdesk, knowledge maintenance, human agents, transfers, retries, QA, infrastructure, integration, and error/customer-trust risk.
- Optimize service quality and customer effort jointly with automation rate.

## Local/Private and Hybrid Route

- Use private/self-hosted inference when customer data boundaries, sovereignty, control, or economics justify it and exact model/runtime/concurrency/voice quality passes evaluation.
- Keep CRM/identity/action systems authoritative and preserve normal security controls.
- Hybrid routes can keep sensitive account processing private while using approved hosted models for public knowledge/language tasks under explicit routing rules.
- Local deployment does not remove prompt injection, action authorization, monitoring, failover, voice latency, or QA requirements.
- Escalate shared inference/gateway operations to `internal-ai-platform/` when they become organization infrastructure.

## Escalation Triggers

- Move from team support to this scenario when scale, omnichannel/voice, centralized routing/QA, autonomous resolution, CRM/tool integration, or contact-center reliability become first-order.
- Move to `enterprise-workflow-automation/` when service agents act across many business systems beyond the contact-center domain.
- Move to `internal-ai-platform/` when centralized model routing, contracts, shared inference, budgets, or agent runtime become primary.
- Move to regulated/high-security routes when customer data/actions require stronger controls.
- Narrow/stop autonomy where resolution/action/authorization/handoff evidence cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted inference target is selected and hardware materially constrains model/voice/concurrency fit.
- Use `../../../hardware/sub/servers/` for organization contact-center inference infrastructure.
- Contact-center hardware/telephony procurement remains outside this scenario.

## Canonical Links

- Link bounded team support to `decision-support/scenarios/teams/customer-success-and-support-team`.
- Link centralized automation/platform concerns to their organization scenario owners.
- Link named contact-center/support services and exact models to canonical catalog owners when materialized.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Salesforce Agentforce Contact Center material and current Intercom/Fin support-agent documentation for channels, resolution, workflows/actions, escalation/handoff, and operational conversation states.
- Current evidence establishes integrated CRM/contact-center AI, digital/voice channels, autonomous resolution, human handoff, configurable workflows/actions, and operational visibility. These capabilities do not establish correct authorization, acceptable resolution, or reliability for the target organization.
- Contact-center channels, models, agent actions, telephony/voice behavior, pricing/outcome definitions, integrations, SLAs, routing, and data terms are mutable; recheck them before rendering current guidance.
- Organization-specific service knowledge, deterministic authorization/policy, QA, and measured customer outcomes remain the acceptance authority.

## Validation

- Organization-scale concurrency/omnichannel/voice/operations distinguish this route from a bounded support team.
- CRM/account/helpdesk/knowledge systems remain authoritative for customer state and policy.
- Customer authentication/authorization is separate from conversational identity.
- Autonomous resolution, human assist, triage, QA, and side-effecting procedures remain distinct risk classes.
- Explicit human handoff exists and degraded AI behavior cannot trap customers.
- Voice is evaluated end-to-end including ASR/TTS/latency/transfer, not only the LLM.
- Side-effecting procedures use deterministic policy, idempotency, confirmation, and audit.
- Outcome metrics include false resolution/recontact/human rework rather than automation rate alone.
- Internal-platform/regulated/high-security concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
