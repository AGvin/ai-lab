# Documentation Requirements

## Requirements

- Identify W&B Weave as the Weights & Biases product for tracing, observing, and evaluating AI applications and agents.
- Cover traces, datasets, scorers/evaluations, experiments, agent trajectories, and OpenTelemetry/integration surfaces only when current documentation supports them.
- Distinguish Weave from the broader W&B Models/MLOps product family; integrations do not make those products one canonical entity.
- Render the standard `entity-relations` block and preserve `produced-by` Weights & Biases, Inc., reciprocated by `produces`; keep CoreWeave's corporate ownership on the producer layer rather than attributing direct Weave production to CoreWeave.
- Document hosted and self-managed availability as deployment modes of the same Weave product when current W&B documentation supports that boundary.
- Keep SDK languages, supported integrations, deployment options, and plan constraints freshness-sensitive.

- Preserve the lifecycle boundary reviewed on 2026-10-17: Weave documentation names CoreWeave Agent Lens as its successor and states that agent-tracing workflows and data are available in both. Do not infer universal SDK/feature migration or create a duplicate identity without separate intake.
- Distinguish the documented shared agent-tracing data destination from unsupported claims about universal SDK or feature migration; preserve the original Weights & Biases provenance.

## Validation

- The canonical product name is W&B Weave rather than a vague generic `Weights & Biases` evaluation-platform entry.
- Weave is not described as the runtime that executes or sandboxes the evaluated agent.
