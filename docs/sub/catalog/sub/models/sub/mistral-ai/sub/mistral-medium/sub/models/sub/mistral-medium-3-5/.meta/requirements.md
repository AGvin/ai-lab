# Documentation Requirements

## Requirements

- Render the standard entity-relations block from the validated current-entity projection.

- Identify Mistral Medium 3.5 as the concrete GA model released on 2026-04-28 with hosted alias `mistral-medium-3-5`.
- Preserve its first-party identity as a multimodal dense 128B model with 256K context and configurable reasoning effort.
- Keep the open-weights Modified MIT v26.04 distribution boundary source-backed and distinguish the trained model from EAGLE/speculative-decoding artifacts.
- Attribute agentic, coding, instruction-following, and frontier positioning to Mistral AI rather than treating it as an independent AI Lab ranking.
- Keep API pricing, product routing, hosted availability, and runtime throughput freshness-sensitive.

## Validation

- EAGLE and other inference artifacts are not represented as separate trained models in this refresh.
- Product aliases and deployment behavior remain distinct from model identity.

## Source-backed profile

- Required reader orientation: Mistral Medium 3.5 is Mistral AI’s multimodal model released on April 28, 2026, combining instruction following, reasoning and coding in one set of weights.
- Preserve this model-scoped fact: It is a dense 128B model with a 256K-token context, text and image inputs, and text output. Reasoning effort supports `none` and `high`. [Mistral Medium 3.5 weights and configuration correction](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)
- Preserve this model-scoped fact: The model card lists the API release `mistral-medium-3-5` as GA. [Mistral Medium 3.5 model card](https://docs.mistral.ai/models/mistral-medium-3-5-26-04)

## Operational and interpretation boundaries

- Explain this boundary: Use the corrected official Transformers configuration. Mistral warns that the original configuration and GGUF conversions made from it degraded long-context performance. [Mistral Medium 3.5 weights and configuration correction](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B)
- Explain this boundary: Its Modified MIT license includes a preceding-month global consolidated revenue threshold of US$20 million for the company or employer; it is not unrestricted MIT. The full license governs weight use. [Mistral Medium 3.5 Modified MIT license](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE)
- Explain this boundary: EAGLE is a companion decoding artifact. Tool execution and validation belong to the application, not to the model’s reasoning setting. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
