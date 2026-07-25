# GPT-5.6 Sol

GPT-5.6 Sol is the flagship tier of the GPT-5.6 generation for complex professional work.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Profile

- Model ID: `gpt-5.6-sol`
- Alias: `gpt-5.6`
- Primary use case: complex reasoning, coding, research, tool use, computer use, science, cybersecurity, and design
- Modalities: text and image input; text output
- Context window: 1,050,000 tokens
- Maximum output: 128,000 tokens
- Knowledge cutoff: February 16, 2026
- Reasoning effort: `none`, `low`, `medium`, `high`, `xhigh`, `max`

## Pricing

Standard API token pricing per one million tokens:

- Input: $5.00
- Cached input: $0.50
- Output: $30.00

Prompts above 272,000 input tokens use the long-context pricing multiplier documented by OpenAI.

## Supported capabilities

The official model page lists streaming, function calling, structured outputs, image input, web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP, and tool search.

Fine-tuning is not supported.

## Selection guidance

Choose Sol when capability and difficult-task reliability matter more than minimum token cost. Use an explicit model ID instead of the generation alias when reproducibility matters.

## Related pages

- [GPT-5.6](../../)
- [GPT model family](../../../..)

## Sources

- [GPT-5.6 Sol model page](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
- [GPT-5.6 launch announcement](https://openai.com/index/gpt-5-6/)
