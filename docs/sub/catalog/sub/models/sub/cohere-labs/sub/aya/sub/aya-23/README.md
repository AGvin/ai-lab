# Aya 23

Aya 23 is the **23 May 2024** multilingual, instruction-tuned research model series from Cohere Labs and Cohere. Its two separately released text-generation models have **8B** and **35B** parameters, **23 languages**, and an **8,192-token** context. [Official announcement](https://cohere.com/blog/aya23) · [8B model card](https://huggingface.co/CohereLabs/aya-23-8B) · [35B model card](https://huggingface.co/CohereLabs/aya-23-35B)

## Model identity and lifecycle

Aya 23 predates Aya Expanse and Aya Vision. Both model cards identify separately released instruction-tuned weights, not interchangeable precision settings or API modes. The Command-family foundation and Aya Collection data are documented at the series level, but **no exact concrete training-parent checkpoint** is independently established in this catalog. Publisher evaluations are not an independent AI Lab benchmark. [Cohere release](https://cohere.com/blog/aya23) · [Model cards](https://huggingface.co/CohereLabs/aya-23-8B)

## Access, rights and deployment

Both Hugging Face repositories currently require agreeing to access conditions to obtain gated files. Both specify **CC-BY-NC-4.0**, the Cohere license addendum and Labs acceptable-use policy; do not treat their weights as unrestricted for commercial use. These are weight releases, not a guarantee of current public Cohere API routes. Deployment requires appropriate memory/accelerator resources, model-compatible tokenizer, runtime and precision. The 35B checkpoint has materially higher footprint. No independent inference, throughput test, weight download or Russian-control/ultimate-beneficial-ownership audit was performed. [8B repository](https://huggingface.co/CohereLabs/aya-23-8B) · [35B repository](https://huggingface.co/CohereLabs/aya-23-35B)

## Represented members

| Model | Scope |
| --- | --- |
| [Aya 23 8B](sub/models/sub/aya-23-8b/README.md) | Distinct smaller model; 8B parameters, 8K context and 23 languages. |
| [Aya 23 35B](sub/models/sub/aya-23-35b/README.md) | Distinct larger model; 35B parameters, 8K context and 23 languages. |

## Relations

- Member of: [Aya](../../README.md).
- Models: [Aya 23 8B](sub/models/sub/aya-23-8b/README.md), [Aya 23 35B](sub/models/sub/aya-23-35b/README.md).

## Official resources

- <https://cohere.com/blog/aya23>
- <https://huggingface.co/CohereLabs/aya-23-8B>
- <https://huggingface.co/CohereLabs/aya-23-35B>
