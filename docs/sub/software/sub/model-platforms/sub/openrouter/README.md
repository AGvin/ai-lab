# OpenRouter

OpenRouter provides one API for accessing models served by multiple providers. It is useful for model choice, fallbacks, and provider routing without integrating every provider separately.

## When it fits

- one application needs models from several providers;
- price, latency, or availability-based routing is useful;
- an OpenAI-compatible endpoint simplifies an existing integration;
- provider or model fallbacks are acceptable.

OpenRouter is an additional service in the data path. It does not make every underlying provider equally suitable for private or regulated data.

## Basic use

1. Create an OpenRouter API key.
2. Select an exact model identifier from the model catalog.
3. Point an OpenAI-compatible client to `https://openrouter.ai/api/v1`.
4. Set the key through a secret or environment variable, never in source control.
5. Record the model and provider returned for requests where routing matters.

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "provider/model",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

The exact model, price, context, provider availability, and terms can change. Recheck them before production use.

## Routing

By default, OpenRouter can select among available providers and use fallbacks. Use explicit routing when provider identity, data policy, price, or reproducibility matters.

Common controls include:

- `only` — allow only specified providers;
- `allow_fallbacks` — permit or prohibit backup providers;
- `data_collection` — permit or deny providers that may collect data;
- `zdr` — require a Zero Data Retention endpoint;
- `sort` — prefer price, throughput, or latency.

<!-- Stable cross-locale anchor; do not translate or remove. -->
<a id="openrouter-data-safety"></a>

## Security and privacy

The effective path is:

```text
client -> OpenRouter -> selected model provider
```

OpenRouter states that it does not retain prompts or completions by default unless prompt logging is enabled. The selected provider still processes the request, and endpoint policies differ.

For sensitive data:

1. Confirm that organizational policy permits both OpenRouter and the selected provider.
2. Keep input and output logging disabled.
3. Enable account-level Zero Data Retention where required.
4. Send `zdr: true` and `data_collection: "deny"`.
5. Allowlist approved providers and disable fallbacks when provider identity must not change.
6. Recheck the endpoint policy, region, retention, training use, and contractual terms.
7. Use a direct approved provider or self-hosted inference when an intermediary is not permitted.

Example restricted routing:

```json
{
  "model": "provider/model",
  "messages": [
    {"role": "user", "content": "Approved content only"}
  ],
  "provider": {
    "zdr": true,
    "data_collection": "deny",
    "allow_fallbacks": false,
    "only": ["approved-provider"]
  }
}
```

These controls reduce exposure but do not replace data classification, access control, secret removal, legal review, or vendor approval.

## Sources

- [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart)
- [Provider Routing](https://openrouter.ai/docs/guides/routing/provider-selection)
- [Zero Data Retention](https://openrouter.ai/docs/guides/features/zdr)
- [Provider Logging](https://openrouter.ai/docs/guides/privacy/provider-logging/)
- [Input and Output Logging](https://openrouter.ai/docs/guides/features/input-output-logging)
