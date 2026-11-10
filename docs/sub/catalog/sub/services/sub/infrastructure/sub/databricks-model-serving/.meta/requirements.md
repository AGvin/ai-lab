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

## Scoped original-source qualification — 2026-11-06

- Databricks Model Serving hosts MLflow-format custom models, Databricks-served foundation models with pay-per-token or provisioned throughput, and external model endpoints that route requests to third-party providers. These are managed endpoint choices under the existing Databricks service; they do not transfer original model ownership or turn MLflow into a Databricks-only runtime.
- Databricks Foundation Model APIs expose a workspace-scoped API contract: pay-per-token, optional priority service tier, and dedicated provisioned throughput differ in billing and expected latency. OpenAI-compatible REST shape is not guaranteed parameter or model portability. Provider-hosted content processing has Databricks-specific geo/data-residency terms, while external routes have independent upstream data terms.
- Cloud-specific region, supported model, rate limits, throughput, cost, authentication, custom container behavior and endpoint revisions remain version- and tenant-dependent; no actual deployment or benchmark was performed.
- Verified first-party source 1: https://docs.databricks.com/aws/en/machine-learning/model-serving
- Verified first-party source 2: https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/
- Verified first-party source 3: https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints
- Source acceptance covers service identity and publisher-scoped limits, not full lifecycle freshness, authenticated provider execution, independent security/legal assurance, root-wide schema/cache/CI/render, reader repairs, clean passes or final delivery.
