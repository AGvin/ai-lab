# FLUX.2 Small Decoder

FLUX.2 Small Decoder is Black Forest Labs' separately distilled VAE decoder component for FLUX.2 image pipelines. The encoder remains unchanged. This component converts compatible latents to images; it does not generate images from a prompt on its own. [Official model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder).

## Relations

| Relation | Target | Target type |
| --- | --- | --- |
| `member-of` | [FLUX.2](../../../../README.md) | `model-series` |

## Learned component and packaging

| Scope | Source-described fact |
| --- | --- |
| Decoder | Approximately 28M parameters; narrower channels [96, 192, 384, 384] |
| Encoder | Retained; channels [128, 256, 512, 512] |
| Combined autoencoder | Repository metadata reports approximately 62.4M parameters, including encoder and decoder |
| Weight packages | Decoder-only and combined-encoder representations; not additional trained decoder identities |

The configuration identifies `AutoencoderKLFlux2`. File size and parameter count do not establish peak RAM/VRAM. [Configuration](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/config.json) [Official weight packages](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/tree/main).

## Integration and limitations

The publisher lists FLUX.2 Klein 4B, Klein 9B, Klein 9B-KV and Dev. This does not establish support for FLUX.1, FLUX 3, hosted-only max/pro/flex or every runtime. The authored usage loads `AutoencoderKLFlux2` and passes it as `vae` to a separately loaded FLUX.2 pipeline; the registry UI's generic `DiffusionPipeline` example is not evidence that this decoder repository is a complete generator. [Authored usage](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder#usage).

Pin the component and generator revisions and select a runtime that honors the distinct decoder channel configuration. Validate latent conventions, precision and representative outputs. At BFL reference commit `50fe5162777813d869182b139e83b10743caef15`, the loader constructs one `ch=128` autoencoder configuration for both halves and strictly loads weights. **Source inference:** overriding `AE_MODEL_PATH` alone does not establish support for the narrower decoder. [Pinned loader](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py) [Pinned autoencoder implementation](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/autoencoder.py).

The approximately 1.4x decoding-speed/memory improvement and quality-preservation claims are publisher measurements, not independently reproduced AI Lab results. No inference or binary tensor comparison was performed for this profile. [Publisher comparison](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder#key-features).

## License and provenance

The component is released under Apache-2.0. The separately loaded generator retains its own weight license and input/output rights requirements. Original publication establishes BFL model attribution; it does not by itself establish current beneficial ownership or supply-chain security. [Official component license](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder#license).

## Official resources

- [Model card and integration instructions](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder)
- [Autoencoder configuration](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/config.json)
- [Weight packages](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/tree/main)
- [BFL reference loader at the audited revision](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py)
- [BFL reference autoencoder at the audited revision](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/autoencoder.py)
