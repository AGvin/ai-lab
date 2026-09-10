# Documentation Requirements

## Requirements

- Use the reader-facing title `Multimodal Models`.
- Define a multimodal model at model level: a model that processes and relates information across more than one modality, with modalities potentially appearing as inputs, conditioning signals, learned representations, or outputs.
- Use examples such as language/text, images/vision, audio/speech, video, touch, or other sensor signals without treating that list as exhaustive or requiring every multimodal model to support the same modalities.
- Distinguish a multimodal model from a multimodal AI system that merely coordinates separate unimodal models or services. A system can be multimodal without every constituent model itself being multimodal.
- Explain that multimodal architectures can relate modalities through different representation, alignment, fusion, translation, or cross-modal mechanisms; do not require one shared embedding space, one fusion stage, or one architectural pattern as part of the category definition.
- Distinguish supported input modalities from supported output modalities and from cross-modal reasoning capability. Accepting an image or generating audio does not by itself establish equal competence across all supported modalities or all cross-modal tasks.
- Explain that modality-specific preprocessing, tokenization/encoding, compression, resolution, sampling, duration, context allocation, or sensor characteristics can constrain what information is actually available to the model, without turning this classification concept into an implementation guide.
- Keep multimodal status separate from foundation-model role, language-model identity and scale, vision-language specialization, architecture, frontier status, deployment mode, access/licensing, and concrete task performance.
- Keep concrete modality limits, model-specific formats, current benchmark results, runtime compatibility, application recipes, and model-selection recommendations with their applicable catalog, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for definition and multimodal-design boundaries when reader-facing rendering is activated.

## Validation

- The page does not classify a complete multimodal system as one multimodal model merely because separate unimodal components are orchestrated together.
- The page does not require one particular fusion mechanism, shared representation, architecture, or set of modalities.
- The page does not infer equivalent competence across modalities from nominal multimodal support.
- The page does not use `multimodal`, `vision-language`, `foundation`, `LLM`, or `frontier` as interchangeable classifications.
- Legacy application examples and model-selection guidance are not duplicated into this canonical classification node.
