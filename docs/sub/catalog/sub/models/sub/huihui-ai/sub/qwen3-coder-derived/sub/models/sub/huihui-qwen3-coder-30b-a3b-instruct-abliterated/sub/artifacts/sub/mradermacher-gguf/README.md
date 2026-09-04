# mradermacher GGUF Artifacts

`mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF` is a static GGUF quantization repository for the canonical huihui.ai derivative model.

## Parent model

- [Huihui Qwen3 Coder 30B A3B Instruct Abliterated](../../../..)

## Artifact profile

- Repository: `mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF`
- Representation: GGUF
- Publisher: `mradermacher`
- Source model: `huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated`
- License: Apache-2.0 as published on the artifact repository
- Intended runtime family: llama.cpp-compatible GGUF tooling and applications

## Published quantizations

The artifact repository currently lists these static quant choices:

| Quantization | Published size |
| --- | ---: |
| `Q2_K` | 11.4 GB |
| `Q3_K_S` | 13.4 GB |
| `Q3_K_M` | 14.8 GB |
| `Q3_K_L` | 16.0 GB |
| `IQ4_XS` | 16.7 GB |
| `Q4_K_S` | 17.6 GB |
| `Q4_K_M` | 18.7 GB |
| `Q5_K_S` | 21.2 GB |
| `Q5_K_M` | 21.8 GB |
| `Q6_K` | 25.2 GB |
| `Q8_0` | 32.6 GB |

mradermacher labels some quant choices with qualitative guidance such as lower quality or recommended/very-good/best-quality. Those labels are publisher guidance, not independent AI Lab acceptance evidence.

Published GGUF file size is not peak runtime VRAM or RAM. Context/KV cache, runtime buffers, GPU offload, batch/concurrency, graph capture, and surrounding services can materially change residency and throughput.

## Boundary

This repository is a set of conversions/quantizations of the huihui.ai derivative weights. It is an artifact identity, not another trained model. Weighted/imatrix variants published in the separate `-i1-GGUF` repository are a different artifact collection and are not silently folded into this node.

Runtime installation commands, Ollama/LM Studio/Pi/OpenClaw integration, hardware fit, measured quantization quality, and workload recommendations belong to deployment/software, selection, or evidence owners.

## Official resources

- [mradermacher GGUF repository](https://huggingface.co/mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-GGUF)
- [huihui.ai source model](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated)
