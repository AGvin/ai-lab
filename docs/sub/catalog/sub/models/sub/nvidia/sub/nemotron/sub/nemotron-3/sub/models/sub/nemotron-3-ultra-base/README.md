# NVIDIA Nemotron 3 Ultra Base

NVIDIA Nemotron 3 Ultra Base is a separately released **pretrained hybrid LatentMoE** checkpoint for further model development, with **550B total / 55B active parameters**. Its official release terms are **OpenMDW-1.1**.

## Training and provenance boundaries

This is not the post-trained Nemotron 3 Ultra model. NVIDIA describes Ultra Base as a **teacher in Super VL distillation**, distinct from the [Nemotron 3 Super Base](../nemotron-3-super-base/) initialization used for the Super VL backbone. The teacher role must not be rewritten as a derivation from post-trained Ultra or as shared model weights.

NVIDIA describes NVFP4 use during pretraining and publishes BF16 weights; neither precision choice creates a separate trained-model identity. Do not transfer post-trained Ultra reasoning results to this base checkpoint. Pin the exact weights, license and runtime before evaluating memory, latency or quality.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-Base-BF16)
