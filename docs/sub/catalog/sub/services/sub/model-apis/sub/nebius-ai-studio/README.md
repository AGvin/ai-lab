# Nebius Token Factory

**Nebius Token Factory** is a managed model-inference and post-training platform operated by [Nebius](../../../../../producers/sub/n/sub/nebius/). The service was previously known as **Nebius AI Studio**; Nebius introduced its current name in November 2025. This catalog retains the original durable `nebius-ai-studio` slug for the same service.

## API and authentication

The [quickstart](https://docs.tokenfactory.nebius.com/quickstart) and [API introduction](https://docs.tokenfactory.nebius.com/api-reference/introduction) document an OpenAI-compatible API at `https://api.tokenfactory.nebius.com/v1/`. Authentication uses `Authorization: Bearer` with a Nebius API key, typically provided through a protected `NEBIUS_API_KEY` environment variable. Do not embed keys in client-side applications or public repositories.

Hosted model choice, dedicated serving, fine-tuning and post-training workflows depend on separately enabled features, account limits and charges. Third-party model authorship and weights are distinct from Nebius' serving service.

## Operating boundaries

Supported models, pricing, API versions, inference throughput, rate limits, regions, private prompt handling and retention can change. Verify actual contract, permissions and data processing before transmitting confidential prompts or fine-tuning datasets. No authenticated inference, benchmark or deployment was run for this profile.

## Relations

- Produced by: [Nebius](../../../../../producers/sub/n/sub/nebius/)

## Official resources

- [Token Factory quickstart](https://docs.tokenfactory.nebius.com/quickstart)
- [API introduction](https://docs.tokenfactory.nebius.com/api-reference/introduction)
- [AI Studio to Token Factory transition](https://nebius.com/newsroom/nebius-launches-nebius-token-factory-to-deliver-production-ai-inference-at-scale)
