# Documentation Requirements

## Requirements

- Identify Amazon SageMaker AI as a long-running fully managed AWS ML/AI development, training, optimization and inference-deployment service. Preserve primary classification under `services/infrastructure` because it manages computing and lifecycle infrastructure for custom models as well as hosted prediction endpoints.
- Distinguish SageMaker AI custom/model endpoints, training jobs, managed real-time hosting and offline/batch deployments from Amazon Bedrock's foundation-model API/product offering and Amazon Bedrock AgentCore's managed agent runtime. A model trained through SageMaker and deployed through Bedrock remains separately governed by the receiving service.
- Treat real-time, serverless, asynchronous and batch-transform inference as deployment modes of one SageMaker service, not four peer commercial service identities. Likewise, SDKs, Studio, Pipeline components and monitoring are product capabilities or interfaces, not necessarily separate catalog services.
- Explicitly track AWS's 2026 lifecycle/access changes: several legacy SageMaker AI features stopped accepting **new customers from July 30, 2026**, while other SageMaker AI capabilities remain available. Do not misstate this feature-specific access restriction as deprecation or end of support for the entire SageMaker AI service.
- Scope region, instance families, accelerators, container/runtime support, authentication, VPC/data access boundaries, model registry, scaling, quotas, supported frameworks and end-to-end cost to dated official documentation.
- Do not generalize SageMaker-specific model inference throughput to other AWS-managed service tiers or third-party models without workload-specific measurement.
- Preserve Amazon Web Services producer provenance and matching inverse relation.

## Validation

- The managed AI/ML platform and its endpoint deployment modes remain distinct from Bedrock, AgentCore, individual trained models and self-managed inference engines.
- Feature-level restrictions and access notices are not converted into an unsupported platform-wide shutdown claim.
- Official references reflect the current provider-managed service lifecycle and deployment boundaries.
- The `produced-by` relation is reciprocal with AWS's `produces`.

## Scoped original-source qualification — 2026-11-06

- Amazon SageMaker AI provides managed ML model development, training, deployment and inference infrastructure. Its real-time, serverless, asynchronous and batch model serving are distinct deployment modes of the SageMaker service, not separate trained-model producers or Amazon Bedrock interfaces.
- AWS's explicit July 30, 2026 availability restriction applies to named legacy SageMaker AI features for new customers, not to the whole SageMaker AI platform. Preserve feature-specific access states and separate mutable instance/GPU options, supported containers, quotas, storage/network access, monitoring and billing.
- Verified first-party source 1: https://aws.amazon.com/sagemaker/ai/features/
- Verified first-party source 2: https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model-options.html
- Scope: originally documented hosted service identity and lifecycle/usage limits only; not a complete freshness/legal/security review, independent runtime execution, full schema/cache/CI/render, clean pass or final delivery gate.
