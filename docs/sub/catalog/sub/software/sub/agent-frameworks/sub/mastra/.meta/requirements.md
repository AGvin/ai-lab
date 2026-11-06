# Documentation Requirements

## Requirements

- Identify Mastra as the canonical software profile for the TypeScript agent/application framework represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Describe its agent-building role and keep tools, workflows, memory, workspaces, model routing, evaluation, and deployment capabilities source-backed when expanded.
- Include the official Mastra website reference.
- Distinguish Mastra's open-ended tool-using agents from typed, graph-based workflows with explicit branches/retries and suspend/resume. Memory, model routing, Studio, hosted cloud, and workspaces are different optional surfaces, not mandatory components of every agent deployment.
- Document the concrete sandbox trust boundary: `LocalSandbox` invokes shell commands on the application host by default and is **not isolated**; enable supported native isolation (macOS Seatbelt, Linux Bubblewrap) or an appropriately restricted remote/container executor for untrusted code. Enforce network/filesystem/tool permissions and human approvals separately.
- Workspaces with a static sandbox are shared across requests unless the application scopes them; for multi-user/thread scenarios configure per-resource sandbox resolvers and cache keys, and explicitly destroy resolver-owned environments and revoke access when users or threads end.
- Preserve Mastra's mixed license boundary: most framework code is Apache-2.0, while source under `ee/` is subject to a separate Mastra Enterprise License. Do not generalize open-source redistribution/production rights to enterprise-only features; confirm current exact package rights before deployment.

## Validation

- The official resource link matches canonical entity metadata.
- The page remains a concrete TypeScript framework profile.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
