# Context Window

The context window is the maximum tokenized information a model can consider during one request, including instructions, conversation history, retrieved documents, tool results, and generated output.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A larger advertised context window allows more material to be supplied, but it does not guarantee that every detail will be used equally well. Relevant facts can be diluted by unrelated content, repeated instructions, or information placed far from the current question. Effective context is therefore both a capacity constraint and an information-selection problem.

## What occupies context

- System and developer instructions.
- User and assistant conversation history.
- Tool schemas, tool results, files, images, and retrieved chunks.
- The model's planned or generated completion.

## Practical use

- Reserve output space instead of filling the entire window with input.
- Summarize or remove stale conversation history.
- Retrieve only evidence relevant to the current task.
- Place critical constraints clearly and repeat them only when necessary.
- Test long-context behavior with realistic documents rather than relying only on the published limit.

## Trade-offs and limitations

Longer context generally increases memory use, processing time, and cost. Some runtimes use a larger KV cache as context grows. Models may also show degraded recall or instruction adherence near their practical limits.

## Common mistakes

- Treating the context limit as a reliable working capacity.
- Appending every available document instead of retrieving selectively.
- Forgetting that the expected output also consumes tokens.
- Assuming old chat messages remain available after truncation or summarization.

## Related concepts

- [Model Usage and Generation](../../)
- [Tokens and Tokenization](../tokens-and-tokenization/)
- [Context Caching](../../../inference-and-serving/sub/context-caching/)
- [Chunking](../../../retrieval-and-knowledge/sub/chunking/)