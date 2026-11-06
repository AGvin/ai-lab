# Documentation Requirements

## Requirements

- Identify GPT-5.6 as a model series within the GPT family with Sol, Terra, and Luna as distinct concrete models.
- Preserve series-level model/API facts genuinely shared by the represented models.
- Keep mutable pricing, rate limits, product availability, regional rollout, and migration/workflow guidance outside the canonical series profile.
- Keep tier-specific identifiers, positioning, and capability differences on exact model pages.

## Content Specification

- Use `GPT-5.6` as the page title and link the GPT family.
- Explain that `5.6` identifies the generation while Sol, Terra, and Luna are durable named capability tiers represented as distinct concrete models.
- Preserve text/image input, text output, multilingual/vision support, 1,050,000-token context, 128,000-token max output, February 16, 2026 knowledge cutoff, and current reasoning-effort controls as shared provider-documented facts.
- Preserve `gpt-5.6` as a mutable routing alias to Sol without treating it as a model entity.
- Link Sol, Terra, and Luna through the concrete-model index.
- Include official GPT-5.6 launch and model-catalog references.

## Validation

- GPT-5.6 is typed as `model-series`, not a second long-lived model family.
- Sol, Terra, and Luna remain separate concrete models.
- The alias `gpt-5.6` is not represented as a fourth model.
- Mutable pricing and product availability are not treated as series identity.

## Source-scoped operating boundaries

- The API alias gpt-5.6 routes to Sol [Sol model reference](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
- The August system card separately identifies ChatGPT updates of Sol and Luna; those updates do not replace the previously released versions across every surface [GPT-5.6 August system card](https://deploymentsafety.openai.com/gpt-5-6-august-update).
- Tool support and reasoning effort are current hosted configuration. Application authorization and tool execution remain separate from the series’ ability to produce a tool call [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Source evidence

- [gpt-5.6-sol model reference](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
- [gpt-5.6-terra model reference](https://developers.openai.com/api/docs/models/gpt-5.6-terra).
- [gpt-5.6-luna model reference](https://developers.openai.com/api/docs/models/gpt-5.6-luna).
- [GPT-5.6 August 2026 system card](https://deploymentsafety.openai.com/gpt-5-6-august-update).
- [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
