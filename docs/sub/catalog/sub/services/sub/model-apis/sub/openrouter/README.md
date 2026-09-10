# OpenRouter

OpenRouter is OpenRouter, Inc.'s hosted Model API service for accessing and routing requests across third-party generative-model providers through a unified API surface.

## Routing and data path

The effective request path is:

```text
client -> OpenRouter -> selected model provider
```

Provider identity still matters. OpenRouter can apply routing controls such as provider allowlists, fallback policy, data-collection restrictions, zero-data-retention requirements, and routing preferences, but downstream providers retain their own model terms, data handling, availability, region, and training/retention policies.

Current OpenRouter documentation distinguishes optional prompt/completion logging and product-use permissions from request metadata retained for service/reporting functions. Treat account privacy settings and downstream-provider policy as separate review layers.

## Related

- [OpenRouter, Inc.](../../../../../producers/sub/o/sub/openrouter-inc/) — canonical producer organization.

## Official resources

- [OpenRouter](https://openrouter.ai/)
- [Documentation](https://openrouter.ai/docs)
- [Data collection](https://openrouter.ai/docs/guides/privacy/data-collection)
- [Provider logging](https://openrouter.ai/docs/guides/privacy/provider-logging/)
- [Privacy Policy](https://openrouter.ai/privacy/)
- [Terms of Service](https://openrouter.ai/terms)
