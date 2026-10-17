# TRL

Hugging Face TRL is an open-source post-training library for language and multimodal models. Its current scope includes supervised fine-tuning, preference optimization, reward modeling, reinforcement-learning-style training, and related alignment workflows.

Although the name expands to Transformers Reinforcement Learning, current TRL is broader than reinforcement learning alone and remains model-development/post-training tooling.

## Telemetry

TRL sends a usage ping when a trainer is instantiated, with categories such as trainer class, model architecture, hardware, and distributed-training configuration. The upstream guide says dataset names, paths, model identifiers, and user-provided training data are excluded, while the receiving server can see the source IP and normal HTTP headers. Set `HF_HUB_DISABLE_TELEMETRY=1` to disable telemetry; TRL also suppresses it in documented CI and offline modes.

## Relations

- Produced by: [Hugging Face, Inc.](../../../../../../../producers/sub/h/sub/hugging-face-inc/)

## Official resources

- [TRL documentation](https://huggingface.co/docs/trl/en/index)
- [TRL repository](https://github.com/huggingface/trl)
- [Usage statistics and opt-out](https://huggingface.co/docs/trl/en/usage_stats)
