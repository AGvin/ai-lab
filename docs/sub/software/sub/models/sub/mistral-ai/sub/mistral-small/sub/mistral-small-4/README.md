# Mistral Small 4

Mistral Small 4 is Mistral AI's open multimodal model for chat, coding, agentic, document, and reasoning workloads.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Official profile

- Canonical identity: Mistral Small 4
- API alias: `mistral-small-latest`
- Access forms: Mistral API, AI Studio, and official open-model distribution
- License: Apache-2.0
- Architecture: mixture of experts with 128 experts and four active per token
- Parameters: 119 billion total and 6 billion active per token
- Context window: 256,000 tokens
- Modalities: text and image input; text output
- Reasoning: configurable, including `none` and `high`

## Pricing

Mistral listed API prices of $0.15 per million input tokens and $0.60 per million output tokens when verified on 2026-07-25. The alias, pricing, and hosted availability can change independently of the open model identity.

## Infrastructure guidance

Mistral's official minimum configurations are four NVIDIA HGX H100 systems, two HGX H200 systems, or one DGX B200 system. Its recommended configurations are four HGX H100 systems, four HGX H200 systems, or two DGX B200 systems.

These are enterprise system configurations. They do not support a claim that the model fits on one consumer GPU. No comparison-specific fine-tune or quantization is selected here.

## Selection guidance and limitations

Evaluate Mistral Small 4 for general chat, coding automation, codebase exploration, document understanding, multimodal analysis, math, research, and complex reasoning. Decide reasoning effort and deployment form from workload tests.

The official launch page does not state a maximum output-token limit. Confirm current API limits and infrastructure guidance before deployment, and treat Mistral's benchmark results as provider-reported evidence.

## Evidence

Identity, architecture, license, capabilities, access, pricing, and infrastructure guidance were verified on 2026-07-25.

## Related pages

- [Mistral Small model family](../../)
- [Mistral AI models](../../../..)

## Sources

- [Introducing Mistral Small 4](https://mistral.ai/news/mistral-small-4/)
