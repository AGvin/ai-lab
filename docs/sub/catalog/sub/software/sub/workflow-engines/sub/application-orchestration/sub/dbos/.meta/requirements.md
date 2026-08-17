# Documentation Requirements

## Requirements

- Identify DBOS as a multi-language open-source durable-execution library family for making ordinary application code resilient through Postgres-backed workflows, steps, queues, scheduling, and related reliability primitives.
- Preserve its primary placement under `workflow-engines/application-orchestration`; DBOS adds durable execution inside application code rather than requiring a separate external workflow-orchestrator service.
- Preserve the current multi-language product boundary across Python, TypeScript, Go, and Java rather than treating one language repository as the entire canonical DBOS identity.
- Distinguish self-managed DBOS libraries from DBOS Cloud and other separately operated service surfaces.
- Keep language-specific APIs, exactly-once semantics, deployment features, and other mutable implementation details source-backed when expanded.
- Include current official DBOS site and documentation references.

## Validation

- The page describes DBOS as a library-based durable-execution family rather than a single-language package.
- Local/self-managed libraries and DBOS Cloud are not conflated.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
