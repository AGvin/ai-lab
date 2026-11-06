# Documentation Requirements

## Requirements

- Identify DeepInfra here as the hosted remote model-inference/API service operated by Deep Infra Inc.
- Keep this model-API identity distinct from DeepInfra's dedicated GPU, custom deployment, or broader infrastructure offerings.
- Keep third-party model identity, licensing, lifecycle, and intrinsic capabilities with their model owners rather than attributing them to DeepInfra merely because they are served there.
- Treat model inventory, API compatibility, pricing, rate limits, context/output limits, regions, throughput, and other hosted state as mutable facts requiring current verification.
- Render the standard `entity-relations` block and preserve Deep Infra Inc. as the producer.

## Validation

- The page remains scoped to hosted remote model APIs rather than absorbing every DeepInfra product.
- Mutable provider inventory is not presented as a timeless service property.
- The `produces` / `produced-by` relation pair resolves consistently to Deep Infra Inc.

## Scoped original-source qualification — 2026-11-06

- DeepInfra is the managed remote model inference API service. Its official documentation distinguishes chat completions, embeddings, images, audio, batch and private-model interfaces from separately operated GPU instances. A model served by DeepInfra does not become a DeepInfra-trained model.
- Supported modalities, the OpenAI-compatible chat endpoint, account limits, privacy rules, GPU-instance terms and custom deployment paths require validation by model and account; these are not independent latency or retention guarantees.
- Verified first-party source 1: https://docs.deepinfra.com/
- Verified first-party source 2: https://docs.deepinfra.com/quickstart
- This bounded source qualification does not establish a full freshness audit, independently validated runtime, legal/model-license clearance, current pricing or entitlements, global schema/cache/CI/render or final publication.
