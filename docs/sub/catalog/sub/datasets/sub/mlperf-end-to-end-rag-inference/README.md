# MLPerf End-to-End RAG Inference

## Relations

- Produced by: [MLCommons](../../../producers/sub/m/sub/mlcommons/)
- Member of: [MLPerf Inference](../mlperf-inference/)

MLPerf End-to-End RAG Inference is MLCommons' benchmark for measuring a complete retrieval-augmented question-answering pipeline, released within MLPerf Inference v6.1.

## Scope and boundaries

The benchmark contains database-ingestion (`e2e-rag-db`) and question-answering (`e2e-rag-qna`) workloads. The initial design uses a frozen FRAMES query/corpus snapshot and multiple model/pipeline components, so it is distinct from FRAMES itself or any one model, vector database or serving framework.

Reference models, corpus preparation, hop limits, accuracy/performance metrics and compliance checks are release-specific. Vendor submissions report the exact pipeline and system configuration tested; they do not establish a universal RAG ranking or transfer component ownership to MLCommons.

## Official resources

- [End-to-End RAG benchmark design](https://mlcommons.org/2026/08/endtoend-inference/)
- [MLPerf Inference v6.1 release](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)
- [Official documentation](https://docs.mlcommons.org/inference/index_gh/)
