# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale security operations covering telemetry/log/event analysis, alert triage, incident investigation, threat hunting/intelligence, detection engineering, response guidance, and bounded remediation across identity, endpoint, cloud, network, email, and data-security systems.
- Keep the scenario organization-scale. General enterprise workflow automation belongs in its own route; high-security/isolated environments belong in `high-security-environment/` when sovereignty/isolation becomes the primary constraint.
- The defining constraints are **evidence integrity, alert volume, analyst triage, investigation reproducibility, attacker-controlled inputs, tool permissions, containment/remediation authority, audit, incident severity, latency, and false-positive/false-negative cost**.
- Do not turn this page into SIEM/SOAR/EDR procurement guidance. It owns the AI model/agent route and security acceptance boundary.

## Security Telemetry and Systems Remain Authoritative

- Keep SIEM, XDR/EDR, identity, cloud-security, network, email, vulnerability, threat-intelligence, asset, case/incident, and ticket systems authoritative for security events/state.
- Use models to summarize, correlate, query, hypothesize, rank, explain, and propose actions from available evidence.
- Do not let model memory become the source of truth for whether an alert occurred, an endpoint is compromised, a user is disabled, a vulnerability exists, or remediation succeeded.
- Preserve alert/incident/entity/evidence/query/action IDs and timestamps for material AI findings.
- When telemetry sources conflict or are incomplete, surface the gap rather than inventing a complete attack narrative.

## Integrated Security-Agent Route

- Prefer an organization-approved security-native AI/agent route when it operates over governed security telemetry, permissions, threat intelligence, case state, and response tools without exporting sensitive telemetry into disconnected consumer services.
- Current Microsoft Security Copilot provides assistive and agentic security workflows across Defender, Sentinel, Entra, Intune, Purview, threat intelligence, and other security surfaces. Current Google Security Operations combines SIEM/SOAR/threat intelligence with Gemini and agentic triage/investigation capabilities. Treat exact products, agents, preview/GA state, connectors, actions, and pricing as mutable.
- Evaluate integrated agents on the organization's actual telemetry, alert mix, attack surface, identities, cloud workloads, analyst processes, and response permissions.
- Start autonomy with bounded repetitive triage/investigation tasks and preserve human control over high-impact containment/remediation until evidence supports a stronger tier.

## Separate Security AI Roles

- Distinguish at least:
  - alert/phishing triage;
  - incident summarization and investigation;
  - threat hunting/query generation;
  - threat-intelligence synthesis;
  - detection-rule engineering;
  - vulnerability/exposure prioritization;
  - identity/endpoint/data-security investigation;
  - response/remediation recommendation;
  - bounded automated response;
  - analyst reporting/documentation.
- A configuration safe for summarization is not automatically safe for autonomous containment.
- Evaluate each role against its own evidence, latency, permission, and failure-severity requirements.

## Alert Triage

- Use AI to correlate alert evidence, enrich entities, classify likely true/false positives, explain rationale, and prioritize analyst attention when validated for supported alert classes.
- Current Microsoft Security Alert/Phishing Triage agents autonomously evaluate supported alerts and expose natural-language rationale/evidence while preserving analyst review; treat supported workloads and preview state as mutable.
- Do not generalize a triage model validated on phishing to identity/cloud/malware/other alerts without separate evidence.
- Preserve original detector verdict, raw indicators, telemetry, enrichment, agent verdict, rationale, confidence/uncertainty, and final analyst disposition where practical.
- Measure false negatives as a first-class cost; reducing alert volume is not sufficient acceptance evidence.

## Incident Investigation

- Use AI to build timelines, correlate users/hosts/IPs/processes/files/cloud events, retrieve threat intelligence, generate queries, identify gaps, and propose hypotheses.
- Preserve each finding's underlying telemetry/query/source so an analyst can reproduce or challenge it.
- Current Security Copilot Security Analyst Agent performs multi-step analysis over Defender/Sentinel telemetry and returns supporting evidence trails; current Google SecOps uses threat-centric case context plus Gemini-assisted investigation. Treat provider workflows as route evidence rather than organization-specific proof.
- Do not let the model connect unrelated incidents/entities merely because names/timestamps look similar.
- Distinguish observed fact, inferred relationship, hypothesis, and recommended next investigation step.

## Threat Hunting and Query Generation

- Use models to translate natural language into KQL/YARA/Sigma/search queries or platform-specific hunting logic only when the generated query remains visible/reviewable.
- Validate tables/fields/time windows/operators/joins and query cost before execution.
- Use deterministic query execution against authoritative telemetry; the query result, not the model's predicted result, owns the evidence.
- Compare generated detections/hunts against known cases, benign baselines, and historical data to estimate noise/misses.
- Do not deploy a detection rule to production solely because its syntax is valid.

## Threat Intelligence

- Use AI to summarize/relate current threat reports, indicators, actor/campaign profiles, vulnerabilities, and internal observations.
- Keep source identity, publication/date, indicator confidence, expiration/last-seen, and internal relevance explicit.
- Distinguish vendor intelligence, public reporting, internal telemetry, analyst assessment, and unverified community claims.
- Do not attribute an incident to a named actor from stylistic similarity or model memory alone.
- Require stronger corroboration for attribution, executive/public claims, or legal/regulatory reporting.

## Detection Engineering

- Use AI to draft/translate/explain detection logic, test cases, exclusions, mappings, and documentation.
- Preserve detector intent, data source, schema, assumptions, expected true-positive behavior, known false-positive conditions, and validation dataset.
- Test new/changed rules in historical/replay/shadow mode where possible before production enforcement.
- Do not let generated exclusions silently suppress broad attack classes to reduce alert noise.
- Version-control or otherwise audit detection changes and retain owner/reviewer.

## Security Actions and Remediation

- Separate read/investigate/recommend from actions such as isolate endpoint, disable user, revoke tokens, quarantine email/file, block indicator, change firewall/WAF policy, delete cloud resource, rotate credentials, patch/remediate, or modify access.
- Define exact action preconditions, target identity/resource, scope, reversibility, approval, timeout, idempotency, verification, and rollback/reconciliation.
- Preserve human approval for high-impact/destructive or uncertain actions unless a deterministic organization policy explicitly authorizes automation.
- Do not allow model-generated severity alone to authorize containment.
- Verify the action completed in the authoritative security/system state rather than assuming success from tool-call acceptance.

## Agent Identity, Permissions, and Triggers

- Give production security agents explicit workload identities and administrator-defined permissions.
- Current Security Copilot agent documentation requires configured identity, access permissions, action rights, and triggers; preserve these as mandatory concepts across platforms.
- Use read-only permissions for investigation-only agents.
- Bind autonomous triggers to specific supported alert/event/schedule conditions and prevent arbitrary user/retrieved content from creating new trigger classes.
- Review agent identity/tool scopes after SOC/platform changes and disable ownerless/unused agents.

## Prompt Injection and Attacker-Controlled Content

- Treat emails, documents, web pages, tickets, logs, usernames/process command lines, file metadata, repository content, threat reports, and other attacker-influenced data as untrusted text.
- Untrusted telemetry/content must not override security-agent instructions, request secrets, change remediation policy, or expand tools.
- Do not follow URLs/commands embedded in suspicious artifacts without sandboxed/approved investigation procedures.
- Include direct/indirect prompt injection in red-team evaluation for any agent that reads attacker-controlled content.
- Keep privileged credentials/context away from the model unless required by the bounded investigation/action.

## Malware, Files, URLs, and Detonation

- Keep static/dynamic malware analysis, sandbox/detonation, reputation, hashes/signatures, and file/URL telemetry as specialized deterministic/security-tool evidence.
- AI may summarize or correlate these outputs; it should not replace sandbox execution or signature/reputation checks.
- Current phishing triage workflows can invoke URL/file analysis and screenshot/context tools; preserve each tool result separately from the agent's final verdict.
- Treat potentially malicious files/links as unsafe and process them in appropriate isolated analysis tools.

## Identity and Account Security

- Preserve authoritative identity provider, sign-in, risk, MFA, token/session, device, privilege, and access records.
- Do not disable users/revoke access solely from free-form model inference when the organization's policy requires deterministic risk or human approval.
- Verify similarly named identities and tenant/domain context before actions.
- Apply stronger controls to privileged/service accounts.
- Record identity actions and downstream restoration/rollback path.

## Vulnerability and Exposure Prioritization

- Use AI to aggregate vulnerability/exposure evidence, asset criticality, exploit intelligence, reachability/context, and remediation status.
- Do not treat CVSS or model priority as a complete risk decision.
- Preserve authoritative asset ownership and vulnerability state.
- Verify patch/config remediation applicability before change.
- Avoid autonomous broad remediation where compatibility/business impact is unknown.

## Incident Severity and Escalation

- Define severity using organization criteria such as affected identities/assets/data, privilege, business impact, persistence, lateral movement, exfiltration, safety/regulatory impact, and confidence.
- Use AI recommendations as decision support, not as an opaque severity authority.
- Escalate missing/conflicting evidence and suspected high-impact incidents early rather than waiting for model certainty.
- Preserve incident commander/analyst ownership and required legal/privacy/communications escalation.

## Evidence Chain and Case Integrity

- Preserve original evidence and timestamps; generated summaries are derived artifacts.
- Keep queries, results, entity relationships, analyst notes, model findings, tool actions, and evidence references traceable.
- Do not overwrite evidence with model-cleaned narratives.
- Apply chain-of-custody/evidence handling requirements where investigation may support legal/regulatory/disciplinary processes.
- Keep raw sensitive telemetry access controlled.

## Autonomous Security Agents

- Use autonomous agents for high-volume, well-bounded tasks whose supported data/tool set and failure semantics are understood.
- Current Microsoft agents include phishing/security-alert triage, threat intelligence briefing, threat hunting, security analysis, and dynamic threat detection; exact availability/support scope remains mutable.
- Define what the agent may close/resolve versus what remains open for analysts.
- Sample and review automated dispositions, including false-positive closures.
- Do not let `autonomous` imply unrestricted remediation authority.

## Human Oversight and Feedback

- Provide analysts sufficient evidence/rationale to validate or override model/agent decisions.
- Capture analyst feedback/corrections where the platform supports it and monitor whether agent behavior improves or drifts.
- Do not use analyst feedback as an excuse to stop independent regression evaluation.
- Preserve senior escalation for novel/high-impact attacks or uncertain remediation.

## Evaluation and Red-Team Suite

- Build a versioned SOC evaluation set from representative/sanitized historical alerts/incidents plus synthetic/adversarial cases.
- Include true/false positives, sparse telemetry, conflicting signals, similar entities, benign admin activity, insider/identity/cloud/email/malware cases, prompt injection, malicious attachment/URL, tool outage, stale threat intel, and a case requiring human escalation.
- Score triage precision/recall, false negatives, investigation evidence correctness, query validity, source attribution, escalation, action safety, time-to-triage/investigate, analyst correction, and cost.
- Evaluate full workflows with the same permission/tools as production where safely possible.
- Re-run after model, agent, detection, telemetry schema, connector, tool, or policy changes.

## Concurrency and SOC Reliability

- Measure alert/event volume, burst behavior, concurrent investigations, model/provider quotas, query/data-lake capacity, tool latencies, queue depth, and analyst workload.
- Define degraded behavior when AI is unavailable; core detection, incident, and response tooling must remain operable.
- Do not silently drop alerts or switch to an unapproved model/provider.
- Track p50/p95/p99 triage/investigation latency where service objectives require it.
- Preserve critical incident paths that bypass nonessential AI dependencies.

## Observability and Audit

- Record agent/model version, trigger, identity, alert/incident/source, queries/tools, evidence used, verdict/recommendation, approvals/actions, errors/retries, analyst override, and final disposition where permitted.
- Current Security Copilot provides agent execution visibility and audit/admin capabilities; treat exact telemetry as product-specific.
- Protect security logs/traces as sensitive data.
- Alert on unusual agent action volume, permission changes, prompt-injection attempts, repeated misclassification, model outages, and cost spikes.

## Data Boundary, Residency, and Security

- Security telemetry can contain credentials/secrets, PII, customer data, sensitive IP, incident details, and highly privileged operational context.
- Use approved enterprise security AI products/accounts and verify processing/storage/retention/residency/subprocessor boundaries for the exact integration.
- Minimize data sent to external models and disable unnecessary connectors/tools.
- Keep authentication secrets/private keys/recovery codes out of prompts/logs.
- Move to `high-security-environment/` when disconnected/sovereign/air-gapped or threat-sensitive isolation dominates.

## Local/Private and Hybrid Route

- Use private/self-hosted inference when security telemetry cannot use managed AI or organization control/latency/economics justify it.
- Keep SIEM/XDR/query/detection/action systems authoritative.
- Hybrid routes can keep internal telemetry private while using hosted services for approved public threat intelligence or sanitized analysis under explicit rules.
- Local inference does not remove prompt injection, permissions, evidence integrity, action safety, monitoring, or model-update risk.
- Escalate shared model gateway/inference to `internal-ai-platform/` when it becomes organization infrastructure.

## Cost per Accepted Security Outcome

- Compare **total cost per accepted SOC outcome**: security AI/API, SIEM/data-lake/query compute, agent/tool integrations, analyst time, false-positive review, false-negative/incident cost, response errors, infrastructure, and governance/audit.
- A high-value agent can be economical if it safely reduces triage/investigation time without increasing missed attacks.
- Do not optimize for alerts auto-closed or investigations generated alone.
- Measure analyst-reviewed true/false outcomes, time-to-detection/triage/investigation/containment, and correction burden.
- Treat vendor productivity claims as external evidence, not organization-specific ROI proof.

## Escalation Triggers

- Move to this scenario when AI operates across organization SOC telemetry, triage, investigation, hunting, detections, and response.
- Move to `enterprise-workflow-automation/` for generic cross-business workflow patterns outside security.
- Move to `internal-ai-platform/` when shared model gateway/runtime/budgets/observability become primary.
- Move to `high-security-environment/` when isolation/sovereignty/air-gap/threat sensitivity dominates.
- Move to `regulated-organization/` when regulatory governance across the organization rather than SOC operational security is primary.
- Narrow/stop autonomy when false-negative, evidence, permission, action, or audit requirements cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` only after an exact private/self-hosted security inference target is selected and hardware materially constrains model/concurrency fit.
- Use `../../../hardware/sub/servers/` for shared SOC inference infrastructure.
- SIEM/security-appliance/hardware procurement remains outside this scenario.

## Canonical Links

- Link enterprise workflow/platform/high-security concerns to their organization scenario owners.
- Link named security AI/SIEM/SOAR services and exact models to canonical catalog owners when materialized.
- Do not duplicate security-product profiles or generic agent decision guidance here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party Microsoft Security Copilot agent/Defender/workflow documentation and current Google Security Operations/Agentic SOC documentation.
- Current evidence establishes autonomous alert/phishing triage, multi-step security analysis, threat hunting/intelligence agents, SIEM/SOAR-integrated generative investigation, administrator-configured identities/permissions/triggers/actions, evidence/rationale visibility, and human oversight. These capabilities do not establish safe autonomous remediation or organization-specific detection quality.
- Security agents, supported alert classes, preview/GA state, plugins/tools, threat intelligence, model behavior, licensing, quotas, and product integrations are mutable; recheck them before rendering current guidance.
- Authoritative telemetry/security systems, analyst-reviewed evidence, deterministic permissions/policy, and organization-specific SOC evaluations remain the acceptance authority.

## Validation

- Security telemetry and executed queries/tools remain evidence owners rather than model memory.
- Triage, investigation, hunting, detection engineering, and remediation remain distinct risk/evaluation classes.
- False-negative cost is explicit; automation rate/alert reduction is not sufficient success evidence.
- Security agents have explicit identity, trigger, read/write permissions, and human oversight.
- Attacker-controlled content cannot expand agent authority through prompt injection.
- High-impact containment/remediation uses deterministic policy/approval and verifies resulting state.
- Evidence chain and incident state remain traceable for audit/escalation.
- Core SOC operation continues during AI degradation/outage.
- Internal-platform/high-security/regulated concerns are escalated rather than duplicated.
- Hardware procurement remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
