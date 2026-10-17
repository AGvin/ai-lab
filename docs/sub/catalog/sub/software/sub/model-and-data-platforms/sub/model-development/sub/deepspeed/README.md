# DeepSpeed

DeepSpeed is an open-source suite originally developed by Microsoft for large-scale model training and memory/compute optimization.

Microsoft contributed DeepSpeed to the Linux Foundation in January 2025. DeepSpeed became a hosted PyTorch Foundation project in May 2025 under the foundation's open governance model; its Microsoft producer relation preserves the project's origin.

## Capabilities and software boundary

Includes distributed training, ZeRO-family optimizer and parameter sharding/offload, model parallelism, mixed precision, and optional inference, compression and profiling surfaces. These are components of the DeepSpeed software suite, not independent model identities.

## Compatibility, evidence and operations

Distinct from PyTorch, schedulers, trained model artifacts, and hosted APIs. Pin PyTorch, CUDA/ROCm, accelerator and DeepSpeed extension versions. Published performance depends on model, batch, precision, GPU topology and network.

## Relations

- Produced by: [Microsoft](../../../../../../../producers/sub/m/sub/microsoft/)

## Official resources

- [Primary source](https://github.com/deepspeedai/DeepSpeed)
- [PyTorch Foundation project profile](https://pytorch.org/projects/deepspeed/)
- [Foundation hosting and governance announcement](https://pytorch.org/blog/press-release-pytorch-foundation-expands-welcomes-projects-vllm-deepspeed/)
