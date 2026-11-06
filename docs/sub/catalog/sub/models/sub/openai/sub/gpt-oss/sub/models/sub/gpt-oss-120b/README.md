# gpt-oss-120b

`gpt-oss-120b` is OpenAI’s downloadable text-only reasoning model in the gpt-oss family, distributed under Apache 2.0.

## Profile

The mixture-of-experts profile reports 117 billion total parameters and 5.1 billion active parameters, a 131,072-token context window, and a June 1, 2024 knowledge cutoff [Model reference](https://developers.openai.com/api/docs/models/gpt-oss-120b).

Reasoning effort supports low, medium, and high. Open weights can be fine-tuned in a compatible deployment [Model reference](https://developers.openai.com/api/docs/models/gpt-oss-120b).

## Operating boundaries

The model is not served in OpenAI’s API or ChatGPT, and OpenAI’s API fine-tuning service does not fine-tune these weights. The deployment operator supplies the runtime and tool-execution controls [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).

Active parameter count measures per-token computation, not the total weights that must be stored. It does not by itself establish VRAM, latency, or hardware fit.

## Relations

- Member of: [gpt-oss](../../../../README.md).

## Official resources

- [gpt-oss-120b model reference](https://developers.openai.com/api/docs/models/gpt-oss-120b).
- [Open-weight FAQ](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss).
