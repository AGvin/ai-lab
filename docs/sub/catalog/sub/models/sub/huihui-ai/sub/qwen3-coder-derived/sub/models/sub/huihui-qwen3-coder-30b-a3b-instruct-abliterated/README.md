# Huihui Qwen3 Coder 30B A3B Instruct Abliterated

Huihui Qwen3 Coder 30B A3B Instruct Abliterated is a distinct modified model published by huihui.ai from the exact Qwen/Qwen3-Coder-30B-A3B-Instruct base. The publisher describes abliteration intended to change refusal behavior. [Primary source](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated)

## Identity and modification

The official card names `Qwen/Qwen3-Coder-30B-A3B-Instruct` as the exact base and describes an abliteration process aimed at refusal behavior. It calls the implementation a proof of concept and reports improvements from its method. Those statements establish intended modification and provenance; they are not independent measures of coding quality, refusal rate or suitability. The existing canonical base and producer relations remain exact. [Official derivative card](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated)

## Source distribution and configuration

At revision `b84c58d52ac44041774fe9542e1943e4d971b5f4`, the source tree lists thirteen SafeTensors shards and their index. The config at that revision identifies Qwen3MoeForCausalLM, `qwen3_moe`, 48 hidden layers, bfloat16 dtype metadata, `max_position_embeddings: 262144` and no configured RoPE scaling. These are published source/configuration facts, not proof of maximum request capacity or memory fit in an arbitrary runtime. The Apache-2.0 declaration is on the model card. [Pinned source file tree](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated/tree/b84c58d52ac44041774fe9542e1943e4d971b5f4) · [Derivative configuration](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated/resolve/main/config.json) · [License metadata](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated)

## Runtime and reasoning controls

Use a runtime supporting Qwen3 MoE, the matching tokenizer and the model's chat template. Pin the model and runtime revisions and record precision, context and generation settings. The publisher's sample includes a four-bit loading setup and passes `enable_thinking` to the template; that argument alone does not establish a new learned reasoning toggle. The exact upstream card documents non-thinking mode. Validate the selected derivative/template behavior directly rather than inferring it from a generic example. [Authored usage example](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated) · [Upstream mode contract](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

## Artifact choice and evaluation

The represented mradermacher distribution is a static GGUF artifact of these modified weights. Pick an exact quantization and compatible loader, and measure quality and memory under the intended context and offload settings. The A3B name is not a complete memory budget, and the base model's benchmark or context-extension claims are not automatic guarantees for this derivative. Record the exact model/artifact revisions when comparing results. [Artifact mapping and quant choices](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF) · [Separate upstream technical context](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

## Catalog navigation

- [Huihui Qwen3 Coder 30B A3B Artifacts](sub/artifacts/README.md) — Artifact navigation
- [huihui.ai Qwen3-Coder-Derived Model Releases](../../README.md) — Containing release collection

## Relations

- Derived from: [Qwen3-Coder 30B-A3B Instruct](../../../../../../../alibaba/sub/qwen/sub/qwen3-coder/sub/models/sub/qwen3-coder-30b-a3b-instruct/README.md)
- Artifacts: [mradermacher GGUF Artifacts](sub/artifacts/sub/mradermacher-gguf/README.md)
- Produced by: [huihui.ai](../../../../../../../../../producers/sub/h/sub/huihui-ai/README.md)

## Official resources

- <https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated>
- <https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated/resolve/main/config.json>
- <https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated/tree/b84c58d52ac44041774fe9542e1943e4d971b5f4>
- <https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct>
- <https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF>
