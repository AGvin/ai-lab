# Granite Vision 3.3 2B Embedding

Granite Vision 3.3 2B Embedding is IBM's multimodal document-retrieval checkpoint derived from [Granite Vision 3.3 2B](../granite-vision-3-3-2b/). It generates ColBERT-style page multi-vectors for retrieval, **not** image-to-text responses.

## Retrieval contract and safeguards

Use the dedicated processor and page multi-vector scoring/index contract. Validate retrieval across tables, charts and complex document layouts. The official example loads custom code: review and pin that code and model weights before execution. Experimental features of the parent generator do not automatically carry over to this derivative.

The published weights use Apache-2.0; hosted terms differ. Benchmark memory, latency and retrieval quality on the actual runtime and corpus.

## Family and official source

- [Granite Vision 3.3 family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-vision-3.3-2b-embedding)
