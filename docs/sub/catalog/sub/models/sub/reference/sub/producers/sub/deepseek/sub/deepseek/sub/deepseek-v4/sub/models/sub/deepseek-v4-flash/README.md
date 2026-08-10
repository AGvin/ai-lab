# DeepSeek-V4-Flash

DeepSeek-V4-Flash is a DeepSeek Mixture-of-Experts language model in the DeepSeek-V4 series.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Canonical profile

- Model repository: `deepseek-ai/DeepSeek-V4-Flash`
- Architecture: Mixture of Experts (MoE), using the DeepSeek-V4 hybrid attention architecture
- Total parameters: 284B
- Activated parameters: 13B
- Context length: 1 million tokens in the current official model card
- License: MIT

The model card and V4 release identify Flash as a distinct model from DeepSeek-V4-Pro. Its smaller active/total parameter profile does not make it a version of Pro.

## Official serving — mutable

DeepSeek's current API exposes the model as `deepseek-v4-flash`, with thinking and non-thinking modes. Current API limits, aliases, output caps, pricing, and concurrency are serving properties and must be rechecked from the provider rather than treated as immutable model facts.

## Evidence boundary

DeepSeek publishes benchmark and agent-capability claims for V4-Flash. AI Lab selection pages must re-evaluate those claims on the target workload before using them as recommendations.

## Official resources

- [DeepSeek-V4-Flash model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)
- [DeepSeek V4 release](https://api-docs.deepseek.com/news/news260424/)
- [DeepSeek API models](https://api-docs.deepseek.com/quick_start/pricing/)
