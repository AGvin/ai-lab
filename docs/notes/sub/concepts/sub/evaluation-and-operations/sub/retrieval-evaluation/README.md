# Retrieval Evaluation

<!--
ai_content:
  managed: true
  l10n: true
-->

Retrieval evaluation measures whether a search or RAG system returns relevant, sufficient, correctly ranked, and authorized evidence.

## Core metrics

- **Recall at k:** whether relevant evidence appears in the top `k` results.
- **Precision at k:** how many retrieved items are relevant.
- **Mean reciprocal rank:** how early the first relevant result appears.
- **NDCG:** ranking quality when relevance has several levels.
- **Context coverage:** whether retrieved evidence is sufficient to answer the question.

## Core idea

Final answer quality alone can hide retrieval failures because a model may answer from prior knowledge or hallucinate. Retrieval and generation should be evaluated separately, then together.

## Practical use

Build query-document relevance labels from real tasks. Include exact identifiers, paraphrases, multi-document questions, no-answer cases, and access-control checks. Compare lexical, semantic, hybrid, and reranked systems.

## Trade-offs and limitations

Relevance labels can be subjective, and one query may have many acceptable evidence sets. Offline metrics may not reflect how a generator uses the context.

## Common mistakes

- Labeling only one passage as relevant when several support the answer.
- Measuring top-one accuracy for multi-document questions.
- Ignoring unauthorized but highly relevant results.
- Tuning retrieval on the final test set.

## Related concepts

- [Evaluation and Operations](../../)
- [Reranking](../../../retrieval-and-knowledge/sub/reranking/)
- [Hybrid Search](../../../retrieval-and-knowledge/sub/hybrid-search/)
- [Grounding](../../../retrieval-and-knowledge/sub/grounding/)
