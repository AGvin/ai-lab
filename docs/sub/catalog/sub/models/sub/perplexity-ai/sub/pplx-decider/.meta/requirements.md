# Documentation Requirements

## Requirements

- Identify PPLX Decider as Perplexity AI's released family of revision-specific decision checkpoints: V1 27B, V1.1 27B, V1.2, and Flash V1.2.
- Keep typed `choice`/`noul`/`score` decision outputs and calibrated probabilities distinct from free-form autoregressive language generation.
- Preserve exact base-model lineage per checkpoint: V1, V1.1 and V1.2 use Qwen3.8-27B; Flash V1.2 uses Qwen3.5-4B and is distilled from the larger decision models.
- Treat V1.2 as a distinct released checkpoint with joint multi-question request semantics, changed training data, multimodal input and a per-marker decision readout; do not reduce it to an API alias for V1.1.
- Treat Flash V1.2 as a distinct smaller released checkpoint with its own base model, calibration and grouping guidance. Its GGUF repository is a packaging/quantization artifact, not a separate trained-model identity.
- Keep the hosted Perplexity Decisions API endpoint, aliases, authentication, billing and provider rankings outside intrinsic model identity.
- Keep the similarly named PPLX 27B local Portable Computer model independent from the Decider family.
- Preserve official model cards as the primary source for weights, revision, access conditions and reproducible self-hosted inference.

## Validation

- All four released checkpoints have distinct canonical model identities and reciprocate the family `has-member` relation.
- Family `produced-by` reciprocates the Perplexity AI producer.
- Qwen base-model lineage is not overwritten, and benchmark claims remain provider-attributed.
- A public model card does not imply anonymous checkpoint download when the card requires authenticated repository access.

## Source-backed reader scope — 2026-10-23

- Identity and provenance: PPLX Decider contains four released decision checkpoints. V1, V1.1 and V1.2 are Qwen3.8-27B-derived; Flash V1.2 is the smaller Qwen3.5-4B-based distilled model.
- Decision and deployment boundary: choose an exact checkpoint and reproduce its documented request format, attention/readout behavior and calibration. V1.2 and Flash V1.2 use the joint request protocol but have different grouping recommendations and resource profiles.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-decider-v1-27b>, <https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b>, <https://huggingface.co/perplexity-ai/pplx-decider-v1.2>, <https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2>.
