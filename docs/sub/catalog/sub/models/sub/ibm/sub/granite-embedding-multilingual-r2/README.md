# Granite Embedding Multilingual R2

Granite Embedding Multilingual R2 is IBM's April 2026 multilingual embedding family with 311M and 97M members.

## Identity and operating boundaries

Both models support long text sequences up to 32,768 tokens. Their cards distinguish broad multilingual pretraining coverage from enhanced support for 52 listed languages plus programming code. The 311M model uses 768-dimensional embeddings and supports Matryoshka outputs at 768, 512, 384, 256 and 128 dimensions; the 97M model uses 384-dimensional embeddings.

The 97M card explicitly documents that it was obtained from the 311M model through layer pruning and vocabulary selection. That exact relationship is materialized in the catalog. Both reviewed checkpoints state Apache-2.0 licensing.

ONNX/OpenVINO conversions and hosted endpoints are distributions or delivery routes, not additional learned models. Retrieval quality still depends on corpus, query/document roles, preprocessing and evaluation.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Embedding 97M Multilingual R2](sub/models/sub/granite-embedding-97m-multilingual-r2/) — member.
- [Granite Embedding 311M Multilingual R2](sub/models/sub/granite-embedding-311m-multilingual-r2/) — member.

## Official resources

- <https://www.ibm.com/granite/docs/models/embedding>
- <https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2>
- <https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2>
