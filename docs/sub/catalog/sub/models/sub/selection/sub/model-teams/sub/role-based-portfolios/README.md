# Models for Different Roles

Choose models for roles inside an agentic or multi-model system by the role contract, required independence, failure severity, and measured workflow benefit.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Role as contract

For each role define responsibilities, required capabilities, allowed tools and data, failure boundaries, verification requirements, retry and escalation behavior, and completion criteria before choosing a model.

Common roles include orchestrator, planner, router, worker, reviewer, verifier, evaluator or judge, advisor, memory manager, and context manager. The role name does not determine a specific model; test the behavior required by that role.

## Consolidate or separate

One model may cover several compatible roles when the workflow is simple, independence is not required, and the combined role meets all quality targets with lower cost or latency.

Treat worker-plus-verifier, worker-plus-final-reviewer, router-plus-sole-routing-evaluator, memory-writer-plus-sole-memory-checker, and similar self-approval combinations cautiously. Separate models or add deterministic/human evidence when failure severity, audit independence, adversarial review, specialization, or materially different latency/context/resource needs justify it.

## Selection evidence

Evaluate role-specific behavior rather than one aggregate benchmark. Depending on role, measure decomposition and constraint retention, routing accuracy, tool discipline, accepted-result rate, defect recall and false positives, unsupported approvals, calibration, state/context retention, privacy behavior, retry limits, and escalation quality.

Document the exact model/version/artifact, role, quality tier, failure severity, context, tools/permissions, known failure modes, verification method, retry limit, escalation target, independence requirements, latency/resource profile, evidence, and verification date.

Link model facts from [Model Reference](../../../../../reference/). More specific portfolio-shape pages are materialized only when their selection evidence differs enough to justify a dedicated node.
