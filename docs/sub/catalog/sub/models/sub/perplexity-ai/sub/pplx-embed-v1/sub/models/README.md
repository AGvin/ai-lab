# PPLX Embed V1 Models

Five distinct Perplexity embedding and retrieval checkpoints are represented, including two standard dense encoders, two document-contextualized dense encoders and a late-interaction derivative.

## Dense embedding models

- [PPLX Embed V1 0.6B](./sub/pplx-embed-v1-0-6b/)
- [PPLX Embed V1 4B](./sub/pplx-embed-v1-4b/)

## Contextualized dense embedding models

- [PPLX Embed Context V1 0.6B](./sub/pplx-embed-context-v1-0-6b/)
- [PPLX Embed Context V1 4B](./sub/pplx-embed-context-v1-4b/)

## Late-interaction retrieval model

- [PPLX Embed V1 Late 0.6B](./sub/pplx-embed-v1-late-0-6b/) — token-level 128-dimensional vectors and MaxSim scoring, derived from standard V1 0.6B.

The late-interaction model's multi-vector scoring contract is not interchangeable with one-vector-per-input dense retrieval. API pricing, quotas and batching are separate hosted-service concerns.

- [PPLX Embed V1 family](../../)
