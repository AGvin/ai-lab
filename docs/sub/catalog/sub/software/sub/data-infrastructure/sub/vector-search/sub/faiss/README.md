# Faiss

Faiss is Meta Fundamental AI Research's open-source C++ library, with Python interfaces, for dense-vector similarity search and clustering.

## Scope and capabilities

Faiss provides embeddable search indexes, including CPU and optional GPU implementations. It is a library, not a managed service or a complete distributed vector database with its own general-purpose storage server and administrative APIs.

## Deployment, evidence and boundaries

Index selection, exact versus approximate retrieval, dimensionality, accelerator support, data distribution and parameters affect latency and recall. Compare benchmarks only with explicit datasets, hardware, software versions and index configurations; verify supported CUDA/ROCm, builds and API versions before deployment.

## Relations

- Produced by: [Meta](../../../../../../../producers/sub/m/sub/meta/)

## Official resources

- [Documentation](https://faiss.ai/)
- [Source repository](https://github.com/facebookresearch/faiss)
