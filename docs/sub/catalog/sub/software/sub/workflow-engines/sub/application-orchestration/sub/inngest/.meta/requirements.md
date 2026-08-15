# Documentation Requirements

## Requirements

- Identify Inngest as an event-driven durable-execution platform for reliable background jobs, multi-step functions, scheduled work, and application workflows.
- Preserve its primary placement under `workflow-engines/application-orchestration`; event triggers and durable steps coordinate application code rather than acting as a data-pipeline-only scheduler.
- Preserve the boundary that user functions execute on application/user compute while Inngest coordinates their workflow execution; self-hosting and managed Inngest service are separate operating modes.
- Keep SDK/runtime support, execution guarantees, hosting architecture, concurrency controls, and other mutable details source-backed when expanded.
- Include current official Inngest documentation and repository references.

## Validation

- The page distinguishes orchestration from the user compute that runs application functions.
- Managed and self-hosted operating boundaries are not conflated.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
