# Choosing Models for Agent Orchestration

Use this guide to select the model or model hierarchy that decomposes work, assigns tasks to agents, controls execution order, manages expensive resources, evaluates quality, and decides when a workflow is complete.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Draft methodology. Concrete orchestrator recommendations require repeatable portfolio-level evaluations rather than chat benchmarks alone.

## Terminology

A **generalist model** is a model with useful capability across several task domains. It describes breadth of capability, not authority in a system.

An **orchestrator agent** or **manager agent** is a system role responsible for coordinating other agents, models, tools, and resources. The orchestrator may use a generalist model, a reasoning-specialized model, or a hierarchy of several manager models.

A generalist can be used as a worker without orchestration responsibilities. An orchestrator can also delegate most domain work and therefore does not need to be the best model at every worker task.

## Primary responsibilities

An orchestrator should be evaluated on its ability to:

- translate a user goal into explicit deliverables and acceptance criteria;
- decompose work into bounded tasks and subtasks;
- identify dependencies, shared state, and conflict risks;
- select suitable agents, models, tools, permissions, and quality tiers;
- decide which tasks may run in parallel and which must run sequentially;
- create isolation or merge plans for parallel work that touches shared resources;
- monitor progress, failures, costs, and resource state;
- validate worker reports against actual results;
- request targeted corrections without restarting unaffected work;
- stop when the required quality is reached or a budget limit is met;
- produce a final result, decision record, and unresolved-risk summary.

The orchestrator is a control function, not merely a model router.

## Planning execution order

### Parallel execution

Use parallel execution when tasks are independent or can be isolated safely.

Examples:

- translating different independent documents;
- researching unrelated alternatives;
- evaluating several generated images without modifying shared state;
- creating competing design proposals;
- running tests on separate immutable snapshots.

Before parallel launch, the orchestrator should identify:

- files, records, services, or resources each task may modify;
- ordering dependencies and required inputs;
- collision risks;
- branch, workspace, namespace, or output-directory isolation;
- the merge and conflict-resolution owner.

### Sequential execution

Use sequential execution when one task consumes another task's result, when several tasks modify the same state, or when a later decision depends on validated earlier work.

The orchestrator should avoid false parallelism that creates rework, merge conflicts, inconsistent assumptions, or duplicate costs.

### Hybrid execution graph

Most substantial workflows are directed dependency graphs rather than fully parallel or fully sequential lists. The orchestrator should launch each ready task when its dependencies and resource requirements are satisfied.

## Agent and model assignment

Assignment should consider more than the task label. For every worker candidate, record:

- demonstrated quality for the exact task class;
- tool, modality, language, and context requirements;
- cost and expected number of retries;
- reliability and common failure modes;
- whether outputs require independent review;
- whether the model tends to stop early, omit cleanup, or report success without verification;
- model residency, startup latency, and concurrency limits;
- data-handling, permission, and policy constraints.

The orchestrator should know when a weaker model is sufficient for a draft and when a stronger model is required for a final deliverable.

## Quality targets

Quality is a workflow requirement, not a single universal score.

Define the requested level before assigning work:

- **Exploration** — fast alternatives, rough estimates, or feasibility checks.
- **Concept draft** — coherent intermediate result suitable for discussion but not publication or production.
- **Working result** — functionally correct output with acceptable presentation and bounded known limitations.
- **Production quality** — verified, maintainable, documented, and ready for operational use.
- **Exceptional quality** — additional refinement, originality, polish, or performance justified by the task value.

The orchestrator should not spend frontier-model tokens or launch expensive infrastructure to create exceptional quality when an exploratory result is sufficient. It should also not accept a merely functional result when visual quality, writing quality, safety, maintainability, or user trust is a material requirement.

## Resource and service lifecycle

Some workers are continuously available; others require expensive on-demand infrastructure such as a GPU pod, temporary service, or remote model endpoint.

For every on-demand worker, the orchestrator should execute a lifecycle state machine:

1. Confirm that the task requires the resource and that budget is available.
2. Start or request the resource through an approved API, MCP server, workflow tool, or control plane.
3. Wait for a verified ready state rather than assuming that the start request completed.
4. Execute the assigned work and preserve required outputs outside ephemeral storage.
5. Validate that the result is complete before releasing the resource.
6. Request shutdown, termination, or scale-to-zero.
7. Re-check provider state until termination is confirmed.
8. Escalate or retry cleanup when billing or resource state remains active.

A worker report that says the task is complete does not prove that the paid resource was stopped.

## Always-on and resident components

A team design should state which components are:

- always running and always resident in RAM or VRAM;
- always reachable but loaded on first use;
- retained for a bounded idle period;
- launched only for one task;
- remote hosted services with no local residency;
- unavailable concurrently because they compete for the same hardware.

This information affects scheduling. The orchestrator must not assign simultaneous local tasks to models that cannot coexist within available memory.

## Reliability profiles and retries

The orchestrator should maintain a profile for each worker model:

- expected task quality;
- common omissions or formatting defects;
- probability of premature completion claims;
- need for retries or stronger prompts;
- tasks that require an independent checker;
- maximum useful retry count;
- escalation model when repeated correction does not improve the result.

Retries must be bounded and evidence-driven. Repeating the same prompt to the same unsuitable model is not a recovery strategy.

## Hierarchical orchestration

Large portfolios may use several management levels:

- a top-level orchestrator owns the global goal, budget, dependencies, and final acceptance;
- department or domain managers own a coherent workstream such as software, localization, design, research, or operations;
- team leads coordinate smaller units such as frontend, support, UX, image evaluation, or test automation;
- workers execute bounded tasks and report evidence to their direct manager.

Each manager should receive an explicit scope, authority, budget, quality threshold, and reporting contract. The upper manager should not need every low-level execution detail, but it must receive enough evidence to validate progress and resolve cross-unit dependencies.

Use hierarchy when it reduces context overload, separates specialized policies, or permits meaningful parallel work. Do not add management layers when a simple workflow graph is clearer.

## Advisory council and review board

A manager may consult several independent models before accepting a plan or result. Suitable names include **advisory council** for non-binding recommendations and **review board** for approval or rejection authority.

A council can include roles such as:

- domain expert;
- risk reviewer;
- cost and infrastructure reviewer;
- quality or design critic;
- adversarial reviewer;
- user-requirement representative.

The orchestrator should receive structured findings rather than unrestricted debate. Preserve a user-visible decision summary containing:

- proposals considered;
- principal arguments and evidence;
- disagreements;
- final decision and responsible decision-maker;
- requested corrections;
- remaining uncertainty.

Do not expose or depend on private hidden chain-of-thought. Record concise decision rationale and inspectable evidence.

## Preventing review loops

A review board can waste time and money by repeatedly rejecting an output that the assigned worker cannot materially improve.

Use controls such as:

- explicit acceptance criteria;
- bounded review and rework rounds;
- issue identifiers so the same unresolved criticism is detected;
- comparison of revisions to determine whether quality is improving;
- escalation to another worker model after repeated failure;
- permission to accept a known limitation when the required quality tier allows it;
- human approval when reviewers disagree or the budget threshold is reached;
- cycle detection for repeated task, reviewer, and feedback states.

The orchestrator should distinguish between a correctable execution defect, an unsuitable worker, an impossible requirement, and a reviewer preference that is outside scope.

## Orchestrator selection criteria

Evaluate candidate orchestrator models using complete workflows that require:

- task decomposition and dependency graph construction;
- conflict-aware parallelization;
- model and tool assignment under budget and hardware constraints;
- adaptation when a worker fails or becomes unavailable;
- resource startup and verified teardown;
- draft-versus-final quality decisions;
- selective escalation rather than universal use of the strongest model;
- concise state and decision records;
- termination without unnecessary loops.

The best worker model is not automatically the best orchestrator. Orchestration rewards consistency, planning, structured state management, verification discipline, and cost-aware judgment.

## Evaluation metrics

Record at least:

- portfolio completion rate;
- acceptance-criteria coverage;
- dependency and conflict errors;
- parallelism achieved without rework;
- worker assignment accuracy;
- unnecessary expensive-model calls;
- retries and repeated feedback cycles;
- resource leak incidents;
- peak RAM and VRAM;
- total API and infrastructure cost;
- wall-clock completion time;
- human interventions;
- final quality tier reached.

## Related pages

- [Model Selection and Team Design](../../)
- [Agent Models](../agents/)
- [Combined Workloads](../combined-workloads/)
- [Multi-Agent Systems](../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
- [Agent Orchestration Tools](../../../../../../../software/sub/agent-orchestration/)
