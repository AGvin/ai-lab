# Hyperbolic Flux Inference

**Hyperbolic Flux Inference** is [Hyperbolic Labs, Inc.](../../../../../producers/sub/h/sub/hyperbolic-labs-inc/)'s current **hosted serverless model API**, introduced on [October 21, 2026](https://www.hyperbolic.ai/blog/flux-inference-api) as the next generation of the earlier Hyperbolic inference service. It provides OpenAI-compatible Chat Completions and streaming without requiring a customer to provision GPUs.

## Product and deployment boundaries

The [current API](https://www.hyperbolic.ai/inference) uses `https://api.hyperbolic.ai/inference/v1`. The vendor states that Flux runs on its **Forge** compute-orchestration control plane, but Flux is the hosted inference service, not Forge software, on-demand GPU instances, Managed Kubernetes, a dedicated inference deployment, or an originally trained model.

The October 2026 launch announcement explicitly describes both **Hyperbolic-hosted** inference engines and routes to **external model providers** behind Hyperbolic authentication and billing. API access to a model from DeepSeek, Z.ai, Moonshot AI, MiniMax, NVIDIA or another publisher does not transfer its trained-model authorship to Hyperbolic. Some vendor-listed models are preview releases, not stable model publications; available models and their supported parameters are subject to change.

## Integration, billing and safety

An OpenAI-compatible client uses a Hyperbolic API key and the published current base URL. The [vendor migration instructions](https://www.hyperbolic.ai/blog/flux-inference-api) state that Flux requires a key beginning `sk_live_`; older-format keys and base URLs must be replaced. A Pro/Organization account with prepaid credits is required, and billing, model limits and rates vary by model. Do not embed credentials in repositories or logs. Test live compatibility, model support, streaming, context windows and charges for the actual account.

**Data-routing warning:** external provider routes may have different data handling, jurisdictions, licensing, availability and security guarantees from Hyperbolic-hosted paths. The vendor's described mutual-TLS GPU ingress controls apply to its own hosted infrastructure, not automatically to all upstream providers. Check the current customer/supplemental contract, retention, training use, data residency, downstream model provider, provenance and sanctions exposure before sending confidential or regulated material.

Current edge/location and model latency are vendor-reported configuration details, not tested regional promises. No authenticated calls, independent performance benchmark, complete beneficial-ownership review or legal certification were performed for this record.

## Provenance

- Produced by: [Hyperbolic Labs, Inc.](../../../../../producers/sub/h/sub/hyperbolic-labs-inc/).

## Official resources

- [Hyperbolic's current Flux product and model/API description](https://www.hyperbolic.ai/inference)
- [October 21, 2026 Flux launch, architecture and legacy migration](https://www.hyperbolic.ai/blog/flux-inference-api)
- [Current Hyperbolic platform overview](https://www.hyperbolic.ai/)
- [Terms identifying the company and applicable supplemental terms](https://www.hyperbolic.ai/terms)
