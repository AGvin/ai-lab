# Documentation Requirements

## Requirements

- Identify Wan2.2-TI2V-5B using the exact canonical identity `catalog/models/alibaba/wan/wan-2-2/models/wan2-2-ti2v-5b`.
- Preserve canonical membership in `catalog/models/alibaba/wan/wan-2-2` and its reciprocal `has-member` relation.
- Treat first-party capability and benchmark statements as publisher claims, not independent acceptance evidence.

## Decision and Operational Boundaries

- Wan2.2-TI2V-5B is a released Apache-2.0 open video checkpoint. The 5B checkpoint supports text-to-video and image-to-video at 720P and 24 fps.
- The generator also needs its text encoder, VAE, scheduler, and preprocessing; model size is not total download size or peak VRAM.
- The official 24GB GPU example depends on CPU/text-encoder offload and dtype conversion; it is not an unconditional peak-memory guarantee.
- Do not infer native sound generation, service APIs, or thirty-second clips from later Wan generations.
- Validate reference-media rights and user authorization before upload or synthesis; generated likeness, voice, text, or video is not evidence of an authentic recording.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Keep runtime artifacts, quantizations, date snapshots, and service routes distinct from trained-model identity.
- Check exact source references before changing release-specific facts; do not infer support from a sibling.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
