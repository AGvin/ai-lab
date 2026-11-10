# Documentation Requirements

## Identity and scope

- Identify this node as IBM's Granite model-domain view, not a duplicate company profile.
- Organize the fourteen materialized families: Granite 4.2, Granite 4.1, Granite 4.0 Nano, Granite Switch 4.1, Granite Docling, Granite Embedding English R2, Granite Embedding Multilingual R2, Granite Guardian 4.1, Granite Guardian HAP, Granite Speech 5.0, Granite Speech 4.1, Granite Time Series, Granite Vision 4.1, and Granite Vision 3.3.
- Keep current specialist and lineage roles explicit; this inventory is not a recommendation to prefer older general checkpoints. Exclude preview models, adapter libraries, ensemble recipes and unresolved geospatial ownership from this trained-model package.
- Keep jointly released IBM-NASA models under their separate collaborative model-domain identity even when IBM is a producer.
- Keep hosted watsonx offerings, inference endpoints, quantized/export artifacts, runtime integrations, and third-party deployment routes separate from trained-model identity.

## Currentness and validation

- Treat family membership and release inventory as freshness-sensitive and verify mutable facts against current first-party model cards or source repositories.
- Do not infer a missing model node solely from a base-model tag, repository branch, quantization, or deployment route.
- Preserve canonical IBM producer provenance at `catalog/producers/i/ibm`.
- This assessment does not establish runtime compatibility, benchmark reproduction, or hosted-provider availability.
