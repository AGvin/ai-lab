# Granite Embedding Small English R2

IBM 47M English ModernBERT bi-encoder producing 384-dimensional retrieval vectors. The official card documents an 8192-token context.

## Retrieval contract

Use checkpoint-specific tokenizer, pooling and normalization. Evaluate retrieval quality, latency and memory on representative inputs. Family membership and architecture similarity do not establish a derivative relation to the larger retriever. Embedding vectors are not cross-encoder scores.

The published weights use Apache-2.0; hosted terms are separate.

- [English R2 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-embedding-small-english-r2)

## Deployment validation

Pin the exact checkpoint revision and compatible runtime version. Measure memory, latency and retrieval or reranking quality on representative inputs. Check runtime-specific artifacts and hosted-service terms separately from the downloaded-weight license.

Published benchmark results are producer claims; this page does not establish independent benchmark reproduction or deployed performance.
