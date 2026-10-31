# Documentation Requirements

## Requirements

- Identify Wan2.2-T2V-A14B using the exact canonical identity `catalog/models/alibaba/wan/wan-2-2/models/wan2-2-t2v-a14b`.
- Preserve canonical membership in `catalog/models/alibaba/wan/wan-2-2` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Wan2.2-T2V-A14B is a released Apache-2.0 open video checkpoint. The MoE text-to-video checkpoint supports 480P/720P generation; its card documents five-second examples.
- The generator also needs its text encoder, VAE, scheduler, and preprocessing; model size is not total download size or peak VRAM.
- Do not infer native sound generation, service APIs, or thirty-second clips from later Wan generations.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
