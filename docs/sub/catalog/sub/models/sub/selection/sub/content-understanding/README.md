# Content Understanding Model Selection

Choose models for understanding images, video, speech, audio, and documents by measurable coverage, grounding, provenance, and error requirements.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Task scope

This area covers image understanding, video understanding, speech and speaker analysis, audio understanding, and document understanding, including OCR-adjacent interpretation, visual question answering, layout reasoning, event analysis, transcription-adjacent understanding, and structured extraction.

Use deterministic tools first when they can prove a property: native text extraction, OCR output, parsers, schema validation, media metadata, geometry, accessibility/DOM state, timestamps, and checksums. Models should interpret ambiguous evidence rather than replace available validators.

## Evaluation dimensions

Define the exact modality, resolution, page/frame/clip sampling, audio conditions, evidence localization, output schema, and acceptable uncertainty. Measure relevant field, region, page, frame, or event coverage together with precision, recall, omission, hallucination, and inconclusive rates.

For documents and OCR-adjacent work, preserve reading order, table/form structure, page linkage, figure/caption association, and source-region provenance. For video/audio, define temporal sampling and do not infer absence of an event outside sampled regions.

A model accepting a modality is not proof that it is reliable for the required understanding task. Link intrinsic capabilities and limits from [Model Reference](../../../reference/) and keep task evidence here.
