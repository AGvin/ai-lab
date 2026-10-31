# Granite 4.1 3B

Granite 4.1 3B is a separately released IBM instruction-tuned language model for assistant and tool-use workflows. It is distinct from Granite 4.1 3B Base.

## Model and deployment boundaries

- **Weights:** Apache-2.0; hosted service terms and runtime-specific artifacts are separate.
- **Training stage:** Instruction-tuned checkpoint, not base weights for adaptation.
- **Deployment:** Pin the exact checkpoint and supported runtime. Check configuration, precision, context state, batch size, memory, latency and task quality on representative inputs. The 3B parameter label does not establish hardware suitability.

Published benchmark claims are not independently reproduced here.

## Source-backed derivative

- [Granite Vision 4.1 4B](../../../../../granite-vision-4-1/sub/models/sub/granite-vision-4-1-4b/) is fine-tuned from this instruction-tuned checkpoint according to IBM's model card. It has a separate vision-language operating contract; this relationship does not imply interchangeable weights or deployments.

## Family and official source

- [Granite 4.1 family](../../../../)
- [Official IBM model card](https://huggingface.co/ibm-granite/granite-4.1-3b)
