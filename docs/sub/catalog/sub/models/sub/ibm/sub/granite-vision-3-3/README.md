# Granite Vision 3.3

Granite Vision 3.3 is IBM's visual-document model family, retaining a generative 2B checkpoint and a separately published specialist embedding derivative. A newer Granite Vision generation exists; the 3.3 generator is retained here as the explicit source model for the retrieval checkpoint.

## Model boundaries

The generative 2B model interprets document images and produces text. The derivative generates ColBERT-style page multi-vectors for retrieval and does not expose the same text-generation contract. The derivative link is explicit; do not project experimental generation features onto the retrieval model. The published weights use Apache-2.0; hosted terms may differ.

## Members

- [Granite Vision 3.3 2B — image-to-text](./sub/models/sub/granite-vision-3-3-2b/)
- [Granite Vision 3.3 2B Embedding — document retrieval](./sub/models/sub/granite-vision-3-3-2b-embedding/)

## Official resources

- [Generative checkpoint](https://huggingface.co/ibm-granite/granite-vision-3.3-2b)
- [Embedding checkpoint](https://huggingface.co/ibm-granite/granite-vision-3.3-2b-embedding)
