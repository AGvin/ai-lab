# NVIDIA NeMo Guardrails

NVIDIA NeMo Guardrails is an open-source Python framework for adding programmable guardrails to language-model and agent applications.

## Scope and capabilities

Input, retrieval, dialog, execution and output rails, Colang flows, custom actions and optional evaluation or tracing components belong to this application framework. They are not independent trained safety models.

## Deployment and safety boundaries

NeMo Guardrails is not a model, NVIDIA NIM or a universal security sandbox. Rails can inspect, allow, transform or block configured interactions, but cannot replace host security, network controls or least-privilege tool credentials. Pin released Colang/runtime and model-provider versions instead of assuming development-branch features are stable.

The v0.24.1 documentation describes anonymous deployment and feature-usage telemetry sent to NVIDIA at startup and through heartbeats. It excludes prompts, completions and API keys. Setting `NEMO_GUARDRAILS_NO_USAGE_STATS=1` before startup disables this usage reporting. It is separate from calls to configured guardrail/model providers and from optional OpenTelemetry tracing to a chosen backend.

## Relations

- Produced by: [NVIDIA](../../../../../../../producers/sub/n/sub/nvidia/)

## Official resources

- [Source repository](https://github.com/NVIDIA-NeMo/Guardrails)
- [Documentation](https://docs.nvidia.com/nemo/guardrails/latest/home)
- [v0.24.1 telemetry and opt-out](https://docs.nvidia.com/nemo/guardrails/v0.24.1/resources/telemetry)
