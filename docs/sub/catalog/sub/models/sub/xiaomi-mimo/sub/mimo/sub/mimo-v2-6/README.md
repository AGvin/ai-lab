# MiMo V2.6

Xiaomi MiMo Team published **MiMo V2.6** in September 2026, with original Pro/Flash reinforcement-learned policies, a Qwen3.5-9B SFT-derived checkpoint, and subsequent separately learned **MOPD2 Pro/Flash** models. [Official release](https://mimo.mi.com/docs/en-US/news/latest/v2-6) [Hugging Face collection](https://huggingface.co/collections/XiaomiMiMo/mimo-v26).

## Model identities

- [MiMo-V2.6-Pro-RL](sub/models/sub/mimo-v2-6-pro-rl/README.md) — original reinforcement-learned; about 1.02T total parameters
- [MiMo-V2.6-Flash-RL](sub/models/sub/mimo-v2-6-flash-rl/README.md) — original reinforcement-learned; about 311B total parameters
- [MiMo-V2.6-Distill-Qwen-9B](sub/models/sub/mimo-v2-6-distill-qwen-9b/README.md) — supervised fine-tuned/distilled; approximately 9.4B total parameters
- [MiMo-V2.6-Pro-MOPD](sub/models/sub/mimo-v2-6-pro-mopd/README.md) — MOPD2 post-trained; about 1.02T total parameters
- [MiMo-V2.6-Flash-MOPD](sub/models/sub/mimo-v2-6-flash-mopd/README.md) — MOPD2 post-trained; about 311B total parameters

**Pro UltraSpeed is a hosted API mode**, not a sixth trained model. Xiaomi describes MOPD2 learning as a mitigation for repeated agentic tool calls, not proof of perfect behavior. [Technical report](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition).

## Operational and ownership scope

Check individual weights, hosted terms, hardware memory and custom code. Xiaomi's [2026 interim report](https://ir.mi.com/static-files/b903a881-8143-44a3-b759-703653bbb043) identifies a controlling shareholder but does not rule out minor indirect holdings; no unverified Russian ownership is alleged. [AI Lab policy](../../../../../../../../../project/sub/policies/sub/russia-linked-ai/README.md).

## Relations

- Member of: [MiMo family](../../)
- Has member: [MiMo-V2.6-Pro-RL](sub/models/sub/mimo-v2-6-pro-rl/README.md)
- Has member: [MiMo-V2.6-Flash-RL](sub/models/sub/mimo-v2-6-flash-rl/README.md)
- Has member: [MiMo-V2.6-Distill-Qwen-9B](sub/models/sub/mimo-v2-6-distill-qwen-9b/README.md)
- Has member: [MiMo-V2.6-Pro-MOPD](sub/models/sub/mimo-v2-6-pro-mopd/README.md)
- Has member: [MiMo-V2.6-Flash-MOPD](sub/models/sub/mimo-v2-6-flash-mopd/README.md)

## Official resources

- <https://mimo.mi.com/docs/en-US/news/latest/v2-6>
- <https://huggingface.co/collections/XiaomiMiMo/mimo-v26>
- <https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition>
