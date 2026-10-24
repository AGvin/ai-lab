# Documentation Requirements

## Requirements

- Identify Voxtral Small 24B 2507 as a distinct released trained-model identity from Mistral AI.
- Render the standard entity-relations block from validated canonical metadata.
- Keep model-specific specifications, artifact representations and hosted access context distinct.

## Validation

- The entity ID matches the canonical path and reciprocal relations resolve.
- Claims stay at the documented release scope, and generated output is not treated as a correctness or security guarantee.

## Source-backed profile

- Required reader orientation: Voxtral Small 24B 2507 is Mistral AI’s July 2025 audio-and-text instruction model for transcription, translation, questions and summaries.
- Preserve this model-scoped fact: The Apache 2.0 weights belong to the Voxtral family; the GA API release is `voxtral-small-2507` with a 32K-token context. [Voxtral Small model card](https://docs.mistral.ai/models/voxtral-small-25-07) [Voxtral Small weights and audio-instruction limitations](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)
- Preserve this model-scoped fact: The model supports audio understanding and function calling, rather than only verbatim speech transcription. [Voxtral Small weights and audio-instruction limitations](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)

## Operational and interpretation boundaries

- Explain this boundary: The released model card says system prompts are not supported. Do not assume the instruction-boundary behavior of general chat models. [Voxtral Small weights and audio-instruction limitations](https://huggingface.co/mistralai/Voxtral-Small-24B-2507)
- Explain this boundary: Spoken tool requests require application authorization and argument validation. A voice instruction alone does not authenticate the speaker. [Function-calling contract](https://docs.mistral.ai/studio/conversations/function-calling)

- Keep source-reported capabilities distinct from application-level correctness, authorization and measured deployment performance.
