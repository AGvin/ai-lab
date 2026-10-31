# Documentation Requirements

## Identity and provenance

- Cohere Transcribe Arabic 07-2026 is a 2B fine-tune for Arabic dialects, English and Arabic–English code-switched speech.
- The official release explicitly calls it a fine-tune of Cohere Transcribe, and the public metadata names cohere-transcribe-03-2026 as its base. The card credits Cohere and Cohere Labs. [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic) [Cohere Transcribe Arabic model card public metadata](https://huggingface.co/api/models/CohereLabs/cohere-transcribe-arabic-07-2026?blobs=true) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026).
- The current card, documentation and live API table agree on cohere-transcribe-arabic-07-2026. One launch-page link instead contains 06-2026; that inconsistent link is not treated as another model or an established alias. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic).

## Operational decision boundaries

- The supported scope is Arabic dialects and English, including code-switching. It does not inherit the general model’s fourteen-language coverage, and the documentation says timestamps and speaker diarization are unavailable. [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026).
- Audio preprocessing resamples to 16kHz and combines stereo channels into mono. Follow the selected runtime’s language and chunking controls, then evaluate dialect, accent and mixed-language transcription on representative audio. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).
- Weights state Apache 2.0 and the architecture remains a Conformer encoder with a lightweight text decoder. Hosted API access and Model Vault deployment have their own service limits; this audit did not run inference or reproduce the source’s accuracy claims. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
