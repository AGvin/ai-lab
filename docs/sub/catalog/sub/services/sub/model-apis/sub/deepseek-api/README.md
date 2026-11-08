# DeepSeek API

DeepSeek API is DeepSeek's directly hosted developer/model-access service. It exposes current DeepSeek model releases through documented chat and compatible developer interfaces, separate from the consumer [DeepSeek assistant](../../../assistant-workspaces/sub/deepseek/). [Official developer documentation](https://api-docs.deepseek.com/).

## Interfaces and identity boundaries

DeepSeek documents OpenAI-compatible and Anthropic-compatible interfaces and a Responses API. Request shape and supported parameters can vary by endpoint and model; the Responses interface is documented as stateless, requiring clients to supply prior conversation history when needed. Compatibility and moving model aliases are not distinct models or a promise of portable semantics. [Responses API guide](https://api-docs.deepseek.com/guides/responses_api/).

The actual DeepSeek V4/V4.1 model lineage belongs in Model Reference, not a duplicated API-service entity. The October 17, 2026 official update changed routing of a released Flash model and the web/app models; future model aliases and defaults remain mutable. [DeepSeek change log](https://api-docs.deepseek.com/updates/).

## Operational boundaries

Verify current models, availability, authentication, context/output limits, vision support, endpoint-specific tool features, caching, rate limits, prices, and retirement notices before relying on a capability. The API, hosted chat application and third-party model hosts may have different terms and data handling.

## Relations

- Produced by [DeepSeek](../../../../../producers/sub/d/sub/deepseek/).

## Official resources

- [DeepSeek API](https://api-docs.deepseek.com/)
- [Responses API guidance](https://api-docs.deepseek.com/guides/responses_api/)
- [API updates](https://api-docs.deepseek.com/updates/)
