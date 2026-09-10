# Huihui Qwen3 Coder 30B A3B Instruct Abliterated

`huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated` is a concrete community-modified model derived from Qwen3-Coder 30B-A3B Instruct and published by huihui.ai.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Publisher

- [huihui.ai](../../../../../../../../../../../../../producers/sub/h/sub/huihui-ai/)

## Base model

- [Qwen3-Coder 30B-A3B Instruct](../../../../../../../alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-30b-a3b-instruct/)

## Canonical profile

- Model repository: `huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated`
- Base model: `Qwen/Qwen3-Coder-30B-A3B-Instruct`
- Task: text generation
- Library/source form: Transformers with SafeTensors weights
- Modification: publisher describes an abliteration process intended to remove/refactor refusal behavior
- Publisher labels: `abliterated`, `uncensored`
- License: Apache-2.0

The base architecture, parameter counts, context semantics, and other unchanged base-model facts are owned by the canonical Qwen3-Coder 30B-A3B Instruct page. This derivative page records only facts that distinguish the modified weights from that base.

## Modification boundary

The publisher calls this a proof-of-concept refusal-removal implementation and describes a newer/faster abliteration method. These statements establish modification intent and provenance; they do not establish independent quality, safety, coding reliability, or workload suitability.

Abliteration creates a separately published modified weight identity, so this is a distinct `model`, not a version or quantization of the Qwen base. GGUF conversions of these modified weights remain artifacts of this derivative model.

## Artifacts

- [mradermacher GGUF artifacts](./sub/artifacts/sub/mradermacher-gguf/) — static GGUF quantizations of this derivative model.

## Scope boundary

This page owns derivative identity, publisher, base lineage, modification provenance, license, and artifact navigation. Sampling settings, runtime setup, memory fit, quantization quality, coding-agent suitability, refusal-rate claims, and accepted-result conclusions belong to artifact/deployment, selection, or evidence owners.

## Official resources

- [huihui.ai model card](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated)
- [Qwen base model](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
