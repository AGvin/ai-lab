# Documentation Requirements

## Requirements

- Identify Gemma 4 E4B Instruct as a concrete dense instruction-tuned multimodal model in the Gemma 4 series.
- Preserve current source-backed model facts and distinct official artifact identities.
- Keep hardware fit, runtime behavior, VRAM planning, and selection conclusions outside the canonical model profile.

## Content Specification

- Use `Gemma 4 E4B Instruct` as the page title and link the Gemma 4 series.
- Preserve 4.5B effective parameters and 8B parameters including embeddings as distinct values.
- Preserve 42 layers, 512-token sliding window, 128K context, text/image/audio input, text output, approximately 150M vision-encoder parameters, and approximately 300M audio-encoder parameters.
- Preserve Apache-2.0 licensing from the current Gemma 4 model card.
- Preserve the official base-model page, the QAT-trained unquantized Safetensors repository, and the separate official QAT Q4_0 GGUF repository.
- Keep artifact identities separate: the QAT-trained unquantized repository is not the GGUF Q4_0 package.
- Record current Hub file evidence with verification scope/date when useful: the unquantized QAT repository exposes a 15.9 GB `model.safetensors`; the official GGUF repository exposes a 5.15 GB Q4_0 model file plus a 992 MB multimodal projector in the verified 2026-08-11 tree.
- Treat repository/file size only as artifact evidence, never as peak RAM/VRAM or complete runtime-memory requirement.

## Validation

- Effective parameters are not presented as complete total-parameter identity.
- Parameters including embeddings are not equated with artifact size or VRAM requirements.
- The unquantized QAT repository is not assigned the legacy GGUF size and the GGUF artifact is not omitted.
- The GGUF model file and required multimodal projector remain distinct components.
- Published artifact/file size is not equated with runtime memory requirement.
- Hardware and selection conclusions are not presented as intrinsic model facts.

## Verified identity and provenance

Instruction-tuned Gemma 4 checkpoint google/gemma-4-E4B-it with 4.5B effective parameters and 8B parameters including embeddings; QAT and GGUF packages remain separate artifacts.

## Source-scoped operating boundaries

- The checkpoint accepts text, image, and audio input and generates text with 128K context. The current card limits audio to 30 seconds and frame-based video to 60 seconds at one frame per second. [Official checkpoint card](https://huggingface.co/google/gemma-4-E4B-it).
- Keep the original instruction checkpoint, QAT-trained unquantized Safetensors, Q4_0 GGUF model, and multimodal projector distinct. Published file sizes are historical artifact evidence, not peak RAM/VRAM; an optimized runtime must support the selected architecture and modalities. [Official checkpoint and artifacts](https://huggingface.co/google/gemma-4-E4B-it).
- Apache-2.0 and the model's safety training do not supply application permissions or guarantee correct output. Validate model-generated tool calls before execution. [Configuration and safety guidance](https://ai.google.dev/gemma/docs/core/model_card_4).

## Source evidence

- <https://huggingface.co/google/gemma-4-E4B-it>
- <https://ai.google.dev/gemma/docs/core/model_card_4>
