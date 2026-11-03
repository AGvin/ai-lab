# DigitalOcean Inference

**DigitalOcean Inference** is a hosted model API, catalog and routing service operated by [DigitalOcean](../../../../../producers/sub/d/sub/digitalocean/). It provides model-access workflows using serverless inference, dedicated inference deployments and an Inference Router. Its catalog includes DigitalOcean-hosted and third-party commercial or open-weight models.

## API and deployment boundaries

The [serverless API](https://docs.digitalocean.com/products/inference/reference/api/serverless-inference/) uses the base URL `https://inference.do-ai.run`, distinct from the main DigitalOcean control-plane API at `https://api.digitalocean.com`. Text inference has OpenAI-compatible endpoints; additional embeddings and media endpoints have modality-specific capabilities. Use permitted access credentials and confirm support for the exact model and account configuration.

Serverless requests do not require users to provision dedicated GPUs; dedicated inference instead provisions hosted compute for specific deployment needs. Inference Router chooses a model according to routing configuration. Neither is a separately trained DigitalOcean foundation model. The adjacent **DigitalOcean Evaluations** service is for assessing responses and agent configurations, not a second duplicate of this API.

## Production and provenance considerations

The model catalog, supported providers, API features, prices, quotas, latency and regional offerings change. An API listing of a model developed by Anthropic, OpenAI, Meta, Alibaba, DeepSeek or another organization does not transfer the underlying model's original authorship or license to DigitalOcean. Validate the publisher, provider route, applicable terms and data processing before transmitting regulated or confidential prompts.

Keep keys in a secret manager, restrict access and spend, and verify the current data privacy and retention settings for the chosen route and customer contract. This record is documentation research, not an authenticated request, independent cost/latency benchmark or full legal model-rights audit.

## Relations

- Produced by: [DigitalOcean](../../../../../producers/sub/d/sub/digitalocean/)
- Related managed evaluation service: [DigitalOcean Evaluations](../../../evaluation-and-observability/sub/digitalocean-evaluations/)

## Official resources

- [Inference overview](https://docs.digitalocean.com/products/inference/)
- [Supported models and deployment types](https://docs.digitalocean.com/products/inference/details/models/)
- [Serverless API reference](https://docs.digitalocean.com/products/inference/reference/api/serverless-inference/)
- [Access and API endpoints](https://docs.digitalocean.com/products/inference/how-to/si-endpoints/)
- [Regional availability](https://docs.digitalocean.com/products/inference/details/availability/)
