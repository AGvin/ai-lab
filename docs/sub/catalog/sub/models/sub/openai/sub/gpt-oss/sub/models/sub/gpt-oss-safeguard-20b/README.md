# gpt-oss-safeguard-20b

`gpt-oss-safeguard-20b` is OpenAI’s publicly downloadable research-preview policy-classification fine-tune of `gpt-oss-20b`, released on October 29, 2025 under Apache 2.0.

## Profile

The fine-tune keeps its base model’s architecture. It evaluates text against a developer-supplied policy and can produce a classification with reasoning [Safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).

## Operating boundaries

Keep the policy in the trusted developer instruction and the content to classify in the user message, following the documented Harmony formatting. Classification is evidence for the application’s policy process, not automatic authorization to act [Safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).

This remains a research preview. It requires local or third-party hosting, and the operator owns policy evaluation, infrastructure, and access controls [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).

The reasoning-based approach has a compute and latency cost; a dedicated classifier can perform better for a policy with substantial training data [Safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).

## Relations

- Member of: [gpt-oss](../../../../README.md).

## Official resources

- [gpt-oss-safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).
- [gpt-oss-safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).
- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- [gpt-oss-20b model reference](https://developers.openai.com/api/docs/models/gpt-oss-20b).
