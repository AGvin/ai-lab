# OmniRoute

OmniRoute is self-hostable model-gateway software that provides a unified API/proxy layer across multiple AI providers, accounts, and compatible model backends.

## Scope and boundaries

- The profile preserves its primary placement under `gateways/model-gateways`: OmniRoute coordinates model-provider access, translation, routing, fallback, quotas, and operational policy rather than acting as a model, inference engine, or hosted model provider itself.
- The profile explains the OpenAI-compatible client boundary and provider abstraction at a durable level without freezing the current provider count, free-tier count, routing-strategy count, supported-model count, or other fast-moving inventory figures.
- The profile treats API-key, OAuth, browser/CLI-account, self-hosted, and custom-compatible integrations as provider-access mechanisms owned by OmniRoute rather than separate canonical AI Lab products unless a future integration has an independently justified identity.
- Self-hosting the gateway remains distinct from self-hosting inference. Requests routed to remote providers may transmit prompts, tool inputs, images, or other request content to those upstream services; do not present local OmniRoute deployment as a guarantee of local/private inference.

## Official resources

- <https://omniroute.online/>
- <https://omniroute.online/docs>
- <https://github.com/diegosouzapw/OmniRoute>
