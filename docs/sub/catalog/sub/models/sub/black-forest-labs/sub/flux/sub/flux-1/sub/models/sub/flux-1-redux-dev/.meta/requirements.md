# Documentation Requirements

## Identity and provenance

- Identify the separately released learned image-variation adapter `black-forest-labs/FLUX.1-Redux-dev`, not a full FLUX.1 generator or serving preset. [Official checkpoint](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev) [BFL release](https://bfl.ai/blog/24-11-21-tools).
- BFL's reference image-variation guide explicitly lists FLUX.1-dev and FLUX.1-schnell as compatible base generators. Do not invent a trained `derived-from` edge to one generator: runtime compatibility is not training lineage. [Reference implementation](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md).
- Render one canonical model identity and its series membership, with a resolving reader link and a single inverse. Do not misclassify Redux's separately learned adapter weights as an alternate format/quantization of FLUX.1-dev.

## Operational decision boundaries

- The open-weight pipeline combines the Redux image adapter with the chosen FLUX.1 base model and autoencoder; BFL's reference command specifies `FLUX_REDUX`, `FLUX_MODEL` and `FLUX_AE`. The adapter does not generate images independently. [Reference guide](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md).
- Preserve the adapter's gated FLUX.1 dev Non-Commercial License independently of a compatible base generator's license. Output rights, production permission and hosted Redux [pro] service terms are distinct. [Official license](https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev).
- Image variation and possible restyling are separate from mask-based Fill editing or text-instructed Kontext editing. Input-image resemblance, diversity and provider quality comparisons are not guarantees. [BFL release](https://bfl.ai/blog/24-11-21-tools).
- Do not infer base-independent image output, exact VRAM/RAM requirements, latency, commercial rights or quality rankings from first-party examples without workload-specific testing.
- BFL's later Tools lifecycle notice deprecates Canny/Depth but explicitly does not deprecate Redux. Do not transfer the unrelated lifecycle status. [BFL Tools notice](https://bfl.ai/blog/24-11-21-tools).

## Validation

- Resolve one `member-of` inverse in FLUX.1 and a local reader path.
- Distinguish adapter weights, compatible base generators, hosted Redux pro and runtime/distribution artifacts.
- No inference benchmark, current-head full documentation CI/cache or exhaustive freshness claim.
