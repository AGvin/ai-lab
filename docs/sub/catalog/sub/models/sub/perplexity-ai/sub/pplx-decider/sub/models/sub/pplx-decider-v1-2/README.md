# PPLX Decider V1.2

PPLX Decider V1.2 is Perplexity AI's separately released **multimodal decision model** based on **Qwen3.8-27B**, distinct from Decider V1 and V1.1. The checkpoint accepts text and image input and is published with **Apache-2.0** license metadata.

## Decision interface

Unlike the earlier one-question-per-forward-pass protocol, V1.2 supports **one joint request with state plus multiple questions** and a **per-question marker readout**. Decision outputs and calibrated probabilities are task-specific; the interface is not unrestricted text generation. Follow the official request template, attention/readout semantics and calibration when testing actual decisions.

Model-card authentication instructions, provider endpoints, billing, grouped inference, memory, compilation paths and benchmark gains depend on the current repository and runtime. A public card does not guarantee anonymous weight download.

## Family and official source

- [PPLX Decider family](../../../../)
- [Official Perplexity checkpoint](https://huggingface.co/perplexity-ai/pplx-decider-v1.2)
