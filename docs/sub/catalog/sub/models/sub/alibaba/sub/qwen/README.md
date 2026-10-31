# Qwen

Qwen is a model family developed by Qwen Team at Alibaba Cloud. This page owns family-level identity and navigation; producer details remain on the canonical producer pages.

## Canonical producer

- [Qwen Team](../../../../../producers/sub/q/sub/qwen-team/)

## Decision and Operational Boundaries

Qwen is the model family produced by Qwen Team; its members include language, vision, coding, image, speech, and retrieval models.

- Do not inherit one member's license, modality, reasoning mode, or context limit across the family; follow the exact checkpoint or hosted model reference.
- Distinguish open-weight execution from Qwen Studio, Qwen Cloud, and Model Studio service behavior.
- For Model Studio use, distinguish the no-training commitment from retention: standard inference data can be retained for up to 30 days subject to exceptions, while stateful features persist until deletion; verify exact feature and model eligibility before relying on ZDR.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

## Official resources

- [Qwen](https://qwen.ai/)
- [Qwen on Hugging Face](https://huggingface.co/Qwen)

## Model series

- [Qwen2.5-Coder](./sub/qwen2-5-coder/) — coding-specialized Qwen series with 3B and 7B Instruct models represented in the catalog.
- [Qwen3](./sub/qwen3/) — Qwen3 language-model series with dense and Mixture of Experts (MoE) models represented in the catalog.
- [Qwen3-Coder](./sub/qwen3-coder/) — coding-specialized Qwen series for coding-agent and software-development workloads.
- [Qwen3.8](./sub/qwen3-8/)

- [Qwen3.5](./sub/qwen3-5/) — represented pretrained Base and post-trained 9B branch.

## Relationships

| Relationship | Catalog page |
| --- | --- |
| Includes | [Qwen Omni](./sub/qwen-omni/) |
| Produced by | [Qwen Team](../../../../../producers/sub/q/sub/qwen-team/) |
| Includes | [Qwen-Audio](./sub/qwen-audio/) |
| Includes | [Qwen-Image](./sub/qwen-image/) |
| Includes | [Qwen2.5-Coder](./sub/qwen2-5-coder/) |
| Includes | [Qwen3](./sub/qwen3/) |
| Includes | [Qwen3-ASR](./sub/qwen3-asr/) |
| Includes | [Qwen3-Coder](./sub/qwen3-coder/) |
| Includes | [Qwen3-Embedding](./sub/qwen3-embedding/) |
| Includes | [Qwen3-Reranker](./sub/qwen3-reranker/) |
| Includes | [Qwen3-TTS](./sub/qwen3-tts/) |
| Includes | [Qwen3-VL](./sub/qwen3-vl/) |
| Includes | [Qwen3.6](./sub/qwen3-6/) |
| Includes | [Qwen3.8](./sub/qwen3-8/) |
| Includes | [Qwen3.5](./sub/qwen3-5/) |

## Primary Sources

- [Official repository: QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)
- [Official repository: QwenLM/Qwen3.8](https://github.com/QwenLM/Qwen3.8)
- [Alibaba Cloud: data retention policy](https://www.alibabacloud.com/help/en/model-studio/data-retention-policy)
