# Documentation Requirements

## Requirements

- Identify PPLX Decider as Perplexity AI's released family of revision-specific decision checkpoints, with V1 27B and updated V1.1 27B.
- Keep the distinction between typed `choice`/`noul` decision outputs with calibrated probabilities and free-form autoregressive language generation.
- Preserve the derivative base-model identity: the original Qwen3.8-27B is independently owned by Alibaba/Qwen; Perplexity owns the post-trained decision checkpoints.
- Treat V1.1 as a distinct released checkpoint with changed attention/calibration behavior and evaluation instructions, not just an API alias, price tier or V1 serving toggle.
- Keep the hosted Perplexity Decisions API endpoint, model aliases, authentication, billing, and rankings outside the intrinsic family identity.
- Keep the similarly named PPLX 27B local Portable Computer model independent from the Decider family.
- Preserve official model cards as the primary source for weights, revision, access conditions and reproducible self-hosted inference.

## Validation

- Both released checkpoints have distinct canonical model identities and reciprocate the family `has-member` relation.
- Family `produced-by` reciprocates the Perplexity AI producer.
- Qwen base-model lineage is not overwritten, and benchmark claims remain provider-attributed.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: PPLX Decider groups Perplexity's distinct V1 and V1.1 decision checkpoints derived from Qwen3.8-27B. They return typed decisions and calibrated probabilities rather than representing a general text-generation service.
- Decision and deployment boundary: Choose an exact revision and reproduce its prescribed inference behavior. The V1.1 card's access instructions differ from V1's download example, so public card visibility and Apache-2.0 metadata do not by themselves establish anonymous access to every artifact.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://huggingface.co/perplexity-ai/pplx-decider-v1-27b>, <https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b>.
