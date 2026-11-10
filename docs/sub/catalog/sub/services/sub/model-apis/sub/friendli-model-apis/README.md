# Friendli Model APIs

**Friendli Model APIs** is [FriendliAI](../../../../../producers/sub/f/sub/friendliai/)'s currently available **hosted serverless model-inference API**. Its [first-party integration guidance](https://learn.friendli.ai/articles/4213111023-q10-1-how-do-i-connect-friendliai-with-litellm-or-other-openai-compatible-client) identifies the OpenAI-compatible base URL `https://api.friendli.ai/serverless/v1` and vendor-documented chat-completions, Responses and Messages interfaces.

## Identity and deployment boundary

[Friendli Model APIs](https://friendli.ai/product/model-apis) provides managed shared-infrastructure access to a selected, changing set of open-weight and third-party models. This is separate from **Friendli Dedicated Endpoints**, which provision dedicated model-serving infrastructure (`https://api.friendli.ai/dedicated/v1`), and from the self-managed **Friendli Container** runtime. Those deployment variants must not be counted here as original trained models or silently conflated with the hosted service.

The [official help center](https://learn.friendli.ai/articles/6490778657-q1-1-which-models-are-available-on-model-api-serverless) distinguishes current serverless model availability from the larger dedicated-deployment catalog. Model IDs, supported response formats, modality, quotas, regions and prices vary; confirm actual provider support and terms before integration. FriendliAI's API availability does not make it the original developer of the models it serves.

## Security, commercial and provenance limits

Use a credential secret store instead of committing API keys; restrict the data sent to remote inference to what the current customer agreement, data-handling terms, processing regions, retention and training-use controls permit. Verify the [current pricing and plan provisions](https://friendli.ai/pricing) and [service status](https://status.friendli.ai/) for the actual endpoint. Vendor performance, uptime and pricing statements are not independent measurements or universal contractual guarantees.

Check the original model publisher, license, origin, ownership and applicable sanctions independently. The corporate producer below is an API operator identity, not proof that every hosted third-party model has safe provenance. This record does not include authenticated API testing, a complete beneficial-ownership audit or an independent benchmark.

## Provenance

- Produced by: [FriendliAI](../../../../../producers/sub/f/sub/friendliai/).

## Official resources

- [Friendli Model APIs product](https://friendli.ai/product/model-apis)
- [Official OpenAI-compatible interface guidance](https://learn.friendli.ai/articles/4213111023-q10-1-how-do-i-connect-friendliai-with-litellm-or-other-openai-compatible-client)
- [Model API inventory boundary](https://learn.friendli.ai/articles/6490778657-q1-1-which-models-are-available-on-model-api-serverless)
- [Vendor pricing and deployment options](https://friendli.ai/pricing)
- [Provider operational status](https://status.friendli.ai/)
