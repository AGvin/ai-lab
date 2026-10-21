# Documentation Requirements

## Identity and provenance

- North Micro Vision Instruct is a compact open-weight model for interleaved text and images, with text output.
- The current card credits Cohere and names CohereLabs/North-Micro-Vision-Instruct. Its publishing namespace does not by itself add a Cohere Labs development claim. The reported 2.4B scale combines a 2B language model and a 400M vision encoder. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- The vision encoder is custom-trained starting from google/siglip2-so400m-patch16-384. This exact component is not the patch16-512 encoder named by A Vision or the patch14-384 encoder named by Aya Vision. No absent Google model node is invented for this source-only dependency. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Aya Vision 8B model card](https://huggingface.co/CohereLabs/aya-vision-8b).

## Operational decision boundaries

- The card states Apache 2.0 weights, native-resolution/aspect-ratio processing, multiple images and multilingual support. It distinguishes the language backbone’s 128K context from a multimodal training and validated range of 8K; longer multimodal use is not established by the backbone number. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- The reviewed card requires Transformers 5.16.0 and documents processor-based image preparation. Match the current model revision, processor and runtime; runtime compatibility and output quality were not executed or measured in this audit. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- It is positioned for prototyping and task-specific adaptation. OCR, grounding, charts and fine visual detail need representative evaluation. A video preprocessor file is not evidence of a released video-understanding capability, and the model does not generate images. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

## Validation

- Preserve this canonical ID, type, aliases and prior relation membership; apply only the exact source-backed additive provenance and derivative repairs assessed for this node.
- Render every visible current-entity relation through the standard entity-relations contract, respecting explicit order and deterministic target-name ordering; resolve every local reader link.
- Project the complete identity and operating contract into the English reader. Attribute current limits and licenses to their precise source and distinguish models, artifacts, organizations and services.
- This documentation assessment grants no runtime, benchmark, downloaded-weight verification, cache, final-rendering, clean-pass or final-gate credit.
