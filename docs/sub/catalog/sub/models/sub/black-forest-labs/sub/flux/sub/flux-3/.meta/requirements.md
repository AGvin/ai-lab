# Documentation Requirements

## Identity and provenance

- FLUX 3 is Black Forest Labs' multimodal model series built around shared image, video and audio learning, with specialized Image, Video and Action members. The series and its rollout program are not one universally released checkpoint.
- The initial 2026-07-23 early-access announcement is historical. Assess current release state per named member: Video, Image, the released Action adaptation base, and the two released Image Klein models have different access paths. [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3) [FLUX 3 Video release](https://bfl.ai/blog/flux-3-video) [FLUX 3 Image API overview](https://docs.bfl.ai/flux_3/flux3_image_overview) [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein).

## Operational decision boundaries

- Do not copy an old rollout paragraph into the current status of every member. Public Action and Image Klein weights do not establish a released public FLUX 3 Dev backbone, nor do they open the hosted Image or Video weights. [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3) [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Image Klein release](https://bfl.ai/blog/flux-3-image-klein).
- Each concrete page owns its modalities, learned identity, license and workflow caveats. Multimodal pretraining does not mean every member exposes all modalities or a complete robot policy. [FLUX 3 initial announcement](https://bfl.ai/blog/flux-3) [FLUX 3 Action adaptation base card](https://huggingface.co/black-forest-labs/flux-3-action-base) [FLUX 3 Image Klein Base model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-base) [FLUX 3 Image Klein distilled model card](https://huggingface.co/black-forest-labs/flux-3-image-klein).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.

## Released FLUX 3 Action policy identities

- Materialize four distinct trained robotics model identities in addition to the existing 7B Action adaptation base: DROID fine-tuned, DROID guidance-distilled, DROID step-distilled, and SO-101 fine-tuned. The DROID variants `variants/gd` and `variants/sd` are different learned weights; `gd-fp8r` and `sd-fp8r` are precision artifacts only. [BFL release](https://huggingface.co/blog/black-forest-labs/flux-3-action) [DROID repository](https://huggingface.co/black-forest-labs/flux-3-action-droid) [Reference setup](https://github.com/black-forest-labs/flux-action/blob/main/docs/setup.md).
- Each action policy is gated under FLUX Kommunity License and requires embodiment-specific action/state encoders, runtime/inference checks and independent physical safety controls. Do not transfer DROID benchmark claims to SO-101 or the base model. [BFL model information](https://bfl.ai/models/flux-3-action).
- Extend exact `has-member` / `member-of` relations and rendered reader links without extra acceptance credit for previously tracked series or adaptation base.
