# Documentation Requirements

## Requirements

- Use the reader-facing title `Vision-Language Models (VLMs)`.
- Define a vision-language model as a model or tightly integrated learned architecture that jointly represents, aligns, conditions on, transforms, or generates across visual and language information so relationships between the two modalities are part of the learned model behavior.
- Keep VLM narrower than the repository's general `multimodal-models/` category. VLMs specifically involve visual and language modalities; multimodal models can combine audio, speech, video, sensor, action, or other modalities without necessarily being vision-language models.
- Do not define VLMs only as large language models with image input. The category also includes contrastive/dual-encoder image-text models, captioning and visual-question-answering architectures, encoder-decoder systems, multimodal instruction-following/generative models, and other learned vision-language designs.
- Distinguish a VLM from a pipeline that merely runs an independent vision/OCR model and inserts its text output into an unrelated language model. Such a system is multimodal at the application level, but the individual models are not automatically VLMs unless their learned architecture/training establishes a vision-language relationship.
- Explain that visual information can enter through pixels, image/video patches, learned visual tokens/features, region/object representations, or other encoded forms, while language can be represented through text tokens or related language representations. One tokenization/connector/projector architecture is not universal.
- Explain common relationship/training families without making one mandatory: paired image-text contrastive alignment, cross-modal matching, captioning/generative objectives, masked modeling, instruction tuning, multimodal pretraining, and combinations.
- Distinguish understanding/retrieval-oriented VLMs from generative VLMs. A model that embeds or ranks image-text pairs need not generate natural-language answers, while a generative VLM can produce text or other outputs conditioned on visual-language context.
- Distinguish model capability from interface support. A provider/API accepting image attachments is not sufficient evidence about the exact visual encoder, resolution policy, token budget, video support, OCR behavior, grounding fidelity, or underlying model architecture; those are concrete model/service facts.
- Explain that preprocessing can resize, crop, tile, sample frames, transcode, compress, OCR, or otherwise transform visual inputs before learned processing, and those transformations can materially affect accessible detail. Do not imply that every input pixel/frame is represented at original fidelity.
- Make clear that vision-language capability does not guarantee exact OCR, counting, spatial measurement, visual grounding, chart interpretation, fine-detail inspection, or factual inference. Evaluate each concrete model on the target visual-language task and input conditions.
- Distinguish VLM identity from `multimodal-context/`. A VLM is a model-classification concept; multimodal context describes the combination of modality-bearing information available during a particular interaction or inference.
- Keep concrete VLM/model identities, image/token limits, supported file types, preprocessing rules, benchmark scores, safety behavior, service features, and model-selection recommendations with their applicable catalog, evidence, service, or decision owners.
- Use the canonical entity references as research inputs for visual-language model scope and the distinction between VLMs and broader multimodal/LLM-only categories when reader-facing rendering is activated.

## Validation

- VLM is not used as a synonym for every multimodal model or every LLM that appears in a multimodal application pipeline.
- A language-generating/chat architecture is not required by definition.
- One projector, visual-token, encoder, resolution, or training-objective design is not universalized.
- API attachment support is not treated as complete evidence of model architecture or visual fidelity.
- Visual-language capability is not presented as proof of exact OCR, counting, grounding, or measurement reliability.
- VLM model identity remains distinct from multimodal context and concrete provider/model support facts.
