# Documentation Requirements

## Requirements

- Identify Strands Decider 2B Qwen3.5 v1-2610 at canonical ID `catalog/models/amazon/strands-decider/models/strands-decider-2b-qwen3-5-v1-2610`.
- Preserve the trained identity, family membership and upstream producer separately from hosted routes, runtime packages and mirrored artifacts.

## Validation

- Use primary identity and operational references and retain the reciprocal catalog relation.

## Decision and operational boundaries

- Preserve this canonical boundary: Released StrandsAgents/strands-decider-2B-qwen3.5-v1-2610 identity on Qwen/Qwen3.5-2B-Base, combining three runs into a rank-48 LoRA adapter and option-scoring head. It is a changed recipe, not a Hobson V21 alias or a separate model for its Amazon mirror. Optional vision is not image-trained. Calibration requires target-traffic testing. The card says the v1 data-mix builders are not yet on main, so published weights do not establish reproducible training from that branch. Runtime state is truncated by default; strict-window mode rejects oversize input.
- The exact model card records an October 9, 2026 release and a three-run adapter/head combination on `Qwen/Qwen3.5-2B-Base`. The v1 name encodes a released recipe, and its Amazon mirror contains the same files. [Strands Decider 2B Qwen3.5 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610) [Strands Decider model release naming](https://github.com/strands-labs/strands-decider/blob/main/docs/naming.md)
- The card distinguishes v1 training from Hobson V21 and says its data-mix builders are not yet on the code repository main branch. Weight availability and full training-data reproduction are separate claims. [Strands Decider 2B Qwen3.5 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610)
- Apply the typed-decision runtime and evaluate confidence on the intended questions. Optional Qwen vision is not image-trained, and missing images need an application-side check before inference. [Strands Decider 2B Qwen3.5 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610) [Strands Decider inference and runtime contract](https://github.com/strands-labs/strands-decider/blob/main/docs/inference.md)
- The model card publishes the adapter/head under Apache-2.0 and loads the base weights separately. Preserve source-specific data terms and pin the released files and compatible code; a model license does not grant a blanket training-data redistribution right. [Strands Decider 2B Qwen3.5 v1-2610 model card](https://huggingface.co/StrandsAgents/strands-decider-2B-qwen3.5-v1-2610)
