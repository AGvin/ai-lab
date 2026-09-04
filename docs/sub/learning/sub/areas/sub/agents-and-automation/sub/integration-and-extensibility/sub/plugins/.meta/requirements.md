# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Plugins` and make this the learning entrypoint for understanding, adopting, creating, testing, publishing, updating, and removing host/ecosystem extension bundles commonly called plugins.
- Explain that `plugin` is not one universal AI package contract: different hosts may bundle skills, agents/commands, hooks, MCP/connectors, executable code, configuration, UI metadata, or other components under different manifests/runtime models.
- Distinguish Plugins from standalone Agent Skills and MCP. A plugin can bundle either, but a portable skill or protocol integration does not require plugin packaging.
- Make `using-ai-plugins/` and `creating-ai-plugins/` visible as the current source-backed learning children.
- Teach the practical decision boundary between a standalone skill and a plugin: prefer a standalone portable skill when instructions/resources are sufficient; use plugin packaging when managed distribution/versioning, multiple bundled capabilities, host-specific hooks/agents/connectors/UI, namespacing, organization policy, or marketplace lifecycle is materially required.
- Teach plugin lifecycle as distinct stages rather than treating installation as successful operation: discovery, review, installation/presence, enablement/loading, execution, update, disablement/removal, and cleanup/revocation can each have different success, failure, and authorization states.
- Explain that removal may leave copied skills, generated configuration, cached dependencies, running processes, MCP registrations, connector authorizations, credentials, or external side effects; cleanup and credential revocation therefore require explicit verification where applicable.
- Teach plugin composition risks: multiple plugins can collide in names, commands, agents, hooks, tools, environment variables, MCP registrations, configuration, instructions, or event ordering, so users/builders should understand the host's precedence/conflict behavior rather than assuming independent composition.
- Teach review and least-privilege practice for consequential plugins. Review publisher/source identity, version/update channel, complete package/manifest/module contents, skills/instructions, hooks/commands, dependencies, MCP/network destinations, connector scopes, filesystem/shell access, credentials/secrets, telemetry/external assets, approval gates, and uninstall behavior according to risk.
- Explain that marketplace presence, publisher identity, signatures, ratings, popularity, or structural/spec conformance can improve provenance and reviewability but do not prove safety, correctness, suitability, or appropriate permissions.
- Treat updates as behavior changes: instructions, executable code, dependencies, hooks, endpoints, component definitions, permissions, or activation behavior can change while the plugin name remains stable; consequential workflows should inspect/pin revisions when justified.
- Teach a portability strategy for multi-host projects: keep genuinely portable skills and independently deployable integrations in neutral source boundaries where practical, then add thin host-specific adapters rather than assuming one host's plugin directory/manifest is portable.
- Keep formal Agent Plugin/vendor manifest/schema requirements with selected/future specification owners; learning pages source current platform contracts rather than universalizing one host.
- Keep concrete plugins, versions, publishers, marketplaces, install commands, host support, compatibility, permissions, and current runtime behavior catalog/platform/evidence-owned and freshness-bound.
- Treat plugin installation/update as a supply-chain and execution-boundary decision because Markdown instructions, hooks, executable code, MCP, connectors, telemetry, credentials, and external services can all change model behavior, data flow, or side effects.

## Validation

- The learning root does not assert one universal plugin manifest or marketplace.
- Readers can distinguish when a standalone skill is sufficient from when host-specific plugin packaging is justified.
- Plugin presence, enablement, execution, update, removal, and cleanup are not collapsed into one state.
- Security guidance distinguishes provenance evidence from trust and keeps host/user authorization authoritative over plugin-declared behavior.
- Transferable lifecycle, composition, review, and portability guidance does not freeze mutable vendor commands, paths, manifests, support matrices, or marketplace behavior.
- Standard navigation exposes only current materialized tutorials.
