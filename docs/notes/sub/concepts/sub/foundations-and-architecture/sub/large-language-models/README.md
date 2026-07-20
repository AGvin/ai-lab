# Large Language Models

A large language model is a neural network trained to model and generate token sequences at substantial scale.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

Most modern LLMs are trained through next-token prediction or related objectives. This produces broad language, coding, reasoning, and pattern-completion capabilities. Instruction tuning and preference optimization then shape the base model into a more useful assistant or task model.

## Capabilities

- Generate, summarize, transform, and classify text.
- Produce and analyze code.
- Use tools through structured calls.
- Work with retrieved documents.
- Follow natural-language instructions.

## Practical use

An LLM should be treated as a probabilistic component. Applications add prompts, tools, retrieval, state, validation, and permissions around it. Model selection depends on quality, context size, latency, cost, deployment, and safety requirements.

## Trade-offs and limitations

LLMs can hallucinate, mishandle exact calculations, and reproduce training-data biases. Their knowledge is not automatically current or attributable. Larger models often improve capability but increase cost and resource use.

## Common mistakes

- Treating generated text as database output.
- Assuming the model knows current private information.
- Using an LLM for deterministic tasks without validation.
- Comparing models only by parameter count.

## Related concepts

- [Foundations and Architecture](../../)
- [Transformers](../transformers/)
- [Tokens and Tokenization](../../../model-usage-and-generation/sub/tokens-and-tokenization/)
- [Hallucinations](../../../model-usage-and-generation/sub/hallucinations/)
