# Documentation Requirements

## Identity and provenance

- Cohere Transcribe 03-2026 is a 2B speech-to-text model covering fourteen languages.
- The public card explicitly credits Cohere and Cohere Labs. It describes a large Conformer encoder with a lightweight Transformer decoder, trained from scratch with supervised cross-entropy, and identifies cohere-transcribe-03-2026. [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe).
- The official Arabic release is explicitly a fine-tune of this general model. The has-derivative relation targets the exact July 2026 Arabic model, not an undated family or a presumed June alias. [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic) [Cohere Transcribe Arabic model card public metadata](https://huggingface.co/api/models/CohereLabs/cohere-transcribe-arabic-07-2026?blobs=true).

## Operational decision boundaries

- The documented languages are Arabic, Chinese, Dutch, English, French, German, Greek, Italian, Japanese, Korean, Polish, Portuguese, Spanish and Vietnamese. The model does not provide automatic language detection, timestamps or speaker diarization. [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe) [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026).
- The processor resamples audio to 16kHz and averages stereo channels. Preselect the language and validate chunking and transcription quality on the intended speech; upload size is an endpoint constraint, not a text context window. [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe).
- Weights state Apache 2.0. The current model table lists the versioned API as live; local Transformers/vLLM workflows and hosted deployment have separate runtime and capacity requirements. Accuracy and throughput claims were not reproduced. [Cohere Transcribe model card](https://huggingface.co/CohereLabs/cohere-transcribe-03-2026) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Cohere Transcribe documentation](https://docs.cohere.com/docs/transcribe).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
