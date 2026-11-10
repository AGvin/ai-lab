# Cloudflare Workers AI

Cloudflare Workers AI is Cloudflare's producer-operated serverless model-execution API and platform for running supported models on Cloudflare's GPU-backed network.

## Service boundary

Workers AI provides managed model access through Workers bindings and HTTP APIs without requiring users to operate inference servers. Cloudflare AI Gateway, Vectorize, Agents, AI Search, the Workers runtime, and individual model identities remain separate even when they integrate directly; Workers AI does not become the producer of third-party models it hosts.

Available models, pricing, limits, bindings and APIs, custom-model options, regional behavior, and plan availability are freshness-sensitive.

## Relations

- Produced by [Cloudflare](../../../../../producers/sub/c/sub/cloudflare/).

## Official resources

- [Cloudflare Workers AI documentation](https://developers.cloudflare.com/workers-ai/)
