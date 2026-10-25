# Granite 4.1 3B Base

Granite 4.1 3B Base is a separately released IBM Granite 4.1 base language model for adaptation. It is distinct from the corresponding instruction-tuned checkpoint.

## Model and deployment boundaries

- **Weights:** Apache-2.0; hosted service terms and runtime-specific artifacts are separate.
- **Training stage:** Base weights for adaptation and pretraining workflows.
- **Deployment:** Pin the exact checkpoint and supported runtime. Check configuration, precision, context state, batch size, memory, latency and task quality on representative inputs. The parameter label does not establish hardware suitability.

Published benchmark claims are not independently reproduced here.

## Family and official source

- [Granite 4.1 family](../../../../)
- [Official IBM model card](https://huggingface.co/ibm-granite/granite-4-1-3b-base)
