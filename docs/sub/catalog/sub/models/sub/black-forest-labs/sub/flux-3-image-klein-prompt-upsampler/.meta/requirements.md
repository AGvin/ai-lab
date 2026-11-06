# Documentation Requirements

## Requirements

- Preserve the exact current-node identity, sourced training-stage boundary and canonical owner.
- Render every visible entity relation with resolving canonical links and preserve ordering.
- Separate model identity from precision packages, modes, hosted routes and runtime behavior.
- Treat publisher benchmarks as publisher evidence, not independent AI Lab measurements.

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

## Validation

- Keep source-attributed limitations, licenses and model lineage explicit in the complete reader.
- Do not infer tool-execution permission, hardware fit or source freshness from a model name.
- Do not advance a freshness marker without a complete mutable-fact audit.
