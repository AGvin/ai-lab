# Granite Embedding English R2

IBM English retrieval family comprising two bi-encoder embedding models and a separately trained cross-encoder reranker. This family is distinct from Granite Embedding Multilingual R2.

## Model boundaries

The 149M retriever produces 768-dimensional vectors; the 47M small retriever produces 384-dimensional vectors. The reranker scores query-document pairs rather than producing interchangeable index vectors. Only the larger retriever has an explicit derivative relation to the reranker. Published weights use Apache-2.0; hosted terms differ.

## Members

- [Granite Embedding English R2 — 149M retriever](./sub/models/sub/granite-embedding-english-r2/)
- [Granite Embedding Small English R2 — 47M retriever](./sub/models/sub/granite-embedding-small-english-r2/)
- [Granite Embedding Reranker English R2 — cross-encoder](./sub/models/sub/granite-embedding-reranker-english-r2/)

## Official resources

- [149M retriever](https://huggingface.co/ibm-granite/granite-embedding-english-r2)
- [47M retriever](https://huggingface.co/ibm-granite/granite-embedding-small-english-r2)
- [Cross-encoder reranker](https://huggingface.co/ibm-granite/granite-embedding-reranker-english-r2)

## Deployment validation

Pin the exact checkpoint revision and compatible runtime version. Measure memory, latency and retrieval or reranking quality on representative inputs. Check runtime-specific artifacts and hosted-service terms separately from the downloaded-weight license.

Published benchmark results are producer claims; this page does not establish independent benchmark reproduction or deployed performance.
