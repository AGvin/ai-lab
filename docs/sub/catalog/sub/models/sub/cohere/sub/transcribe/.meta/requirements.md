# Documentation Requirements

## Identity and provenance

- Cohere Transcribe groups the general multilingual and Arabic-specialized speech-recognition models.
- The materialized members are the March 2026 general model and the July 2026 Arabic fine-tune. Their public cards explicitly credit Cohere and Cohere Labs and state Apache 2.0 weights. [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic).

## Operational decision boundaries

- Both accept audio and emit text, but the general model’s fourteen-language coverage does not transfer to the Arabic specialist. Neither documented model supplies timestamps or speaker diarization. [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).
- Audio resampling, channel conversion, language selection and chunking are implementation steps. Hosted Audio Transcriptions API limits and Model Vault capacity are separate service constraints; Apache weight licensing is not a service-level guarantee. [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
