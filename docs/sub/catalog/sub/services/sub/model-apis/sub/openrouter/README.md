# OpenRouter

OpenRouter is OpenRouter, Inc.'s hosted model-API service for accessing and routing requests across third-party generative-model providers through a unified API surface.

## Service boundary

The effective data path runs from the client through OpenRouter to the selected model provider. Provider identity, model terms, logging, retention, training policies, regions, and availability therefore remain independently material. OpenRouter supports routing controls such as provider selection and allowlisting, fallback control, data-collection restrictions, zero-data-retention routing, and price, latency, or throughput preferences where currently available.

Current OpenRouter documentation describes prompt and completion logging and product-use permissions as configurable and off by default, while request metadata is retained for service and reporting functions; downstream providers retain their own policies. Exact model lists, provider availability, pricing, routing behavior, account limits, regional options, and other service state are freshness-sensitive.

## Relations

- Produced by [OpenRouter, Inc.](../../../../../producers/sub/o/sub/openrouter-inc/).

## Official resources

- [OpenRouter](https://openrouter.ai/)
- [OpenRouter documentation](https://openrouter.ai/docs)
- [Privacy Policy](https://openrouter.ai/privacy/)
- [Terms of Service](https://openrouter.ai/terms)
