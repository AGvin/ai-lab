# Documentation Requirements

## Requirements

- Identify **Nebius Token Factory** as the current name of hosted Nebius AI Studio API, preserving the frozen canonical slug `nebius-ai-studio` solely for identity continuity. The 2025 transition does not create an additional product or require a second accepted candidate.
- Support current OpenAI-compatible API base `https://api.tokenfactory.nebius.com/v1/` and bearer token authentication from the [first-party quickstart](https://docs.tokenfactory.nebius.com/quickstart) and [API introduction](https://docs.tokenfactory.nebius.com/api-reference/introduction).
- Describe cloud-hosted inference and supported dedicated deployment, post-training and observability as vendor product capabilities with distinct eligibility and costs, not a guaranteed included self-hosted API package.
- Keep chosen model, exact endpoint, terms, GPU/dedicated deployment, pricing and retention scoped to the particular account and current docs. Do not assume that third-party models served by Nebius become Nebius-owned models.
- Never expose `NEBIUS_API_KEY` in a browser or repository. Protect prompts and uploaded fine-tuning data, obtain lawful input/data rights and confirm provider agreements, region and retention before deploying.
- Record historical name provenance from the [official announcement](https://nebius.com/newsroom/nebius-launches-nebius-token-factory-to-deliver-production-ai-inference-at-scale); the old name is an alias and not a second live API.
- Preserve reciprocal `produced-by` / `produces` linkage to Nebius; index one Model APIs identity. Avoid claims of a live API request, paid usage, performance/freshness audit, full CI or whole-catalog clean pass.

## Validation

- Producer inverse, Model APIs index and documentation links resolve.
- Historical/current naming, API URL, authentication and original model-publisher boundaries are explicit.
