# Axolotl

Axolotl is an open-source model-development/post-training framework for LLM/VLM fine-tuning and related training workflows.

## Scope and boundaries

SFT, LoRA/QLoRA, preference optimization, reinforcement-learning methods, reward modeling, and distributed training are capabilities of the same model-development framework. Supported models, trainers, accelerators, optimization libraries, configuration schema, hardware requirements, and package versions vary by release.

## Telemetry

Axolotl enables telemetry by default through PostHog. Documented event categories include system and hardware information, selected model/configuration information, training runtime metrics, and sanitized error details. Set `AXOLOTL_DO_NOT_TRACK=1` or `DO_NOT_TRACK=1` to disable it.

## Relations

- Produced by: [`catalog/producers/a/axolotl-ai-cloud`](../../../../../../../producers/sub/a/sub/axolotl-ai-cloud/)

## Official resources

- <https://docs.axolotl.ai/>
- <https://github.com/axolotl-ai-cloud/axolotl>
- [Telemetry documentation](https://docs.axolotl.ai/docs/telemetry.html)
