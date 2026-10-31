# Documentation Requirements

## Requirements

- Identify Restate as a source-available durable application runtime for resilient services, workflows, stateful functions, and AI-agent/application backends.
- Preserve its primary placement under `workflow-engines/application-orchestration`; durable execution, persisted state, timers, and reliable communication form an application-runtime layer rather than a data scheduler.
- Preserve Restate GmbH as the company behind the project while keeping the company, self-managed runtime, and Restate Cloud as distinct identity/operation layers.
- Preserve the distinction between Restate's runtime/service model and library-only durable execution such as DBOS.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep SDK support, deployment topology, durability semantics, cloud offerings, and other mutable implementation details source-backed when expanded.
- Include current official Restate documentation, repository, legal, and project-history references.

- State the current runtime licensing boundary: Business Source License 1.1 with an additional use grant permits internal production and the documented application abstractions while restricting the defined Public Restate Platform Service; each release changes to Apache 2.0 four years after release. MIT-licensed SDKs are a separate licensing surface.
- Distinguish customer-operated self-hosting from vendor-operated Restate Cloud and BYOC deployments; locating a BYOC deployment in customer infrastructure does not make its operation customer-managed.

## Validation

- The page presents Restate as a durable application runtime, not a model provider or generic data pipeline tool.
- Restate GmbH is not conflated with either the self-managed runtime or hosted service surface.
- Hosted and self-managed Restate operation are not conflated when expanded.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
