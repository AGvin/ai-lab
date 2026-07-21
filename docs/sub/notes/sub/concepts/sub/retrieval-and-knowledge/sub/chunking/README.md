# Chunking

Chunking divides source material into smaller retrievable units that can be indexed, ranked, and placed into a model context.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Core idea

A chunk should be small enough to retrieve precisely but large enough to preserve the information needed to understand it. Good boundaries usually follow document structure such as headings, paragraphs, functions, table rows, or conversation turns rather than arbitrary character counts.

## Common strategies

- Fixed token windows with overlap.
- Paragraph or heading-based segmentation.
- Recursive splitting that falls back to smaller units.
- Code-aware splitting by function, class, or module.
- Parent-child retrieval, where small chunks find a larger context block.

## Practical use

Choose chunk sizes using the tokenizer and the downstream model's context budget. Preserve source metadata, headings, page numbers, and document versions. Test retrieval with realistic questions, including questions whose answer crosses a boundary.

## Trade-offs and limitations

Small chunks improve precision but may omit context. Large chunks preserve context but reduce ranking specificity and consume more tokens. Excessive overlap increases storage and can return duplicate evidence.

## Common mistakes

- Splitting tables, code blocks, or definitions in the middle.
- Applying one chunk size to every content type.
- Dropping titles and hierarchy from chunk metadata.
- Evaluating only whether a chunk contains keywords, not whether it answers the query.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Embeddings](../embeddings/)
- [Reranking](../reranking/)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)