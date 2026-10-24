# Documentation Requirements

## Requirements

- Identify Qwen3.8-Flash using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-8/models/qwen3-8-flash`.
- Preserve canonical membership in `catalog/models/alibaba/qwen/qwen3-8` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- qwen3.8-flash is the independently documented hosted multimodal Qwen3.8 Flash identity with image/text/video input, text output, and a one-million-token context.
- Keep the hosted service contract separate from the released experimental Flash-Next checkpoint and its weight license.
- OpenAI- and Anthropic-compatible service routes do not guarantee feature parity with those vendors; confirm the exact tools, output budgets, region, and snapshot.
- Treat regional endpoints, API credentials, retention, and optional tools as hosting-service controls; the model name does not establish privacy, tool permissions, or access to external data.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
