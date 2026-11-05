# BitNet b1.58 2B4T

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Ownership/control-chain review is incomplete; no Russian-control finding or adoption clearance is established. See the [provenance policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/).

## Model and access

Microsoft Research's roughly 2B-parameter checkpoint was trained on 4T tokens with native ternary W1.58A8 weights/activations and reports a 4,096-token sequence limit. The card declares MIT. Packed, BF16 master and GGUF distributions represent one trained model. It is not an ordinary model compressed only after training, nor the separately cataloged bitnet.cpp runtime.

## Integration and evidence

The publisher explicitly says standard Transformers execution does not deliver its reported speed/energy gains; specialized bitnet.cpp kernels are required for that efficiency path. Pin and review model code, artifact and runtime before loading; do not infer measured CPU throughput or memory fit from 1.58-bit branding.

Publisher capability and benchmark claims are not independently reproduced. Source review: 2026-11-05; no weights, remote model code, inference or tools were executed.

## Relations

- Member of: [Model family](../..//)

## Official resources

- [First-party model card](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T)
- [License or terms](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T/blob/main/LICENSE)
