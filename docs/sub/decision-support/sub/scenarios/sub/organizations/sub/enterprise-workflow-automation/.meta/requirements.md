# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale agents/automations that act across business systems from events, schedules, requests, records, documents, messages, or other triggers and may create/update records, communicate, route work, request approvals, or invoke downstream processes.
- Keep the scenario organization-scale. A bounded project/operations team workflow belongs in `teams/project-and-operations-team/`; domain-specific finance, sales, supply-chain, or support automation remains in its domain route while consuming this common organization-level agent-control pattern.
- The defining constraints are **agent identity, triggers, tool/action scopes, deterministic workflow boundaries, approvals, least privilege, idempotency, audit, recovery, concurrency, cost, and prompt-injection/data-exfiltration risk**.
- Do not turn the page into low-code/RPA vendor procurement guidance. It owns the model/agent route and safety/acceptance architecture.

## Deterministic Workflow Before Free-Form Agency

- Separate deterministic workflow steps from model-dependent judgment.
- Use normal rules/code/flows for stable transformations, routing conditions, exact calculations, approvals, retries, state transitions, and integration orchestration when they can express the requirement reliably.
- Use an LLM/agent only where semantic interpretation, unstructured extraction, prioritization, drafting, flexible planning, or uncertain decision support materially adds value.
- Current Copilot Studio agent flows are explicitly deterministic and can be invoked manually, by agents, events, or schedules; use this as the conceptual baseline for keeping predictable work outside free-form model reasoning.
- Do not let a language model choose a non-deterministic path where a deterministic business rule already owns the decision.

## Agent Identity Is a First-Class Control

- Give every production agent/service a distinct machine/workload identity rather than borrowing a human user's broad credentials by convenience.
- Current Copilot Studio can create Microsoft Entra Agent IDs, exposing connector permissions and authentication activity to centralized identity/governance systems. Treat exact implementation as product-specific but preserve the principle for every platform.
- Bind agent identity to owner, purpose, environment, permitted tools, data classes, lifecycle, and review responsibility.
- Separate build/maker identity from runtime identity and from the end user's delegated identity where applicable.
- Revoke or disable agent identity when the workflow is retired, compromised, ownerless, or no longer approved.

## Triggers and Autonomous Execution

- Define every trigger explicitly: user request, API call, new/changed record, message/email, queue event, schedule, file upload, monitoring signal, or another bounded event.
- For autonomous agents, record trigger source, authentication, required context, deduplication key, expected frequency, allowed window, and failure behavior.
- Current Copilot Studio autonomous agents can run from events without waiting for a user prompt; therefore trigger design becomes an authorization boundary, not just a convenience.
- Do not use a high-frequency trigger when the business process only requires periodic/batched handling.
- Prevent trigger storms and repeated processing with rate limits, idempotency keys, event-version checks, debouncing/batching, and queue/backpressure controls where appropriate.

## Tool and Connector Inventory

- Inventory every external capability separately: read/search, create, update, delete, send/publish, approve/reject, execute code, make HTTP requests, access files, query databases, call another agent, deploy, or change permissions.
- Map each tool to its system owner, authentication model, scopes, rate limits, SLA, data classification, error modes, and reversibility.
- Current Copilot Studio governance can control knowledge, connectors/actions, HTTP requests, triggers, channels, and other capabilities through data policies; preserve equivalent explicit capability inventory even on other platforms.
- Do not grant an entire connector if only one action is needed when the platform can scope permissions at action level.
- Treat custom connectors, MCP servers, browser/computer-use tools, and external agents as third-party code/data boundaries requiring the same review as APIs.

## Least Privilege and Environment Boundaries

- Restrict agents to the minimum systems, records, folders, projects, tenants, environments, and operations required by the workflow.
- Use separate development/test/production environments and credentials.
- Do not give a development/test agent production write access for convenience.
- Apply network, connector, DLP/data-policy, allowlist, secret, and output-destination controls outside the model where the platform supports them.
- Current Microsoft guidance exposes connector dependencies, DLP, environment routing, Conditional Access, RBAC/ABAC, and centralized agent governance; treat these as examples of deterministic baseline controls rather than model instructions.

## Read, Propose, Approve, Execute

- Classify each workflow step as read, analysis/proposal, approval, or execution.
- Start new high-impact workflows in read/proposal mode and add write actions only after accuracy and authorization are proven.
- Use human approvals at the point where consequence or ambiguity exceeds the permitted autonomous tier.
- Current Copilot Studio multistage approvals combine deterministic conditions, AI review, and human approval stages; treat preview/feature state as mutable but preserve the architectural principle.
- An AI approval result must not bypass mandatory legal, financial, security, HR, medical, regulatory, or organization-defined human approvals.

## Human Approval Contract

- Define who may approve, what evidence they see, whether one or multiple approvers are required, timeout/escalation, delegation, and what happens after rejection.
- Present source records, proposed changes, confidence/uncertainty, affected systems, and material downstream consequences to the approver.
- Do not ask humans to approve opaque model conclusions without sufficient underlying evidence.
- Avoid approval fatigue by keeping low-risk deterministic decisions automated and routing only meaningful exceptions to people.
- Preserve approval identity/time/result/rationale where audit requires it.

## State Machine and Idempotency

- Model durable workflow state explicitly rather than relying on conversation history.
- Define states such as received, validated, enriched, awaiting approval, approved/rejected, executing, completed, partially completed, failed, retrying, cancelled, and reconciled as appropriate.
- Generate idempotency/correlation keys so retries do not duplicate records, messages, payments, orders, tickets, or external actions.
- Before executing a repeated request, check whether the intended side effect already occurred.
- Make partial completion visible; do not mark a multi-system workflow successful if one downstream step failed.

## Retry and Failure Handling

- Classify failures into transient infrastructure/provider, rate-limit, authentication/authorization, invalid input, business-rule rejection, model/format error, tool failure, and irreversible downstream error.
- Retry only transient/retriable failures with bounded backoff and attempt limits.
- Do not repeatedly ask a model to invent new values until a deterministic validation passes.
- Use dead-letter/manual-review queues for persistent failures.
- Define compensation/reconciliation for side effects that cannot be atomically rolled back across systems.

## Structured Outputs and Validation

- Use explicit schemas for model outputs consumed by automation.
- Validate types, required fields, enums, identifiers, dates, amounts, URLs, destination systems, and business constraints before executing tools.
- Reject malformed/ambiguous/unsupported output rather than coercing it into a plausible action.
- Keep deterministic calculations and policy checks outside model prose.
- Version output schemas/prompts/tool contracts where changes can alter workflow behavior.

## Prompt Injection and Untrusted Inputs

- Treat emails, tickets, documents, web pages, chat messages, uploaded files, external APIs, retrieved knowledge, and tool output as untrusted content.
- Untrusted content must not expand agent tool scopes, request secrets, alter system instructions, disable approvals, or redirect output to unauthorized destinations.
- Keep system policy/tool permissions outside retrieved content.
- Test direct and indirect prompt injection, malicious URLs/files, hidden instructions, and tool-output manipulation.
- Do not expose secrets or privileged context to the model solely because an untrusted input requests them.

## Secrets and Credentials

- Use approved secret stores/managed identities/connection references rather than embedding credentials in prompts, code, workflow definitions, environment variables exposed to models, or documents.
- Scope credentials to the minimum action/system/environment.
- Rotate/revoke credentials and maintain ownership/lifecycle.
- Do not allow model-generated text to choose arbitrary secret names/credential sources.
- Keep secret values out of logs, traces, chat transcripts, approval payloads, and error messages.

## Multi-Agent Workflows

- Use multiple agents only when decomposition produces clear ownership or isolation benefits.
- Define each agent's input/output contract, tools, authority, data boundary, stopping behavior, and failure propagation.
- A coordinator/orchestrator must not silently grant a worker broader permissions than the worker's explicit identity/tool policy.
- Avoid circular delegation and unbounded agent-to-agent loops.
- Preserve traceability across handoffs so a final action can be traced through the agents/decisions that produced it.

## Cross-System Transactions

- Treat multi-system changes as distributed transactions with explicit order, preconditions, downstream verification, and reconciliation.
- Determine which system is authoritative for each state transition.
- Avoid compensating a failure by guessing a reverse action; define tested compensation workflows.
- Verify external IDs and final state after writes.
- For money, access, contracts, identity, customer commitments, production, or safety-relevant operations, require stronger approvals and reconciliation.

## Eventual Consistency and Stale State

- Define expected propagation delays between systems.
- Re-read authoritative state before a consequential action when stale cached/retrieved context could change the decision.
- Do not let an agent act on an old message/document if the source record has since changed.
- Use timestamps/version/ETag or equivalent optimistic concurrency controls when APIs provide them.
- Handle conflicts explicitly rather than overwriting newer state.

## Observability and Audit

- Record agent/workflow/model version, trigger, identity, source records, tools called, inputs/outputs as allowed by data policy, policy/approval decisions, side effects, errors/retries, and final state.
- Current Copilot Studio/Agent 365/Microsoft Purview guidance provides centralized identity/audit/observability examples; preserve equivalent production traceability on any stack.
- Protect logs as potentially sensitive business data and apply retention/minimization.
- Use correlation IDs to join agent, workflow, connector, application, and downstream-system logs.
- Alert on unexpected tools/data access, unusual action volume, repeated failures, approval bypass attempts, cost spikes, and policy violations.

## Data Movement and Governance

- Map where prompts, outputs, connector payloads, documents, tool results, traces, caches, and audit events are processed/stored.
- Do not infer one platform's privacy/residency boundary covers third-party connectors, custom tools, downstream APIs, or separate governance/audit planes.
- Current Copilot Studio documentation explicitly notes that some audit/governance telemetry can flow through separate Microsoft services/control planes; verify each data path for sensitive workflows.
- Use DLP/data policies and connector governance to prevent prohibited cross-boundary movement.
- Escalate regulated/high-security workflows when normal enterprise controls are insufficient.

## Testing Strategy

- Test deterministic workflow logic independently from model quality.
- Maintain representative model evaluation cases for classification, extraction, reasoning, routing, approval recommendation, and tool-argument generation as applicable.
- Include adversarial cases: missing data, conflicting records, duplicate event, stale state, unauthorized request, prompt injection, tool outage, malformed model output, high-cost action, rejected approval, and partial downstream failure.
- Run end-to-end tests in non-production environments using safe test data and sandboxed endpoints.
- Re-run regression after model, prompt, tool, connector, schema, policy, workflow, or permission changes.

## Autonomy Tiers

- Define explicit autonomy levels rather than one `autonomous` flag.
- Example progression: summarize only → propose action → prefill action → execute reversible low-risk action → execute bounded action with post-check → fully autonomous only within deterministic low-risk constraints.
- Tie each tier to tool scopes, data classes, value/quantity limits, approval requirements, monitoring, and rollback.
- Promote a workflow to higher autonomy only after measured evidence at the lower tier.
- Demote/disable autonomy after incidents, model/tool changes, or drift until revalidated.

## Throughput, Rate Limits, and Scheduling

- Measure event volume, burst size, concurrency, tool/API quotas, model capacity, queue depth, workflow duration, and approval latency.
- Schedule/batch non-urgent work when it reduces cost/rate-limit risk.
- Avoid autonomous loops consuming capacity without new business value.
- Define backpressure and degraded operation when model/tool capacity is unavailable.
- Prioritize business-critical queues deterministically rather than by model-generated urgency alone.

## Cost per Accepted Automated Outcome

- Compare **total cost per accepted automated outcome**: model/API/agent-flow charges, connector/API costs, workflow infrastructure, human approvals/review, retries, observability, integration/admin/security, failures/reconciliation, and incident risk.
- A deterministic flow with small AI stages can be cheaper and safer than a fully agentic loop.
- A stronger model can reduce exception/review cost for semantic decisions, but measure this on the actual workflow.
- Do not optimize on number of agent runs or actions executed.
- Include cost of duplicated/incorrect side effects as a first-class metric.

## Change Management and Lifecycle

- Assign owner, technical maintainer, business owner, data/security approver, and support/escalation path for production agents where appropriate.
- Version and review changes to triggers, instructions, tools, policies, schemas, model configuration, and approvals.
- Use source control/ALM/deployment history when the platform supports it; current Copilot Studio governance includes Git-backed deployment/audit capabilities as one example.
- Define rollback/disable/kill-switch procedures.
- Remove unused identities, connectors, secrets, queues, and scheduled triggers when an agent is retired.

## Local/Private and Hybrid Route

- Use private/self-hosted models when the workflow's data boundary prohibits managed inference or organization control/economics justify it.
- Keep workflow engine, identity, deterministic policy, state machine, approvals, and audit independent of model location.
- Hybrid routes may route specific approved data/task classes to hosted models while protected processing remains private.
- Never silently fail over a restricted workflow to an unapproved provider.
- Escalate model gateway/shared runtime ownership to `internal-ai-platform/` when it becomes centralized infrastructure.

## Escalation Triggers

- Move from a bounded team automation to this scenario when agents act across organization systems with shared identity, policy, approvals, audit, or high action volume.
- Move to domain scenarios when finance, sales, supply chain, customer service, security, or another business domain supplies the primary transactional rules.
- Move to `internal-ai-platform/` when centralized model/provider gateway, agent runtime, common tools, budgets, observability, and platform SLOs become primary.
- Move to regulated/high-security routes when data/action severity requires stronger isolation/compliance.
- Stop/narrow autonomy when identity, authorization, idempotency, audit, rollback/reconciliation, or evaluation cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after a private/self-hosted model/runtime target is selected and exact hardware materially constrains model/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared organization agent inference infrastructure.
- Workflow/orchestration platform procurement remains outside this scenario.

## Canonical Links

- Link domain-specific finance, sales, supply-chain, support, security, and other automation to their scenario owners.
- Link centralized AI runtime/gateway concerns to `catalog/models/selection/user-scenarios/organizations/internal-ai-platform`.
- Link exact agent platforms/services/models to canonical catalog owners when named/materialized.
- Keep generic agent reasoning/tool-selection candidate ranking in applicable model decision guides rather than duplicating it here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Microsoft Copilot Studio agent-flow, autonomous-agent, approvals, Entra Agent ID, connector-governance, security/governance, and agent-design documentation.
- Current evidence establishes deterministic agent flows, event/schedule triggers, autonomous agents, scoped permissions, agent identities, action-level connector governance, human/AI multistage approvals, centralized observability, and data-policy controls. These capabilities do not establish business-process correctness or authorization for a particular organization.
- Agent/flow features, preview/GA state, approvals, identities, connectors/actions, data policies, governance planes, quotas, credits, models, and product pricing are mutable; recheck them before rendering current guidance.
- Deterministic business systems/policies, explicit agent identity/permissions, approvals, and end-to-end workflow evidence remain the acceptance authority.

## Validation

- Deterministic workflow/state/policy remains separate from model judgment.
- Every autonomous workflow has an explicit authenticated trigger and workload identity.
- Tools/actions are inventoried and least-privilege rather than one broad connector permission.
- Read/propose/approve/execute are distinct states with consequence-based human gates.
- Durable state/idempotency/retry/reconciliation prevent duplicated or hidden partial side effects.
- Untrusted content cannot expand agent authority or expose secrets.
- Multi-agent delegation preserves explicit identity/tool/data boundaries.
- Audit/observability can trace triggers, decisions, approvals, actions, failures, and final state.
- Cost is measured per accepted automated outcome including correction/reconciliation/incident burden.
- Internal-platform/regulated/high-security concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
