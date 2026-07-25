# Selecting Models by Agent Role

Use this guide to choose models for the roles inside an agentic or multi-agent system. Select models by the behavior required from each role, not by model popularity or a single aggregate benchmark.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Initial canonical framework. Concrete model recommendations must include exact versions, runtime assumptions, evidence, and verification dates.

## Core principle

A role is a contract. It defines:

- responsibilities;
- required capabilities;
- allowed tools and data;
- failure boundaries;
- verification requirements;
- retry and escalation behavior;
- completion criteria.

The same model may cover several roles when this does not create unacceptable conflicts or quality loss. A dedicated model is justified only when specialization produces a measurable operational benefit.

## Role selection workflow

1. Enumerate the decisions and actions in the workflow.
2. Group them into roles with clear responsibility boundaries.
3. Define the quality tier and failure severity for each role.
4. Identify deterministic checks before assigning model-based verification.
5. Test whether one model can cover several compatible roles.
6. Separate roles when independence, specialization, or risk requires it.
7. Define routing, retry, escalation, and human approval gates.
8. Measure complete workflow quality and cost per accepted result.

## Canonical roles

### Orchestrator

Coordinates the complete workflow and controls task state.

Responsibilities:

- accept goals and constraints;
- decompose work or delegate decomposition;
- track dependencies and progress;
- select workers and tools;
- enforce retry and escalation policies;
- decide when the workflow is complete;
- verify that external resources are started and stopped correctly.

Required capabilities:

- strong instruction following;
- state tracking across long workflows;
- dependency reasoning;
- tool-use discipline;
- conservative completion decisions;
- reliable structured output.

Common failures:

- premature completion;
- omitted requirements;
- lost task state;
- duplicate or contradictory assignments;
- unbounded retries;
- trusting worker self-reports without evidence;
- failing to verify resource teardown.

A dedicated orchestrator is justified when the workflow is long-running, high-risk, expensive, or contains heterogeneous workers and services.

### Planner

Transforms a goal into an executable plan.

Responsibilities:

- identify requirements and unknowns;
- decompose the goal into tasks;
- define dependencies and order;
- assign acceptance criteria;
- identify risks and fallback paths;
- estimate resource needs.

Required capabilities:

- decomposition quality;
- constraint retention;
- causal and dependency reasoning;
- awareness of tool and worker limits;
- ability to produce concise executable plans.

Common failures:

- plans that are descriptive rather than executable;
- missing dependencies;
- hidden assumptions;
- over-decomposition;
- assigning impossible tasks;
- omitting validation steps.

The planner may be merged with the orchestrator for simple workflows. Separate it when planning quality materially affects cost or success rate.

### Router

Chooses the model, worker, tool, or workflow path for each task.

Responsibilities:

- classify task type and risk;
- select capability and quality tier;
- respect privacy, cost, latency, and availability constraints;
- escalate uncertain cases;
- record routing reasons when auditability is required.

Required capabilities:

- accurate task classification;
- calibrated uncertainty;
- knowledge of worker capability boundaries;
- low-latency structured decisions;
- deterministic policy compliance.

Common failures:

- sending difficult work to weak models;
- unnecessary escalation to expensive models;
- routing by superficial keywords;
- ignoring privacy or hardware constraints;
- failing to adapt when a service is unavailable.

Prefer deterministic routing rules where task classes are stable and explicit. Use a model-based router when classification requires semantic interpretation.

### Worker

Performs the primary task and produces the artifact or result.

Responsibilities depend on the workload, such as:

- writing or modifying code;
- generating text or media;
- extracting information;
- operating tools;
- analyzing data;
- executing a bounded research task.

Required capabilities:

- domain competence;
- instruction following;
- tool-use reliability;
- artifact quality at the required tier;
- awareness of uncertainty and missing inputs.

Common failures:

- incomplete output;
- fabricated completion;
- silent requirement changes;
- overconfident unsupported claims;
- damaging tool actions;
- poor artifact persistence.

Workers should not be the sole authority on whether their own work is accepted.

### Reviewer

Examines a worker result for quality, maintainability, consistency, or policy compliance.

Responsibilities:

- compare the artifact with requirements;
- identify defects, omissions, and risks;
- distinguish blocking issues from optional improvements;
- recommend acceptance, revision, or escalation;
- provide actionable feedback.

Required capabilities:

- critical evaluation;
- domain knowledge;
- sensitivity to omissions and edge cases;
- ability to avoid rewriting the task unnecessarily;
- clear severity classification.

Common failures:

- approving plausible but incorrect work;
- focusing on style while missing functional defects;
- inventing requirements;
- producing vague criticism;
- excessive false positives.

Use an independent reviewer for high-impact work. Reusing the worker model with a different prompt offers weaker independence and must be treated accordingly.

### Verifier

Determines whether explicit acceptance criteria are satisfied.

Responsibilities:

- run or inspect tests, validators, diffs, schemas, and evidence;
- confirm required artifacts exist;
- check claims against observable state;
- produce a pass, fail, or inconclusive decision;
- identify the exact unmet criterion.

Required capabilities:

- strict adherence to acceptance criteria;
- evidence-based decisions;
- structured reporting;
- low tolerance for unsupported completion claims.

Common failures:

- accepting narrative claims instead of evidence;
- substituting subjective quality review for verification;
- ignoring partial failures;
- reporting pass when checks were not executed.

Prefer deterministic verification whenever possible. A model should interpret evidence, not replace available tests.

### Evaluator or judge

Compares candidates, scores outputs, or selects a preferred result.

Responsibilities:

- apply a defined rubric;
- compare alternatives consistently;
- expose uncertainty and ties;
- avoid preference leakage from ordering or formatting;
- provide evidence for high-impact decisions.

Required capabilities:

- rubric adherence;
- comparative reasoning;
- calibration;
- resistance to verbosity, style, and position bias;
- consistent structured scoring.

Common failures:

- favoring longer answers;
- position bias;
- inconsistent scores;
- rewarding confident language over correctness;
- evaluating outside the rubric.

For important decisions, combine deterministic metrics, multiple evaluators, or human review rather than relying on one model score.

### Advisor

Provides options, expertise, or alternative approaches without controlling execution.

Responsibilities:

- surface trade-offs;
- identify risks and overlooked alternatives;
- supply domain-specific guidance;
- challenge assumptions;
- support a planner, orchestrator, or human decision-maker.

Required capabilities:

- domain depth;
- concise reasoning;
- uncertainty disclosure;
- ability to separate facts, assumptions, and recommendations.

Common failures:

- taking control of the workflow;
- presenting speculation as fact;
- producing generic advice;
- ignoring operational constraints.

Advisors are useful when the core model is operationally reliable but lacks specialist depth.

### Memory manager

Controls what information is stored, retrieved, updated, or forgotten across interactions.

Responsibilities:

- identify durable information;
- separate transient context from persistent memory;
- deduplicate and reconcile updates;
- enforce privacy and retention rules;
- retrieve relevant memories without flooding the context.

Required capabilities:

- precise information extraction;
- entity and timeline resolution;
- relevance ranking;
- conservative persistence decisions;
- structured storage output.

Common failures:

- storing temporary or incorrect information;
- duplicate memories;
- stale facts overriding newer ones;
- privacy leakage;
- retrieving irrelevant history.

Deterministic schemas and explicit retention rules should constrain this role.

### Context manager

Builds the working context for the next model call.

Responsibilities:

- select relevant documents, memories, tool results, and instructions;
- preserve source hierarchy and recency;
- remove redundant or low-value material;
- fit the context budget;
- keep critical constraints visible.

Required capabilities:

- relevance ranking;
- summarization without loss of constraints;
- source-aware conflict handling;
- token-budget management;
- awareness of task stage.

Common failures:

- dropping critical requirements;
- including excessive irrelevant content;
- merging conflicting sources without disclosure;
- using stale context;
- allowing summaries to replace authoritative source material.

A context manager may be deterministic, model-based, or hybrid. High-risk workflows should preserve traceability to source material.

## Role compatibility

### Common consolidations

These combinations are often practical for small systems:

- orchestrator and planner;
- router and orchestrator;
- worker and summarizer;
- reviewer and advisor;
- memory manager and context manager.

Consolidation is appropriate when:

- the workflow is simple;
- task volume is low;
- independence is not required;
- the model meets all role-specific quality thresholds;
- reduced service count materially lowers cost or latency.

### Risky consolidations

Treat these combinations cautiously:

- worker and verifier;
- worker and final reviewer;
- router and sole evaluator of routing quality;
- memory writer and sole authority for memory correctness;
- orchestrator and sole auditor of resource shutdown;
- planner and verifier when the planner may redefine success criteria.

The conflict is not always prohibited, but the reduced independence must be explicit.

### Strong separation candidates

Separate roles when:

- failure severity is high;
- regulatory or audit independence is required;
- a specialist materially outperforms the generalist;
- adversarial review is useful;
- the worker can influence or hide the evidence used for verification;
- one role needs very different latency, context, or hardware characteristics.

## Capability dimensions by role

Evaluate only the dimensions that matter for the assigned role.

| Capability | Orchestrator | Planner | Router | Worker | Reviewer | Verifier | Judge | Memory / Context |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Instruction following | High | High | High | High | High | High | High | High |
| Long-horizon state tracking | High | Medium | Low | Task-dependent | Medium | Low | Low | High |
| Tool-use reliability | High | Low | Medium | Task-dependent | Medium | High | Low | Medium |
| Domain specialization | Medium | Medium | Medium | High | High | Medium | High | Medium |
| Structured output | High | High | High | Medium | High | High | High | High |
| Calibrated uncertainty | High | High | High | High | High | High | High | High |
| Independence from worker | N/A | N/A | Medium | N/A | High | High | High | Medium |
| Low latency | Medium | Medium | High | Task-dependent | Medium | Medium | Medium | High |

Use this table as a starting point, not as a universal scorecard.

## Model selection record

Document each role assignment with a compact record:

```text
Role:
Responsibilities:
Quality tier:
Failure severity:
Candidate model and exact version:
Runtime and quantization:
Required context:
Tools and permissions:
Known strengths:
Known failure modes:
Verification method:
Retry limit:
Escalation target:
Can share a model with:
Must remain independent from:
Latency target:
Resource profile:
Evidence:
Verified:
```

Do not retain empty fields only to satisfy the template.

## Selection tests

### Orchestrator test

Evaluate whether the model can:

- preserve all constraints across multiple steps;
- maintain a valid task state;
- recover from worker failure;
- stop retrying at the defined limit;
- demand evidence before completion;
- verify external resource state.

### Planner test

Evaluate whether the model can:

- produce executable tasks;
- identify dependencies;
- retain acceptance criteria;
- expose assumptions;
- include verification and rollback steps.

### Router test

Evaluate:

- task-class accuracy;
- false escalation rate;
- missed escalation rate;
- policy violations;
- cost and latency impact of misrouting.

### Worker test

Use representative task sets and measure:

- accepted-result rate;
- omission rate;
- tool failure rate;
- correction success after feedback;
- cost and latency per accepted result.

### Reviewer and verifier tests

Measure separately:

- defect recall;
- false-positive rate;
- unsupported approval rate;
- consistency across repeated evaluations;
- ability to identify the exact failed criterion.

### Memory and context tests

Measure:

- relevant retrieval rate;
- omission of critical constraints;
- stale-memory usage;
- duplicate persistence;
- privacy violations;
- context size versus task success.

## Retry and escalation policy

Retries should be bounded and role-specific.

Retry the same model when:

- the failure is transient;
- a tool or service was temporarily unavailable;
- the feedback identifies a correctable local defect;
- the model has demonstrated useful correction behavior.

Escalate when:

- repeated failures are materially similar;
- the model repeatedly omits the same requirement;
- the failure indicates a capability ceiling;
- retry cost exceeds stronger-model cost;
- the role's failure severity exceeds the model's verified reliability.

Do not let a worker decide its own escalation policy without orchestration constraints.

## Human approval gates

Require human approval when:

- actions are irreversible or externally visible;
- financial, legal, security, or safety impact is material;
- the model would change production infrastructure or protected data;
- evidence is incomplete or contradictory;
- the system has not been validated for the required quality tier.

The human gate should receive a concise summary, the artifact, known risks, and verifiable evidence.

## Anti-patterns

Avoid:

- choosing one powerful model and assuming it is optimal for every role;
- assigning roles only by prompt wording without role-specific evaluation;
- allowing workers to verify their own completion claims;
- using a model judge without a rubric;
- using model-based verification where deterministic tests exist;
- unlimited retries;
- silent role consolidation that removes independence;
- letting a router ignore privacy, hardware, or provider constraints;
- persisting memory without retention and correction rules;
- treating context length as a substitute for context quality;
- publishing exact role rankings without reproducible evidence.

## Related pages

- [AI Model Selection and Team Design](../..)
- [Choosing Models for AI Agents](../agents/)
- [Choosing Models for Orchestration](../orchestration/)
- [Choosing Model Portfolios for Combined Workloads](../combined-workloads/)
- [Multi-Agent Systems](../../../../../concepts/sub/agents-and-automation/sub/multi-agent-systems/)
