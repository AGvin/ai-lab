# Databricks Model Serving

Databricks Model Serving is Databricks' managed infrastructure for deploying, governing and querying AI and ML models through serving endpoints, supporting real-time and batch inference. Model Serving endpoints are workspace-governed REST services built on provider-managed scaling infrastructure. [Databricks Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving).

## Model and endpoint boundaries

Serving an MLflow-format custom model, using a Databricks-hosted foundation model, routing through an external model proxy, or selecting pay-per-token versus provisioned throughput are endpoint/deployment options within the platform, not necessarily separate vendor services. A model deployed via Databricks keeps its original trained-model producer; MLflow software and Unity Catalog governance are distinct adjacent components.

## Operational boundaries

Supported endpoints, rate limits, pricing, model catalog, geographic/data-residency rules, authentication, container formats, quotas and monitoring differ by AWS, Azure and GCP deployment. Third-party external model calls can involve another provider's data terms. API compatibility does not imply equivalent feature support or reproducible throughput; verify the concrete model, region, tier, precision and workload. [Foundation Model API documentation](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/).

## Relations

- Produced by [Databricks](../../../../../producers/sub/d/sub/databricks-inc/).

## Official resources

- [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving)
- [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
- [Foundation model endpoint configuration](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints)
