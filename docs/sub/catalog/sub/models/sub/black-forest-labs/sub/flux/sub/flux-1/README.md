# FLUX.1

FLUX.1 is the first FLUX image-model series from Black Forest Labs. This catalog materializes FLUX.1-schnell, FLUX.1-dev, FLUX.1 Krea [dev], FLUX.1 Kontext [dev], FLUX.1 Fill [dev] and FLUX.1 Redux [dev], together with hosted Kontext [pro] and [max], as distinct catalog model identities. Redux is a dependent adapter; proprietary hosted weights and local dev weights must not be conflated. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Identity and scope

The existing series and its Models index organize concrete FLUX.1 models. Do not infer that only the materialized schnell member exists upstream. [BFL official model registry](https://huggingface.co/black-forest-labs) [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

FLUX.1 Krea [dev] was jointly developed with Krea; this namespace does not imply exclusive BFL authorship. Its technical provenance is documented in the model profile.

Redux [dev] conditions a compatible FLUX.1-dev or schnell base generator with an image, rather than generating on its own. The separately gated Redux adapter retains non-commercial model-weight terms even if paired with schnell. [BFL reference](https://github.com/black-forest-labs/flux/blob/main/docs/image-variation.md).

Kontext [pro] and [max] are separately named hosted BFL model options for image creation and editing, with distinct API routes and no published local weights. BFL currently lists both but recommends FLUX.2 for new applications. [Launch](https://bfl.ai/blog/flux-1-kontext) [Current guide](https://help.bfl.ai/articles/5186006235-what-is-flux-1-kontext).

## Use and limitations

License, distillation method and inference-step facts belong to individual FLUX.1 models; do not apply schnell's Apache 2.0 license to the entire series. [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX](../../README.md) | `model-family` |
| `has-member` | [FLUX.1 Fill [dev]](sub/models/sub/flux-1-fill-dev/README.md) | `model` |
| `has-member` | [FLUX.1 Kontext [dev]](sub/models/sub/flux-1-kontext-dev/README.md) | `model` |
| `has-member` | [FLUX.1 Kontext [max]](sub/models/sub/flux-1-kontext-max/README.md) | `model` |
| `has-member` | [FLUX.1 Kontext [pro]](sub/models/sub/flux-1-kontext-pro/README.md) | `model` |
| `has-member` | [FLUX.1 Krea [dev]](sub/models/sub/flux-1-krea-dev/README.md) | `model` |
| `has-member` | [FLUX.1 Redux [dev]](sub/models/sub/flux-1-redux-dev/README.md) | `model` |
| `has-member` | [FLUX.1-dev](sub/models/sub/flux-1-dev/README.md) | `model` |
| `has-member` | [FLUX.1-schnell](sub/models/sub/flux-1-schnell/README.md) | `model` |

## Navigation

- [FLUX.1 Models index](sub/models/README.md)

## Sources

- [BFL official model registry](https://huggingface.co/black-forest-labs)
- [FLUX.1-schnell model card](https://huggingface.co/black-forest-labs/FLUX.1-schnell)
- [FLUX.1-dev model card](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- [Current dev weight license terms](https://bfl.ai/legal/non-commercial-license-terms)
