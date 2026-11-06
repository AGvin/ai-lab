# mradermacher GGUF Artifacts

mradermacher GGUF Artifacts is the existing static GGUF quantization collection for huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated. The card identifies mradermacher as the quantizer and the exact huihui derivative as its base model. [Primary source](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)

## Artifact provenance

The source card states `base_model: huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated`, `quantized_by: mradermacher` and Apache-2.0 metadata. This record describes representations of the modified huihui model. Quantization publication does not make mradermacher a co-producer of that learned model. [Exact artifact metadata](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)

## Choosing a quantization

The table below is the publisher's current static quant inventory, with rounded sizes in GB and its exact download links. Size order does not guarantee quality order; any qualitative recommendations in the original card are publisher guidance. Check the selected files and revision before use, and compare output quality under the intended workload. [Provided quant table](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)

| Quantization | Published size (GB) | Download |
| --- | ---: | --- |
| Q2_K | 11.4 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q2_K.gguf) |
| Q3_K_S | 13.4 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q3_K_S.gguf) |
| Q3_K_M | 14.8 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q3_K_M.gguf) |
| Q3_K_L | 16.0 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q3_K_L.gguf) |
| IQ4_XS | 16.7 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.IQ4_XS.gguf) |
| Q4_K_S | 17.6 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q4_K_S.gguf) |
| Q4_K_M | 18.7 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q4_K_M.gguf) |
| Q5_K_S | 21.2 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q5_K_S.gguf) |
| Q5_K_M | 21.8 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q5_K_M.gguf) |
| Q6_K | 25.2 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q6_K.gguf) |
| Q8_0 | 32.6 | [GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF/resolve/main/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.Q8_0.gguf) |

## Runtime and memory

Use a GGUF loader with the required Qwen3 MoE and tokenizer/template support, and record the exact quantization and artifact revision. Published file size is not a runtime RAM/VRAM requirement: context/KV cache, buffers, GPU offload and concurrency affect memory and throughput. Follow the distribution's file layout when a loader expects a particular file or complete set of parts. [Artifact usage and file links](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)

## Separate weighted collection

The publisher explicitly links `mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-i1-GGUF` for weighted/imatrix quantizations. That separate artifact route is not part of the static file inventory represented here, and it does not by itself identify newly trained model weights. [Separate collection link](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)

## Catalog navigation

- [Huihui Qwen3 Coder 30B A3B Artifacts](../../README.md) — Containing artifact index

## Relations

- Artifact of: [Huihui Qwen3 Coder 30B A3B Instruct Abliterated](../../../../README.md)

## Official resources

- <https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF>
- <https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated>
