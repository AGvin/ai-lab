# Documentation Requirements

## Requirements

- Identify Gemma 4 31B Instruct using the exact canonical identity and official model or artifact identifier.
- Preserve membership in `catalog/models/google/gemma/gemma-4` and producer provenance through that family or series.
- Keep the trained model separate from API routes, products, deployment configurations, and optimized artifacts.

## Validation

- Every concrete model identifier and capability is supported by a current primary source.
- Access restrictions, license scope, and unsupported capabilities remain explicit.
- Model-generated output or tool requests do not establish application authorization.

## Verified identity and provenance

Gemma 4 31B Instruct is the 30.7B-parameter dense instruction model; it is a distinct checkpoint from the 26B A4B sparse model.

## Source-scoped operating boundaries

- Text/image and frame-based video input produce text with 256K context. Audio input is unsupported; the audio capabilities of smaller Gemma 4 variants do not transfer to this checkpoint. [Official checkpoint card](https://huggingface.co/google/gemma-4-31B-it).
- Apache-2.0 applies to the released checkpoint. Runtime memory depends on precision, context, and implementation; the parameter count is not a complete memory requirement. [Official checkpoint card](https://huggingface.co/google/gemma-4-31B-it).
- Use the model-specific chat template and validate generated tool calls and outputs in the application. Safety training and open-weight access do not supply application permissions. [Gemma 4 configuration and limitations](https://ai.google.dev/gemma/docs/core/model_card_4).

## Source evidence

- <https://huggingface.co/google/gemma-4-31B-it>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
