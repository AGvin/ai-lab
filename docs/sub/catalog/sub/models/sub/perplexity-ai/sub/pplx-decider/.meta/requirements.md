# Documentation Requirements

## Requirements

- Identify PPLX Decider as Perplexity AI's independent, released family of local/open-weight decision checkpoints, beginning with October 2026 V1 27B and updated V1.1 27B.
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
