# Documentation Requirements

## Requirements

- Identify PPLX Decider V1.1 27B as Perplexity AI's distinct updated decision checkpoint with noncausal full-attention mode and expanded decision training data.
- Preserve the original Qwen/Qwen3.8-27B base-model attribution; this model is a Perplexity post-trained derivative, not a newly trained Qwen checkpoint.
- The official model card requires the saved noncausal attention behavior and application of calibration temperature exactly once for comparable inference. It states authenticated Hugging Face access for inference; re-check repo accessibility and weights before claiming open anonymous download.
- Treat exact benchmark/index scoring, accuracy, access/visibility, package file sizes, licensing, hardware memory, calibration and compatible runtimes as mutable source-backed facts. Do not equate a class name inside checkpoint code with its training lineage.
- Keep the local PPLX 27B Portable Computer model, Perplexity Decisions API endpoint and provider service terms outside this trained-model identity.

## Validation

- The checkpoint ID matches the first-party model card.
- Its `member-of` relation is reciprocated by the PPLX Decider family `has-member` entry.
- Model revision-specific inference and calibration behavior are not conflated with another version.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Decider V1.1 27B is the updated Qwen3.8-27B-derived decision artifact with a separate 255-row decision readout. Its model card declares Apache-2.0.
- Decision and deployment boundary: Preserve the saved noncausal full-attention behavior and apply calibration exactly once. The card calls for authenticated repository access; access and weights were not independently downloaded here. Its evaluation uses a smaller image-resolution setting than the inference default, so those configurations must remain distinct.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b>.
