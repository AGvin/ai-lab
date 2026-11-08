# Claude API

Claude API is Anthropic's directly operated hosted developer service for programmatic use of Claude models. It exposes the Messages API and related facilities such as batching, token counting, model discovery, files and supported tools. [Anthropic API overview](https://platform.claude.com/docs/en/api/overview).

## Service and product boundaries

The API is not itself a Claude trained-model family or the consumer Claude application. Anthropic's managed agents platform, Claude Code, client SDKs, Agent SDK and Console are adjacent product or tool surfaces rather than interchangeable service identities. Model access through Amazon Bedrock, Vertex AI or another provider does not change the original Anthropic model producer.

## Integration and safety boundaries

Check the current API version headers, optional beta headers, model IDs, authentication and workspace permissions, tool availability, message and file retention, pricing, rate limits and deprecations. A beta API or cloud-provider-compatible route need not offer the same features or authorization as the direct stable API. External tool invocation and data forwarding require separate application controls. [API HTTP guidance](https://platform.claude.com/docs/en/api/http).

## Relations

- Produced by [Anthropic](../../../../../producers/sub/a/sub/anthropic/).

## Official resources

- [Claude API documentation](https://platform.claude.com/docs/en/api/overview)
- [Claude API HTTP guidance](https://platform.claude.com/docs/en/api/http)
- [Anthropic platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
