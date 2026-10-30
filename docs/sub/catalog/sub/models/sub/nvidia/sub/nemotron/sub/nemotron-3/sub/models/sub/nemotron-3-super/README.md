# NVIDIA Nemotron 3 Super

**NVIDIA Nemotron 3 Super** is a separately released post-trained **120 billion total / 12 billion active-parameter** hybrid Mamba-2/Transformer LatentMixture-of-Experts (LatentMoE) language model, released **March 11, 2026** under the **NVIDIA Nemotron Open Model License**. It is positioned for reasoning, coding and high-volume multi-agent tool-use workloads.

## Architecture and operating boundaries

The model uses sparse expert routing, Mamba-2 and attention layers, and multi-token prediction (MTP) for speculative decoding. NVIDIA advertises **up to 1 million tokens of context**, with actual supported sequence length, throughput and GPU memory dependent on model format, inference stack and workload.

The released **Super Base** is a distinct pretrained checkpoint, not an alias of post-trained Super. BF16, FP8 and NVFP4 are alternative published weight or serving formats of the post-trained identity; NVFP4 pretraining does not create an additional trained model. NVIDIA also distributes optional MTPv2-related checkpoints for speculative decoding: evaluate these as serving components, not independent Super identities.

NVIDIA benchmark accuracy, comparative throughput and cost-efficiency figures are **producer-reported**, not independent AI Lab results. Do not infer consumer-GPU support from the 12B active-parameter figure: the BF16 model card describes a substantial multi-GPU baseline, while quantized deployment requirements differ. Pin exact released files, model-serving versions and context settings and benchmark memory, output quality and throughput under the target workload.

## Translations

- English

## Relations

- [Nemotron 3 series](../../../../)
- [Super Base pretrained checkpoint](../nemotron-3-super-base/)

## Official resources

- [NVIDIA Super BF16 checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16)
- [NVIDIA Super NVFP4 serving artifact](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4)
- [NVIDIA Nemotron 3 Super research page](https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/)
- [NVIDIA release article](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/)
