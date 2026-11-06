# NVIDIA Nemotron 3 Super Base

NVIDIA Nemotron 3 Super Base is a separately published **pretrained hybrid LatentMoE language model** intended for further training. NVIDIA identifies **120B total / 12B active parameters** and the **NVIDIA Nemotron Open Model License** for this base release.

## Model and derivative boundaries

The base checkpoint is not the post-trained Nemotron 3 Super. NVIDIA identifies it as an initialization source for [Nemotron 3.5 Super VL](../nemotron-3-5-super-vl/) and [Super VL Base](../nemotron-3-5-super-vl-base/). That backbone relation is distinct from the Ultra Base teacher-distillation role. NVFP4 use during pretraining and BF16 release weights are not additional trained-model identities.

Do not transfer post-trained capabilities or benchmark claims to the base checkpoint. Verify the exact weights, runtime and hardware behavior under representative training or inference conditions.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-Base-BF16)
