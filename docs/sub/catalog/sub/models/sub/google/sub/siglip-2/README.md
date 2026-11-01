# SigLIP 2

Google's SigLIP 2 is a multilingual image/text encoder family introduced in the **20 February 2025** publication. This catalog currently represents three fixed-resolution So400m checkpoints, each trained at its target patch/resolution; it does not claim exhaustive family coverage. [Paper](https://arxiv.org/html/2502.14786v1) [Official release table](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).

## Decision and operating boundaries

These checkpoints are image/text encoders for retrieval and zero-shot classification, not chat or image generators. Use the exact checkpoint processor and tokenizer; fixed-resolution preprocessing does not inherit NaFlex native-aspect behavior. The So400m label refers to the vision tower, while the full image/text checkpoint is approximately 1.136B stored parameters. Equal vector widths do not establish shared embedding spaces. Re-embed/re-index incompatible spaces and evaluate representative retrieval/classification workloads. [Paper](https://arxiv.org/html/2502.14786v1) [Official implementation](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).

The exact Google Hub cards declare Apache-2.0; their public roots have no standalone LICENSE file listed. The big_vision software LICENSE is Apache-2.0, while the SigLIP2 release README separately marks other materials CC-BY. Preserve distribution-specific notices rather than transferring one software license to every NPZ, weight artifact or downstream VLM. [Release notices](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).

Downstream VLM relations refer to their vision-component initialization and subsequent adaptation. They do not establish inclusion of the Google text tower, sole ancestry, Google authorship of a complete downstream VLM or inherited downstream licensing. Publisher evaluations have not been independently reproduced here.

## Catalog relations

- [Google](../../../../../producers/sub/g/sub/google/) — producer.
- [SigLIP 2 So400m patch14 384](sub/models/sub/siglip2-so400m-patch14-384/) — member.
- [SigLIP 2 So400m patch16 384](sub/models/sub/siglip2-so400m-patch16-384/) — member.
- [SigLIP 2 So400m patch16 512](sub/models/sub/siglip2-so400m-patch16-512/) — member.

## Official resources

- [Publication](https://arxiv.org/html/2502.14786v1).
- [Release table and licensing notices](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
