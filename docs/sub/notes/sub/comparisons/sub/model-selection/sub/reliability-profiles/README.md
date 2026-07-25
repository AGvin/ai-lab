# Defining Model Reliability Profiles

Use this guide to record how reliably one exact model or service assignment performs one defined task class under one deployment and verification regime.

## Translations

- English

## Status

Initial canonical framework. Concrete profiles require repeatable evaluation evidence, exact deployment conditions, and a verification date.

## Profile unit

A reliability profile is not a universal score for a model family. One profile binds:

- the exact model identity, downloadable artifact, or hosted API snapshot;
- the provider endpoint, runtime, quantization, hardware, tools, prompts, parameters, and permissions that affect behavior;
- one bounded task class and input distribution;
- one required quality tier;
- the evaluation cases, trial count, acceptance criteria, and verification design;
- the evidence provenance and verification date.

Create separate profiles when a material part of that unit changes. Do not transfer a result from a hosted service to a local deployment, from one quantization to another, from coding to orchestration, or from exploratory work to production work without evidence that the result still applies.

## Quality tiers

Set the target before evaluating the assignment. Use the repository's five [quality tiers](../combined-workloads/#quality-tiers): **Exploration**, **Concept draft**, **Working result**, **Production quality**, and **Exceptional quality**.

The profile's **quality ceiling** is the highest tier the assignment has repeatedly reached under the recorded conditions. It is an observed boundary, not a promise that every future result will reach that tier.

## Reliability dimensions

Record behavior that changes routing, review, retry, or acceptance decisions.

### Strengths and common errors

Describe demonstrated strengths narrowly, such as reliable schema conformance for a named extraction task or strong correction behavior for a defined code-change class.

List recurring errors with observable signatures. Include:

- incorrect or unsupported content;
- format, schema, or tool-use defects;
- destructive or unauthorized actions;
- lost constraints and partial artifacts;
- unstable behavior across equivalent trials.

Do not replace measured results with provider capability claims or a general impression of model quality.

### Omitted requirements

Measure the **omitted-requirement risk** against an explicit checklist. Record which requirement types are commonly missed, whether the omission is detectable automatically, and whether correction succeeds.

An accepted-looking artifact can still be incomplete. Missing tests, files, citations, cleanup, edge cases, or user constraints should count as omissions even when the worker reports success.

### Premature completion

Measure the **premature-completion risk**: how often the worker claims completion before required artifacts exist, checks have run, external state is confirmed, or acceptance criteria pass.

Worker self-report is not proof of completion. Verify claims against artifacts, deterministic checks, tool results, provider state, or an independent reviewer.

### Review and independent verification

State:

- which deterministic validators must pass;
- which defects require a reviewer with domain knowledge;
- whether the reviewer must use a different model, provider, prompt context, or a human;
- what evidence the verifier receives;
- which quality tiers or risk levels require human approval.

Prefer deterministic validation before model-based or human review where possible. Tests, schemas, parsers, checksums, repository diffs, policy engines, and provider-state queries should establish what they can establish. Use reviewers for judgments that cannot be reduced to those checks.

Reusing the worker model as reviewer is not independent verification. It may be useful as a correction step, but record the weaker independence explicitly.

### Unsuitable tasks and quality ceiling

List forbidden or unsuitable tasks, including assignments that:

- exceed the observed quality ceiling;
- require an unsupported modality, tool, context length, language, or runtime;
- carry a failure severity above the verified profile;
- conflict with privacy, policy, permission, or deployment constraints;
- require independent judgment that the same assignment cannot provide.

A quality ceiling or unsuitable-task rule should route work to a named fallback, stronger model, specialist, deterministic process, or human owner.

### Cost per accepted result

Measure total cost until acceptance, not cost per initial call. Include:

- successful and failed model calls;
- tool, storage, grounding, and infrastructure charges;
- local runtime, model-loading, and hardware occupancy;
- retry and escalation calls;
- deterministic validation and reviewer calls;
- human review time when it is part of the operating process.

Keep the numerator and currency or resource unit explicit. Report the number of accepted results and rejected or abandoned cases used in the calculation.

## Failure classification and response

Classify a failure before deciding to retry.

| Failure class | Examples | Same-assignment retry | Required response |
| --- | --- | --- | --- |
| Transient infrastructure failure | Timeout, throttling, temporary endpoint or network unavailability | Yes, only within the infrastructure retry budget and when the operation is safe to repeat | Use bounded backoff with jitter, respect provider guidance, verify idempotency or protect side effects, then fail over or surface unavailability |
| Correctable output defect | Invalid format, one missed criterion, repairable tool argument | Sometimes, when evaluation shows that targeted feedback produces improvement | Preserve the failed criterion, request one bounded correction, re-run validation, and count the retry |
| Capability gap | Repeated reasoning failure, unsupported modality, quality ceiling below the target | No repeated retry with the same assignment | Escalate to a validated stronger model, specialist, deterministic workflow, or human |
| Policy or permission failure | Denied action, missing approval, provider policy refusal | No | Stop; request the required authority or use an approved alternative without bypassing the control |
| Missing-input failure | Absent file, ambiguous requirement, unavailable credential or context | No until the input exists | Ask the input owner, mark the result blocked or inconclusive, and resume only with the missing input |

This classification is repository-authored operational guidance. It applies retry principles to model workflows; it does not claim to be a new general reliability standard.

## Retry budgets and repeated failure signatures

Record both the observed **useful retry count** and the enforced budget.

The useful retry count is the number of additional attempts after which acceptance still improves materially for this assignment and failure class. Derive it from repeat trials; do not choose a universal number for every model.

The enforced budget should bound:

- attempts per task;
- cumulative attempts across nested workflow layers;
- wall-clock time;
- model, infrastructure, and review cost;
- external side effects;
- retries per service or tenant during an incident.

Infrastructure retries should use backoff and jitter and should not repeat unsafe non-idempotent actions without an idempotency key, transaction, or state check. Avoid multiplying retries at the client, orchestrator, worker, tool, and provider layers.

Normalize every failed attempt into a signature containing:

```text
Failure class:
Failed acceptance criteria:
Error or validator codes:
Missing or invalid artifacts:
Tool or provider state:
Correction requested:
```

Compare the signature with prior attempts. Stop same-assignment retries when:

- the same material criteria fail again after targeted correction;
- the output changes but the failure signature does not;
- the useful retry count or any enforced budget is exhausted;
- the failure is reclassified as a capability, policy, permission, or missing-input problem;
- expected retry cost exceeds validated escalation cost.

Record the terminal reason and escalation. Never reset the counter by moving the same unsuitable model into another workflow layer.

## Escalation strategy

Name an escalation target or deterministic selection rule before deployment. Possible targets include:

- another snapshot or deployment with a separate reliability profile;
- a stronger generalist;
- a task specialist;
- a deterministic tool or non-model workflow;
- an independent reviewer or human owner;
- a queue, fail-closed state, or reduced service tier.

Define triggers, allowed data transfer, maximum escalation cost, quality target, and who can accept a known limitation. Escalation is successful only when the target's own acceptance and verification requirements pass.

## Degraded operation and fallback profiles

A fallback is a separate assignment and therefore needs its own profile. Do not assume provider substitution or a smaller local model preserves quality, privacy, tool behavior, or policy controls.

### Local systems

Test loss of the preferred GPU, insufficient memory, runtime failure, model corruption, and overload. A degraded profile may use a smaller validated local model, CPU execution, reduced context, deterministic functions, delayed batch work, or a lower quality tier.

Keep protected data local unless an explicit rule permits hosted escalation. State which tasks must queue or fail closed because no local fallback meets their threshold.

### Hosted systems

Test throttling, endpoint outage, snapshot retirement, regional unavailability, latency spikes, and quota exhaustion. A degraded profile may use a validated alternate snapshot, region, or provider; queue work; reduce noncritical features; or require human handling.

Provider substitution must pass privacy, policy, permission, data-residency, tool-compatibility, and quality checks before traffic moves.

### Hybrid systems

Test the local and hosted paths independently and together. Define:

- which sensitive tasks remain local during hosted failure;
- which sanitized or approved inputs may move to hosted services during local failure;
- how the system behaves when the network and local accelerator are both unavailable;
- whether fallback lowers the quality tier or disables external actions;
- how queued work is deduplicated when the preferred path returns.

Record fallback activation, recovery, and return-to-primary criteria. Degraded operation must remain observable and must not silently claim the primary quality tier.

## Evaluation procedure

Official OpenAI evaluation guidance recommends task-specific evaluations that reflect real-world distributions, automated scoring where possible, calibration with human feedback, and continued evaluation as the system changes. The procedure below adapts those principles into a repository profile record.

1. Freeze the profile unit: model or API snapshot, deployment, runtime, tools, prompts, parameters, task class, quality tier, and date.
2. Define measurable acceptance criteria, trial eligibility, exclusion rules, and the independent verification path before running cases.
3. Build representative cases from expected production or local usage. Include typical, boundary, difficult, adversarial, historical-failure, missing-input, permission-denied, and infrastructure-failure cases where relevant.
4. Schedule a declared number of independent trials per case. Use enough repeat trials to expose nondeterminism; do not hide variance behind one best result or collapse repeats into one case outcome.
5. Create and independently approve the escalation ground-truth set before execution.
6. Mark which checks are deterministic and run them before model-based review.
7. For each trial and attempt, capture artifacts, failed criteria, failure class, latency, model and infrastructure use, review effort, cost, retry, escalation, and terminal disposition.
8. Exercise the proposed correction and retry budget. Confirm that repeated signatures stop further attempts and route to the declared escalation.
9. Exercise local, hosted, or hybrid fallback paths and re-evaluate them at their declared quality tiers.
10. Compare trial-level results with the acceptance threshold. Record uncertainty, eligible and excluded populations, and repeat count.
11. Have the required independent reviewer approve, reject, or mark the profile inconclusive.

Keep evaluation data representative of the deployment's real input distribution. Add newly observed failures to the case set and re-run affected evaluations after material changes.

## Outcome measures

### Trial unit and eligibility

A **case** is one fixed input scenario with acceptance criteria. An **attempt** is one initial call or retry within execution. An **eligible trial** is one scheduled independent execution of a case through its allowed attempts, verification, and escalation path under the frozen profile conditions.

Use eligible trials as the primary measurement unit. Decide eligibility and exclusions before execution. Exclude only invalid evaluation events outside the assignment being measured, such as a corrupted case fixture, evaluation-harness defect, or accidental duplicate run. Model or service timeouts, refusals, missing-input handling, policy or permission handling, budget exhaustion, and failed escalations remain eligible when they are part of the case or deployed operating conditions.

Report:

- scheduled, eligible, and excluded trial counts;
- the exclusion reason and affected case for every excluded trial;
- results for every eligible trial, including blocked, inconclusive, rejected, abandoned, and no-output dispositions.

Do not silently replace an excluded or failed trial with a successful rerun. If an issue discovered after execution invalidates a trial, require independent review of the exclusion and preserve it in the exclusion count.

Case-level coverage or stability is secondary. If it is reported, pre-register an aggregation rule such as “case passes when at least four of five eligible trials pass.” State the required number of eligible repeats and threshold. A case with fewer repeats after exclusions is inconclusive; do not choose the aggregation rule after seeing results.

### Escalation ground truth

Before execution, freeze the escalation policy as observable trigger rules, then create a scored escalation set in which every scheduled trial is labelled **should escalate** or **should not escalate**.

Use this procedure:

1. Construct cases with fixed risk, failure class, retry state, permission state, and repeated-signature or budget condition. Use injected or prerecorded failures when needed so the expected decision is knowable before the run.
2. Give the policy and case evidence to a reviewer who is independent of the worker and router. The reviewer assigns the label and records the triggering rule.
3. Resolve disagreements before execution. Remove any still-indeterminate case from the scored set before scheduling trials, and report the ground-truth exclusion and reason.
4. Freeze the labelled set, policy version, reviewer provenance, and adjudication record before the system under test routes any trial.
5. Do not relabel a trial after observing the system's routing decision. Report a trial invalidated by a ground-truth fixture or reference-policy defect as excluded from the labelled set, with its reason and independent approval. A routing or escalation policy failure in the system under test remains eligible and scored.

Natural-traffic escalation rate may be reported separately, but unnecessary and missed escalation require this pre-labelled ground truth.

### Metrics

Use counts and explicit denominators, not adjectives alone.

| Outcome | Measure |
| --- | --- |
| Acceptance | Eligible trials whose terminal disposition satisfies every acceptance criterion / all eligible trials. Also report first-attempt acceptance and assignment-only acceptance before escalation using the same eligible-trial denominator |
| Omission | For trials whose expected correct behavior requires an artifact: eligible trials whose first-attempt artifact omits at least one applicable requirement / all such eligible trials, and eligible trials whose terminal artifact omits at least one applicable requirement / all such eligible trials. Count a missing artifact as omitting all required artifact criteria. Also report omitted requirement checks / all applicable requirement checks across this trial population |
| Premature completion | Completion claims made before required verification passed / all completion claims made across eligible trials |
| Acceptance gained after retry | Retry-eligible trials accepted by a same-assignment retry before escalation / all eligible trials whose first attempt failed and for which policy allowed at least one same-assignment retry. Report separately by retry ordinal |
| Exhausted-budget rate | Retry-eligible trials that reached an attempt, time, cost, or side-effect limit before same-assignment acceptance / all eligible trials whose first attempt failed and for which policy allowed at least one same-assignment retry |
| Repeated-signature stop rate | Trials with no further same-assignment attempt after the first pre-declared repeated-signature stop condition / all eligible trials in which the independent verifier detected that stop condition |
| Escalation rate | Eligible trials in which the system initiated escalation / all eligible trials. Report the pre-labelled evaluation set and natural traffic separately |
| Escalation acceptance rate | Actually escalated eligible trials whose escalation target produced an independently accepted terminal result / all actually escalated eligible trials, including target timeouts, failures, and unavailable targets |
| Unnecessary-escalation rate | Eligible pre-labelled **should not escalate** trials that actually escalated / all eligible trials labelled **should not escalate** |
| Missed-escalation rate | Eligible pre-labelled **should escalate** trials that did not escalate / all eligible trials labelled **should escalate** |
| Latency | End-to-end time per eligible trial, including queue, retry, validation, review, and escalation; report terminal-disposition groups and percentiles when the sample supports them |
| Cost | Total measured model, infrastructure, validation, review, and human cost / accepted results |

For omission, pre-label trials whose correct behavior is a refusal, permission stop, or missing-input request as not requiring a result artifact; evaluate those trials against their explicit safe-handling acceptance criteria instead. Report this population and rule rather than mixing it into the artifact-omission denominator.

## Compact profile record

Use this record directly or link to equivalent structured data:

```text
Profile ID:
Model, artifact, or API snapshot:
Provider and endpoint:
Runtime, hardware, and quantization:
Tools, prompts, parameters, and permissions:
Task class and input distribution:
Quality tier:
Evaluation cases and repeat trials:
Trial eligibility and exclusion rules:
Acceptance criteria:
Deterministic validators:
Required reviewer and independence:
Strengths:
Common errors and failure signatures:
Omitted-requirement risk:
Premature-completion risk:
Useful retry count:
Retry budgets:
Escalation ground-truth set and policy:
Forbidden or unsuitable tasks:
Quality ceiling:
Escalation target or strategy:
Local, hosted, or hybrid fallback profile:
Degraded-operation behavior:
Acceptance, omission, and premature-completion outcomes:
Retry and escalation outcomes:
Outcome populations and denominators:
Latency outcomes:
Cost per accepted result:
Evidence provenance:
Evidence limitations:
Verified date:
Profile owner:
Re-evaluation triggers:
```

Do not include empty fields only to make the record look complete. Missing evidence should be explicit and may prevent production use.

## Evidence provenance and freshness

For each material claim, record whether the evidence is:

- first-party model or provider documentation;
- an external benchmark or independent evaluation;
- repository-run evaluation;
- production or local operational observation;
- deterministic tool output;
- model review or human review.

Preserve source URLs or artifact identifiers, access dates, evaluation code and case-set versions, raw results, hardware and runtime details, and known conflicts or limitations. Separate observed evidence from assumptions and provider claims.

The verification date describes when the complete profile unit was checked. It does not make old evidence current. Set an explicit review interval appropriate to model and provider change frequency, and mark a profile stale when its bound conditions or critical sources can no longer be reproduced.

## Maintenance and re-evaluation triggers

Re-evaluate the affected profile after:

- model, artifact, API snapshot, system prompt, parameter, tool, or policy changes;
- provider routing, moderation, pricing, rate-limit, region, or data-handling changes;
- runtime, quantization, driver, hardware, dependency, or permission changes;
- task distribution, acceptance criteria, quality tier, or failure severity changes;
- new repeated failure signatures, premature-completion incidents, privacy events, or external side effects;
- material drift in acceptance, omission, retry, escalation, latency, or cost outcomes;
- fallback activation that exposes an untested path;
- the defined freshness interval expires.

Retire or restrict a profile when its evidence cannot support the assigned tier. Keep historical records when they are needed to explain routing or incident decisions.

## Safe-use constraints

Every profile must define operational boundaries:

- **Privacy** — classify inputs and outputs, minimize disclosed data, record retention and region constraints, and prohibit transfer to a fallback that is not approved for the data.
- **Provider substitution** — treat every substitute endpoint, snapshot, or provider as a separate profile; do not silently inherit quality or safety claims.
- **Permissions** — use least privilege, preserve approval gates, and treat denials as stop conditions rather than prompts to bypass controls.
- **External side effects** — default evaluations to sandboxes or dry runs; require explicit authorization, idempotency or rollback controls, state verification, and human approval for irreversible, financial, public, production, or safety-relevant actions.

The worker must not expand its own authority, approve its own high-impact action, or treat a successful tool request as proof that the intended external state was reached.

## Source basis

The profile fields, failure taxonomy, thresholds, and operating rules in this page are repository-authored guidance. They apply established evaluation and reliability principles and make no claim of novelty.

Primary sources supporting the external principles are:

- [NIST AI RMF Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — a cross-sectoral companion resource for incorporating trustworthiness considerations into the design, development, use, and evaluation of generative AI systems.
- [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — task-specific evaluation, representative datasets, automated scoring where possible, human calibration, and continuous evaluation.
- [AWS retry with backoff pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) — backoff for transient failures, idempotency considerations, and fail-fast handling for identifiable non-transient errors.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — randomized exponential backoff, bounded per-request retries, service-wide retry budgets, graceful degradation, and avoidance of retry multiplication across layers.
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — environmental ground truth, human checkpoints, stopping conditions, sandbox testing, and guardrails for agent workflows.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Selecting Models by Agent Role](../agent-role-selection/)
- [Choosing Models for Agent Orchestration](../orchestration/)
