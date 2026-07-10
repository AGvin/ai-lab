# Mixture of Experts

Mixture of Experts is a sparse architecture in which a router selects a small subset of expert networks to process each token or input.

## Core idea

Experts are typically alternative feed-forward blocks. The router scores them and activates the top choices. This increases total model capacity without multiplying computation by the full number of experts.

## Practical implications

- Total parameter count can be much larger than active parameter count.
- Storage and memory must still accommodate expert weights.
- Inference efficiency depends on routing, batching, and device placement.
- Training includes load-balancing objectives to avoid expert collapse.

## Trade-offs and limitations

MoE models can achieve strong quality per unit of compute, but serving them across devices may require expensive communication. Small local batches may not utilize experts efficiently. Routing decisions can also make behavior harder to analyze.

## Common mistakes

- Assuming inactive experts consume no memory.
- Comparing an MoE model with a dense model only by total parameters.
- Expecting all runtimes to support the architecture efficiently.
- Treating experts as clean human-understandable domains.

## Related concepts

- [Foundations and Architecture](../../)
- [Dense and Sparse Models](../dense-and-sparse-models/)
- [Model Loading](../../../inference-and-serving/sub/model-loading/)
- [Throughput](../../../inference-and-serving/sub/throughput/)
