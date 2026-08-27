# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Plugins` and make this the learning entrypoint for understanding, adopting, creating, testing, publishing, updating, and removing host/ecosystem extension bundles commonly called plugins.
- Explain that `plugin` is not one universal AI package contract: different hosts may bundle skills, agents/commands, hooks, MCP/connectors, executable code, configuration, UI metadata, or other components under different manifests/runtime models.
- Distinguish Plugins from standalone Agent Skills and MCP. A plugin can bundle either, but a portable skill or protocol integration does not require plugin packaging.
- Make `using-ai-plugins/` and `creating-ai-plugins/` visible as the current source-backed learning children.
- Keep formal Agent Plugin/vendor manifest/schema requirements with selected/future specification owners; learning pages source current platform contracts rather than universalizing one host.
- Keep concrete plugins, versions, publishers, marketplaces, install commands, host support, compatibility, permissions, and current runtime behavior catalog/platform/evidence-owned and freshness-bound.
- Treat plugin installation/update as a supply-chain and execution-boundary decision because Markdown instructions, hooks, executable code, MCP, connectors, telemetry, and credentials can all change behavior.

## Validation

- The learning root does not assert one universal plugin manifest or marketplace.
- Readers can distinguish when a standalone skill is sufficient from when host-specific plugin packaging is justified.
- Standard navigation exposes only current materialized tutorials.
