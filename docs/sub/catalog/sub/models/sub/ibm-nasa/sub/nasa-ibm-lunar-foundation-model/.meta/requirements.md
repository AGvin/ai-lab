# Documentation Requirements

## Identity and provenance

- Present NASA-IBM Lunar Foundation Model as the jointly released multimodal, multi-resolution lunar remote-sensing foundation model, distinct from the IBM-only Granite families and from the IBM-NASA collaboration view.
- Preserve the current model-card identity: ViT-B encoder-decoder, pretrained from scratch on SomBench, nearly two million co-registered lunar tile bundles, 11 modalities, and the two represented spatial scales of roughly 1 m/pixel and 100 m/pixel.
- Preserve both IBM and NASA producer relations and their exact reciprocal `produces` edges.
- Keep SomBench datasets, TerraTorch integration, technical papers, demonstrations, and downstream crater/IMP/ice task adaptations as related artifacts or follow-up identities rather than duplicate aliases of the pretrained checkpoint.

## Operational decision boundaries

- Record Apache-2.0 for the released model weights and code only where the current first-party card or repository states it; do not infer licensing for datasets, papers, hosted demos, or unrelated downstream artifacts.
- Distinguish the pretrained representation from downstream fine-tuning. The current card supports adaptation for detection, segmentation, and regression and describes qualitative any-to-any generation, but generated fields are not calibrated scientific predictions.
- Preserve the current model-card limitation that the model is not validated for operational decisions such as landing-site certification or hazard clearance, does not maintain an absolute geodetic reference frame, and has not been evaluated beyond the Moon or on products absent from SomBench.
- Benchmark improvements are source-specific results, not locally reproduced measurements. Runtime compatibility, throughput, memory, and downstream accuracy require independent validation on the chosen TerraTorch/runtime configuration.

## Validation

- Both producer relations resolve and have matching inverse `produces` edges.
- The reader distinguishes source-reported architecture/data facts from benchmark claims and operational limitations.
- Local navigation and all cited first-party resources resolve.
- No inference execution, benchmark reproduction, cache validation, clean-pass, or final-gate credit is implied by this documentation assessment.
