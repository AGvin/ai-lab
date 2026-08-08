# Documentation Requirements

## Requirements

- Identify Gemma 4 E4B Instruct as a concrete dense instruction-tuned multimodal model in the Gemma 4 generation.
- Preserve intrinsic model facts and official artifact identity from the legacy E4B documentation.
- Keep contextual scale classification, hardware fit, runtime behavior, VRAM planning, and model-selection conclusions outside the canonical model profile.
- Do not invent a total-parameter value when the current migration pass has not independently confirmed one.

## Content Specification

- Use `Gemma 4 E4B Instruct` as the page title.
- Link the canonical Gemma 4 generation.
- Preserve the dense architecture classification and the 4B effective-parameter identity.
- Preserve the 128K context length.
- Preserve text, image, and audio input with text output.
- Preserve Apache-2.0 licensing from the represented Gemma 4 release.
- Preserve the official `google/gemma-4-e4b-it` model page.
- Preserve the official `google/gemma-4-e4b-it-qat-q4_0-unquantized` QAT distribution and the legacy published size of approximately 3.68 GB.
- Explain that the QAT file includes model tensors plus multimodal components such as the vision encoder; file size is therefore an artifact property and not a complete RAM/VRAM estimate.
- State that `E4B` denotes effective parameters and that a distinct total-parameter figure should be added only when independently verified.

## Excluded Residual Content

Preserve outside this canonical model profile:

- contextual AI Lab `SLM` classification;
- RAM/VRAM, KV-cache, runtime-buffer, encoder, concurrency, and hardware-fit conclusions;
- recommendations for local, edge, or other deployment classes;
- runtime compatibility, quantization-performance, throughput, latency, or quality conclusions;
- model-selection and accepted-result-cost guidance.

## Validation

- Effective parameter count is not presented as total model size.
- Published QAT file size is not equated with runtime memory requirement.
- No total-parameter value is inferred without source confirmation.
- Hardware and selection conclusions are not presented as intrinsic model facts.
- The `member-of` relation resolves to Gemma 4.
