# Documentation Requirements

## Identity and provenance

- FLUX.2 [klein] is the specialized compact-model subseries within FLUX.2. It groups separately published 4B and 9B base and distilled models; it is not one checkpoint with a common weight license.
- BFL's launch distinguishes four scale/distillation choices. The current upstream table also lists 9B-KV, but the reviewed card and code do not establish learned parameters distinct from ordinary 9B; its model intake remains unresolved. [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence) [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2-klein-9b-kv model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv) [FLUX.2 model loader configuration](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py).
- The original four models were released on 2026-01-15. The later 9B-KV distribution has separate registry history; its exact public release date is not established here. [FLUX.2 Klein launch](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence) [FLUX.2-klein-9b-kv model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv).

## Operational decision boundaries

- Use the concrete model pages to choose scale, distillation and rights. Both 4B models use Apache 2.0; both original 9B models and 9B-KV use FLUX Non-Commercial terms. No group-wide permission follows from one member. [FLUX.2-klein-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) [FLUX.2-klein-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) [FLUX.2-klein-base-4B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B) [FLUX.2-klein-base-9B model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B) [FLUX.2-klein-9b-kv model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv) [FLUX Non-Commercial License v2.1](https://github.com/black-forest-labs/flux2/blob/main/model_licenses/LICENSE-FLUX-NON-COMMERICAL) [FLUX.2 Klein 4B Apache License](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/main/LICENSE.md).
- FP8, NVFP4 and BF16 distributions describe precision or packaging. The separately named 9B-KV distribution provides a cache-enabled editing workflow. Retain its source evidence without assuming a distinct trained model, an alias of ordinary 9B, or a proven derivation; neither naming nor serialized-file digests settles that boundary. [FLUX.2 inference repository](https://github.com/black-forest-labs/flux2) [FLUX.2-klein-9b-kv model card](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv) [FLUX.2 Klein KV cache implementation](https://github.com/black-forest-labs/flux2/blob/main/docs/flux2_klein_kv_cache.md) [FLUX.2 model loader configuration](https://github.com/black-forest-labs/flux2/blob/50fe5162777813d869182b139e83b10743caef15/src/flux2/util.py).

## Validation

- Preserve the canonical identity, model hierarchy and exact reciprocal relation targets; distinguish producer, family, series, model, artifact and serving identities.
- Render all visible current-node relations in deterministic order and resolve local reader links. Restore missing readers from canonical facts without granting dependency-domain credit.
- Keep source dates, availability, license conditions and service-specific limits attributable. Do not turn provider claims into local runtime, performance or benchmark verification.
- Keep this series at the grouping path directly beneath FLUX.2, with concrete children under its models path. The former concrete-model path is removed; no redirect or duplicate active identity is allowed.
