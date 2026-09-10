# Documentation Requirements

## Requirements

- Identify Inngest as an event-driven durable-execution platform for reliable background jobs, multi-step functions, scheduled work, and application workflows.
- Preserve its primary placement under `workflow-engines/application-orchestration`; event triggers and durable steps coordinate application code rather than acting as a data-pipeline-only scheduler.
- Preserve Inngest Inc as the company behind the platform while keeping the canonical self-hostable software identity distinct from the managed Inngest service.
- Preserve the boundary that user functions execute on application/user compute while Inngest coordinates their workflow execution; self-hosting and managed Inngest service are separate operating modes.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep SDK/runtime support, execution guarantees, hosting architecture, concurrency controls, and other mutable details source-backed when expanded.
- Include current official Inngest documentation, repository, legal, and open-source history references.

## Validation

- The page distinguishes orchestration from the user compute that runs application functions.
- Inngest Inc is not conflated with the self-hosted software or managed service surface.
- Managed and self-hosted operating boundaries are not conflated.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
