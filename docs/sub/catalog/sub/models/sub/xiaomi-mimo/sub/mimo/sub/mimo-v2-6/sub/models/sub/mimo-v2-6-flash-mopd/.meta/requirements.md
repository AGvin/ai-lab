# Documentation Requirements

## Identity and provenance

- Treat [MiMo-V2.6-Flash-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD) as a separate released MOPD2 post-trained learned-model checkpoint in MiMo V2.6, not an API alias, UltraSpeed mode or a V2.5 variant.
- Preserve source-specific parameter count (about 311B total parameters) and input/usage scope (native multimodal text, image, video, audio) without inferring unsupported sibling modalities or independent AI Lab performance tests.
- Distinct learned Flash weights after multi-teacher on-policy distillation targeting repetitive tool use; not a serving-only setting. Publisher results do not guarantee complete loop prevention. [Xiaomi release](https://mimo.mi.com/docs/en-US/news/latest/v2-6) [Technical MOPD research](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition).

## Operational boundaries

- The model card labels downloadable weights MIT; API terms, support for custom code, dependency integrity, runtime fit and access contracts are separate. Pin and inspect revisions before any custom-code execution.
- Xiaomi's [2026 interim report](https://ir.mi.com/static-files/b903a881-8143-44a3-b759-703653bbb043) identifies a controlling shareholder. It neither proves nor rules out all small indirect or minority Russian interests; ownership-screening remains open, with no unsupported Tier 1/Tier 2 accusation. [AI Lab provenance policy](../../../../../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md).
- Publisher benchmark claims and post-training mitigations have not been independently reproduced. Avoid static rank, latency, inference memory or security assurances.

## Validation

- One `member-of` to MiMo V2.6 with reciprocal `has-member`; all reader paths resolve.
- Full current-head cache/schema/CI, independent evaluation, comprehensive ownership diligence and final acceptance gates are not credited.
