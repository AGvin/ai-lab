# Granite 4.1

Granite 4.1 is an IBM language-model family with six separately published checkpoints across 3B, 8B and 30B parameter classes. Each size has distinct base and instruction-tuned weights; do not treat this established generation as IBM's newest language-model release.

## Model boundaries

Base checkpoints target adaptation and pretraining workflows, while instruction-tuned checkpoints target assistant and tool-use workflows. Select the exact checkpoint and verify its context, languages, architecture, runtime compatibility and task behavior from the official model card. The weights are published under Apache-2.0; hosted terms are separate. Evaluate memory, latency and quality rather than inferring hardware fit from size labels.

## Models

- [Granite 4.1 3B](./sub/models/sub/granite-4-1-3b/)
- [Granite 4.1 3B Base](./sub/models/sub/granite-4-1-3b-base/)
- [Granite 4.1 8B](./sub/models/sub/granite-4-1-8b/)
- [Granite 4.1 8B Base](./sub/models/sub/granite-4-1-8b-base/)
- [Granite 4.1 30B](./sub/models/sub/granite-4-1-30b/)
- [Granite 4.1 30B Base](./sub/models/sub/granite-4-1-30b-base/)

## Official resources

- [Granite 4.1 3B — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-3b)
- [Granite 4.1 3B Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-3b-base)
- [Granite 4.1 8B — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-8b)
- [Granite 4.1 8B Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-8b-base)
- [Granite 4.1 30B — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-30b)
- [Granite 4.1 30B Base — IBM model card](https://huggingface.co/ibm-granite/granite-4.1-30b-base)

## Deployment checks

Pin the exact checkpoint revision and runtime version, preserving the checkpoint-specific configuration. Check architecture support, precision, context-state memory and batch size together; measure memory, latency and task quality on representative inputs. Runtime-specific artifacts and hosted-service terms require separate checks from the Apache-2.0 downloaded weights.

Published benchmark results are producer claims and are not independently reproduced here.
