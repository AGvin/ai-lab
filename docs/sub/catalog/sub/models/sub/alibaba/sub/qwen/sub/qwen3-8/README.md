# Qwen3.8

Qwen3.8 is a model series within Qwen based on first-party Qwen release repositories.

## Scope and boundaries

- Coding, professional-work, research, and long-horizon agentic positioning only as current Qwen Team claims.
- Includes the independently published hosted `Qwen3.8-Max` model; descriptive labels such as `Max-class` do not create additional model identities.

## Relations

- Member of: [`catalog/models/alibaba/qwen`](../..//)
- Produced by: [`catalog/producers/q/qwen-team`](../../../../../../../producers/sub/q/sub/qwen-team/)
- has-member: [`catalog/models/alibaba/qwen/qwen3-8/models/qwen3-8-2-4t-a95b`](sub/models/sub/qwen3-8-2-4t-a95b/)
- has-member: [`catalog/models/alibaba/qwen/qwen3-8/models/qwen3-8-27b`](sub/models/sub/qwen3-8-27b/)
- has-member: [`catalog/models/alibaba/qwen/qwen3-8/models/qwen3-8-flash-next`](sub/models/sub/qwen3-8-flash-next/)
- has-member: [`catalog/models/alibaba/qwen/qwen3-8/models/qwen3-8-max`](sub/models/sub/qwen3-8-max/)

## Decision and Operational Boundaries

Qwen3.8 includes separately released open checkpoints and independently named hosted Max and Flash models.

- Do not infer a common license: 27B is Apache-2.0, the 2.4T-A95B checkpoint uses a separate Qwen3.8-Max license, and Flash-Next uses Qwen Community License 1.0.
- Separate the text-only, thinking-only 2.4T-A95B weights from the multimodal hosted Max service; distinguish native checkpoint context from extended or hosted limits.
- Keep Flash-Next as a released experimental architecture preview and avoid presenting it as a stable Qwen4 release.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- <https://github.com/QwenLM/Qwen3.8>

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Member of | [Qwen](../../) |
| Produced by | [Qwen Team](../../../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen3.8-2.4T-A95B](./sub/models/sub/qwen3-8-2-4t-a95b/) |
| Includes | [Qwen3.8-27B](./sub/models/sub/qwen3-8-27b/) |
| Includes | [Qwen3.8-Flash](./sub/models/sub/qwen3-8-flash/) |
| Includes | [Qwen3.8-Flash-Next](./sub/models/sub/qwen3-8-flash-next/) |
| Includes | [Qwen3.8-Max](./sub/models/sub/qwen3-8-max/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- [Official model card or license: Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Official model card or license: Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Official model card or license: Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- [Alibaba Cloud: qwen3 8 flash](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash)
