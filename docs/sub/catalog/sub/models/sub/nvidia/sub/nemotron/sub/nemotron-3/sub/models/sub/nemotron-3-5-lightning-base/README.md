# NVIDIA Nemotron 3.5 Lightning Base

NVIDIA Nemotron 3.5 Lightning Base is a separately published **pretrained 30B-total / 3B-active** checkpoint intended for further development. It is **not** the post-trained Nemotron 3.5 Lightning model.

## Model and release boundaries

The official registry publishes the base checkpoint under **OpenMDW-1.1** terms. Its pretrained stage is a distinct trained-model identity, not a quantized format of the instruction/post-trained sibling. Parameter counts are total versus active MoE parameters; do not treat 3B active as a dense 3B memory footprint.

BF16 and other serving representations are artifacts, not new model identities. Verify the selected weights and runtime support, and evaluate memory, latency and task quality before deployment.

## Series and official source

- [Nemotron 3 series](../../../../)
- [Official NVIDIA checkpoint](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-Base-BF16)
