# PPLX Embed V1 Late 0.6B

PPLX Embed V1 Late 0.6B is Perplexity AI's released **late-interaction retrieval model**, continued from [PPLX Embed V1 0.6B](../pplx-embed-v1-0-6b/). It is a distinct trained checkpoint, not a pooling or quantization option of the dense encoder.

## Retrieval representation

The model emits **128-dimensional token-level embeddings** and uses **MaxSim** late-interaction scoring over query and document tokens. This requires a compatible multi-vector index and scoring pipeline; it is **not** interchangeable with the standard family's single dense vector per text or with ordinary dense-cosine search.

The published weights use the **MIT license**. Benchmarks, optimized kernels, GPU-specific integrations and serving speed are runtime- and configuration-dependent; validate retrieval accuracy and latency on representative queries and documents.

## Family and official source

- [PPLX Embed V1 family](../../../../)
- [Official Perplexity checkpoint](https://huggingface.co/perplexity-ai/pplx-embed-v1-late-0.6b)
