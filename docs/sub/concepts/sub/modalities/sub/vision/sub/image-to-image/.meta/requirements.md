# Documentation Requirements

## Requirements

- Use the reader-facing title `Image-to-Image Generation` and introduce `image-to-image translation` / `image-to-image` as common related names.
- Define image-to-image generation as a learned transformation in which an existing source image or image-like spatial representation is a defining condition for synthesizing a target image while preserving, translating, restyling, reconstructing, or otherwise changing selected source information.
- Keep the concept architecture-neutral. Conditional GANs, autoregressive/transformer models, diffusion/score-based methods, flow/matching methods, encoder-decoder systems, and hybrids can implement image-to-image transformations.
- Do not define image-to-image through diffusion-specific partial noising or a `denoising strength` control. Those are common implementation/UI patterns for some diffusion systems rather than universal operation semantics.
- Explain that the source and target can belong to the same visual domain or different domains/representations, including photo-to-photo variation, sketch/edge/label/depth/map-to-image translation, colorization, style/domain translation, restoration, or other learned mappings.
- Distinguish paired from unpaired training. Some image-to-image methods learn from aligned source-target pairs, while others learn mappings from unpaired domain collections or use pretrained/generative priors; one supervision regime is not universal.
- Explain that preservation and transformation are method/task-specific. The source image can constrain layout, geometry, identity, color, style, semantics, or only a subset of features; image conditioning does not imply pixel-perfect preservation.
- Distinguish image-to-image from `inpainting/`. Inpainting specifically owns filling/reconstructing a designated missing/masked region while surrounding image context is intended to constrain the completion.
- Distinguish image-to-image from `outpainting/`. Outpainting specifically owns extending generated content beyond an existing image boundary/canvas while using the original image as contextual constraint.
- Explain that text prompts, masks, reference embeddings, structural maps, labels, or other controls can be added to an image-conditioned transformation without changing the operation's primary image-to-image ownership when the source image remains the defining condition.
- Make clear that stochastic or learned transformations can drift in identity, geometry, typography, fine detail, color, or source semantics. Strong visual similarity is separate from semantic correctness and task acceptance.
- Keep concrete denoising strengths, guidance values, prompt recipes, checkpoint compatibility, preprocessing/aspect-ratio behavior, model architectures, training datasets, benchmark results, and editing workflows with their applicable catalog, runtime, evidence, learning, or decision owners.
- Use the canonical entity references as research inputs for paired and unpaired image-to-image transformation boundaries when reader-facing rendering is activated.

## Validation

- Image-to-image is not defined only through diffusion/noising or one `strength` parameter.
- Paired supervision, unpaired supervision, text prompting, style transfer, or one source-target domain is not required universally.
- A source image condition is not presented as guaranteeing pixel-perfect identity or geometry preservation.
- Inpainting and outpainting remain distinct selected sibling concepts with narrower spatial contracts.
- Concrete runtime controls, model recipes, training datasets, and benchmark outcomes remain outside the abstract image-to-image owner.
