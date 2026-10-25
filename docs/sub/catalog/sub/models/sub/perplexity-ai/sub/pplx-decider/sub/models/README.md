# PPLX Decider Models

Four **separately trained and released decision checkpoints** belong to the PPLX Decider family. They produce typed decisions and calibrated probabilities rather than unrestricted language-generation responses.

## Members

- [PPLX Decider V1 27B](./sub/pplx-decider-v1-27b/) — original Qwen3.8-27B-based checkpoint.
- [PPLX Decider V1.1 27B](./sub/pplx-decider-v1-1-27b/) — separate Qwen3.8-27B-based update.
- [PPLX Decider V1.2](./sub/pplx-decider-v1-2/) — multimodal joint multi-question protocol.
- [PPLX Decider Flash V1.2](./sub/pplx-decider-flash-v1-2/) — smaller Qwen3.5-4B-based distilled checkpoint.

The GGUF distribution of Flash V1.2 is a packaging artifact, not a fifth trained model. Hosted Decisions API routes and provider aliases are separate access surfaces.

- [PPLX Decider family](../../)
