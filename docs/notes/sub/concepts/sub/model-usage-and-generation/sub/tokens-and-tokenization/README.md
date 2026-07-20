# Tokens and Tokenization

Tokens are the units a model reads and generates. Tokenization converts text, code, punctuation, and sometimes whitespace into token identifiers from a fixed vocabulary.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A token is not the same as a word or character. Common words may map to one token, while uncommon words, identifiers, URLs, or non-Latin text may be split into several. Models operate on token sequences rather than raw text, so tokenization directly affects context usage, generation cost, latency, and how reliably a model handles unusual strings.

## Key points

- Different model families may tokenize the same text differently.
- Input tokens, generated output tokens, and hidden reasoning tokens may be counted separately by an API.
- Code, JSON, long numbers, and repeated whitespace can consume more context than their visual length suggests.
- Token boundaries can influence spelling, copying, arithmetic, and exact-string tasks.

## Practical use

- Estimate whether a prompt and expected answer fit inside the model context window.
- Compare API costs using token counts rather than character counts.
- Inspect unexpectedly expensive prompts, especially logs, source code, and large documents.
- Design chunk sizes for retrieval systems using the tokenizer of the generation or embedding model.

## Trade-offs and limitations

Larger vocabularies can represent frequent strings efficiently but require larger embedding tables. Smaller vocabularies split more text into pieces and may increase sequence length. Token count is therefore model-specific and should not be estimated with a tokenizer from an unrelated model.

## Common mistakes

- Treating one word as one token.
- Assuming the same token count across providers.
- Ignoring output and reasoning-token budgets when sizing a request.

## Related concepts

- [Model Usage and Generation](../../)
- [Context Window](../context-window/)
- [Sampling Parameters](../sampling-parameters/)