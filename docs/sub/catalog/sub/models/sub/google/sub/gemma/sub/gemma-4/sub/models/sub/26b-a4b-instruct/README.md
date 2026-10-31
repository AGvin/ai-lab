# Gemma 4 26B A4B Instruct

Gemma 4 26B A4B Instruct is the Mixture-of-Experts instruction model with 25.2B total and 3.8B active parameters; active parameters do not represent complete weight storage or memory residency.

## Relations

- Member of: [Gemma 4](../../../../)

## Source-scoped operating boundaries

- Text/image and frame-based video input produce text with 256K context. Audio input is unsupported for this variant, unlike E2B/E4B/12B. [Official checkpoint card](https://huggingface.co/google/gemma-4-26B-A4B-it).
- Apache-2.0 applies to the released checkpoint. Keep total parameters, active parameters, quantized artifact size, and measured runtime memory distinct; do not plan memory from the active count alone. [Official checkpoint card](https://huggingface.co/google/gemma-4-26B-A4B-it).
- Use the model-specific chat template and validate generated tool calls and outputs in the application. Safety training and open-weight access do not supply application permissions. [Gemma 4 configuration and limitations](https://ai.google.dev/gemma/docs/core/model_card_4).

## Official resources

- <https://huggingface.co/google/gemma-4-26B-A4B-it>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
