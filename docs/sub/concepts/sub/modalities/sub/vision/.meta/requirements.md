# Documentation Requirements

## Requirements

- Use the reader-facing title `Vision`.
- Present this node as the canonical modality owner for reusable AI concepts whose primary information domain is visual imagery and image-based structure, while keeping temporally extended video concepts under the selected sibling `video/` domain.
- Distinguish the visual modality from computer-vision model identity and architecture. Models can encode, classify, retrieve, transform, or generate visual information through many architectures; this node organizes modality-owned concepts rather than defining one model family.
- Explain that visual source data can include pixels, raster or vector imagery, rendered documents, diagrams, charts, screenshots, depth/segmentation/pose maps, or other visual representations, but model access normally occurs through preprocessing and learned representations rather than raw human-equivalent perception.
- Distinguish visual information from its storage/container format. JPEG, PNG, SVG, PDF, tensors, patch sequences, visual tokens, and latent representations are different encodings/containers and do not redefine the modality itself.
- Keep the selected descendants `image-generation/`, `image-to-image/`, `inpainting/`, and `outpainting/` as distinct concepts. `text-to-image/` remains a selected child of `image-generation/`.
- Do not infer unlisted perception, classification, detection, segmentation, OCR, or other vision children merely because they are legitimate vision tasks; exact descendants require separate architecture selection.
- Distinguish still-image vision ownership from `video/`. Video combines temporally ordered visual information and can include audio or other tracks; cross-domain relationships should be linked rather than duplicating concepts.
- Explain that image resolution, color space, crop/tiling, aspect ratio, compression, metadata, preprocessing, and model-specific visual tokenization can affect usable visual information without becoming universal modality semantics.
- Make clear that visual model output or interpretation is not automatically factual measurement or verified observation. Exact counting, geometry, identity, text/OCR, and fine-detail claims require task-appropriate evaluation and source verification.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete model capabilities, accepted image formats/resolutions, preprocessing pipelines, benchmark results, safety policies, service limits, and model-selection recommendations with their applicable catalog, runtime/service, evidence, or decision owners.

## Validation

- Vision is not equated with one model architecture, file format, or API image-input feature.
- Video remains a separate selected sibling rather than being silently absorbed into still-image vision ownership.
- Only explicitly selected/materialized vision descendants appear in canonical navigation.
- Image resolution/tokenization/preprocessing rules are not universalized across concrete models.
- Visual inference/generation is not presented as inherently factual or measurement-accurate.
- Concrete model/service support facts and benchmark outcomes remain outside the modality owner.
