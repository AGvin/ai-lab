# Documentation Requirements

## Requirements

- Identify gpt-oss as OpenAI's released open-weight family of reasoning models and their separately named policy-classification fine-tunes.
- Preserve the shared source-backed boundary: downloadable open weights, Apache 2.0 licensing, Harmony-formatted interaction, configurable reasoning effort, text-only model modality, fine-tuning support, and agent/tool-oriented capabilities where applicable.
- Keep concrete parameter counts, active-parameter counts, memory/hardware fit, artifacts, quantizations, runtime support, and benchmark claims with the concrete model or artifact/runtime owner.
- Keep OpenAI-hosted API endpoint listings, third-party inference-provider availability, pricing, runtime-specific tool emulation, and integration behavior outside intrinsic open-weight model identity.
- Keep OpenAI Harmony as a separate canonical format/specification identity rather than duplicating it into the model family.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- gpt-oss remains an open-weight model family rather than an inference runtime or API service.
- Concrete 120B and 20B members remain distinct.
- Producer provenance resolves bidirectionally to OpenAI.

## Source-scoped operating boundaries

- These weights are not served through OpenAI’s API or ChatGPT. Deployment, fine-tuning, tool execution, infrastructure, and data handling are the operator’s or hosting provider’s responsibility [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- Safeguard models classify content against a supplied policy. Their preview status and policy-driven task differ from a general-purpose chat assistant [Safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).

## Source evidence

- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
- [gpt-oss-safeguard release](https://openai.com/index/introducing-gpt-oss-safeguard/).
- [gpt-oss-safeguard guide](https://developers.openai.com/cookbook/articles/gpt-oss-safeguard-guide).
- [gpt-oss-120b model reference](https://developers.openai.com/api/docs/models/gpt-oss-120b).
- [gpt-oss-20b model reference](https://developers.openai.com/api/docs/models/gpt-oss-20b).
