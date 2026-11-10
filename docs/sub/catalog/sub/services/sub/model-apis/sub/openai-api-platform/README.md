# OpenAI API Platform

## Relations

- Produced by: [OpenAI](../../../../../producers/sub/o/sub/openai/)

## Service purpose and access

OpenAI API Platform is the hosted developer service for programmatic model access and API-native generation and tools. Its documented surfaces include Responses, streaming, batch processing, embeddings, image and audio generation, realtime interactions, and supporting files and vector stores. Applications select compatible models, endpoints, and tool configurations through authenticated API requests. [Developer documentation](https://developers.openai.com/api/docs).

The service is distinct from the trained models it exposes. OpenAI Agents API separately provides managed agent infrastructure; OpenAI Agents SDK is software; ChatGPT is an assistant workspace; and Codex is an agent product. Shared accounts or billing leave these product and operating boundaries intact.

## Dated API changes

The [official changelog](https://developers.openai.com/api/docs/changelog) records these October 2026 changes:

- **October 6:** the beta Decisions API, `v1/decisions`, initially supports `gpt-6-luna`. This is an API feature with its own beta schema and rollout, distinct from Responses and from trained-model identity.
- **October 7:** the `chat-latest` alias was refreshed. It is a moving route; resolve the active snapshot before attributing behavior to a particular model revision.
- **October 8:** GPT-6.1 Sol gained the `service_tier: "ultrafast"` processing option in Responses. It is a model-specific service tier, with compatibility and availability governed by current documentation.

## Operating boundaries

Pin the endpoint, model or snapshot, processing mode, and API configuration when reproducing a result. Current documentation owns pricing, quotas, rate limits, supported tools, data controls, regions, migrations, and deprecation schedules. A feature announcement does not make those conditions permanent, or establish availability for every model and account.

## Official resources

- [API documentation](https://developers.openai.com/api/docs)
- [API changelog](https://developers.openai.com/api/docs/changelog)
