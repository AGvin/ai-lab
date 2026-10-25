# Granite Embedding Reranker English R2

IBM 149M English cross-encoder trained from [Granite Embedding English R2](../granite-embedding-english-r2/) to score query-document pairs.

## Reranking contract

Use joint query-document encoding to rerank candidate results. This checkpoint produces relevance scores rather than independent document vectors for a vector index. Measure reranking quality and candidate-batch latency separately from first-stage retrieval.

The published weights use Apache-2.0; hosted terms are separate.

- [English R2 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-embedding-reranker-english-r2)

## Deployment validation

Pin the exact checkpoint revision and compatible runtime version. Measure memory, latency and retrieval or reranking quality on representative inputs. Check runtime-specific artifacts and hosted-service terms separately from the downloaded-weight license.

Published benchmark results are producer claims; this page does not establish independent benchmark reproduction or deployed performance.
