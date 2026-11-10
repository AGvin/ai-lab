# Tencent Hy4 preview

**Tencent Hy4 preview** is a **released, open-sourced preview checkpoint** announced on **August 28, 2026**. Tencent Hy Team reports a sparse Mixture-of-Experts backbone with **770 billion total / 49 billion active parameters**, plus a separate native MTP speculative-decoding layer. Its published weights use **Apache-2.0**. *Preview* is part of the model's release identity: it does not mean the weights are merely announced or that the model is a fully stable production service.

## Architecture and context scope

The official source repository documents gated sparse attention, shared/routed MoE experts and **1M backbone context**. Tencent's corporate launch article separately describes a context window **exceeding 1 million tokens**; these source-specific statements should not be silently combined into a single tested deployment guarantee. The release's total/active parameter counts refer to the backbone and must not be conflated with the separately reported MTP layer.

Tencent positions Hy4 preview for coding, office productivity, scientific research and agent workflows, citing internal expert evaluations. These are **publisher benchmarks**, not independent AI Lab performance measurements. The upstream repository explicitly describes an **early version with known reasoning/over-verification limitations**.

Published FP8 or other precision variants are serving artifacts, not new trained Hy4 model identities. API providers, introductory promotions, software integrations, quotas, context behavior, runtime compatibility, inference throughput and GPU/VRAM needs require separate deployment validation.

## Translations

- English

## Relations

- Member of: [Tencent Hy family](../../../../)

## Official resources

- [Tencent release announcement (2026-08-28)](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/)
- [Tencent Hy4 preview official source repository](https://github.com/Tencent-Hunyuan/Hy4-preview)
- [Tencent Hy4 preview trained weights](https://huggingface.co/tencent/Hy4-preview)
