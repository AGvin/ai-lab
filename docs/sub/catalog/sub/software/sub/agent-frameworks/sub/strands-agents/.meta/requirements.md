# Documentation Requirements

## Requirements

- Identify Strands Agents as the canonical software profile for the open-source agent SDK represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Preserve current AWS provenance without treating individual AWS hosting or model services as part of the Strands software identity.
- Keep current Python and TypeScript language support, model-provider support, tools, memory, evaluation, deployment, and multi-agent capabilities source-backed when expanded.
- Anchor current source ownership to `strands-agents/harness-sdk` monorepo, which unifies Python and TypeScript SDKs, separately packaged assembled harnesses, CLI, MCP and documentation. Older `strands-agents/sdk-typescript` was archived on 2026-06-03 and must not be treated as the live TypeScript source.
- Distinguish self-hosted library/runtime (agent loop running in the user's process) from optional remote model and cloud infrastructure providers; the SDK and preassembled harness are not a vendor-managed agent-hosting service.
- Preserve the difference between lower-level `strands-agents` / `@strands-agents/sdk` and assembled `strands-harness` / `@strands-agents/harness` packages as installable components within the Strands product family, not automatically separate canonical service identities.
- Explain operational trust boundaries for tool code execution, MCP connections, external models, filesystem/network access, sandbox policies, credentials and human-intervention safeguards.
- Include the official Strands Agents website/documentation, current monorepo, and official changelog references.

## Validation

- The official resource link matches canonical entity metadata.
- Language-support and monorepo claims remain synchronized with current upstream documentation; independent Python/TypeScript versions are time-scoped, not fixed in product identity.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
