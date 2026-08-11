# Documentation Requirements

## Requirements

- Treat each role as an explicit behavioral contract before selecting a model.
- Preserve the useful legacy role vocabulary: orchestrator, planner, router, worker, reviewer, verifier, evaluator/judge, advisor, memory manager, and context manager.
- Require role-specific responsibilities, capabilities, tools/data, failure boundaries, verification, retries/escalation, and completion criteria.
- Preserve the following role-specific selection contracts from the legacy role guide without turning them into fixed model assignments:
  - **Orchestrator:** coordinate the complete workflow, retain global constraints and task state, manage dependencies/budgets/progress, select workers/tools/routes, enforce retry/escalation/termination, and demand evidence before completion; test premature completion, lost state, duplicate or conflicting assignments, unbounded loops, worker-self-report trust, and failure to verify external resource state.
  - **Planner:** turn goals into executable tasks with dependencies, acceptance criteria, assumptions, risks, fallback paths, and validation steps; test hidden assumptions, missing dependencies, descriptive-but-not-executable plans, over-decomposition, impossible assignments, and omitted verification.
  - **Router:** choose model/worker/tool/workflow paths under capability, risk, privacy, cost, latency, availability, and quality constraints; prefer deterministic routing where stable rules suffice; measure false escalation, missed escalation, policy violations, and superficial-keyword routing.
  - **Worker:** execute the bounded domain task, respect tools/permissions/scope, preserve required artifacts, and expose uncertainty or missing inputs; test incomplete output, fabricated completion, silent requirement changes, unsupported claims, damaging tool use, and poor artifact persistence.
  - **Reviewer:** compare artifacts against requirements and identify defects, omissions, risks, severity, and actionable corrections; measure defect recall and false positives and test plausible-but-wrong approval, style fixation, invented requirements, and vague criticism.
  - **Verifier:** decide pass/fail/inconclusive from explicit acceptance criteria and observable evidence such as tests, validators, diffs, schemas, artifacts, or tool/provider state; prefer deterministic verification and test narrative-claim acceptance, skipped checks, and false pass decisions.
  - **Evaluator/Judge:** apply a defined rubric consistently across candidates while exposing uncertainty, ties, abstention, and relevant bias; require calibration and test position, order, verbosity, style, identity, self-preference, and inconsistent-scoring effects before granting decision authority.
  - **Advisor:** surface specialist options, trade-offs, risks, and challenges without owning execution; test generic advice, unsupported speculation, takeover of workflow authority, and disregard for operational constraints.
  - **Memory manager:** select, reconcile, persist, update, or forget durable information under explicit privacy/retention rules; test stale or incorrect persistence, duplicates, privacy leakage, entity/timeline confusion, and irrelevant retrieval.
  - **Context manager:** assemble current working context from authoritative instructions, documents, memories, and tool results under relevance, recency, source hierarchy, and token-budget constraints; test dropped requirements, irrelevant context flooding, stale context, and silent merging of conflicting sources.
- Preserve the legacy distinction between role capability and role authority: a strong generalist or worker is not automatically a reliable orchestrator, router, reviewer, verifier, or memory authority.
- Require role-specific tests when relevant: orchestrator constraint/state/recovery/termination tests; planner dependency/acceptance/assumption tests; router false- and missed-escalation tests; worker acceptance/omission/tool/correction tests; reviewer/verifier defect-recall, false-positive, unsupported-approval, and failed-criterion tests; memory/context relevance, stale-state, duplicate, privacy, and critical-constraint-retention tests.
- Permit role consolidation only when independence is unnecessary and measured workflow quality remains acceptable.
- Flag self-approval combinations such as worker/verifier and worker/final-reviewer as reduced-independence designs requiring explicit evidence or compensating controls.
- Also treat router/sole-routing-evaluator, memory-writer/sole-memory-checker, orchestrator/sole-resource-shutdown-auditor, and planner/verifier combinations as potentially reduced-independence designs when the first role can influence the evidence or success criteria used by the second.
- Require role-specific evaluation rather than one aggregate benchmark or popularity ranking.
- Require exact model/version/artifact and evidence boundaries for role assignments.
- Require each material role assignment to record the role, responsibilities, quality tier, failure severity, exact candidate identity, relevant runtime/scaffold, context, tools/permissions, observed strengths/failures, verification method, retry limit, escalation target, independence constraints, latency/resource evidence, and verification date; omit empty fields that add no evidence.
- Link canonical model facts from `../../../../../reference/`.
- Materialize specific portfolio shapes only when they have distinct selection evidence or reader value.

## Validation

- Role names are not mapped to models without evidence.
- The detailed role contracts remain reproducible from canonical inputs after the legacy `agent-role-selection` page is removed.
- Independence requirements are explicit where material.
- Worker self-report, reviewer prose, or model confidence is not substituted for deterministic evidence when deterministic validation exists.
- Role-specific failure modes and evaluation signals are retained without presenting them as universal performance claims about any model.
- The page does not duplicate generic orchestration mechanics unrelated to choosing models for roles.
