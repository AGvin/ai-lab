# gpt-oss

gpt-oss is OpenAI’s downloadable open-weight model family. It includes the general reasoning releases gpt-oss-120b and gpt-oss-20b and the policy-classification fine-tunes gpt-oss-safeguard-120b and gpt-oss-safeguard-20b.

## Profile

The models are distributed under Apache 2.0. The safeguard fine-tunes were publicly released as research previews in October 2025 [Safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).

## Operating boundaries

These weights are not served through OpenAI’s API or ChatGPT. Deployment, fine-tuning, tool execution, infrastructure, and data handling are the operator’s or hosting provider’s responsibility [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).

Safeguard models classify content against a supplied policy. Their preview status and policy-driven task differ from a general-purpose chat assistant [Safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).

## Child pages

- [Models](sub/models/README.md).

## Relations

- Member: [gpt-oss-120b](sub/models/sub/gpt-oss-120b/README.md).
- Member: [gpt-oss-20b](sub/models/sub/gpt-oss-20b/README.md).
- Member: [gpt-oss-safeguard-120b](sub/models/sub/gpt-oss-safeguard-120b/README.md).
- Member: [gpt-oss-safeguard-20b](sub/models/sub/gpt-oss-safeguard-20b/README.md).
- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- [gpt-oss-safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).
- [gpt-oss-safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).
- [gpt-oss-120b model reference](https://developers.openai.com/api/docs/models/gpt-oss-120b).
- [gpt-oss-20b model reference](https://developers.openai.com/api/docs/models/gpt-oss-20b).
