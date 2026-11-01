# Documentation Requirements

## Identity and scope

- Identify Google's SigLIP 2 multilingual image/text encoder family from the 20 February 2025 publication and official checkpoint release. Materialize the three exact So400m fixed-resolution models currently reviewed; this is not exhaustive coverage of all sizes, resolutions or NaFlex. [Paper](https://arxiv.org/html/2502.14786v1) [Official releases](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
- The paper section 2.4.1 describes resuming training at target resolutions after embedding resizing, so these are distinct learned checkpoints, not inference-only resize flags. Do not infer an exact released parent edge between them from an intermediate training procedure. [Paper](https://arxiv.org/html/2502.14786v1).

## Decision and operating boundaries

- These checkpoints are image/text encoders for retrieval and zero-shot classification, not chat or image generators. Use the exact checkpoint processor and tokenizer; fixed-resolution preprocessing does not inherit NaFlex native-aspect behavior. The So400m label refers to the vision tower, while the full image/text checkpoint is approximately 1.136B stored parameters. Equal vector widths do not establish shared embedding spaces. Re-embed/re-index incompatible spaces and evaluate representative retrieval/classification workloads. [Publication](https://arxiv.org/html/2502.14786v1) [Release implementation](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
- The exact Google Hub cards declare Apache-2.0; their public roots have no standalone LICENSE file listed. The big_vision software LICENSE is Apache-2.0, while the SigLIP2 release README separately marks other materials CC-BY. Preserve distribution-specific notices rather than transferring one software license to every NPZ, weight artifact or downstream VLM. [Release notices](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
- Four downstream VLM relationships apply to learned vision components only. Do not imply inclusion of the Google text tower, exclusive SigLIP ancestry, Google co-production of the downstream models, or downstream permissive weight rights.
- Published evaluations are author-reported. No independent inference, benchmark, hardware fit, full beneficial-ownership audit or sanctions conclusion is established.

## Validation

- Preserve one reciprocal Google producer relation, three reciprocal model membership pairs and the exact component-scoped derivative pairs.
- Render complete English reader navigation, exact model facts and bounded license/operating guidance. No final render/cache/schema/CI, clean-pass or publication-gate credit.
