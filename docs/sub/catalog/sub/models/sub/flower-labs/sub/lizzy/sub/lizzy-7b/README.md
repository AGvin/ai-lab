# Lizzy 7B

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Ownership/control-chain review is incomplete; no Russian-control finding or adoption clearance. See the [provenance policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Flower Labs' 7B-class decoder-only English assistant targets British English and UK-oriented knowledge. The publisher declares Apache-2.0 for the base checkpoint and distinguishes original BF16 Safetensors from GGUF quantizations. Its up-to-65,536-token context depends on runtime and serving profile. BF16 and GGUF are artifacts of one trained model, not extra accepted models. Special GGUF architecture support and a publisher-tested fork do not establish general llama.cpp compatibility. Review and pin the chosen runtime/artifact; verify facts and cultural assumptions and sandbox any generated code.

Source review: 2026-11-05. Publisher benchmarks and deployment claims were not independently reproduced. No weights, source code or inference executed.

## Relations

- member-of: [catalog/models/flower-labs/lizzy](../..//)

## Official resources

- <https://flower.ai/docs/model/lizzy-7b.html>
- <https://flower.ai/docs/model/>
