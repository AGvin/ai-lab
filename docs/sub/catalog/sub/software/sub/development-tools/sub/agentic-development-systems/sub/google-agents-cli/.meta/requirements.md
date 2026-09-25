# Documentation Requirements

## Requirements

- Identify Google Agents CLI (`agents-cli`) as Google's released development CLI and bundled-skill system for scaffolding, evaluating, deploying, governing, and optimizing agents on Gemini Enterprise Agent Platform / Google Cloud.
- Preserve its primary identity as developer tooling that augments coding assistants with agent-development commands and skills; do not classify it as an autonomous coding agent, hosted agent platform, or duplicate identity for Google ADK.
- Keep bundled skills as part of the CLI/tooling distribution unless an independently durable collection identity is explicitly selected; the separate `Google Agent Skills` collection remains the broader official repository-backed skill collection.
- Keep Agent Platform, ADK, Cloud Run, Agent Runtime, Agent Gateway, Agent Registry, Terraform, and supported external coding assistants as separate dependencies/integrations rather than parts of the CLI's producer identity.
- Treat release versions, default models, supported deployment targets, command/extension inventory, bundled skill contents, platform feature support, and compatibility requirements as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains installable developer tooling rather than a hosted service or model.
- GA status is grounded in the 1.0.0 release note and later version numbers do not imply a new canonical identity.
- Producer provenance resolves to Google.
