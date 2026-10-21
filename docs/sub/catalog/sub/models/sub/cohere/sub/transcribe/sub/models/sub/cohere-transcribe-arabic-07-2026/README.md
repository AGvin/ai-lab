# Cohere Transcribe Arabic

Cohere Transcribe Arabic 07-2026 is a 2B fine-tune for Arabic dialects, English and Arabic–English code-switched speech.

## Identity and provenance

The official release explicitly calls it a fine-tune of Cohere Transcribe, and the public metadata names cohere-transcribe-03-2026 as its base. The card credits Cohere and Cohere Labs. [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic) [Cohere Transcribe Arabic model card public metadata](https://huggingface.co/api/models/CohereLabs/cohere-transcribe-arabic-07-2026?blobs=true) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026).

The current card, documentation and live API table agree on cohere-transcribe-arabic-07-2026. One launch-page link instead contains 06-2026; that inconsistent link is not treated as another model or an established alias. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic).

## Decision and operating boundaries

- The supported scope is Arabic dialects and English, including code-switching. It does not inherit the general model’s fourteen-language coverage, and the documentation says timestamps and speaker diarization are unavailable. [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic) [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026).
- Audio preprocessing resamples to 16kHz and combines stereo channels into mono. Follow the selected runtime’s language and chunking controls, then evaluate dialect, accent and mixed-language transcription on representative audio. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).
- Weights state Apache 2.0 and the architecture remains a Conformer encoder with a lightweight text decoder. Hosted API access and Model Vault deployment have their own service limits; this audit did not run inference or reproduce the source’s accuracy claims. [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026) [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).

## Catalog relations

- [Cohere Labs](../../../../../../../../../producers/sub/c/sub/cohere-labs/) — producer.
- [Cohere Transcribe](../../../../) — series or family.
- [Cohere Transcribe](../cohere-transcribe-03-2026/) — derived from.

## Official resources

- [Cohere Transcribe Arabic documentation](https://docs.cohere.com/v2/docs/transcribe-arabic).
- [Transcribe Arabic release](https://docs.cohere.com/changelog/transcribe-arabic).
- [Cohere Transcribe Arabic model card public metadata](https://huggingface.co/api/models/CohereLabs/cohere-transcribe-arabic-07-2026?blobs=true).
- [Cohere Transcribe Arabic model card](https://huggingface.co/CohereLabs/cohere-transcribe-arabic-07-2026).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
