# NVIDIA Nemotron 3.5 Lightning

**NVIDIA Nemotron 3.5 Lightning** is an open-weight, text-input/text-output **30B-total / 3B-active-parameter** hybrid Mamba-2/Transformer LatentMoE model released on **August 11, 2026**. NVIDIA positions it as a low-latency execution model for long-running multi-agent workflows, including specialized coding and tool-use tasks. Released weights use **OpenMDW-1.1** terms.

## Training, context and artifacts

Lightning combines sparse expert routing with attention and Mamba-2 components and supports multi-token prediction for speculative decoding. NVIDIA advertises model context **up to 1 million tokens**; actually feasible context, speed and memory depend on the exact weight format, deployment engine and hardware. This limit is not a claim that a single consumer GPU can serve the full context.

The full-precision **BF16 checkpoint** and separately released **NVFP4 quantization** are serving or weight representations of the same post-trained model, not separately trained model identities. The separately released **Lightning Base** is a *pretrained* checkpoint for further adaptation and must not inherit this model's post-training capabilities. DSpark and DFlash are optional speculative-decoding drafters rather than Lightning aliases.

NVIDIA's evaluation scores, latency comparisons and efficiency rankings are **publisher-reported**, not independently reproduced by AI Lab. Pin the model and runtime versions; validate supported precision, context, throughput, safety and correctness on the intended workload before deployment.

## Translations

- English

## Relations

- [Nemotron 3 model series](../../../../)
- [Lightning Base checkpoint](../nemotron-3-5-lightning-base/)

## Official resources

- [NVIDIA Lightning BF16 checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16)
- [NVIDIA Lightning announcement (2026-08-11)](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
- [NVIDIA Nemotron model family](https://developer.nvidia.com/topics/ai/nemotron)
