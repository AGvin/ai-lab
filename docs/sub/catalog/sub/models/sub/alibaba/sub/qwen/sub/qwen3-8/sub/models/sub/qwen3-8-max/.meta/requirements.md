# Documentation Requirements

## Requirements

- Identify Qwen3.8-Max as the stable Qwen3.8 model identity exposed as `qwen3.8-max` by Alibaba Cloud Model Studio.
- Keep dated service snapshots such as `qwen3.8-max-0902` as versioned snapshots of Qwen3.8-Max rather than peer model identities unless a later source establishes an independent model identity.
- Keep mutable serving aliases, regional availability, quotas, pricing, and provider routing outside intrinsic model identity.
- Preserve only source-backed capabilities and limits; re-check current first-party Model Studio documentation before updating mutable service facts.

## Decision and Operational Boundaries

- Qwen3.8-Max is the independently documented hosted model ID qwen3.8-max, distinct from its released text-only 2.4T-A95B checkpoint.
- The service supports image/text/video input and text output, with a documented one-million-token context; exact input/output budgets and tools remain region- and snapshot-specific.
- Keep dated snapshots such as 0902 beneath the stable identity and do not assume a rolling alias reproduces an earlier snapshot.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Qwen3.8-Max remains a concrete model within the Qwen3.8 series.
- Snapshot identifiers are not duplicated as standalone models without independent identity evidence.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
