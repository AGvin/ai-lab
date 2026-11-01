# Huihui Qwen3.5 35B-A3B Abliterated

> **Experimental derivative — controlled research use.** The publisher describes its refusal-removal method as a crude proof of concept and advises against direct public-facing production.

`huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated` is the exact **experimental abliterated weight derivative** in this record. It retains a separate model identity from other training-stage checkpoints, serialization formats, runtime settings and the existing Huihui Qwen3-Coder30B derivative. [Original](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated).

## Training-stage boundary

The publisher describes a crude proof-of-concept modification to reduce refusals and recommends research/controlled experimentation rather than direct public-facing production. Preserve that suitability warning; this is not an independently safety-reviewed default assistant. [Publisher source](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated).

Its exact immediate parent is **Qwen3.5 35B-A3B**. Abliteration is a weight modification; the sources do not establish a separate fine-tuning or training run. These relations do not transfer downstream quality, behavior, license or deployment guarantees.

## Configuration and operation

The exact config has a vision component and text MoE with 262,144 maximum text positions, 40 layers, 256 experts/8 routed plus a shared expert. These are config values, not measured long-context quality or memory fit. Do not inherit the Qwen parent's optional million-token extension, benchmarks or tool competence without testing. [Model source](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated) [Exact config](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated/blob/main/config.json).

Match the exact processor, tokenizer/chat template, runtime revision and precision to the chosen weights. Evaluate accuracy, modality handling, memory, latency and output review for the intended workload. Publisher results are not independent tests.

## License and provenance

The exact original LICENSE was retrieved as Apache-2.0 text with a 2026 Alibaba Cloud notice. This is stronger than a mirror's declaration; it is not a complete training-data rights audit or a safety warranty. [License evidence](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated/blob/main/LICENSE).

No model was executed or benchmarked here. Current beneficial ownership, indirect Russian stakes/control and sanctions were not established by this bounded source review.

## Quantized distributions

The [static GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3.5-35B-A3B-abliterated-GGUF) and [weighted/imatrix GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3.5-35B-A3B-abliterated-i1-GGUF) name this exact original. Calibration files, bit widths and vision-projector supplements are artifacts; they do not create more trained models or transfer authorship to the quantizer. Backend/projector compatibility remains to be tested.

## Catalog relations

- [huihui.ai](../../../../../producers/sub/h/sub/huihui-ai/) — derivative publisher.
- [Qwen3.5 35B-A3B](../../../alibaba/sub/qwen/sub/qwen3-5/sub/models/sub/qwen3-5-35b-a3b/) — exact parent.

## Official resources

- [Exact original](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated).
