# Agents and Automation Model Selection

Choose models for tool-using, multi-step, and agentic execution by evaluating the complete loop rather than chat quality alone.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers tool use and function calling, general agents, browser/desktop/mobile computer use, voice agents, planning and execution, long-running task execution, and models used as orchestrators or manager agents.

Small or inexpensive models may be useful as bounded workers, routers, extractors, or formatters without being reliable primary agents. Open weights, long context, low token price, or an `agentic` product label do not establish long-horizon reliability.

## What to evaluate

Evaluate the complete execution loop with the same tools, permissions, environment snapshot, initial context, and stopping rules:

- planning and task decomposition;
- tool selection and argument accuracy;
- structured-output reliability;
- recovery after tool or environment failures;
- context and state retention across long workflows;
- unnecessary loops, duplicate actions, and token use;
- compliance with permissions and human-approval boundaries;
- terminal acceptance, retries, corrections, wall-clock time, and total cost per accepted result.

Include adversarial and degraded cases such as missing files, timeouts, conflicting instructions, stale documentation, prompt injection, and failed verification.

Use application-level trust boundaries, least privilege, explicit stopping rules, and independent verification where risk requires it. Model safeguards are not a substitute for those controls.

## Orchestrator or manager model

The best worker model is not automatically the best orchestrator. When selecting a model to coordinate agents or tools, evaluate whether the exact model can reliably perform the **control role** under the intended workflow constraints.

A candidate orchestrator should be tested on its ability to:

- translate a goal into explicit deliverables and acceptance criteria;
- decompose work into bounded tasks and identify material dependencies;
- recognize shared-state, ordering, and conflict risks before recommending parallel execution;
- assign suitable workers/models/tools according to role, permissions, quality target, and evidence;
- preserve concise workflow state, decisions, unresolved risks, and evidence across steps;
- validate worker completion claims against observable artifacts or independent checks rather than trusting self-report;
- request targeted correction while preserving already valid work;
- distinguish a correctable defect from a capability gap, missing input, permission failure, or contradictory requirement;
- stop or escalate when retries, quality limits, risk, or expected accepted-result cost justify a different route;
- make a terminal completion decision only after the declared acceptance path has passed.

Evaluate dependency mistakes, unsafe/false parallelism decisions, worker/tool assignment accuracy, missed constraints, unnecessary expensive escalations, repeated correction loops, premature completion, and final criterion coverage. A model that is strong at producing work but weak at monitoring evidence or stopping can still be a poor orchestrator.

### Orchestrator stopping and escalation

Set the target quality and stop conditions before evaluation. A valid orchestrator should stop when every required criterion passes, when an authorized known limitation is accepted, when a declared retry/review budget is exhausted, when the requirement is impossible or contradictory, or when human judgment or a stronger/specialist route has higher expected value than another same-model attempt.

Attach assignment-specific reliability evidence from the [Model Selection methodology](../..) and use [Model Teams](../model-teams/) for portfolio/routing/escalation topology. The producing worker or orchestrator must not be the sole authority on its own completion when independent verification is material.

## Ownership boundary

This page evaluates **model capability for agent/orchestrator roles**. Designing the actual workflow engine or execution graph, choosing orchestration software, coordinating branches/workspaces, managing runtime/service lifecycle, GPU residency, provider resource startup/teardown, billing reconciliation, or infrastructure fault recovery are broader software/deployment/operations concerns and remain outside this subtree.

Those operational conditions may be recorded as frozen evaluation context when they materially affect model behavior, but they are not themselves reasons to classify an orchestration system as a model-selection page.

Link intrinsic model facts from [Model Reference](../../../reference/) and keep agent-workload evidence here.
