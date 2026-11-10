# FLUX.2

FLUX.2 is a Black Forest Labs image-generation and image-editing model series. It groups the named max, pro, flex and dev models and the specialized Klein subseries without collapsing their distinct deployment or licensing boundaries. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

## Identity and scope

The series includes max, pro, flex and dev alongside the specialized Klein subseries. Klein contains separately published scale, base, distilled and KV model choices. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence).

The series also includes [FLUX.2 Small Decoder](sub/models/sub/flux-2-small-decoder/README.md), a separately distilled VAE decoder component. It is not an additional image generator; its decoder-only and combined-encoder packages represent the component, and Apache-2.0 component terms do not replace generator licenses. [Official component card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder).

## Use and limitations

FLUX.2 includes hosted offerings and separately licensed downloadable weights. Do not give the whole series one license, parameter count, reference-image limit or hardware minimum. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2).

Provider reference limits, resolutions, sampling controls and preview endpoints vary by exact model and access route. Pin those choices for a workflow; a preview alias may change its underlying weights without creating a new canonical identity automatically. [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX](../../README.md) | `model-family` |
| `has-member` | [FLUX.2 [dev]](sub/models/sub/flux-2-dev/README.md) | `model` |
| `has-member` | [FLUX.2 [flex]](sub/models/sub/flux-2-flex/README.md) | `model` |
| `has-member` | [FLUX.2 [klein]](sub/flux-2-klein/README.md) | `model-series` |
| `has-member` | [FLUX.2 [max]](sub/models/sub/flux-2-max/README.md) | `model` |
| `has-member` | [FLUX.2 [pro]](sub/models/sub/flux-2-pro/README.md) | `model` |
| `has-member` | [FLUX.2 Small Decoder](sub/models/sub/flux-2-small-decoder/README.md) | `model` |

## Sources

- [FLUX.2 overview](https://docs.bfl.ai/flux_2/flux2_overview)
- [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2)
- [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence)

- [FLUX.2 Small Decoder model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder)
