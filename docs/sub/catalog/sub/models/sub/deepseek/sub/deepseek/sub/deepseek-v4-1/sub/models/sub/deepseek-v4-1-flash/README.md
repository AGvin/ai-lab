# DeepSeek-V4.1-Flash

DeepSeek-V4.1-Flash is a concrete model in the [DeepSeek-V4.1 series](../../../../). It was introduced on 2026-09-10 and is distinct from DeepSeek-V4-Flash.

## Model facts

| Property | Published V4.1-Flash profile |
| --- | --- |
| Architecture | Mixture-of-Experts with a Causal Encoder–Decoder |
| Backbone parameters | 552B |
| Activated parameters | 8B for input; 16B for output |
| Context | 1M tokens |
| Modalities | Text and image input; text output |
| License | MIT, as declared by the official model repository |

The [release announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) establishes the asymmetric architecture and active counts; the [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) documents context and multimodal behavior. The input and output counts describe different execution paths. They must not be added together or treated as the total weights or serving-memory requirement.

## Checkpoints and availability

The original release is published at `deepseek-ai/DeepSeek-V4.1-Flash`. The later [DeepSeek-V4.1-Flash-1017 checkpoint](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) was [released on 2026-10-17](https://api-docs.deepseek.com/news/news261017/). Both official repositories declare MIT licensing. Preserve the repository and revision when recording evaluations or deployment results; a dated checkpoint and an unpinned repository name are not interchangeable identifiers.

Local deployment needs an implementation compatible with the chosen checkpoint, its multimodal encoding, and attention architecture. Published active counts or cache-efficiency claims do not by themselves establish hardware fit. Benchmark claims remain conditional on their harness, settings, and tested workload.

## Serving boundary

As checked on 2026-10-18, the [current API model table](https://api-docs.deepseek.com/quick_start/pricing/) identifies `deepseek-flash` as DeepSeek-V4.1-Flash-1017. Mutable aliases, output limits, modes, and pricing belong to the [DeepSeek API service](../../../../../../../../../../../services/sub/model-apis/sub/deepseek-api/), separately from the model and weight revision.

## Official resources

- [Original model card and weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)
- [September release announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
- [1017 checkpoint](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [October checkpoint announcement](https://api-docs.deepseek.com/news/news261017/)
- [Current API model table](https://api-docs.deepseek.com/quick_start/pricing/)
