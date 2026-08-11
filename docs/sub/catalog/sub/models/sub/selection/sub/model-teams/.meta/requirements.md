# Documentation Requirements

## Requirements

- Define model-team selection around measurable workflow benefit rather than an assumption that more models are better.
- Cover the selected conceptual areas: role-based portfolios, routing portfolios, and ensembles/consensus, but materialize only reviewed branches with real content.
- Require comparison against a simpler single-model baseline when practical.
- Preserve portfolio-topology guidance for single generalist, generalist plus specialist fallback, quality-tier routing, specialist teams, and ensemble/consensus when the choice is specifically about models and their roles.
- Require specialists or additional models to justify their coordination/review cost through measured quality, independence, task coverage, or accepted-result benefit.
- Require fallback and escalation triggers to be explicit and testable rather than depending only on worker self-assessment.
- Evaluate routing quality separately when a router chooses among model tiers or specialists.
- Require independent verification when the producing model cannot credibly be the sole approver for the stated assignment.
- Require bounded retry and escalation logic for repeated capability failures or when expected retry/review cost exceeds a stronger valid route.
- Require workflow evidence for acceptance, correlated errors, independence, handoffs, retries, escalation frequency, routing errors, model-call latency, review effort, and cost per accepted result when relevant.
- Treat shared lineage/provider/context as possible sources of correlated error; do not assume different model names imply independent judgment.
- Require fallback models to satisfy the relevant acceptance and data-boundary requirements rather than assuming a stronger model is automatically valid.
- Link the currently materialized `role-based-portfolios/` guidance.
- Link every participating model to canonical reference facts instead of duplicating profiles.
- Keep GPU placement, concurrent/sequential loading design, runtime/service lifecycle, cloud resource startup/shutdown, hardware selection, and environment-profile architecture outside model-selection ownership.
- Allow operational residency/infrastructure metrics only as evidence conditions when they materially affect a model-team comparison.

## Validation

- Empty routing or ensemble skeletons are not created merely because they exist in the selected conceptual tree.
- Specialist roles require a documented benefit or independence need.
- Team complexity, routing errors, retries, and verification cost are included in the decision.
- Worker self-assessment is not the sole fallback/escalation mechanism when independent evidence is material.
- Infrastructure lifecycle and environment design are not migrated into this subtree.
