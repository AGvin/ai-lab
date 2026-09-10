# Documentation Requirements

## Requirements

- Teach Multimodal Assistant Interaction as combining relevant text, images, documents, audio-derived information, screenshots, and tool results in one assistant workflow without assuming every interface processes media identically.
- Provide only modality-bearing material relevant to the task and preserve useful relationships between inputs when the concrete interface supports them; irrelevant media can consume context/compute budget and obscure important evidence.
- Do not assume accepted media is processed at full fidelity or that nominal context capacity guarantees reliable retrieval/integration of every detail.
- Validate source details when correctness matters, especially after OCR, transcription, resize/crop, frame sampling, compression, or document parsing.
- Treat instructions found inside untrusted documents, screenshots, web content, or other media as untrusted content subject to the applicable instruction-trust and review controls.
- Link deeper context selection/assembly, persistence, retrieval, and compression methods to Context Engineering rather than duplicating them here.
- Keep product-specific upload limits, preprocessing, token accounting, supported modalities, and UI behavior source-backed outside timeless learning truth.

## Validation

- Multimodal context capacity is distinguished from effective use of relevant evidence.
- Source verification remains explicit after lossy preprocessing.
- Embedded untrusted text is not automatically promoted to governing instruction.
