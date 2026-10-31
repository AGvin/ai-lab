# Documentation Requirements

## Requirements

- Identify ZenML as an open-source MLOps/AI framework for developing, evaluating, deploying, and operating pipelines and AI systems across classical ML, LLM, and agent workloads.
- Preserve its primary placement under `model-and-data-platforms/lifecycle-platforms`; pipelines, stacks, infrastructure/tool integrations, artifacts, models, and deployments form the ZenML lifecycle framework.
- Keep Kitaru, the separately documented agent-evaluation and improvement project, distinct from the ZenML framework.
- Preserve ZenML GmbH as the company that creates and maintains the open-source ZenML project.
- Preserve stack separation as a core architectural concept: pipeline code describes work while stack components determine where and how it runs.
- Distinguish open-source ZenML capabilities from ZenML Pro/Cloud features such as commercial visual management surfaces.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve the Python package analytics boundary: anonymized usage analytics are enabled by default and can be disabled with `zenml analytics opt-out`.
- Keep stack components, Pro feature boundaries, model-control features, integrations, and other mutable details source-backed when expanded.
- Include current official ZenML documentation, repository, and company references.

## Validation

- ZenML supports ML and LLM pipelines without treating Kitaru's separate agent lifecycle as an inseparable ZenML feature.
- ZenML GmbH's producer/maintenance role does not collapse the open-source project and commercial Pro/Cloud surfaces.
- Open-source and Pro/Cloud capabilities are not conflated.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
