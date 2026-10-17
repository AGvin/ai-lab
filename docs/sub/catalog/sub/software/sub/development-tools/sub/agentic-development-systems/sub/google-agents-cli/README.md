# Google Agents CLI

Google Agents CLI (`agents-cli`) is Google's released development CLI and bundled-skill system for scaffolding, evaluating, deploying, governing, and optimizing agents on Gemini Enterprise Agent Platform / Google Cloud.

## Scope and boundaries

- The profile preserves its primary identity as developer tooling that augments coding assistants with agent-development commands and skills; do not classify it as an autonomous coding agent, hosted agent platform, or duplicate identity for Google ADK.
- The profile keeps bundled skills as part of the CLI/tooling distribution unless an independently durable collection identity is explicitly selected; the separate `Google Agent Skills` collection remains the broader official repository-backed skill collection.
- The profile keeps Agent Platform, ADK, Cloud Run, Agent Runtime, Agent Gateway, Agent Registry, Terraform, and supported external coding assistants as separate dependencies/integrations rather than parts of the CLI's producer identity.
- The profile treats release versions, default models, supported deployment targets, command/extension inventory, bundled skill contents, platform feature support, and compatibility requirements as freshness-sensitive.

## Relations

- Produced by: [`catalog/producers/g/google`](../../../../../../../producers/sub/g/sub/google/)

## Official resources

- <https://github.com/google/agents-cli>
- <https://github.com/google/agents-cli/blob/main/RELEASE_NOTES.md>
