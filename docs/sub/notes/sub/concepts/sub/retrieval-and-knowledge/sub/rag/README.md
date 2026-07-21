# RAG (Retrieval-Augmented Generation)

Retrieval-Augmented Generation (RAG) is an architecture that gives a language model relevant external information before it generates an answer.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Purpose

Use this page to understand RAG as a practical pattern for grounding large language model responses in private, current, or domain-specific data without retraining the model.

## What it is

RAG combines two operations:

1. Retrieve relevant information from an external knowledge source.
2. Generate an answer using the retrieved information as model context.

```text
LLM + retrieval from external data = RAG
```

RAG is not a separate model type. It is a system architecture built around a language model, one or more data sources, and a retrieval pipeline.

## How it works

A typical RAG system has an indexing flow and a query flow.

### Indexing flow

```text
Documents
    -> parsing and normalization
    -> chunking
    -> embeddings and metadata
    -> search index
```

Documents are divided into smaller units called chunks. Each chunk is stored with useful metadata such as its source, title, section, path, version, or access policy.

Many systems also create an embedding for each chunk. An embedding is a numerical representation used to find semantically similar content.

### Query flow

```text
User question
    -> query analysis
    -> retrieval
    -> optional reranking
    -> prompt context
    -> LLM
    -> grounded answer
```

The retriever searches for candidate chunks. An optional reranker then orders those candidates more precisely before the best results are added to the model context.

## Core components

| Component | Responsibility |
| --- | --- |
| Data source | Stores the original documents or records. |
| Loader or parser | Extracts and normalizes text, structure, and metadata. |
| Chunker | Divides large documents into retrievable units. |
| Embedding model | Converts text into vector representations for semantic search. |
| Search index | Stores searchable text, vectors, and metadata. |
| Retriever | Selects candidate chunks for a query. |
| Reranker | Reorders candidates by estimated relevance. |
| Generator | Produces the final answer from the question and retrieved context. |

Common search indexes include PostgreSQL with `pgvector`, Qdrant, Milvus, Weaviate, Pinecone, Elasticsearch, OpenSearch, and Chroma.

## Retrieval strategies

### Vector search

Vector search is useful when the query and the relevant text express the same idea with different words.

For example:

```text
Query: How can I reduce model memory usage?
Document: Four-bit quantization lowers VRAM requirements.
```

### Keyword search

Keyword or BM25 search is often better for exact identifiers such as:

- model names;
- function names;
- version numbers;
- configuration keys;
- error messages;
- product identifiers.

### Hybrid search

Practical RAG systems often combine semantic and keyword retrieval:

```text
vector search + keyword search + reranking
```

This improves recall for natural-language questions while preserving precision for exact terms.

## Practical example

Assume AI Lab contains notes about local models, quantization, GPUs, and inference runtimes.

A user asks:

```text
Which model can I run on a GPU with 12 GB of VRAM?
```

A RAG pipeline can retrieve:

- model memory requirements;
- quantization notes;
- runtime compatibility details;
- local benchmark results;
- hardware-specific findings.

The language model then answers from those retrieved notes instead of relying only on its training data.

## Minimal implementation flow

```js
const queryEmbedding = await embeddingModel.embed(question);

const candidates = await vectorStore.search({
    vector: queryEmbedding,
    limit: 20
});

const rankedChunks = await reranker.rank({
    query: question,
    documents: candidates
});

const context = rankedChunks
    .slice(0, 5)
    .map((chunk) => chunk.content)
    .join('\n\n');

const answer = await llm.generate({
    system: [
        'Answer from the supplied context.',
        'Do not invent facts that are absent from the sources.',
        'State clearly when the available evidence is insufficient.'
    ].join(' '),
    prompt: `Context:\n${context}\n\nQuestion:\n${question}`
});
```

This example omits production concerns such as access control, caching, observability, source citations, prompt injection defenses, and index synchronization.

## RAG compared with related approaches

| Approach | Primary purpose | Changes model weights | Best suited for |
| --- | --- | --- | --- |
| RAG | Supply external knowledge at query time | No | Current, private, or frequently changing information |
| Fine-tuning | Adapt model behavior or task performance | Yes | Style, output format, domain behavior, or specialized tasks |
| Prompt engineering | Guide behavior through instructions | No | Response constraints and task framing |
| Long-context prompting | Send source material directly to the model | No | Small or bounded document sets that fit the context window |

Fine-tuning is not a dependable replacement for a searchable factual knowledge base. RAG is generally easier to update because documents can be reindexed without retraining the model.

## Advantages

- Uses private or organization-specific information.
- Supports information that changes after model training.
- Allows source attribution and evidence inspection.
- Avoids retraining for ordinary knowledge updates.
- Can reduce unsupported answers when retrieval returns relevant evidence.
- Can work with hosted or local language models.
- Can enforce document-level access controls before context reaches the model.

## Limitations

RAG does not guarantee a correct answer.

Typical failure modes include:

- the required source was never indexed;
- chunk boundaries removed important context;
- retrieval returned irrelevant candidates;
- the correct result did not enter the selected `top-k` set;
- stale or contradictory documents were retrieved;
- the model ignored or misinterpreted the supplied context;
- retrieved content contained prompt injection or untrusted instructions;
- the final answer made claims not supported by the retrieved evidence.

A strong language model cannot reliably compensate for a weak retrieval pipeline.

## RAG for source code

Code retrieval often needs more than generic text embeddings.

Useful signals include:

- file paths;
- symbols and signatures;
- classes and functions;
- imports and exports;
- abstract syntax trees;
- dependency graphs;
- exact string search;
- Git history and version metadata.

A query such as `Where is createEmbedding defined?` is usually better served by symbol or keyword search than by vector similarity alone.

## Evaluation

Evaluate retrieval and generation separately.

### Retrieval evaluation

Measure whether the system returns the required evidence:

- recall at `k`;
- precision at `k`;
- mean reciprocal rank;
- normalized discounted cumulative gain;
- reranker quality;
- retrieval latency.

### Answer evaluation

Measure whether the final response is useful and supported:

- factual correctness;
- faithfulness to retrieved evidence;
- citation accuracy;
- completeness;
- refusal when evidence is insufficient;
- answer latency and cost.

End-to-end answer quality can hide retrieval failures, so both layers should be tested independently.

## Common use cases

- Documentation assistants.
- Repository and source-code search.
- Internal company knowledge bases.
- Customer-support assistants.
- Contract and policy analysis.
- Research assistants with source citations.
- Product catalogs and technical support.
- Personal knowledge bases.

## Summary

RAG connects a language model to external knowledge at query time.

```text
user question
    + relevant retrieved evidence
    + language model
    = context-grounded answer
```

Its effectiveness depends on data quality, document structure, retrieval, reranking, prompt construction, and answer evaluation rather than on the language model alone.

## References

- Patrick Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), 2020.