# Documentation Requirements

## Requirements

- Identify DBOS as a multi-language open-source durable-execution library family for making ordinary application code resilient through Postgres-backed workflows, steps, queues, scheduling, and related reliability primitives.
- Preserve its primary placement under `workflow-engines/application-orchestration`; DBOS adds durable execution inside application code rather than requiring a separate external workflow-orchestrator service.
- Preserve DBOS, Inc. as the company behind the DBOS software family while keeping the company, self-managed libraries, and hosted DBOS services as distinct identity/operation layers.
- Preserve the current multi-language product boundary across Python, TypeScript, Go, and Java rather than treating one language repository as the entire canonical DBOS identity.
- Distinguish self-managed DBOS libraries from DBOS Cloud and other separately operated service surfaces.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep language-specific APIs, exactly-once semantics, deployment features, and other mutable implementation details source-backed when expanded.
- Include current official DBOS site, documentation, legal, and product-history references.

## Validation

- The page describes DBOS as a library-based durable-execution family rather than a single-language package.
- DBOS, Inc. is not conflated with the software entity or with DBOS Cloud.
- Local/self-managed libraries and DBOS Cloud are not conflated.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
