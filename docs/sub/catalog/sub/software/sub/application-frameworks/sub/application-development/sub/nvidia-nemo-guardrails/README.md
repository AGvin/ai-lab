# NVIDIA NeMo Guardrails

NVIDIA NeMo Guardrails is an open-source Python framework for adding programmable guardrails to language-model and agent applications.

## Scope and capabilities

Input, retrieval, dialog, execution and output rails, Colang flows, custom actions and optional evaluation or tracing components belong to this application framework. They are not independent trained safety models.

## Deployment and safety boundaries

NeMo Guardrails is not a model, NVIDIA NIM or a universal security sandbox. Rails can inspect, allow, transform or block configured interactions, but cannot replace host security, network controls or least-privilege tool credentials. Pin released Colang/runtime and model-provider versions instead of assuming development-branch features are stable.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source repository](https://github.com/NVIDIA-NeMo/Guardrails)
- [Documentation](https://docs.nvidia.com/nemo/guardrails/latest/home)
