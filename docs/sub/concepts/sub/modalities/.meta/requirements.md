# Documentation Requirements

## Requirements

- Use the reader-facing title `AI Modalities`.
- Present this domain as the canonical owner for reusable concepts organized by the kind of information or signal an AI system consumes, represents, relates, transforms, or produces, including language, vision, audio/speech, video, and multimodal combinations selected by the repository architecture.
- Define a modality as a form/channel of information with its own representation and structure relevant to model input, output, learning, or interaction; do not treat `modality` as a model architecture, provider feature, file format, or deployment mode.
- Explain that physical source media and model representations are distinct. Text, pixels, waveforms, frames, documents, or sensor signals can be tokenized, encoded, sampled, transformed, or compressed before becoming model-consumable representations.
- Distinguish modality concepts from model classification. A model can support one or several modalities, while the modality domain owns reusable knowledge about the information type/task rather than the concrete model identity.
- Distinguish modality from application/system composition. A system can combine several single-modality components and be multimodal at the application level without every component being a multimodal model.
- Keep the selected direct-child domains `language/`, `vision/`, `audio-and-speech/`, `video/`, and `multimodal/` conceptually distinct. Materialize and navigate only children that currently have substantive canonical content.
- Explain that boundaries can overlap in real systems: speech carries language through audio, video contains visual frames and often audio, and documents can contain text and images. Primary ownership follows the repository taxonomy while cross-domain relationships are expressed through links/relations rather than duplicate canonical definitions.
- Avoid universal assumptions about token accounting, fidelity, sampling rate, resolution, context cost, supported formats, or preprocessing. Those are concrete model/runtime/service facts unless a child concept owns a stable general principle.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete model/service modality support, file/container formats, codec limits, preprocessing implementations, benchmarks, prices, and model-selection guidance with their applicable catalog, specification, runtime, evidence, or decision owners.

## Validation

- Modality is not equated with model architecture, file format, API attachment support, or deployment mode.
- Source media is distinguished from internal model representation.
- A multimodal application pipeline is not automatically described as a single multimodal model.
- Overlapping information types do not create duplicate canonical ownership.
- Concrete support matrices, limits, prices, formats, and preprocessing rules remain outside the abstract modality owner.
- Direct-child navigation contains only currently materialized selected descendants.
