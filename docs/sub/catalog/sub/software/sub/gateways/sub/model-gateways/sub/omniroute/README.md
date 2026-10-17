# OmniRoute

OmniRoute is self-hostable model-gateway software that provides a unified API/proxy layer across multiple AI providers, accounts, and compatible model backends.

## Scope and boundaries

OmniRoute provides an OpenAI-compatible client interface and coordinates provider access, translation, routing, fallback, quotas, and operating policies. Provider integrations can use API keys, OAuth, browser or CLI accounts, self-hosted backends, and custom compatible endpoints. Support varies by provider and release.

Self-hosting the gateway does not make remote inference local. Requests routed to external providers can transmit prompts, tool inputs, images, and other request content to those services.

## Operational and security boundary

Stored credentials use the documented encryption-at-rest path only when the operator configures `STORAGE_ENCRYPTION_KEY`. The upstream security policy documents plaintext passthrough when that key is absent; local deployment alone does not establish encrypted credential storage.

TLS/browser fingerprinting, CLI compatibility shaping and local MITM functionality require authorized interoperability or troubleshooting. These features do not confer permission to bypass provider restrictions, account controls or upstream terms. Configure deployment authentication, network access, credential handling and request budgets for the operated environment.

The repository's MIT license applies to its software source; separate website, provider, and integration terms still apply.

## Official resources

- <https://omniroute.online/>
- <https://omniroute.online/docs>
- <https://github.com/diegosouzapw/OmniRoute>
- <https://github.com/diegosouzapw/OmniRoute/blob/main/SECURITY.md>
