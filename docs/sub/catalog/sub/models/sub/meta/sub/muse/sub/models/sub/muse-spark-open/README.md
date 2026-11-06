# Muse Spark Open

Muse Spark Open is Meta's released **open-weight multimodal sparse-mixture-of-experts model**, distinct from hosted Muse Spark checkpoints. Meta documents **816B total parameters**, **42B active parameters** and a **one-million-token context window**.

## Weight and deployment boundaries

The checkpoint is published under the **Muse Model License**, not the Apache-2.0 license of some other Muse releases. Self-hosted inference and provider-hosted access are separate deployment surfaces. Total and active parameter counts do not imply a simple hardware-memory requirement; concrete format, precision, context state, batching, distributed runtime and available infrastructure all matter.

Pin the selected weights, inference stack and current license terms; test multimodal and agentic behavior on representative inputs. Hosted pricing, routing and availability are mutable.

## Family and official sources

- [Muse family](../../../../)
- [Meta release announcement](https://research.meta.ai/blog/muse-spark-open)
- [Meta developer documentation](https://dev.meta.ai/docs/muse-spark-open)
- [Official open-weight checkpoint](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
