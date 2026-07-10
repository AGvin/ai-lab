# Chunking

<!--
ai_content:
  managed: true
  l10n: true
-->

Dividing source material into retrievable units while preserving enough context for use.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

## Core idea

Dividing source material into retrievable units while preserving enough context for use. In practical AI work, the term is useful because it names a specific part of the system rather than treating the model as a single opaque component. Understanding where it appears in the workflow makes configuration choices and failure analysis more precise.

## How it works

- Chunking divides source material into units that can be indexed and inserted into model context.
- Chunk size, overlap, section boundaries, code symbols, tables, and metadata determine whether the retrieved unit is understandable.
- Hierarchical or structure-aware chunking can retain parent headings and neighboring context without indexing entire documents as one block.

The exact implementation varies by model family, provider, and runtime. The important distinction is the role the concept plays in the end-to-end system and which inputs, state, or resources it changes.

## Why it matters

Chunking affects how an AI system should be selected, configured, tested, or operated. It can influence output quality, resource requirements, reliability, or the amount of control available to the surrounding application.

## Practical uses

- Prepare documentation, code, transcripts, contracts, and knowledge bases for retrieval.
- Balance retrieval precision against the need for enough surrounding context.

## Example

A Markdown guide can be chunked by headings while preserving the document title, section path, and version as metadata.

## Trade-offs and limitations

- Chunks that are too small lose meaning; chunks that are too large reduce retrieval precision and consume context.
- Simple fixed-size splitting can break tables, functions, or argument chains.

Do not evaluate this concept in isolation. Test it together with the actual model, data, runtime, tools, and workload that will be used in production or local experiments.

## Practical checklist

- What problem is Chunking expected to solve in this workflow?
- Which inputs, settings, or resources does it depend on?
- How will success and failure be measured?
- What changes when the model, runtime, dataset, or context size changes?

## Related concepts

- [Retrieval and Knowledge](../../)
- [Embeddings](../embeddings/)
- [Semantic Search](../semantic-search/)
