# Documentation Requirements

## Requirements

- Present Microsoft Foundry Models as Microsoft's hosted model catalog, deployment, and inference-access service for Microsoft/Azure OpenAI and third-party/community models through Microsoft Foundry.
- Preserve the primary hosted model-access boundary: discovery/evaluation plus managed-compute and serverless deployments, including the unified Foundry inference endpoint where supported.
- Keep concrete model identity and upstream producer provenance with each model owner; availability in Microsoft Foundry does not make Microsoft the producer of partner/community models.
- Keep Microsoft Foundry Agent Service, Microsoft Agent Framework, Copilot Studio, and broader Foundry workspace/platform features separate from the model-access service identity.
- Treat model inventory, deployment modes, endpoint compatibility, regions, lifecycle, pricing, quotas, Azure support/SLA distinctions, content filtering, fine-tuning, and capacity options as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.

## Validation

- Microsoft Foundry Models remains a hosted model-access/deployment service rather than a model family.
- Partner/community model provenance is not reassigned to Microsoft.
- Agent Service remains separately owned.
- Producer provenance resolves bidirectionally to Microsoft.

## Scoped original-source qualification — 2026-11-06

- Microsoft Foundry Models is a hosted catalog and inference deployment surface rather than the author of every model. Microsoft's deployment overview distinguishes serverless API serving Azure-sold and partner/community models from managed compute (preview) on dedicated GPUs. Instant model access is also preview; neither preview is the universal Foundry deployment experience.
- Separate upstream model authorship and license from Microsoft hosting. Validate exact model card, region, deployment type, capacity, billing/SLA responsibility and preview/GA state per endpoint. Foundry Agent Service remains a different entity.
- Verified first-party source 1: https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview
- Verified first-party source 2: https://learn.microsoft.com/en-us/azure/foundry/concepts/deployments-overview
- This source qualification accepts only the existing hosted-service identity and bounded claims. It does not establish full freshness, legal/ownership/license clearance, independent security or performance, authenticated endpoints, complete schema/cache/CI/render, clean pass or final delivery.
