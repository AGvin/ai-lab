# NVIDIA Nemotron 3 Ultra GenRM

NVIDIA Nemotron 3 Ultra GenRM is a separately released **generative reward model** for evaluating assistant responses, with **550B total / 55B active parameters**. NVIDIA publishes it under **OpenMDW-1.1**.

## Reward-model boundaries

This checkpoint is not an inference-oriented alias of Nemotron 3 Ultra, nor a precision variant of Ultra Base. The official model card describes an **early Ultra checkpoint** as its foundation; that text does not establish a verified derivative relation to the final released Ultra or Ultra Base checkpoint.

Evaluate the reward-scoring interface and agreement on intended examples. Use source-specific parameter counts and evaluation configuration; pin the weights and runtime. Separate service routes, quantizations and memory-capacity estimates from the trained-model identity.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-GenRM)
