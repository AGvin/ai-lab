# Choosing Model Portfolios for Combined Workloads

Use this guide to select the smallest practical set of models for a workload that spans several tasks, modalities, quality levels, deployment environments, and cost constraints.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Initial framework. Concrete model assignments must be added only when the exact model version, access conditions, hardware profile, evidence, and verification date are known.

## Purpose

Combined workloads should not be designed by independently choosing the strongest model for every task and then summing the results. That approach often creates unnecessary VRAM pressure, service count, cold starts, provider dependencies, and orchestration complexity.

A useful portfolio recommendation should answer:

- which tasks must be covered;
- which tasks may share one generalist model;
- where a specialist materially improves accepted-result quality;
- which models must remain resident concurrently;
- which models may be loaded sequentially or called remotely;
- how failures are reviewed, retried, escalated, or accepted with known limitations;
- how the complete system behaves under the required quality, latency, privacy, and budget constraints.

The objective is the smallest economically justified portfolio that meets every required quality threshold.

## Start with the workload, not the models

Describe the workload before naming candidates.

Record:

```text
Workload name:
Primary tasks:
Secondary tasks:
Required modalities:
Quality tier by task:
Failure severity by task:
Privacy and offline constraints:
Latency target:
Concurrency:
Hardware:
Hosted-service constraints:
Budget model:
Evidence date:
```

Do not assume that every task needs a separate model. Group tasks by capability overlap, execution schedule, and quality threshold first.

## Portfolio topologies

### Single generalist

One model performs all supported tasks.

Prefer this when:

- hardware is constrained;
- tasks are mostly text or share the same modality;
- operational simplicity matters more than maximum specialist quality;
- model switching would dominate execution time;
- privacy or offline operation rules out hosted specialists.

Reject this topology when one task has a materially higher quality threshold than the generalist can meet.

### Generalist with specialist fallback

A resident generalist handles routine work. A specialist is loaded or called only when a task exceeds the generalist's quality ceiling.

Prefer this when:

- most work is routine;
- difficult cases are infrequent;
- specialist startup or API cost is acceptable only for escalations;
- the generalist can reliably identify when escalation is needed, or an independent verifier can make that decision.

The fallback trigger must be explicit. Do not rely only on the worker model's self-assessment.

### Router with quality tiers

A router assigns work to low-cost, standard, or high-capability models based on task type, risk, and required quality.

Prefer this when:

- the workload contains clearly separable task classes;
- expensive models should be reserved for difficult or high-risk cases;
- routing decisions can be audited and tested;
- misrouting has bounded consequences.

Evaluate routing quality separately. A weak router can erase expected savings by sending difficult work to unsuitable models or escalating too often.

### Specialist team

Several models are assigned to distinct task classes or modalities.

Prefer this when:

- specialists produce a material quality gain;
- tasks use different modalities or runtimes;
- models can be scheduled sequentially or the available hardware supports concurrent residency;
- the additional orchestration and maintenance cost is justified.

Avoid a specialist team when a generalist already meets the required quality for most tasks.

### Local core with hosted escalation

A local model handles private, routine, or always-on work. Hosted models are called for difficult reasoning, specialized generation, or rare high-quality tasks.

Prefer this when:

- sensitive context can remain local;
- hosted access is acceptable for selected inputs;
- local infrastructure should cover normal operation;
- cloud cost should scale with exceptional demand rather than idle availability.

Document exactly what data may leave the local environment.

### Orchestrator with disposable workers

A resident orchestrator starts temporary workers, hosted jobs, or GPU services only when needed.

Prefer this when:

- workloads are bursty;
- specialist services are expensive to keep running;
- startup latency is acceptable;
- the orchestration layer can verify service readiness and teardown.

A worker reporting completion is not proof that a billable resource stopped. Provider state must be checked independently.

## Role assignment

A model may hold several roles only when its behavior is adequate for each role and the consolidation reduces meaningful operational cost.

Common roles include:

- orchestrator or manager;
- planner;
- router;
- worker;
- reviewer;
- verifier;
- evaluator or judge;
- advisor;
- summarizer;
- memory or context manager.

The strongest worker is not automatically the best orchestrator. Evaluate decomposition, dependency handling, routing, retry discipline, completion decisions, and resource control separately from task execution quality.

## Quality tiers

Assign a quality tier per task, not only per portfolio.

1. **Exploration** — fast feasibility check with approximate output.
2. **Concept draft** — meaningful draft suitable for discussion.
3. **Working result** — functionally acceptable with known limitations.
4. **Production quality** — verified, maintainable, documented, and ready for real use.
5. **Exceptional quality** — additional polish or depth that justifies higher cost and iteration count.

A portfolio may use different models for the same task at different quality tiers.

## Residency and scheduling

Record the execution model explicitly.

### Concurrent residency

Several models remain loaded because tasks run in parallel or because switching latency is unacceptable.

Record peak combined VRAM, RAM, KV-cache growth, and runtime overhead.

### Sequential residency

Models are loaded one after another because task dependencies allow reuse of the same hardware.

Record unload time, load time, warm-up time, state persistence, and whether intermediate artifacts survive model changes.

### Shared model service

Several agents use the same loaded model with different prompts, tools, or roles.

Record concurrency limits, queueing behavior, context isolation, and whether one long request can block other agents.

### Remote specialist

The specialist runs through a hosted API or external service.

Record provider latency, rate limits, retry behavior, data exposure, regional constraints, and cost assumptions.

### On-demand GPU or service

A temporary resource is started only when required.

The lifecycle should include:

1. need check;
2. budget check;
3. startup request;
4. provider-state readiness verification;
5. workload execution;
6. artifact persistence;
7. result verification;
8. shutdown request;
9. provider-state shutdown verification;
10. cleanup retry and escalation when shutdown fails.

## Reliability and escalation

Define a reliability profile for each assigned model or service.

Record:

```text
Strengths:
Common failures:
Omitted-requirement risk:
Premature-completion risk:
Useful retry count:
Required reviewer:
Escalation target:
Unsuitable tasks:
Quality ceiling:
Cost per accepted result:
```

Use bounded retries. Repeating the same task with the same unsuitable model is not a recovery strategy.

Escalate when:

- repeated failures are substantially similar;
- the model omits the same requirement after correction;
- a reviewer identifies a capability gap rather than a prompt defect;
- the expected retry cost exceeds the cost of a stronger model;
- the task risk exceeds the model's verified reliability profile.

## Verification design

Do not let the worker be the only judge of its own output.

Possible verification patterns:

- deterministic tests or validators;
- independent reviewer model;
- specialist evaluator;
- human approval gate;
- comparison against acceptance criteria;
- artifact diff or regression check;
- multi-model advisory or jury review for high-impact decisions.

The verifier should receive explicit acceptance criteria and enough evidence to detect unsupported completion claims.

## Cost model

Measure total system cost rather than isolated token price or raw inference speed.

Include:

- local hardware occupancy;
- model load and unload time;
- idle residency;
- API input, cached-input, output, tool, storage, and grounding charges;
- retries and review calls;
- failed starts and abandoned jobs;
- human review time;
- orchestration maintenance;
- cost of incorrect routing;
- cost per accepted result.

The cheapest model per request may be more expensive per accepted result when retries and verification dominate.

## Common environment profiles

### One 24 GB GPU

Typical constraints:

- one medium or large quantized language model at a time;
- limited concurrent residency;
- sequential specialist loading may be necessary;
- image, speech, or language models may compete for the same VRAM;
- hosted escalation can reduce local switching and residency pressure.

Recommended design direction:

- keep one generalist resident when it covers most routine work;
- use sequential local specialists only for frequent tasks with clear quality gains;
- use hosted or on-demand specialists for rare expensive tasks;
- persist artifacts before unloading a model;
- measure real reload latency before assuming frequent switching is acceptable.

### Two 24 GB GPUs

Possible strategies:

- one model per GPU;
- tensor or pipeline parallel execution for a larger model;
- resident generalist plus resident specialist;
- dedicated inference GPU plus generation or evaluation GPU.

The best layout depends on task concurrency. Two GPUs do not automatically justify one larger model if two independent resident services improve the complete workflow.

### CPU-only

Prefer:

- smaller quantized models;
- low-concurrency workloads;
- background or batch processing;
- deterministic tools for tasks that do not require a model;
- hosted escalation for latency-sensitive or high-quality work.

### Cloud-only

Prioritize:

- provider capability coverage;
- rate limits and concurrency;
- data handling and retention;
- model version stability;
- fallback across providers;
- total cost under retries and review.

### Hybrid local and hosted

Use local models for privacy, routine work, offline resilience, and cost control. Use hosted models for capability peaks, rare modalities, and high-quality escalation.

Document routing and data-boundary rules explicitly.

### Always-on local core with on-demand specialist

Keep a generalist, router, or orchestrator available locally. Start or call specialists only when required.

This topology is suitable for home labs and constrained servers when specialist demand is intermittent.

## Portfolio recommendation record

Use a compact record such as:

```text
Portfolio name:
Workload:
Environment:
Quality tiers:
Selected models or candidate classes:
Assigned roles:
Role consolidation:
Fallback and escalation:
Verification:
Concurrent or sequential residency:
Peak RAM and VRAM:
Startup and switching overhead:
Hosted-service assumptions:
Privacy boundary:
Reliability constraints:
Rejected alternatives:
Evidence:
Verified:
```

Do not include empty fields only to satisfy the template.

## Evaluation procedure

1. Enumerate all tasks and required modalities.
2. Assign quality tiers and failure severity.
3. Identify capability overlap between tasks.
4. Test whether one generalist meets the minimum threshold for each task.
5. Add a specialist only where the measured quality gain justifies its total cost.
6. Define roles, routing, verification, retries, and escalation.
7. Model concurrent and sequential residency.
8. Measure startup, switching, throughput, and complete workflow latency.
9. Calculate cost per accepted result.
10. Test degraded operation when a local model, provider, GPU service, or network dependency is unavailable.
11. Record exact versions, hardware, runtime, evidence, and verification date.

## Anti-patterns

Avoid:

- choosing one model per task without checking capability overlap;
- keeping rarely used specialists resident without measuring the cost;
- treating quantizations as unrelated base models;
- relying on one aggregate benchmark for portfolio design;
- letting a worker declare its own success without independent checks;
- unlimited retries with the same model;
- starting billable resources without verified teardown;
- hiding routing, review, or retry costs from the recommendation;
- assuming a larger model is always better than two smaller concurrent services;
- publishing exact rankings without reproducible evidence.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Choosing Models for AI Agents](../agents/)
- [Choosing Models for Coding](../coding/)
- [Choosing Models for Orchestration](../orchestration/)
- [Defining Model Reliability Profiles](../reliability-profiles/)
- [Multi-Agent Systems](../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
- [Models](../../../../../../../software/sub/models/)
