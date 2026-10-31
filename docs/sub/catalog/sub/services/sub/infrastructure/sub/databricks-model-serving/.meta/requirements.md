# Documentation Requirements

## Requirements

- Identify Databricks Model Serving as Databricks' released managed/serverless infrastructure for deploying, governing and querying AI/ML models as online or batch inference endpoints.
- Preserve the distinction between custom MLflow-format model serving, externally hosted model proxy endpoints, Databricks-hosted foundation models and pay-per-token or provisioned throughput Foundation Model API options as service capabilities/deployment modes, not independent canonical products by default.
- Do not conflate Model Serving with standalone MLflow software, Unity Catalog data governance, vector search, Databricks Mosaic model authorship or every model served through the platform.
- Keep runtime and interface support, versioned API routes, region/data-residency rules, authentication, inference pricing, model availability, endpoint scaling and quotas freshness-sensitive.
- Scope references to the applicable cloud provider (AWS, Azure and GCP) because supported models, features, governance and geos may differ.
- Model serving throughput, response latency, tokens/s and vendor claims require exact hardware, model, tier, precision, request mix and regions for cross-platform comparisons.
- Preserve Databricks Inc. as service operator with reciprocal producer provenance.

## Validation

- The managed model-serving service is distinguished from an open-source inference engine and from specific trained models.
- The Foundation Model API is represented as a surface of the service until a separately operated identity is established.
- Model lifecycle and region availability claims stay current and sourced.
- Producer relation is symmetric.
