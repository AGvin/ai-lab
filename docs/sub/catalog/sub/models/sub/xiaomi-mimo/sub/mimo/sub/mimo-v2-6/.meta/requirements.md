# Documentation Requirements

## Identity and provenance

- Represent September 2026 MiMo V2.6 as one model series with five distinct learned checkpoints: Pro-RL, Flash-RL, Distill-Qwen-9B, Pro-MOPD and Flash-MOPD. [Official release](https://mimo.mi.com/docs/en-US/news/latest/v2-6) [Model collection](https://huggingface.co/collections/XiaomiMiMo/mimo-v26).
- The Qwen3.5-9B-derived SFT checkpoint, original RL checkpoints, and separately published MOPD2 trained weights are not API aliases or mere quantizations. Pro UltraSpeed is an **API serving mode**, not an additional model. [Publisher MOPD analysis](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition).

## Operational boundaries

- Pro, Flash and Distill have different parameter/storage, modality and runtime requirements; source comparisons are not independent AI Lab tests.
- Publisher reports repeated tool calls in original RL policies and improved behavior after MOPD2. These observations do not guarantee flawless agent tool use in all contexts.
- The [2026 Xiaomi interim report](https://ir.mi.com/static-files/b903a881-8143-44a3-b759-703653bbb043) identifies a controlling shareholder but does not confirm every indirect/minority holding. Do not invent Russian ownership or infer complete clearance. Continue source-backed review under the [AI Lab provenance policy](../../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md).

## Validation

- Family/series inverse relation pair and five reciprocal series/model relation pairs; all reader links resolve.
- No whole-catalog freshness, exhaustive ownership validation, full rendering/cache/schema/CI or final gates credited.
