# Documentation Requirements

## Requirements

- Identify Runpod as a hosted GPU/CPU infrastructure service for AI, machine-learning, and other compute-intensive workloads.
- Preserve its primary placement under `services/infrastructure/`: Runpod operates externally managed compute and deployment surfaces rather than being self-managed inference software or a model provider.
- Explain the major current service modes at a durable level: Pods provide dedicated containerized GPU/CPU instances, while Serverless provides autoscaling execution for variable workloads; Public Endpoints or other managed model-access surfaces remain capabilities of the Runpod service unless later decomposition is independently justified.
- Preserve the current marketplace/infrastructure boundary without assuming one uniform hardware source: Runpod may expose Secure Cloud and Community Cloud capacity with different operational characteristics.
- Treat `runpodctl`, REST API access, templates, network volumes, container-registry integration, SSH/Jupyter/IDE connectivity, and similar mechanisms as interfaces or supporting capabilities of Runpod rather than separate canonical catalog products unless a future client gains independently meaningful lifecycle/ownership value.
- Distinguish cloud compute from inference runtime. A Runpod Pod or Serverless worker may run vLLM, Ollama, ComfyUI, custom containers, or other software, but Runpod does not become the canonical owner of those runtimes or applications.
- Treat GPU availability, hardware inventory, regions, prices, billing rates, queue/startup behavior, storage/network costs, limits, and service-specific feature counts as mutable state that must be source-backed and freshness-scoped when expanded.
- Preserve billing semantics only at a source-backed level; do not infer that stopping or deleting one resource has the same billing effect across compute, storage, network volumes, and Serverless resources.
- Treat provider security/compliance claims, isolation properties, and data-center classifications as first-party claims unless independently verified; do not generalize them beyond the documented service scope.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include the official service site, documentation, and legal identity source from canonical entity metadata.

## Validation

- Runpod remains a hosted infrastructure service rather than inference runtime software, a hosted model API only, or a generic hardware profile.
- Pods and Serverless are represented as service modes/capabilities without unnecessary duplicate canonical entities.
- Runpod CLI/API surfaces do not become separate canonical products solely because they are installable or programmatically addressable.
- Mutable pricing, hardware, availability, limits, and compliance state are not frozen as timeless facts.
- The `produced-by` relation resolves to Runpod, Inc. and is matched by the producer's inverse `produces` relation.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
