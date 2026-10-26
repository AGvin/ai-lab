# Granite 4.1 30B Base

Granite 4.1 30B Base is a separately released IBM Granite 4.1 base language model for adaptation. It is distinct from the corresponding instruction-tuned checkpoint.

## Model and deployment boundaries

- **Weights:** Apache-2.0; hosted service terms and runtime-specific artifacts are separate.
- **Training stage:** Base weights for adaptation and pretraining workflows.
- **Deployment:** Pin the exact checkpoint and supported runtime. Check configuration, precision, context state, batch size, memory, latency and task quality on representative inputs. The parameter label does not establish hardware suitability.

Published benchmark claims are not independently reproduced here.

## Family and official source

- [Granite 4.1 family](../../../../)
- [Granite 4.2 30B](../../../../../granite-4-2/sub/models/sub/granite-4-2-30b/) — separately post-trained derivative of this base checkpoint.
- [Official IBM model card](https://huggingface.co/ibm-granite/granite-4.1-30b-base)
