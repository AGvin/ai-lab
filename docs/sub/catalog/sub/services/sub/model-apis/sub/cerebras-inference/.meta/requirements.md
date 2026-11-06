# Documentation Requirements

## Requirements

- Identify Cerebras Inference as Cerebras Systems Inc.'s hosted inference-as-a-service offering for remote model access.
- Preserve Cerebras's current distinction between production models and preview models; preview availability must not be used as evidence that a model or feature is production-stable.
- Keep third-party model identity, licensing, lifecycle, and intrinsic model facts with their canonical model owners.
- Treat model inventory, pricing, rate limits, API behavior, context limits, throughput, availability, and other service state as mutable and time-scoped.
- Keep the hosted service distinct from Cerebras hardware systems and self-managed software stacks.
- Render the standard `entity-relations` block and preserve Cerebras Systems Inc. as the producer.

## Validation

- Preview models are not described as production-stable merely because they are callable.
- The page remains a hosted model-API service profile rather than a hardware or model profile.
- The `produces` / `produced-by` relation pair resolves consistently to Cerebras Systems Inc.

## Scoped original-source qualification — 2026-11-06

- Cerebras Inference is the remote Cerebras-operated model inference service, not the WSE-3 wafer or CS-4 rack hardware. The public first-party model catalog separately labels production and preview models; dedicated endpoint access is a distinct capacity/contract offering. Third-party model authors retain their model provenance.
- Do not convert preview callable status into production SLAs or imply hardware-rack memory/compute totals are available as service quotas for every hosted model.
- Verified first-party source 1: https://inference-docs.cerebras.ai/models/overview
- Verified first-party source 2: https://inference-docs.cerebras.ai/
- This bounded source qualification does not establish a full freshness audit, independently validated runtime, legal/model-license clearance, current pricing or entitlements, global schema/cache/CI/render or final publication.
