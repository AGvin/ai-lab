# North Micro Vision Instruct

North Micro Vision Instruct is a compact open-weight model for interleaved text and images, with text output.

## Identity and provenance

The current card credits Cohere and names CohereLabs/North-Micro-Vision-Instruct. Its publishing namespace does not by itself add a Cohere Labs development claim. The reported 2.4B scale combines a 2B language model and a 400M vision encoder. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

The vision encoder is custom-trained starting from google/siglip2-so400m-patch16-384. This exact component is not the patch16-512 encoder named by A Vision or the patch14-384 encoder named by Aya Vision. The exact Google parent is now materialized with reciprocal component-scoped lineage. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct) [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025) [Aya Vision 8B model card](https://huggingface.co/CohereLabs/aya-vision-8b).

## Decision and operating boundaries

- The card states Apache 2.0 weights, native-resolution/aspect-ratio processing, multiple images and multilingual support. It distinguishes the language backbone’s 128K context from a multimodal training and validated range of 8K; longer multimodal use is not established by the backbone number. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- The reviewed card requires Transformers 5.16.0 and documents processor-based image preparation. Match the current model revision, processor and runtime; runtime compatibility and output quality were not executed or measured in this audit. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- It is positioned for prototyping and task-specific adaptation. OCR, grounding, charts and fine visual detail need representative evaluation. A video preprocessor file is not evidence of a released video-understanding capability, and the model does not generate images. [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

## Vision-component provenance

The exact Google `google/siglip2-so400m-patch16-384` vision initialization is now materialized with a reciprocal derived-from relation. This is component-scoped: no Google text-tower inclusion, sole ancestry, inherited fixed-resolution behavior or downstream license transfer is implied. [Exact component training evidence](https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct).

## Catalog relations

- [SigLIP 2 So400m patch16 384](../../../../../../../google/sub/siglip-2/sub/models/sub/siglip2-so400m-patch16-384/) — source of the adapted vision component.
- [North](../../../../) — series or family.

## Official resources

- [Cohere models overview](https://cohere.com/models-overview).
- [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
- [Command A Vision model card](https://huggingface.co/CohereLabs/command-a-vision-07-2025).
- [Aya Vision 8B model card](https://huggingface.co/CohereLabs/aya-vision-8b).
