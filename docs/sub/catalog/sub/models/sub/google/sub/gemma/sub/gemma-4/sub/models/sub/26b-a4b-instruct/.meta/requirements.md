# Documentation Requirements

## Requirements

- Identify Gemma 4 26B A4B Instruct using the exact canonical identity and official model or artifact identifier.
- Preserve membership in `catalog/models/google/gemma/gemma-4` and producer provenance through that family or series.
- Keep the trained model separate from API routes, products, deployment configurations, and optimized artifacts.

## Validation

- Every concrete model identifier and capability is supported by a current primary source.
- Access restrictions, license scope, and unsupported capabilities remain explicit.
- Model-generated output or tool requests do not establish application authorization.

## Verified identity and provenance

Gemma 4 26B A4B Instruct is the Mixture-of-Experts instruction model with 25.2B total and 3.8B active parameters; active parameters do not represent complete weight storage or memory residency.

## Source-scoped operating boundaries

- Text/image and frame-based video input produce text with 256K context. Audio input is unsupported for this variant, unlike E2B/E4B/12B. [Official checkpoint card](https://huggingface.co/google/gemma-4-26B-A4B-it).
- Apache-2.0 applies to the released checkpoint. Keep total parameters, active parameters, quantized artifact size, and measured runtime memory distinct; do not plan memory from the active count alone. [Official checkpoint card](https://huggingface.co/google/gemma-4-26B-A4B-it).
- Use the model-specific chat template and validate generated tool calls and outputs in the application. Safety training and open-weight access do not supply application permissions. [Gemma 4 configuration and limitations](https://ai.google.dev/gemma/docs/core/model_card_4).

## Source evidence

- <https://huggingface.co/google/gemma-4-26B-A4B-it>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
