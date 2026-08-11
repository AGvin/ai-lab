# Model Teams

Choose a model portfolio only when role separation, routing, specialization, or independent evaluation produces a measurable benefit over one model.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Team-design boundary

Model-team selection covers role-based portfolios, model routing, and ensembles or consensus. Start with the smallest portfolio that can meet the complete workflow acceptance criteria.

The same model may cover several compatible roles when doing so does not create unacceptable conflicts, correlated failure, quality loss, latency, or cost. Add a specialist or independent model only when the measured gain justifies the additional model calls, context transfer, routing, review, and maintenance complexity.

This subtree selects **models and their roles**. GPU placement, concurrent/sequential loading, runtime lifecycle, cloud resource startup/shutdown, service topology, hardware purchasing, and environment-profile design are broader deployment/operations decisions and remain outside model-selection ownership.

## Portfolio topologies

Treat the simplest valid topology as the baseline and add complexity only when evidence requires it.

### Single generalist

One model covers all validated roles or compatible tasks. Prefer this baseline when it meets every required acceptance threshold and role-independence requirement. Reject it when a material task exceeds its verified quality ceiling or when independent review cannot credibly be performed by the same model/configuration.

### Generalist with specialist fallback

A generalist handles routine assignments while an exact specialist handles declared gaps. Use this only when the fallback trigger can be defined and tested. The worker's self-assessment alone is not a reliable escalation policy; deterministic evidence, an independent verifier, or explicit task rules may be required.

### Router with quality tiers

A router assigns work among lower-cost, standard, or stronger models according to explicit task/risk/quality conditions. Evaluate routing accuracy independently because misrouting and excessive escalation can erase the expected quality or cost benefit.

### Specialist team

Use distinct models for materially different tasks or roles when specialist quality or independence exceeds the simpler baseline by enough to justify the additional coordination cost. Do not create a specialist role merely because a specialized model exists.

### Ensemble or consensus

Use multiple independent candidates or judges only when disagreement handling or reduced correlated error materially improves the target decision. Diversity of model names is not sufficient evidence of independence; shared training lineage, provider stack, prompt context, or evaluation bias can still correlate failures.

## Current materialized guidance

- [`role-based-portfolios/`](./sub/role-based-portfolios/) — choose models by planner, worker, reviewer, verifier, evaluator, advisor, memory/context, and related role contracts.

Routing and ensemble branches are materialized only when reviewed task content requires them; the selected navigation is not created as an empty skeleton.

## Escalation and verification

Define bounded retries, escalation conditions, and terminal acceptance before execution. Escalate when repeated failures indicate a capability gap, an important requirement is repeatedly omitted, the expected retry/review cost exceeds a stronger route, or the task risk exceeds the current model's verified reliability.

Do not let the producing model be the only approver of its own output when independent verification is material. Depending on the assignment, verification may use deterministic tests, a separate reviewer/verifier model, a specialist evaluator, explicit acceptance criteria, artifact diffs/regression checks, or human approval.

A fallback model must satisfy the same relevant acceptance and data-boundary requirements as the primary route; being stronger or more expensive does not automatically make it a valid fallback.

## Portfolio evidence

Evaluate terminal workflow acceptance, role coverage, correlated errors, role independence, handoff quality, retries, escalation frequency, routing mistakes, model-call latency, review effort, and total cost per accepted result. Compare the proposed team against a single-generalist baseline rather than assuming more models improve quality.

Record exact participating model identities and evaluated roles. Link canonical facts for every participating model from [Model Reference](../../../reference/) rather than copying technical profiles here.

Operational residency and infrastructure metrics may be recorded as **evidence conditions** when they materially affect a model-team comparison, but selecting runtimes, GPU schedules, provider resources, or lifecycle automation belongs outside this subtree.
