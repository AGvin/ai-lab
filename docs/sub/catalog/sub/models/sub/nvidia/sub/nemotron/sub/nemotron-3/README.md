# Nemotron 3

Nemotron 3 is an NVIDIA **model series** within the broader [Nemotron family](../../). Its separately released language, vision-language, compressed and reward-model members include Nemotron 3 Nano, Super, Ultra and 3.5 variants. They share series membership but do not inherit one another's training stage, license or benchmark results.

## Models

**Nano and Super**

- [Nemotron 3 Nano](./sub/models/sub/nemotron-3-nano/)
- [Nemotron 3 Nano Base](./sub/models/sub/nemotron-3-nano-base/)
- [Nemotron 3 Nano Omni](./sub/models/sub/nemotron-3-nano-omni/)
- [Nemotron 3 Super](./sub/models/sub/nemotron-3-super/)
- [Nemotron 3 Super Base](./sub/models/sub/nemotron-3-super-base/)

**Ultra and reward evaluation**

- [Nemotron 3 Ultra](./sub/models/sub/nemotron-3-ultra/)
- [Nemotron 3 Ultra Base](./sub/models/sub/nemotron-3-ultra-base/)
- [Nemotron 3 Ultra GenRM](./sub/models/sub/nemotron-3-ultra-genrm/)

**Nemotron 3.5**

- [Nemotron 3.5 Lightning](./sub/models/sub/nemotron-3-5-lightning/)
- [Nemotron 3.5 Lightning Base](./sub/models/sub/nemotron-3-5-lightning-base/)
- [Nemotron 3.5 Super VL](./sub/models/sub/nemotron-3-5-super-vl/)
- [Nemotron 3.5 Super VL Base](./sub/models/sub/nemotron-3-5-super-vl-base/)
- [Nemotron 3.5 Bolt](./sub/models/sub/nemotron-3-5-bolt/)

[Browse the complete Nemotron 3 model index](./sub/models/).

## Identity boundaries

A pretrained Base checkpoint is distinct from a post-trained sibling. Precision, quantization, serving routes and speculative-decoding helpers do not automatically become separate canonical trained models. Compare total and active MoE parameters carefully, and keep lineage, workload claims and licensing scoped to the exact member.

## Translations

- English

## Official resources

- [NVIDIA Nemotron overview](https://developer.nvidia.com/topics/ai/nemotron)
- [NVIDIA Nemotron 3.5 Lightning announcement](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)
