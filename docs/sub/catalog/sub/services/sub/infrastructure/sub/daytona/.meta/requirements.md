# Documentation Requirements

## Requirements

- Present Daytona as producer-operated secure sandbox/composable-computer infrastructure for running AI-generated code and agent workloads in isolated environments.
- Cover programmatic sandbox lifecycle, code execution, filesystem/process access, networking, snapshots or persistent state, and agent-framework integrations only where current first-party documentation supports them.
- Keep Daytona distinct from ordinary developer IDE/workspace products when its primary catalog value is isolated runtime infrastructure for agents and code execution.
- Do not infer arbitrary security guarantees beyond the isolation and control properties documented by Daytona.
- Treat runtime limits, regions, supported resources, persistence behavior, pricing, and quotas as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Classification reflects sandbox/runtime infrastructure rather than generic development tooling.
- Security claims remain source-bounded.
- Producer provenance resolves to Daytona Platforms Inc.

## Scoped original-source qualification — 2026-11-06

- Daytona documents cloud sandbox lifecycles, execution, snapshots and independent storage, but persistence differs substantially by sandbox class: container stop/start preserves filesystem but not memory, supported VMs can pause/resume memory, and GPU sandboxes are ephemeral and need separately mounted volumes for retained results.
- Do not collapse Daytona v2 alpha documentation into the latest stable v0 API: the v2 docs explicitly describe an alpha surface with different lifecycle and state guarantees. Snapshot, fork, networking, resource class, timeout, billing and host failure semantics must be scoped to the exact documented version and sandbox type.
- Sandbox isolation is not independently verified resistance against hostile code; agent-produced commands, external access, credentials, retention and egress remain the customer's operational responsibility.
- Verified first-party source 1: https://www.daytona.io/docs/en/persistence/
- Verified first-party source 2: https://www.daytona.io/docs/en/v2/persistence/
- Verified first-party source 3: https://www.daytona.io/docs/en/troubleshooting/
- Acceptance scope: present hosted infrastructure identity and publisher-documented feature/version boundaries only. No model/runtime execution, complete freshness, independent security/legal review, rights clearance, root-wide schema/cache/CI/render, clean pass, final-delivery or merge credit.
