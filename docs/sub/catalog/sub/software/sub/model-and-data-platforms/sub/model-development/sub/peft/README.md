# PEFT

Hugging Face PEFT is an open-source library and framework for parameter-efficient model adaptation. It supports multiple methods that adapt large pretrained models by training or modifying a relatively small amount of model state rather than fully updating every base-model parameter.

PEFT integrates with Transformers, Diffusers, Accelerate, and related tooling while remaining a distinct model-adaptation library.

PEFT adapter checkpoints store adaptation parameters and configuration separately from the base model. Loading an unmerged adapter also requires the compatible original base model.

## Relations

- Produced by: [Hugging Face, Inc.](../../../../../../../producers/sub/h/sub/hugging-face-inc/)

## Official resources

- [PEFT documentation](https://huggingface.co/docs/peft/index)
- [PEFT repository](https://github.com/huggingface/peft)
- [PEFT checkpoint format](https://huggingface.co/docs/peft/developer_guides/checkpoint)
