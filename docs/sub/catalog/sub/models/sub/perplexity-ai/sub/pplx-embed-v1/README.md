# PPLX Embed V1

PPLX Embed V1 is Perplexity AI's **Qwen3-derived retrieval-model family**. Four concrete models provide **standard dense** or **document-contextualized dense** embeddings at 0.6B and 4B parameter classes. The separately released **Late 0.6B** checkpoint is a derivative using token-level multi-vector retrieval.

## Retrieval and deployment boundaries

Use standard dense checkpoints for independent query/text vectors and contextual variants where chunks depend on their enclosing document. The late-interaction derivative emits token-level vectors and uses MaxSim rather than the same single pooled vector; their indexing and scoring contracts must not be interchanged. Pooling, normalization, length constraints and performance belong to the chosen member.

The Perplexity Embeddings API is a separate hosted service: prices, rate limits, batching, endpoint behavior and client versions are not stable model-family properties. The late-interaction checkpoint has its own **MIT** weight license; do not generalize licensing from one member to every sibling.

## Relations

- Produced by: [Perplexity AI](../../../../../producers/sub/p/sub/perplexity-ai/)
- Members:
  - [PPLX Embed V1 0.6B](./sub/models/sub/pplx-embed-v1-0-6b/)
  - [PPLX Embed V1 4B](./sub/models/sub/pplx-embed-v1-4b/)
  - [PPLX Embed Context V1 0.6B](./sub/models/sub/pplx-embed-context-v1-0-6b/)
  - [PPLX Embed Context V1 4B](./sub/models/sub/pplx-embed-context-v1-4b/)
  - [PPLX Embed V1 Late 0.6B](./sub/models/sub/pplx-embed-v1-late-0-6b/)

[Open the model index](./sub/models/).

## Official resources

- [Perplexity Embeddings documentation](https://docs.perplexity.ai/docs/embeddings/quickstart)
- [Standard 0.6B model card](https://huggingface.co/perplexity-ai/pplx-embed-v1-0.6b)
- [Context 4B model card](https://huggingface.co/perplexity-ai/pplx-embed-context-v1-4b)
- [Late 0.6B model card](https://huggingface.co/perplexity-ai/pplx-embed-v1-late-0.6b)
