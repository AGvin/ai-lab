# Documentation Requirements

## Requirements

- Identify Wan 2.2 using the exact canonical identity `catalog/models/alibaba/wan/wan-2-2`.
- Preserve canonical membership in `catalog/models/alibaba/wan` and its reciprocal `has-member` relation.
- Preserve the canonical `produced-by` relation to `catalog/producers/w/wan-team` and the reciprocal producer relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Wan 2.2 has released open checkpoints for text-to-video, image-to-video, and the compact combined TI2V model, with Apache-2.0 distribution.
- Keep 14B-expert MoE T2V/I2V checkpoints distinct from the 5B TI2V model and from separate S2V/Animate releases.
- Do not inherit Wan3.0 hosted audio, editing, thirty-second, or service-retention guarantees into the open 2.2 checkpoints.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
