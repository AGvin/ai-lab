# Documentation Requirements

## Requirements

- Identify E2B as a producer-operated cloud sandbox service that gives AI agents isolated Linux execution environments for files, commands, code, and application workloads.
- Preserve the service classification because normal operation depends on E2B-operated sandbox infrastructure/control-plane APIs even though SDKs and repository code are publicly available.
- Treat the core sandbox identity separately from individual beta-only SDK surfaces. Do not generalize `betaCreate`, pause/resume, MCP, persistence, regional, or other explicitly beta behavior into the stable service contract.
- Render the standard `entity-relations` block from validated current-entity relations and preserve E2B as the producer.
- Treat sandbox limits, regions, lifecycle controls, templates, SDK versions, pricing, network behavior, persistence, and integration support as mutable facts requiring current first-party verification.
- Explain that sandbox isolation reduces risk but does not remove the caller's responsibility for credentials, secrets, sensitive data, network access, side effects, resource limits, and authorization when executing untrusted or agent-generated code.
- Include current official E2B site, documentation, and repository references.

## Validation

- E2B is presented as hosted agent/application execution infrastructure rather than a local agent framework or generic sandboxing concept.
- Explicitly beta API surfaces are not represented as stable service guarantees.
- The `produces` / `produced-by` relation pair is materially consistent.
- Safe-use boundaries remain explicit for agent-generated or untrusted code execution.

## Scoped original-source qualification — 2026-11-06

- E2B's first-party service supplies isolated cloud Linux microVM/sandbox execution via a managed API, with code-interpreter and desktop/computer-use products as supported SDK/runtime surfaces. An E2B SDK or open repository does not make the hosted infrastructure automatically self-operated, nor remove untrusted-code execution risk.
- The E2B product updates dated October–November 2026 distinguish recently added pause modes, filesystem-only snapshots, network/DNS controls, idempotent creation and streaming uploads. Version/region/SDK-specific availability, persistence, pricing and quotas are mutable, not universal or retroactive stable guarantees.
- Protect injected credentials and egress destinations; use least-privilege policies, capture outputs outside sandboxes before destruction where needed, and verify retention/contract boundaries before running sensitive agent workloads.
- Verified first-party source 1: https://e2b.dev/
- Verified first-party source 2: https://e2b.dev/product-updates
- Verified first-party source 3: https://e2b.dev/docs
- Acceptance scope: present hosted infrastructure identity and publisher-documented feature/version boundaries only. No model/runtime execution, complete freshness, independent security/legal review, rights clearance, root-wide schema/cache/CI/render, clean pass, final-delivery or merge credit.
