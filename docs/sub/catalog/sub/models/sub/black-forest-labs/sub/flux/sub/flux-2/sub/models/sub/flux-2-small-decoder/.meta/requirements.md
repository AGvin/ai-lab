# Documentation Requirements

## Identity and provenance

- Identify one separately distilled learned VAE decoder component published by Black Forest Labs; retain the unchanged encoder boundary and FLUX.2 series organization. It is not an independent prompt-to-image generator or a hosted API. [Model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder).
- Distinguish approximately 28M decoder parameters from the repository's approximately 62.4M combined-autoencoder parameter metadata. The decoder-only and combined-encoder packages are representations of this learned component, not automatic additional model identities. File size is not peak runtime memory. [Model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder) [Files](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/tree/main).
- Describe separate decoder channel widths [96, 192, 384, 384] versus encoder widths [128, 256, 512, 512], using the exact AutoencoderKLFlux2 configuration. Do not transfer component architecture facts to the generator. [Configuration](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/blob/main/config.json).

## Operational decision boundaries

- State Apache-2.0 for this component without extending it to the separately loaded generator weights. Respect the exact generator's license and input/output rights. [Model card and license](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder#license).
- Attribute approximately 1.4x decoding speed/memory improvements and quality preservation to the publisher; no independently reproduced AI Lab inference or benchmark is established.
- Limit publisher compatibility evidence to FLUX.2 Klein 4B, Klein 9B, Klein 9B-KV and Dev; do not infer support for FLUX.1, FLUX 3 or hosted-only max/pro/flex. Compatibility does not guarantee support in every loader. [Model card](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder).
- Follow the authored integration pattern: load AutoencoderKLFlux2 and inject it as vae into a separately loaded FLUX.2 pipeline. Generic registry UI DiffusionPipeline snippets do not establish a standalone image-generation pipeline. Pin component/generator revisions and a runtime honoring the separate decoder channels; validate latent conventions, precision and representative output.
- At BFL reference commit 50fe5162777813d869182b139e83b10743caef15, load_ae constructs AutoEncoderParams with one ch=128 for both halves and strictly loads the weights. Explicitly label the conclusion as source inference: changing only AE_MODEL_PATH does not establish compatibility with this narrower decoder. [Loader](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py) [Autoencoder](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/autoencoder.py).

## Validation

- Render visible entity relations and resolve the parent-series link without invented compatibility/dependency relation types.
- Preserve learned component, complete generator, packaging, producer and runtime identities.
- Treat missing upstream decoder training details or benchmark reproduction as unknown; do not manufacture a derived-from relation to a generator.
