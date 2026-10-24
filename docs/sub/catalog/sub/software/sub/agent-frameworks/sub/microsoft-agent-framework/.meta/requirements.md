# Documentation Requirements

## Requirements

- Identify Microsoft Agent Framework as the canonical software profile for Microsoft's open-source agent framework represented at this path.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Cover agents, opinionated Harness Agents, and explicit functional/graph workflows as distinct framework surfaces, with providers, MCP/A2A interop, context providers, middleware and session state grounded in current primary docs.
- Record Microsoft Agent Framework 1.0 as a production-ready successor to AutoGen and Semantic Kernel while distinguishing stable .NET/Python SDKs from Go SDK public preview and its narrower feature coverage; package versions and preview tiers are freshness-sensitive.
- Distinguish the self-managed SDK/framework from optionally Microsoft-managed Foundry Hosted Agents or other model/agent services; hosting choices do not create separate framework identities.
- Include official Microsoft Learn documentation and repository references.
- Preserve current migration relationships from AutoGen and Semantic Kernel only as source-backed migration guidance, not as identity equivalence; migration may change agent turns, orchestrator behavior, tool schemas, and supported distributed features.
- Explain workflow checkpoints as opt-in state persistence, not automatic crash recovery: persist a supported storage backend, maintain compatible executor identities and topology when restoring, and guard saved state, pending requests and tool approvals as sensitive material. Durable/shared production storage differs from ephemeral in-memory/local-disk setups.
- Explicitly distinguish approval-required tools from ordinary tool functions, and document how request/response-based human-in-the-loop pauses and resumes interact with saved workflow state; custom handlers must enforce authorization for sensitive actions instead of treating a model request or approval middleware as universal permission.
- Keep workflow language/API differences source-backed: Python has an experimental functional workflow API in addition to graphs; .NET and Go use graph-based workflow builders, and Go's package preview status does not imply parity with stable .NET/Python components. Recheck current checkpoint schema/version compatibility before claiming replays will work across upgrades.

## Validation

- Official resource links match canonical entity metadata.
- The page does not conflate Microsoft Agent Framework with Semantic Kernel, AutoGen, Microsoft Foundry Agent Service, or a hosted model API.
- Public-preview language SDK capabilities are not generalized into stable production guarantees across all languages.
- The page contains no temporary-placeholder wording.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
