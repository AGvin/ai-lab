# FLUX 3 Image Klein Prompt Upsampler

FLUX 3 Image Klein Prompt Upsampler is Black Forest Labs' separately trained 9B vision-language prompt-rewriting model derived from post-trained Qwen3.5-9B. It is a learned upstream prompt component for the Klein image pipeline, distinct from its image generator and Qwen3-VL-4B-Instruct text encoder.

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `produced-by` | [Black Forest Labs](../../../../../producers/sub/b/sub/black-forest-labs/README.md) | `organization` |
| `derived-from` | [Qwen3.5-9B](../../../alibaba/sub/qwen/sub/qwen3-5/sub/models/sub/qwen3-5-9b/README.md) | `model` |

## Training and input/output

BFL describes a full fine-tune of [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) with the vision tower frozen, supervised request-to-prompt training followed by preference tuning on prompts assessed through generated images. The [original component card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) specifies a short request, up to ten reference images and optional bounding boxes as inputs, with one English prompt as output. Four supplied system prompts select generation/editing and layout modes; those modes and quantizations do not create four new learned models.

## Pipeline and license boundary

Prompt upsampling is part of BFL's intended generation/editing/layout workflow. The [reference implementation](https://github.com/black-forest-labs/flux-3-image-klein) loads this model by default, while BFL permits another LLM with its supplied system prompts. This model's Apache-2.0 license does not replace the separate Klein image-generator FLUX Kommunity terms. The component produces text, not the final image; it is not a weight-derived FLUX image generator or FLUX 3 series backbone.

## Use and limitations

Pin weights, processor, system-prompt and runtime revisions; account for prompt-model execution separately from generator memory/latency. In a runtime without automatic upsampling, run the prompt component explicitly before image generation. Reference resizing can lose small details and output is English. BFL says the model does not refuse requests; optional wrapper checks are not proof that every loader enables filtering. Review rewritten prompts and final output, verify the actual local/remote data route before using confidential inputs, and keep tool execution behind application permissions. [Official limitations](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup#limitations). No independent inference, benchmark, all-runtime compatibility or beneficial-owner verification is claimed.

## Pipeline navigation

- [Klein generator](../flux/sub/flux-3/sub/models/sub/flux-3-image-klein/README.md)
- [Klein Base generator](../flux/sub/flux-3/sub/models/sub/flux-3-image-klein-base/README.md)

These are downstream application links, not training-lineage or series-membership claims.

## Official resources

- [flux-3-image-klein-pup original model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup)
- [BFL reference inference repository](https://github.com/black-forest-labs/flux-3-image-klein)
- [Qwen3.5-9B original model card](https://huggingface.co/Qwen/Qwen3.5-9B)
- [flux-3-image-klein-pup weight and processor files](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/tree/main)
