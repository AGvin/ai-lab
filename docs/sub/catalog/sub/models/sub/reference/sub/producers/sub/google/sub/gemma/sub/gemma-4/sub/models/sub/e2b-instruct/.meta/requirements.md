# Documentation Requirements

## Requirements

- Identify Gemma 4 E2B Instruct as a concrete dense instruction-tuned multimodal model in the Gemma 4 series.
- Preserve current source-backed model facts and official artifact identity.
- Keep hardware fit, runtime behavior, VRAM planning, and selection conclusions outside the canonical model profile.

## Content Specification

- Use `Gemma 4 E2B Instruct` as the page title and link the Gemma 4 series.
- Preserve 2.3B effective parameters and 5.1B parameters including embeddings as distinct values.
- Preserve 35 layers, 512-token sliding window, 128K context, text/image/audio input, text output, approximately 150M vision-encoder parameters, and approximately 300M audio-encoder parameters.
- Preserve Apache-2.0 licensing from the current Gemma 4 model card.
- Preserve the official model page and QAT artifact reference.
- Preserve the legacy published QAT size only as artifact evidence, not as runtime memory.

## Validation

- Effective parameters are not presented as the complete total-parameter identity.
- Parameters including embeddings are not equated with artifact size or VRAM requirements.
- Published QAT file size is not equated with runtime memory requirement.
- Hardware and selection conclusions are not presented as intrinsic model facts.
