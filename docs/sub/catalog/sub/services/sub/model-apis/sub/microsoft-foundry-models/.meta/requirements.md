# Documentation Requirements

## Requirements

- Present Microsoft Foundry Models as Microsoft's hosted model catalog, deployment, and inference-access service for Microsoft/Azure OpenAI and third-party/community models through Microsoft Foundry.
- Preserve the primary hosted model-access boundary: discovery/evaluation plus managed-compute and serverless deployments, including the unified Foundry inference endpoint where supported.
- Keep concrete model identity and upstream producer provenance with each model owner; availability in Microsoft Foundry does not make Microsoft the producer of partner/community models.
- Keep Microsoft Foundry Agent Service, Microsoft Agent Framework, Copilot Studio, and broader Foundry workspace/platform features separate from the model-access service identity.
- Treat model inventory, deployment modes, endpoint compatibility, regions, lifecycle, pricing, quotas, Azure support/SLA distinctions, content filtering, fine-tuning, and capacity options as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Microsoft Foundry Models remains a hosted model-access/deployment service rather than a model family.
- Partner/community model provenance is not reassigned to Microsoft.
- Agent Service remains separately owned.
- Producer provenance resolves bidirectionally to Microsoft.
