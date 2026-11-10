# text-embedding-3-small

`text-embedding-3-small` is OpenAI’s third-generation text-to-vector embedding model. OpenAI positions the small variant for a lower-cost, smaller-vector option.

## Profile

Its default output is 1,536 dimensions, with an 8,192-token maximum input. The dimensions parameter can shorten the output vector [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).

## Operating boundaries

Vector length is an adjustable representation choice, not proof of downstream retrieval quality. Choose and evaluate the dimensions used by the index and queries together [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).

Vectors from different model/configuration spaces should not be compared as if interchangeable. The retrieval application still controls which source documents a user may access.

## Relations

- Member of: [OpenAI Text Embedding](../../../../README.md).

## Official resources

- [text-embedding-3-small model reference](https://developers.openai.com/api/docs/models/text-embedding-3-small).
- [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings).
