# Granite Embedding English R2

IBM 149M English ModernBERT bi-encoder producing 768-dimensional vectors for retrieval, not cross-encoder relevance scores.

## Retrieval contract

Use the checkpoint-specific tokenizer, pooling and normalization consistently for queries and indexed documents. Validate retrieval quality on the target corpus and measure memory and latency. This checkpoint is the explicitly named parent of [Granite Embedding Reranker English R2](../granite-embedding-reranker-english-r2/).

The published weights use Apache-2.0; hosted terms are separate.

- [English R2 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-embedding-english-r2)

## Deployment validation

Pin the exact checkpoint revision and compatible runtime version. Measure memory, latency and retrieval or reranking quality on representative inputs. Check runtime-specific artifacts and hosted-service terms separately from the downloaded-weight license.

Published benchmark results are producer claims; this page does not establish independent benchmark reproduction or deployed performance.
