# OpenAI Harmony

OpenAI Harmony is OpenAI's response and chat format for the gpt-oss open-weight model series.

## Format boundary

gpt-oss models were trained on Harmony, so direct inference must apply the format correctly; provider or runtime integrations may apply that formatting on the user's behalf. The format defines message roles, channels, recipients and tool-call structure, instruction hierarchy, and serialization or parsing boundaries according to the current official specification.

Harmony is distinct from the `openai-harmony` reference implementation and from the gpt-oss model identities themselves. Encoding details, package versions, token sequences, supported runtime integrations, and implementation APIs are version-sensitive. Harmony compatibility must not be generalized to models that were not trained for the format.

## Relations

- Produced by [OpenAI](../../../../../producers/sub/o/sub/openai/).

## Official resources

- [OpenAI Harmony format](https://cookbook.openai.com/articles/openai-harmony)
- [OpenAI Harmony repository](https://github.com/openai/harmony)
- [gpt-oss deployment safety information](https://deploymentsafety.openai.com/gpt-oss/a2)
