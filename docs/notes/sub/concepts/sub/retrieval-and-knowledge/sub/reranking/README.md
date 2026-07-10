# Reranking

Reranking applies a more precise relevance model to a small set of candidates returned by an initial retriever.

## Core idea

Fast retrievers optimize recall and may return many weak candidates. A reranker examines the query and each candidate more deeply, then reorders or filters them. Cross-encoder rerankers often provide better relevance because they process the query and passage together, but they are slower than embedding similarity.

## Practical use

- Improve the evidence passed to a RAG model.
- Combine candidates from semantic and lexical search.
- Remove near-duplicate or weakly related chunks.
- Select the best few passages under a tight context budget.

## Trade-offs and limitations

Reranking adds latency and compute proportional to the number of candidates. If the initial retriever fails to include the correct document, the reranker cannot recover it. Reranker scores are also task- and model-specific.

## Good practice

Tune the initial candidate count and final context count separately. Evaluate retrieval recall before reranking and precision after reranking. Preserve diversity when a question requires evidence from several documents.

## Common mistakes

- Reranking only the top two or three weak candidates.
- Passing every reranked result to the model regardless of score.
- Optimizing reranker metrics without measuring final answer quality.
- Removing supporting passages because they repeat a topic from another source.

## Related concepts

- [Retrieval and Knowledge](../../)
- [Hybrid Search](../hybrid-search/)
- [Retrieval Evaluation](../../../evaluation-and-operations/sub/retrieval-evaluation/)
- [Context Window](../../../model-usage-and-generation/sub/context-window/)
