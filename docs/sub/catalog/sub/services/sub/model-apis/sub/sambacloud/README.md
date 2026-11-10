# SambaCloud

SambaCloud (SambaNova Cloud) is [SambaNova Systems, Inc.](../../../../../producers/sub/s/sub/sambanova-systems-inc/)'s **hosted model-inference API** for accessing third-party AI models. Its [current developer dashboard](https://cloud.sambanova.ai/dashboard) documents an OpenAI-compatible request interface at `https://api.sambanova.ai/v1`, using authenticated API keys.

## Hosted-service boundary

This is remote, provider-operated inference. It differs from SambaNova's **SambaStack** dedicated/on-premises platform and its separately designed RDU inference hardware. Access to models developed by OpenAI, Google, Meta, DeepSeek or other publishers through SambaCloud does **not** transfer original trained-model authorship to SambaNova.

The [vendor's current service plans](https://cloud.sambanova.ai/plans) distinguish production and preview model access, rate-limit tiers and commercial options. Model availability, preview status, pricing, regions, context lengths, API capabilities and account limits can change; confirm them for the actual model and plan before use. This profile contains no independently measured throughput, quality ranking or authenticated API test.

## Operational and privacy considerations

Treat API tokens as secrets and keep them out of repository code and telemetry. The current [SambaNova developer integration guide](https://docs.sambanova.ai/docs/en/integrations/vscode) shows how to configure an authenticated hosted endpoint; configuration of a development environment does not establish production capacity or all security controls.

Before transmitting confidential prompts or customer data, verify the actual SambaCloud contractual terms, retention, training-use, processing geography and security obligations. Broad vendor statements about model/data ownership and different SambaStack on-premises agreements should **not** be substituted for the relevant cloud contract. Avoid assuming that trial availability, free plans or a particular model remain unchanged.

## Provenance

- Produced by: [SambaNova Systems, Inc.](../../../../../producers/sub/s/sub/sambanova-systems-inc/).

## Official resources

- [Current SambaCloud dashboard and API quickstart](https://cloud.sambanova.ai/dashboard)
- [SambaNova API integration documentation](https://docs.sambanova.ai/docs/en/integrations/vscode)
- [SambaCloud plan structure](https://cloud.sambanova.ai/plans)
- [Official distinction between cloud and dedicated/on-premises deployments](https://sambanova.ai/solutions/ai-natives-enterprises)
