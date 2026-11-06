# Documentation Requirements

## Requirements

- Identify Hugging Face Inference Endpoints as the canonical hosted infrastructure-service profile represented at this path.
- Include the official service page and official documentation as source references.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep concrete model identity with Model Reference and keep mutable deployment options, pricing, limits, regions, and availability source-backed and time-scoped when added.

## Validation

- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
- The page contains no temporary-summary or placeholder wording.
- Official resource links match canonical entity references.
- The page does not duplicate concrete model profiles.

## Scoped original-source qualification — 2026-11-06

- Hugging Face Inference Endpoints is a dedicated managed model deployment/serving infrastructure service, separate from routed Inference Providers and from the upstream authors of models deployed on the endpoint. A custom container can alter supported model/runtime contracts; the service does not itself establish model authorship.
- Publisher documentation distinguishes manual Pause/Resume from automatic Scale-to-Zero; a scaled-to-zero endpoint wakes on a new request with cold-start latency, while a paused endpoint requires explicit resume. Endpoint autoscaling, minimum replicas, quota usage, GPU/CPU provisioning, secure networking, data policy, cost and configuration remain mutable by deployment and account.
- Do not promise warm response, automatic request buffering, constant scaling thresholds or identical version support for all inference engines. Inference compatibility and performance need task-specific evaluation rather than extrapolation from a hosted API's existence.
- Verified first-party source 1: https://huggingface.co/docs/inference-endpoints/index
- Verified first-party source 2: https://huggingface.co/docs/inference-endpoints/guides/autoscaling
- Verified first-party source 3: https://huggingface.co/docs/huggingface_hub/guides/inference_endpoints
- Acceptance scope: present provider documentation of the existing service identity and deployment-specific conditions only; not new metadata, reader repair, independent hardware execution, complete freshness/legal/security audit, root-wide schema/cache/CI/render, clean pass, final-delivery gate or merge.
