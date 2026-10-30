# FLUX.1 Redux [dev]

FLUX.1 Redux [dev] is Black Forest Labs' separately released learned image-variation **adapter** for FLUX.1 generators, not a standalone image generator. It conditions a compatible generator on an input image to produce image variations. [Official weights and model card](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev).

## Identity and scope

The BFL reference implementation supports both FLUX.1-dev and FLUX.1-schnell as base generators. Compatibility does not establish that Redux was trained from either released checkpoint, so no speculative training-lineage edge is recorded. [BFL image-variation guide](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md).

## Use and limitations

A complete open-weight workflow loads the Redux adapter, a compatible FLUX.1 generator and its autoencoder. BFL's reference setup uses `FLUX_REDUX`, `FLUX_MODEL` and `FLUX_AE`; downloading the adapter alone does not provide a full image-generation pipeline.

Redux weights are gated under the FLUX.1 dev Non-Commercial License, even when paired with FLUX.1-schnell. Model use, generated-output rights, production use and hosted Redux [pro] terms require separate evaluation. Image resemblance, diversity, speed, memory fit and commercial suitability have not been independently tested.

Unlike FLUX.1 Fill [dev]'s mask-guided inpainting or Kontext [dev]'s text-instructed editing, Redux is an image-variation conditioning component. BFL's Canny/Depth deprecation does **not** apply to Redux. [Official lifecycle notice](https://bfl.ai/blog/24-11-21-tools).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.1](../../../../README.md) | `model-series` |

## Sources

- [BFL official Redux checkpoint](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev)
- [BFL image-variation reference implementation](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md)
- [BFL FLUX.1 Tools and lifecycle notice](https://bfl.ai/blog/24-11-21-tools)
- [FLUX.1 dev model license](https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev)
