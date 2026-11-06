# Documentation Requirements

## Requirements

- Identify Gemma 4 12B Unified Instruct using the exact canonical identity and official model or artifact identifier.
- Preserve membership in `catalog/models/google/gemma/gemma-4` and producer provenance through that family or series.
- Keep the trained model separate from API routes, products, deployment configurations, and optimized artifacts.

## Validation

- Every concrete model identifier and capability is supported by a current primary source.
- Access restrictions, license scope, and unsupported capabilities remain explicit.
- Model-generated output or tool requests do not establish application authorization.

## Verified identity and provenance

Gemma 4 12B Unified Instruct is the 11.95B-parameter encoder-free dense multimodal instruction model; raw image patches and audio inputs use lightweight projections rather than separate modality encoders.

## Source-scoped operating boundaries

- Text, image, audio, and frame-based video input produce text with 256K context. The unified architecture changes encoder and runtime requirements; it does not imply support in a runtime that only understands earlier Gemma layouts. [Official checkpoint card](https://huggingface.co/google/gemma-4-12B-it).
- Apache-2.0 applies to the released checkpoint. Published model size does not include all runtime memory, KV cache, or workload overhead; verify the exact artifact, precision, and context configuration before deployment. [Official checkpoint card](https://huggingface.co/google/gemma-4-12B-it).
- Use the model-specific chat template and validate generated tool calls and outputs in the application. Safety training and open-weight access do not supply application permissions. [Gemma 4 configuration and limitations](https://ai.google.dev/gemma/docs/core/model_card_4).

## Source evidence

- <https://huggingface.co/google/gemma-4-12B-it>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
