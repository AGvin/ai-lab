# K2-Horizon-375B-A23B

K2-Horizon-375B-A23B is a concrete model represented in AI Lab.

## Translations

- English

## Relations

- Member of: [`catalog/models/institute-of-foundation-models/k2-horizon`](../../../../)

## Specifications and operating boundaries

IFM describes this sparse Mixture-of-Experts model as having 375B total parameters and 23B activated per token. These are publisher-reported figures, not an independent tensor count.

The official model card reports native 524,288-token context and Apache-2.0 licensing. Activated parameters do not represent the full weight-storage footprint. Memory and throughput depend on precision, KV cache, batch size and serving implementation; published deployment recipes are examples rather than minimum hardware requirements.

Benchmark results are publisher evaluations and have not been independently reproduced here. Quantized packages remain distributions of this trained model rather than additional model identities.

## Official resources

- <https://huggingface.co/IFM/K2-Horizon-375B-A23B>
