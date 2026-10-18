# DeepSeek-V4-Pro

DeepSeek-V4-Pro is a concrete model in the [DeepSeek-V4 series](../../../../). It is distinct from DeepSeek-V4-Flash.

## Model facts

The original preview model card identifies these properties:

| Property | Original V4-Pro backbone |
| --- | --- |
| Architecture | Mixture-of-Experts with V4 hybrid attention |
| Total parameters | Approximately 1.6T |
| Activated parameters | 49B |
| Context | 1M tokens |
| Modality | Text input and text generation |
| License | MIT, as declared by the official model repository |

[Source: DeepSeek-V4-Pro model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro). The activated count does not describe total weight storage or the memory needed to serve the model. The selected weight format, auxiliary modules, runtime, and context use also matter.

## Checkpoints and availability

The unversioned `deepseek-ai/DeepSeek-V4-Pro` repository publishes the original preview. [DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) is the later official-release checkpoint associated with the [2026-08-13 general availability announcement](https://api-docs.deepseek.com/news/news260813/). Its card describes the preview model structure with an attached DSpark speculative-decoding module. The two repositories are distinct artifacts and both declare MIT licensing; choose and pin the intended checkpoint.

## Serving boundary

As checked on 2026-10-18, the [current API model table](https://api-docs.deepseek.com/quick_start/pricing/) maps `deepseek-v4-pro` to DeepSeek-V4-Pro-0813. The provider's [change log](https://api-docs.deepseek.com/updates/) explicitly continues V4-Pro service after 2026-09-14, superseding the earlier announced retirement plan.

Hosted availability, API modes, prices, limits, and throughput are properties of the [DeepSeek API service](../../../../../../../../../../../services/sub/model-apis/sub/deepseek-api/), not of the weight artifact. Provider benchmark rankings must be evaluated for the intended workload and harness before use in recommendations.

## Official resources

- [Original preview model card and weights](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [V4-Pro general availability announcement](https://api-docs.deepseek.com/news/news260813/)
- [0813 official checkpoint](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813)
- [Provider change log](https://api-docs.deepseek.com/updates/)
- [Current API model table](https://api-docs.deepseek.com/quick_start/pricing/)
