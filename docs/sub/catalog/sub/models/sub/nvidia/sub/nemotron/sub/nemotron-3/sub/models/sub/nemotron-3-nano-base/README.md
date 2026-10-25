# NVIDIA Nemotron 3 Nano Base

NVIDIA Nemotron 3 Nano Base is a separately published **pretrained language-model checkpoint** intended for further adaptation, distinct from the post-trained Nemotron 3 Nano and Nano Omni models.

## Training and license boundaries

The released BF16 weights use the **NVIDIA Nemotron Open Model License** according to NVIDIA's model card. This base release must not inherit instruction-following, multimodal or benchmark claims from post-trained siblings. BF16 describes a release representation, not a separately trained identity.

Pin the upstream weights and runtime; test model behavior, supported precision, memory and latency rather than assuming deployment fit from a model name. Local inference and hosted endpoints are not validated by this catalog entry.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16)
