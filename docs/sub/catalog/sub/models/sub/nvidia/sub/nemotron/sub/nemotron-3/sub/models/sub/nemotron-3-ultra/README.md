# NVIDIA Nemotron 3 Ultra

**NVIDIA Nemotron 3 Ultra** is a separately released **post-trained hybrid Mamba-2/Transformer LatentMoE language model** with **550 billion total / 55 billion active parameters**, published on **June 4, 2026** under **OpenMDW-1.1**. NVIDIA positions Ultra for complex reasoning, tool use, and multi-step orchestration in long-running agent systems.

## Architecture and execution boundaries

Ultra combines sparse expert routing, selective attention, Mamba-2 and multi-token prediction (MTP). NVIDIA reports **up to one million tokens of model context** and configurable reasoning mode, but actual supported context, inference throughput and memory requirements depend on the exact model artifact, runtime and hardware.

The separately published **Ultra Base** checkpoint is pretrained for further development; **Ultra GenRM** is a generative reward model for evaluating responses. Neither is interchangeable with this post-trained Ultra checkpoint. The BF16 and NVFP4 weight releases are distinct serving/precision artifacts of **the same trained Ultra model**, not additional model identities. NVIDIA's NVFP4 pretraining recipe should not be confused with a separate training lineage.

NVIDIA's benchmark, throughput, price-efficiency and comparative quality results remain **publisher-reported claims**, not independently reproduced AI Lab findings. The official BF16 model card specifies substantial multi-GPU requirements. Do not infer local single-GPU feasibility from the 55B active-parameter figure; validate quality, supported runtime, precision, peak memory and context length on the target deployment.

## Translations

- English

## Relations

- [Nemotron 3 series](../../../../)
- [Ultra Base pretrained checkpoint](../nemotron-3-ultra-base/)
- [Ultra GenRM reward-model checkpoint](../nemotron-3-ultra-genrm/)

## Official resources

- [NVIDIA Ultra BF16 checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16)
- [NVIDIA Ultra NVFP4 serving artifact](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4)
- [NVIDIA Nemotron 3 Ultra research page](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/)
- [NVIDIA Ultra release article](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/)
