# Documentation Requirements

## Requirements

- Use the reader-facing title `Retrieval Evaluation`.
- Define retrieval evaluation as measuring how effectively a retrieval system or retrieval stage maps an information need/query to an ordered or unordered set of corpus items/evidence under explicit relevance, utility, authorization, and workload criteria.
- Keep retrieval evaluation architecture-neutral. Lexical, sparse, dense/vector, hybrid, learned reranking, late-interaction, graph-assisted, metadata-filtered, or other retrieval approaches can be evaluated through the same high-level evidence framework when their outputs are comparable.
- Define the evaluated retrieval stage explicitly: candidate generation, filtering, reranking, final top-k selection, or the complete retrieval pipeline. A strong reranker can hide poor candidate recall, while a strong candidate retriever can be harmed by later filtering/reranking.
- Require the query/information-need set, corpus/index version, item granularity, relevance judgments or utility criteria, retrieval cutoff(s), filtering/access policy, and metric definitions to be versioned/identified for meaningful comparison.
- Distinguish retrieval effectiveness from end-to-end RAG/generation quality. A generator can answer correctly from prior knowledge despite retrieval failure or produce an incorrect/unfaithful answer despite retrieving excellent evidence; evaluate retrieval and downstream generation separately and together when both matter.
- Explain relevance as a task/query-dependent judgment rather than an intrinsic document property. Binary relevance, graded relevance, passage-level support, novelty/diversity, answer sufficiency, authority, freshness, and task utility can require different judgment schemes and metrics.
- Treat relevance judgments as incomplete or uncertain when the assessment process does not exhaustively label the corpus. An unjudged item must not automatically be interpreted as non-relevant unless the evaluation protocol explicitly establishes that assumption.
- Explain that multiple items or evidence sets can legitimately satisfy one information need. Evaluation should not require a single canonical passage/document when several independent or complementary sources are acceptable.
- Introduce precision@k as the proportion of retrieved top-k items judged relevant under the defined relevance scheme and recall@k as the proportion of the judged/known relevant set retrieved within top-k, while making clear that interpretation depends on judgment completeness and the selected denominator.
- Introduce rank-sensitive metrics such as reciprocal rank/MRR, average precision/MAP, and DCG/nDCG as common families without making one metric universal. MRR emphasizes the first relevant result; MAP/precision-recall families reward broader retrieval; nDCG supports graded relevance and rank discounting.
- Distinguish retrieval recall from `context coverage` or answer sufficiency in multi-evidence tasks. Retrieving one relevant item can be insufficient when a task requires multiple facts/documents, while high document-level recall can still omit the exact evidence needed downstream.
- Include no-answer/no-relevant-document cases where appropriate. A retrieval system should be evaluated for returning little/no evidence or appropriately abstaining/filtering when the corpus lacks relevant authorized material, rather than always being rewarded for returning something.
- Treat access-control/authorization as a separate correctness requirement where applicable. A highly relevant but unauthorized item is not a successful retrieval for a user/request whose policy excludes that item.
- Explain that duplicates/near-duplicates, chunking/granularity, corpus freshness, metadata quality, query formulation, filters, top-k, reranker depth, index construction, and retrieval-time configuration can materially change metrics without changing the underlying model alone.
- Distinguish effectiveness metrics from efficiency/operational metrics. Latency, throughput, memory/index size, storage, query cost, and refresh/build cost matter to retrieval-system selection but retain metric/performance/cost ownership rather than being collapsed into relevance quality.
- Require matched corpora/query sets/judgments/protocols for direct comparison. Cross-dataset or cross-version score differences do not by themselves establish that one retriever is universally better.
- Keep concrete retrieval benchmarks/datasets, query sets, qrels, corpus/index artifacts, model/service identities, current scores, tuning parameters, benchmark runs, and deployment recommendations with their applicable catalog/evidence/benchmark/decision owners.
- Use the canonical entity references as research inputs for test-collection/relevance-judgment evaluation and architecture-diverse retrieval comparison when reader-facing rendering is activated.

## Validation

- Retrieval evaluation is distinguished from end-to-end answer/RAG evaluation and from retrieval-system architecture itself.
- Candidate retrieval, filtering, reranking, and final selection stages are not silently conflated when stage-specific evidence matters.
- Unjudged documents/items are not universally treated as irrelevant without an explicit protocol assumption.
- Precision/recall/rank-sensitive metrics are defined with their cutoffs/denominators/relevance assumptions rather than as context-free numbers.
- Multiple relevant/sufficient evidence sets and multi-document requirements are supported rather than assuming one reference passage.
- Unauthorized retrieval is not counted as successful simply because it is semantically relevant.
- Concrete corpora, qrels, scores, models, runtime settings, and deployment recommendations remain outside the reusable retrieval-evaluation owner.
