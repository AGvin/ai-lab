# Megatron Bridge

A PyTorch-native training and model-interoperability library in the NeMo ecosystem, distributed as `megatron-bridge` and imported through `megatron.bridge`. Upstream also calls it NeMo Megatron Bridge.

## Capabilities and software boundary

Megatron Bridge provides pretraining, supervised fine-tuning, LoRA/PEFT, customizable training loops and model recipes built on [Megatron Core](../megatron-core/). It also converts supported checkpoints between Hugging Face and Megatron formats with verification workflows.

[Megatron-LM](../megatron-lm/) remains a separate reference implementation. [NVIDIA NeMo RL](../nvidia-nemo-rl/) and serving engines retain their own roles. The current NVIDIA-maintained project acknowledges its MBridge predecessor and community contributions.

## Compatibility, evidence and operations

Loading an architecture for random-initialized pretraining does not require importing pretrained weights. When weights are imported or exported, check the model-specific mapping, tokenizer/configuration assets, precision and verification results.

The package is classified Production/Stable, while model support, deprecations and experimental features vary by release. Match Bridge with its documented Megatron Core revision, Python/PyTorch/CUDA/Transformers stack, optional dependencies and container configuration. Validate the selected model and distributed layout; a conversion example or benchmark does not establish universal model equivalence or performance.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Megatron Bridge documentation](https://docs.nvidia.com/nemo/megatron-bridge/latest/)
- [Repository and predecessor acknowledgement](https://github.com/NVIDIA-NeMo/Megatron-Bridge)
- [Megatron-LM migration guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/megatron-lm-to-megatron-bridge.html)
- [Package and lifecycle metadata](https://pypi.org/project/megatron-bridge/)
