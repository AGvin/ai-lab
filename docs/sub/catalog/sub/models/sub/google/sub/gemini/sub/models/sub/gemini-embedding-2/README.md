# Gemini Embedding 2

Gemini Embedding 2 is Google's stable multimodal embedding model, generally available since 2026-04-22.

## Relations

- Member of: [Gemini](../../../../)

## Official resources

- <https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2>
- <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-embedding-2-generally-available/>
- <https://ai.google.dev/gemini-api/docs/deprecations>

## Source-scoped operating boundaries

- The model accepts text, images, audio, video, and PDFs with an 8,192-token input limit. Output dimensionality is configurable from 128 to 3,072; Google recommends 768, 1,536, or 3,072. Preserve dimensionality and model identity when comparing or maintaining an index. [Embedding model reference](https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2).
- Use the stable gemini-embedding-2 identity. The preview endpoint's listed shutdown was August 10, 2026; a stale preview label in an overview is not evidence of current preview-only status. [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Embedding similarity is a retrieval signal, not a correctness guarantee, access-control decision, or guarantee that source material is anonymous.
