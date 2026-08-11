# Models for Different Roles

Choose models for roles inside an agentic or multi-model system by the role contract, required independence, failure severity, and measured workflow benefit.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Role as contract

Before choosing a model, define the role's responsibilities, required capabilities, allowed tools and data, failure boundaries, verification requirements, retry and escalation behavior, and completion criteria. A capable generalist or strong worker is not automatically a reliable orchestrator, router, reviewer, verifier, evaluator, or memory authority.

## Role contracts

| Role | Selection contract | Failure signals to test |
| --- | --- | --- |
| Orchestrator | Retain global constraints and task state, manage dependencies/budgets/progress, select workers/tools/routes, enforce retry/escalation/termination, and demand evidence before completion | Premature completion, lost state, duplicate/conflicting assignments, unbounded loops, trusting worker self-report, failure to verify external resource state |
| Planner | Turn goals into executable tasks with dependencies, acceptance criteria, assumptions, risks, fallback paths, and validation steps | Hidden assumptions, missing dependencies, descriptive but non-executable plans, over-decomposition, impossible assignments, omitted verification |
| Router | Choose model/worker/tool/workflow paths under capability, risk, privacy, cost, latency, availability, and quality constraints | False or missed escalation, policy violations, superficial-keyword routing, unnecessary expensive routes |
| Worker | Execute the bounded task, respect tools/permissions/scope, preserve required artifacts, and expose uncertainty or missing inputs | Incomplete output, fabricated completion, silent requirement changes, unsupported claims, damaging tool use, poor artifact persistence |
| Reviewer | Compare artifacts with requirements and identify defects, omissions, risks, severity, and actionable corrections | Plausible-but-wrong approval, low defect recall, excess false positives, style fixation, invented requirements, vague criticism |
| Verifier | Decide pass/fail/inconclusive from explicit acceptance criteria and observable evidence | Accepting narrative claims, skipping available checks, false pass decisions, failing to name the unmet criterion |
| Evaluator / judge | Apply a defined rubric consistently, expose uncertainty/ties/abstention, and operate only within calibrated decision authority | Position/order/verbosity/style/identity/self-preference bias, inconsistent scoring, unsupported confidence |
| Advisor | Surface specialist options, trade-offs, risks, and challenges without owning execution | Generic advice, unsupported speculation, taking workflow authority, ignoring operational constraints |
| Memory manager | Select, reconcile, persist, update, retrieve, or forget durable information under explicit privacy and retention rules | Stale or incorrect persistence, duplicates, privacy leakage, entity/timeline confusion, irrelevant retrieval |
| Context manager | Assemble current context from authoritative instructions, documents, memories, and tool results under relevance, recency, source hierarchy, and token limits | Dropped constraints, irrelevant context flooding, stale context, silent merging of conflicting sources |

Prefer deterministic routing or verification where stable rules or validators can prove the required property. Model judgment should interpret evidence rather than replace an available deterministic check.

## Consolidate or separate

One model may cover several compatible roles when the workflow is simple, independence is unnecessary, and the combined assignment meets its measured quality targets with lower cost or latency.

Treat worker/verifier, worker/final-reviewer, router/sole-routing-evaluator, memory-writer/sole-memory-checker, orchestrator/sole-resource-shutdown-auditor, and planner/verifier combinations as reduced-independence designs when the first role can influence the evidence or success criteria used by the second. Add deterministic evidence, a separate model, or a human authority where the risk requires it.

## Role-specific evaluation

Use tests that match the role instead of one aggregate benchmark:

- orchestrator — constraint retention, state continuity, recovery, retry discipline, and termination;
- planner — executable decomposition, dependencies, assumptions, acceptance criteria, and verification steps;
- router — classification accuracy, false escalation, missed escalation, policy compliance, cost and latency impact;
- worker — accepted-result rate, omissions, tool failures, correction behavior, and artifact integrity;
- reviewer/verifier — defect recall, false positives, unsupported approvals, consistency, and exact failed-criterion identification;
- evaluator/judge — rubric adherence, calibration, bias tests, disagreement, abstention, and human overturn where relevant;
- memory/context — relevant retrieval, stale-state use, duplicates, privacy violations, critical-constraint retention, and context efficiency.

## Assignment record

For a material role assignment, record the role, responsibilities, quality tier, failure severity, exact model/version/artifact, relevant runtime or scaffold, context, tools and permissions, observed strengths and failure modes, verification method, retry limit, escalation target, independence constraints, latency/resource evidence, and verification date. Omit fields that add no evidence.

Link model facts from [Model Reference](../../../../../reference/). More specific portfolio-shape pages are materialized only when their selection evidence differs enough to justify a dedicated node.
