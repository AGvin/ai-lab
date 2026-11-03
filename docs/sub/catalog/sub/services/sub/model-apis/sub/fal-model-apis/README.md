# fal Model APIs

**fal Model APIs** is a managed model endpoint platform operated by [fal (Features & Labels, Inc.)](../../../../../producers/sub/f/sub/features-and-labels-inc/). It offers API access to hosted image, video, speech, audio and other generative models. The platform brand **fal.ai** is already represented by that legal producer; it is not a second independently owned producer.

## Integration and execution modes

The [official overview](https://fal.ai/docs/documentation/model-apis/overview) distinguishes direct synchronous `run`, queue-backed `subscribe`, and asynchronous `submit` with polling or webhooks. Some models also offer streaming or WebSocket-based real-time access, but support is model-specific. One example queue request uses `https://queue.fal.run/<model-path>` with an `Authorization: Key` header. SDK wrappers can manage retries and polling; never expose a permanent API key in a public client.

The model catalog includes multiple third-party publishers, and fal's Serverless/Compute products for custom model deployment are related but distinct services. Serving a model does not transfer its original authorship, training data rights or output permissions to fal.

## Security and terms

Uploads and generated media may contain personal, proprietary or copyright-protected material. Use approved inputs, protect credentials, constrain usage costs and check current [API service terms](https://fal.ai/legal/terms-of-service), per-model licensing, retention and output rights before production use. Pricing, concurrency, available models and data locations can change. No authenticated API call, media generation or deployment was performed for this profile.

## Relations

- Produced by: [fal (Features & Labels, Inc.)](../../../../../producers/sub/f/sub/features-and-labels-inc/)

## Official resources

- [fal Model APIs](https://fal.ai/docs/documentation/model-apis/overview)
- [fal developer documentation](https://fal.ai/docs/documentation)
- [fal terms of service](https://fal.ai/legal/terms-of-service)
