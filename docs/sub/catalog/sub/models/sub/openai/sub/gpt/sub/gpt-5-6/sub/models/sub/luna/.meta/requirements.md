# Documentation Requirements

## Requirements

- Identify GPT-5.6 Luna as a concrete model in the GPT-5.6 series.
- Preserve exact model/API identity and current provider-documented model capabilities.
- Keep pricing, rate limits, low-cost routing recommendations, hardware assumptions, and workload-specific accepted-result conclusions outside the canonical model profile.

## Content Specification

- Use `GPT-5.6 Luna` as the page title and link the GPT-5.6 series.
- Preserve model ID `gpt-5.6-luna`, text/image input, text output, 1,050,000-token context, 128,000-token max output, February 16, 2026 cutoff, reasoning-token support, current hosted feature support, and lack of fine-tuning support.
- Preserve the boundary that no downloadable weights/local hardware profile is provided by the current source; do not infer VRAM.
- Present cost-sensitive high-volume positioning as provider guidance rather than independent AI Lab evidence.

## Validation

- Luna remains distinct from Sol and Terra.
- Pricing/rate limits are not treated as model identity.
- No local-hardware claim is inferred.
- Hosted capability support is distinguished from architectural facts.

## Source-scoped operating boundaries

- The August 2026 ChatGPT update is distinguished from earlier releases in the system card. Its evaluation results and deployment behavior should not be assigned automatically to every use of this model name [GPT-5.6 August system card](https://deploymentsafety.openai.com/gpt-5-6-august-update).
- Reasoning effort and tool availability are API configuration. Validate tool arguments and application permissions before executing a model-proposed action [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).

## Source evidence

- [gpt-5.6-luna model reference](https://developers.openai.com/api/docs/models/gpt-5.6-luna).
- [Latest-model guide](https://developers.openai.com/api/docs/guides/latest-model).
- [GPT-5.6 August 2026 system card](https://deploymentsafety.openai.com/gpt-5-6-august-update).
