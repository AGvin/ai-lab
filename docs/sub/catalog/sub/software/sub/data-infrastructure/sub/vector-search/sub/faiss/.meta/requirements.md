# Documentation Requirements

## Requirements

- Identify Faiss as Meta Fundamental AI Research's released open-source C++ library (with Python interfaces) for dense-vector similarity search and clustering, not as a managed database or a hosted service.
- Keep Faiss under the role-based `software/data-infrastructure/vector-search` owner because its primary role is vector indexing and similarity search; the taxonomy includes libraries/extensions as well as database systems when that is their primary role.
- Distinguish an embeddable vector index library from full database products with storage servers, metadata APIs, operational controls, and hosted management.
- Treat CPU/GPU implementation choices, Python wrappers, index algorithms, and optional integrations as parts of Faiss, not automatically separate software identities.
- Attribute speed and recall benchmarks to exact index, dataset, accelerator, software version, and configuration; do not present project-maintained performance descriptions as universal comparative measurements.
- Keep current supported hardware, CUDA/ROCm compatibility, binary distributions, release behavior, and APIs freshness-sensitive.
- Preserve Meta producer provenance with an inverse `produces` relation.

## Validation

- The reader can distinguish Faiss the vector-search library from managed vector databases and from independent self-managed vector database products.
- Official repository and documentation links match the entity metadata.
- GPU and CPU implementation variants are not duplicated as separate products.
- Meta has the reciprocal `produces` relation.
