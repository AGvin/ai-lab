# Documentation Requirements

## Requirements

- Identify the exact `Tongyi-MAI/Z-Image-Turbo` checkpoint as a concrete trained model in the Z-Image family, not as an artifact, hosted alias, or synonym for the base `Tongyi-MAI/Z-Image` model.
- Preserve the source-backed lineage that Z-Image-Turbo is a distilled derivative of the base Z-Image model and keep the canonical derivative relation consistent in both endpoint entity documents.
- Preserve the current source-backed approximately 6B-parameter S3-DiT architecture context, text-to-image modality, November 26, 2025 public checkpoint release, and Apache-2.0 license.
- Preserve the provider-documented fast-generation recipe at a stable level: Turbo is trained for eight model evaluations/DiT forwards and does not use classifier-free guidance in the official pipeline recipe; keep exact library call details in upstream documentation rather than turning the canonical profile into a quick-start guide.
- Treat Tongyi-MAI claims about photorealism, bilingual English/Chinese text rendering, instruction adherence, sub-second H800 latency, and comfortable operation within 16 GB consumer VRAM as provider evidence requiring independent workload/runtime validation before becoming AI Lab quality, latency, or hardware-fit conclusions.
- Keep leaderboard positions and dated comparison claims outside immutable model identity; when they inform selection, validate the current leaderboard/evaluation source and evidence boundary.
- Keep hosted demos, third-party inference providers, runtime integration status, pricing, availability, and deployment-specific performance outside immutable model identity.
- Keep creative-task recommendations, accepted-result quality, local-resource fit, runtime performance, and workflow guidance in their corresponding selection/evidence owners.

## Validation

- Z-Image-Turbo remains distinct from the base Z-Image model and from future artifacts/quantizations of either model.
- The `derived-from` relation resolves to the canonical base Z-Image model and has a matching `has-derivative` inverse.
- Apache-2.0 licensing is not generalized to unrelated Z-Image family variants without source evidence.
- Provider quality, latency, VRAM, and leaderboard claims are not presented as independent AI Lab measurements.
- Eight-NFE generation behavior is not confused with a universal wall-clock latency guarantee.
