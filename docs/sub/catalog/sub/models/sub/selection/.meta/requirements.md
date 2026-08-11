# Documentation Requirements

## Requirements

- Present model selection as task-oriented decision support using the natural-intent test `I want a model to <task>`.
- Materialize only task areas that have real reviewed content; do not create the complete selected skeleton preemptively.
- Link canonical model facts from `../reference/` instead of duplicating full model descriptions.
- Require concrete recommendations to identify exact model/version/artifact scope, acceptance criteria, evidence basis, material deployment assumptions, and trade-offs.
- Define the assignment before candidate choice, including relevant input/output contract, quality target, failure severity, modalities, privacy/data boundary, latency or throughput requirement, budget, and model-specific access/deployment conditions when they affect the decision.
- Compare exact model/version/artifact identities rather than vague family names when exact identity materially affects behavior or operation.
- Treat derived artifacts as separate evaluated selection units only when their behavior or operating constraints materially differ, while preserving their relationship to the base model.
- Use deterministic validators before model judgment when they directly prove an acceptance property.
- Keep provider-documented claims distinct from independent AI Lab task evidence.
- Preserve explicit evidence states such as provider-documented, AI Lab tested, external benchmark, community report, inference, and untested; keep conflicting evidence visible.
- Do not collapse recommendation, evidence, deployment context, classification, price, benchmark, or reliability outcomes into one unsupported aggregate score.
- Use recommendation labels only as task- and evidence-bounded conclusions, never as intrinsic model properties.
- Evaluate terminal acceptance and workload-specific failure modes rather than selecting from parameter count, one benchmark, token price, or provider positioning alone.
- Treat reliability as an assignment-specific profile bound to exact model/version/artifact or hosted snapshot, bounded task class, quality tier, representative input distribution, acceptance criteria, verification design, and behavior-affecting runtime/hosted conditions.
- Require separate reliability evidence when material profile conditions change; do not transfer reliability across quantizations, hosted/local routes, unrelated task classes, or quality tiers without evidence.
- Preserve observable reliability dimensions when relevant: strengths, recurring failure signatures, omitted-requirement risk, premature-completion risk, correction behavior, useful retry count, quality ceiling, unsuitable tasks, failure-severity limits, and required independent validation.
- Treat worker self-report as insufficient proof of terminal acceptance when artifacts, deterministic checks, tool results, provider state, or independent QC can verify the claim.
- Treat repeated materially similar failures after targeted correction as possible capability-gap evidence rather than justification for unlimited retries.
- Keep model-team escalation logic under `model-teams/`; keep infrastructure retry/backoff, provider failover, GPU/runtime degraded operation, and service recovery outside model-selection ownership.
- Compare cost per accepted result, including material retries and verification/reviewer calls, rather than isolated request price or raw inference speed.
- Require material recommendations to record evaluation date, exact evaluated identity, relevant runtime/hosted conditions, prompt/tool/context assumptions, limitations, conflicting evidence, and re-evaluation triggers.
- Require mutable pricing, availability, hosted features, limits, aliases, and provider terms to be rechecked when they materially affect the decision.
- Keep broader software/service/hardware/runtime/deployment/operations selection outside this subtree when the decision is not model-specific.
- Treat legacy model-selection pages as recycling input rather than destination-preserving migration source.
- Keep practical user-scenario material outside the current migration scope.

## Validation

- Every materialized child corresponds to an approved destination in the selected model-selection target tree.
- Selection pages do not become alternate sources of canonical model identity or technical facts.
- Provider claims are not presented as independent AI Lab benchmark evidence.
- Recommendation and reliability labels are scoped to explicit task, conditions, constraints, and evidence.
- Worker self-assessment is not used as sole completion evidence when independent validation is material.
- No broad infrastructure lifecycle, failover architecture, or solution-architecture guide is migrated into model selection merely because models are components.
- No practical user-scenario page is created, moved, or rewritten by this migration.
