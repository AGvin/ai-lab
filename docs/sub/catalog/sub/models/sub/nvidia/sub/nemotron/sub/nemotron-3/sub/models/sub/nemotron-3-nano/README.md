# NVIDIA Nemotron 3 Nano

**NVIDIA Nemotron 3 Nano** is a separately released, post-trained **hybrid Mamba-2/Transformer sparse Mixture-of-Experts language model** for chat, reasoning and agentic tasks, published on **December 15, 2025**. Its 30B-total / 3B-active name is rounded: NVIDIA's technical report describes approximately **31.6B total / 3.2B active parameters** (3.6B including embeddings). Public weights are governed by the **NVIDIA Nemotron Open Model License**.

## Model and serving boundaries

NVIDIA documents long-context support **up to 1 million tokens**. This is an architectural/model-card limit, not a guarantee that a particular runtime, precision, GPU or workload can serve the full length. BF16 and FP8 are published formats of the same post-trained trained identity, not new models.

The separately released [Nano Base](../nemotron-3-nano-base/) is a **pretrained checkpoint** for further adaptation; its training-stage capabilities cannot be assumed to match post-trained Nano. [Nano Omni](../nemotron-3-nano-omni/) is a **separate multimodal derivative** that uses Nano's language backbone, not an alias or quantization. Nano itself is text-focused; Omni's image, video and audio modalities are not transferred to Nano.

Provider-reported quality, throughput and benchmark comparisons are specific to NVIDIA's configurations and have **not** been independently replicated by AI Lab. Confirm exact model weights, model card, supported runtime, memory and context under the intended deployment.

## Translations

- English

## Relations

- [Nemotron 3 model series](../../../../)
- [Nano Base pretrained checkpoint](../nemotron-3-nano-base/)
- [Nano Omni multimodal derivative](../nemotron-3-nano-omni/)

## Official resources

- [NVIDIA Nano BF16 checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16)
- [NVIDIA Nemotron 3 family and model artifacts](https://research.nvidia.com/labs/nemotron/Nemotron-3/)
- [NVIDIA Nemotron 3 Nano technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf)
