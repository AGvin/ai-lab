# DeepSeek-V4-Flash

DeepSeek-V4-Flash is a concrete model in the [DeepSeek-V4 series](../../../../), separate from DeepSeek-V4-Pro and DeepSeek-V4.1-Flash.

## Model facts

The original preview model card identifies these properties:

| Property | Original V4-Flash backbone |
| --- | --- |
| Architecture | Mixture-of-Experts with V4 hybrid attention |
| Total parameters | 284B |
| Activated parameters | 13B |
| Context | 1M tokens |
| Modality | Text input and text generation |
| License | MIT, as declared by the official model repository |

[Source: DeepSeek-V4-Flash model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash). Activated parameters describe computation per token; they are not the total weights or a memory-residency estimate. Context capacity alone does not establish the memory required by a deployment.

## Checkpoints and availability

The original repository, `deepseek-ai/DeepSeek-V4-Flash`, publishes the preview weights. [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) is a later official-release checkpoint that supersedes the preview and includes a DSpark speculative-decoding module. Its published artifact is distinct from the original preview; pin the intended repository revision and use its encoding and inference instructions. Both repositories declare MIT licensing.

## Serving boundary

As checked on 2026-10-18, the provider reports the V4-Flash hosted model retired. The accepted legacy name `deepseek-v4-flash` now routes to DeepSeek-V4.1-Flash-1017, not these V4 weights. See the [current model table](https://api-docs.deepseek.com/quick_start/pricing/) and the [change log](https://api-docs.deepseek.com/updates/).

This hosting change does not remove the published weight repositories. API modes, output limits, pricing, and concurrency remain properties of the [DeepSeek API service](../../../../../../../../../../../services/sub/model-apis/sub/deepseek-api/).

## Evaluation boundary

Published agent and reasoning benchmark results depend on the checkpoint, harness, settings, and workload. They are evidence for evaluation, rather than a general recommendation or a claim that a deployment fits particular hardware.

## Official resources

- [Original model card and weights](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [V4 preview announcement](https://api-docs.deepseek.com/news/news260424/)
- [0731 official checkpoint](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731)
- [Provider change log](https://api-docs.deepseek.com/updates/)
- [Current API model table](https://api-docs.deepseek.com/quick_start/pricing/)
