# SigLIP 2 So400m patch16 512

`google/siglip2-so400m-patch16-512` is a **separately trained fixed-resolution image/text encoder**, using patch 16 and **512×512** image input preprocessing. It is a complete contrastive checkpoint rather than a chat model or an inference resize setting. [Exact card](https://huggingface.co/google/siglip2-so400m-patch16-512) [Training procedure](https://arxiv.org/html/2502.14786v1) [Official release](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).

## Parameters and preprocessing

These checkpoints are image/text encoders for retrieval and zero-shot classification, not chat or image generators. Use the exact checkpoint processor and tokenizer; fixed-resolution preprocessing does not inherit NaFlex native-aspect behavior. The So400m label refers to the vision tower, while the full image/text checkpoint is approximately 1.136B stored parameters. Equal vector widths do not establish shared embedding spaces. Re-embed/re-index incompatible spaces and evaluate representative retrieval/classification workloads. Use this checkpoint's 512×512 processor; target resolution is part of its learned identity. [Config](https://huggingface.co/google/siglip2-so400m-patch16-512/blob/main/config.json) [Processor](https://huggingface.co/google/siglip2-so400m-patch16-512/blob/main/preprocessor_config.json).

## License and evaluation

The exact Google Hub cards declare Apache-2.0; their public roots have no standalone LICENSE file listed. The big_vision software LICENSE is Apache-2.0, while the SigLIP2 release README separately marks other materials CC-BY. Preserve distribution-specific notices rather than transferring one software license to every NPZ, weight artifact or downstream VLM. [Exact declaration](https://huggingface.co/google/siglip2-so400m-patch16-512) [Original release notices](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).

Test retrieval, label prompts and thresholds on representative languages and images. Publisher evaluation results do not establish independent quality, memory fit or latency. No current beneficial-ownership, indirect Russian stake/control or sanctions determination was made.

## Component-scoped derivatives

Command A Vision uses this exact pretrained vision component and adapts it within its own VLM training; this does not include the complete Google text tower or replace the downstream license. [First-party source](https://huggingface.co/blog/CohereLabs/introducing-command-a-vision-07-2025).

No exact released sibling parent or additional learned identity is inferred from serialization, quantization or intermediate training stages.

## Catalog relations

- [Command A Vision](../../../../../../../cohere/sub/command/sub/command-a/sub/models/sub/command-a-vision-07-2025/) — derivative through the vision component.
- [SigLIP 2](../../../../) — family.

## Official resources

- [Exact card](https://huggingface.co/google/siglip2-so400m-patch16-512).
- [Paper](https://arxiv.org/html/2502.14786v1).
- [Original release](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md).
