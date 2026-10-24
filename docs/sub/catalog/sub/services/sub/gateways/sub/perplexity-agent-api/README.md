# Perplexity Agent API

Perplexity Agent API is a hosted gateway for multiple model providers with configurable tools and reasoning. The current request endpoint is /v1/agent; /v1/responses is a documented compatibility alias.

## Use and deployment boundaries

Web search must be explicitly enabled with an appropriate tool or preset; a plain model request does not provide citations. Configure model, tool and spending scope, and evaluate each provider's data terms. Zero data retention requires an eligible configured account and agreement; it is not the default.

## Producer

- [Perplexity AI](../../../../../producers/sub/p/sub/perplexity-ai/README.md).

## Official resources

- [API documentation](https://docs.perplexity.ai/docs/agent-api/quickstart).
- [API privacy and retention](https://docs.perplexity.ai/docs/resources/privacy-security).
