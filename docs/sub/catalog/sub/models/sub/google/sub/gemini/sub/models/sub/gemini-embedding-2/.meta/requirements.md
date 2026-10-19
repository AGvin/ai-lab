# Documentation Requirements

## Requirements

- Identify Gemini Embedding 2 as Google's stable multimodal embedding model, generally available since 2026-04-22.
- Preserve its source-backed role mapping text, images, video, audio, and PDF/document inputs into a unified embedding space for retrieval, similarity, classification, clustering, and related applications.
- Keep preview predecessor identifiers separate from the stable `gemini-embedding-2` model identity rather than materializing them as current peer models.
- Treat token limits, output dimensions, modality limits, API availability, and product integration as mutable/version-sensitive facts.

## Validation

- Gemini Embedding 2 is not described as preview based on stale preview documentation; current first-party model/deprecation documentation identifies `gemini-embedding-2` as stable.
- The model is not conflated with vector databases, managed retrieval services, or RAG methodology.

## Verified identity and provenance

Stable multimodal embedding model served as gemini-embedding-2; output vectors support retrieval and similarity tasks rather than generated conversational answers.

## Source-scoped operating boundaries

- The model accepts text, images, audio, video, and PDFs with an 8,192-token input limit. Output dimensionality is configurable from 128 to 3,072; Google recommends 768, 1,536, or 3,072. Preserve dimensionality and model identity when comparing or maintaining an index. [Embedding model reference](https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2).
- Use the stable gemini-embedding-2 identity. The preview endpoint's listed shutdown was August 10, 2026; a stale preview label in an overview is not evidence of current preview-only status. [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Embedding similarity is a retrieval signal, not a correctness guarantee, access-control decision, or guarantee that source material is anonymous.

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2>
- <https://ai.google.dev/gemini-api/docs/deprecations>
