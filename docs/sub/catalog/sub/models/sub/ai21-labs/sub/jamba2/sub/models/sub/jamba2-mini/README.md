# Jamba2 Mini

Jamba2 Mini is AI21 Labs' hybrid SSM-Transformer Mixture-of-Experts model with 52 billion total and 12 billion active parameters. The official AI21-Jamba2-Mini weights are published under Apache 2.0 with a documented 256K-token context window. [Primary source](https://www.ai21.com/blog/introducing-jamba2/)

## Model and artifact

The official `ai21labs/AI21-Jamba2-Mini` model card describes a hybrid SSM-Transformer model with 52B total parameters and 12B active parameters, Apache 2.0 licensing and a 256K-token context window. The active count does not mean the full model consists of only 12B parameters. [Official Mini model card](https://huggingface.co/ai21labs/AI21-Jamba2-Mini) · [Release architecture details](https://www.ai21.com/blog/introducing-jamba2/)

## Hosted and local access

AI21's current documentation maps both `jamba-mini` and `jamba-mini-2` to `jamba-mini-2-2026-01`. Prefer an explicitly selected snapshot for reproducibility; hosted aliases can move without creating a new catalog model. For local use, plan for the total weights, precision, runtime and context workload. Pin the weight revision and matching tokenizer/chat template. [API versioning](https://docs.ai21.com/docs/jamba-foundation-models) · [Published artifact](https://huggingface.co/ai21labs/AI21-Jamba2-Mini)

## Evaluation boundary

Evaluate factual grounding, instruction following and long-context behavior on the actual task. Compare identical prompts, retrieval inputs and serving settings. Vendor benchmark positioning does not replace application evaluation or external controls on tools and consequential actions.

## Relations

- Member of: [Jamba2](../../../../README.md)

## Official resources

- <https://www.ai21.com/blog/introducing-jamba2/>
- <https://docs.ai21.com/docs/jamba-foundation-models>
- <https://huggingface.co/ai21labs/AI21-Jamba2-Mini>
