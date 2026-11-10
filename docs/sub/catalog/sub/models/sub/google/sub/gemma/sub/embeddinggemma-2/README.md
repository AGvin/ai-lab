# EmbeddingGemma 2

Google DeepMind's 740M-parameter open multimodal embedding model, combining a 270M text backbone with optional 170M vision and 300M audio encoders in a shared 768-dimensional space.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- The model uses an 8K context and supports 128-, 256-, 512-, and 768-dimensional Matryoshka embeddings. Re-normalize vectors after truncation before cosine similarity; truncation alone does not preserve unit length. [Model and retrieval instructions](https://huggingface.co/google/embeddinggemma-2).
- Use the task prefixes for text queries/documents; image, video, and audio input do not take those prefixes. The 270M text-only configuration is distinct from the complete 740M multimodal model. [Prompt and component configuration](https://huggingface.co/google/embeddinggemma-2).
- Apache-2.0 governs the current released weights. Embedding output is a retrieval representation, not generated text, an access-control mechanism, or a guarantee of anonymization. [Model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2).

## Official resources

- <https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2>
- <https://deepmind.google/models/gemma/embeddinggemma/>
- <https://huggingface.co/google/embeddinggemma-2>
