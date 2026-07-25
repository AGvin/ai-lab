# Human Approval Gate Architecture

A human approval gate pauses an agent workflow before a declared consequential transition and requires an authorized person to approve, reject, modify, defer, or escalate the pending action.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established human-in-the-loop workflow pattern.

## Core idea

The workflow prepares a specific proposed action and durable evidence, then suspends before the side effect:

```text
agent plan -> validation -> pending action -> human gate
                                          -> approve -> execute -> verify
                                          -> modify  -> revalidate
                                          -> reject  -> stop or revise
                                          -> expire  -> fail closed
```

Approval is authorization for the exact reviewed action under the exact reviewed state. It is not a blanket endorsement of the model, workflow, or future actions.

## Use a gate for declared risk

Examples include:

- sending email or messages externally;
- publishing content or synthetic media;
- purchases, transfers, subscriptions, or billable resource allocation;
- deleting, overwriting, deploying, merging, or modifying production data;
- creating accounts, changing permissions, or exposing credentials;
- medical, legal, financial, employment, safety, or public-facing decisions;
- voice, face, identity, biometric, or consent-sensitive operations;
- actions whose effects are difficult to reverse or independently verify.

Do not add approval to every harmless step. Excessive low-value prompts create fatigue and encourage automatic approval.

## Pending-action record

Persist a deterministic record before pausing:

```text
Approval ID:
Workflow, task, and state version:
Requested action and exact arguments:
Target system, account, environment, and resource IDs:
User-visible summary:
Expected effect and reversible or irreversible status:
Evidence and validation results:
Data, privacy, rights, and consent classification:
Estimated cost, duration, and resource lifetime:
Known risks, uncertainty, and alternatives:
Requester and executing identity:
Required approver role and separation-of-duty rule:
Created at, expires at, and maximum delay:
Allowed decisions and modification schema:
Post-approval verification and rollback plan:
```

The record must be understandable without exposing private hidden chain-of-thought. Show material facts, evidence, assumptions, and consequences.

## Exact-scope approval

Bind approval cryptographically or deterministically to:

- action type;
- normalized arguments;
- target identifiers;
- artifact checksums or revisions;
- authoritative state version;
- cost and quantity limits;
- execution deadline;
- approver identity and authority.

If any material field changes after review, invalidate the approval and request a new one. Do not reuse approval after an agent edits the message, file, amount, recipient, deployment, permissions, or resource specification.

## Decisions

Support explicit outcomes:

- **Approve:** authorize the exact pending action.
- **Reject:** prohibit execution and record the reason where appropriate.
- **Modify:** supply changes through a constrained schema, then re-run validation and usually re-approve the resulting action.
- **Defer:** retain the pending request until a deadline without executing.
- **Escalate:** transfer approval to a more qualified or privileged authority.
- **Expire:** automatically invalidate the request when time or state constraints are no longer valid.
- **Cancel:** requester or workflow withdraws the request before execution.

Free-form human text should not be interpreted as permission for unrelated actions. Parse decisions through an explicit interface or schema.

## Pause and resume

Before pausing:

- persist the workflow and pending action;
- release resources that need not remain allocated;
- retain or deliberately expire leases required for safe continuation;
- prevent other workers from executing the same action;
- define notification and escalation;
- set expiry and fail-closed behavior.

On resume:

1. authenticate the approver and check authority;
2. load the exact workflow and approval record;
3. verify state, inputs, artifacts, permissions, cost, and deadlines have not materially changed;
4. fence stale controllers and duplicate executions;
5. re-run required deterministic checks;
6. execute idempotently using a stable operation ID;
7. verify the external result;
8. record actual effect, cost, and residual risk.

A workflow engine acknowledging an approval does not prove that the external action executed successfully.

## Separation of duties

For high-risk operations, require that the approver is not the same identity that:

- generated the proposal;
- controls the evaluated model;
- owns the target resource;
- benefits from bypassing the gate;
- performs final verification.

Possible controls include two-person approval, role-based authority, value thresholds, environment-specific approvers, or specialist review before executive approval.

Do not treat a second model as a human approver. Model review can prepare evidence but cannot satisfy a policy that explicitly requires accountable human authorization.

## Least privilege

Approval should grant only the minimum authority required for the pending action:

- one operation rather than an open session;
- one target and environment;
- bounded amount, quantity, duration, or scope;
- short expiry;
- no reusable credentials in the model context;
- no permission to create further approvals.

The execution service should enforce the authorization independently from the model's prompt.

## Presentation quality

The approval interface should show:

- what will happen;
- where and to whom;
- material content or diff;
- why approval is required;
- cost and irreversibility;
- source evidence and validation;
- alternatives, rollback, and uncertainty;
- exact decision options.

Prevent dark patterns, truncated diffs, hidden recipients, collapsed warnings, ambiguous buttons, or default approval. For long artifacts, show both summary and inspectable source.

## Prevent approval fatigue

Classify actions by risk and aggregate only when the bundle is coherent and bounded.

Measure:

- approval frequency;
- time to decision;
- rejection and modification rate;
- incidents after approval;
- repeated low-value requests;
- approver disagreement;
- expired or abandoned approvals.

Use deterministic policy for harmless actions and reserve human attention for material decisions. Never reduce prompts by silently widening model authority.

## Failure behavior

Define behavior when:

- no approver is available;
- approval expires;
- the workflow changes while paused;
- notification fails;
- the approver lacks authority;
- two approvers conflict;
- execution times out after approval;
- the action succeeds but the response is lost;
- rollback is unavailable;
- the approval store or audit log is unavailable.

Consequential action should normally fail closed. After ambiguous execution, reconcile external state before asking for another approval or retrying.

## Human limitations

Human approval reduces uncontrolled autonomy but does not guarantee correctness. Approvers can:

- misunderstand technical details;
- trust fluent but unsupported model summaries;
- miss defects in large diffs or media;
- approve under time pressure;
- lack domain expertise;
- become habituated to frequent prompts.

Support approval with deterministic checks, qualified review, source evidence, usable interfaces, training, and post-action verification.

## Suitable uses

- tool calls with material external side effects;
- publication and release workflows;
- infrastructure provisioning or teardown;
- deployment and repository merge gates;
- high-value purchases and financial actions;
- identity, voice, biometric, or consent-sensitive media;
- exceptional cases routed from an otherwise automated workflow;
- decisions where accountable authority must remain human.

## Poor fits

Avoid or simplify this pattern when:

- the action is harmless, easily reversible, and already governed by deterministic policy;
- the approver cannot inspect the evidence or understand the consequence;
- the gate occurs after the irreversible action;
- approval is treated as a substitute for validation, security, or least privilege;
- the workflow presents hundreds of indistinguishable low-risk requests;
- policy falsely assumes that any human click transfers all responsibility away from system designers.

## Strengths

- preserves accountable authority for consequential transitions;
- creates a pause point for evidence and risk review;
- limits autonomous side effects;
- supports modification, escalation, and rejection;
- produces an auditable authorization record;
- integrates with graph, evaluator, and resource-lifecycle workflows.

## Limitations

- adds latency and operational dependency on approvers;
- can create approval fatigue and rubber-stamping;
- state may become stale during a pause;
- poor interfaces can hide material changes;
- human expertise and consistency vary;
- approval cannot make an unsafe or invalid action safe by itself.

## Evaluation metrics

Record:

- actions requiring approval and policy coverage;
- unauthorized or bypassed-action attempts;
- approval, rejection, modification, escalation, expiry, and cancellation rates;
- state-change invalidations;
- time to decision and workflow delay;
- duplicate or stale execution incidents;
- post-approval validation failures and adverse outcomes;
- rollback success;
- approver workload, disagreement, and fatigue indicators;
- cost per safely completed action.

## Evidence and established usage

The OpenAI Agents SDK documents human-in-the-loop tool approval that pauses a run and resumes from stored state after approval or rejection. LangGraph documents interrupts that persist graph state and resume after human input.

Sources:

- [OpenAI Agents SDK: Human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [LangGraph interrupts](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/breakpoints/)
- [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)

## Related concepts

- [Multi-Agent Systems](../..)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Evaluator-Optimizer Architecture](../evaluator-optimizer/)
- [Advisory Council, Jury, and Review Board](../advisory-council-review-board/)
- [Handoff or Swarm Architecture](../handoff-swarm/)
- [Agent State](../../../agent-state/)
