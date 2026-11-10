# PPLX Decider

PPLX Decider is Perplexity AI's **family of four released decision checkpoints**, distinct from the hosted Decisions API and from the unrelated PPLX 27B Portable Computer model. These models produce task-specific typed `choice`, `noul` and `score` decisions with calibrated probabilities rather than free-form text.

## Checkpoints and protocol

V1 and V1.1 are distinct Qwen3.8-27B-backed checkpoints. V1.2 retains the Qwen3.8-27B foundation but adds **text/image inputs and joint state-plus-multiple-question requests** with per-marker decision readout. Flash V1.2 is a **separate smaller checkpoint**, based on Qwen3.5-4B and distilled from the larger decision models; it shares the joint protocol but has its own calibration and runtime profile.

Pin the exact checkpoint, request schema, attention/readout contract and calibration. Publisher benchmarks and runtime figures require reproduction. Public cards do not guarantee unauthenticated downloads; repository access, hosted API aliases and commercial conditions may change.

## Relations

- Produced by: [Perplexity AI](../../../../../producers/sub/p/sub/perplexity-ai/)
- Members:
  - [PPLX Decider V1 27B](./sub/models/sub/pplx-decider-v1-27b/)
  - [PPLX Decider V1.1 27B](./sub/models/sub/pplx-decider-v1-1-27b/)
  - [PPLX Decider V1.2](./sub/models/sub/pplx-decider-v1-2/)
  - [PPLX Decider Flash V1.2](./sub/models/sub/pplx-decider-flash-v1-2/)

[Open the model index](./sub/models/).

## Official resources

- [Decider V1 card](https://huggingface.co/perplexity-ai/pplx-decider-v1-27b)
- [Decider V1.1 card](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b)
- [Decider V1.2 card](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
- [Decider Flash V1.2 card](https://huggingface.co/perplexity-ai/pplx-decider-flash-v1.2)
