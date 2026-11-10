# Documentation Requirements

## Requirements

- Identify Qwen3.6 using the exact canonical identity `catalog/models/alibaba/qwen/qwen3-6`.
- Preserve canonical membership in `catalog/models/alibaba/qwen` and its reciprocal `has-member` relation.
- Preserve the canonical `produced-by` relation to `catalog/producers/q/qwen-team` and the reciprocal producer relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Released dense and MoE vision-language checkpoints with separate weight identities and Apache-2.0 licensing.
- Preserve the exact member's input/output and license contract; do not turn toolkit options, quantizations, or hosted aliases into peer model identities.
- Dense 27B and MoE 35B-A3B have different total-weight requirements; active parameters are not a runtime memory estimate.
- Keep model-generated text, code, and tool arguments separate from permission to execute them; the application owns command validation, tool access, network access, and sandboxing.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
