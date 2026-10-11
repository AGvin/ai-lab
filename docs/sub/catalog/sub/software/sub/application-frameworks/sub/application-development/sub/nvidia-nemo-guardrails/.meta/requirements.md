# Documentation Requirements

## Requirements

- Identify NVIDIA NeMo Guardrails as NVIDIA's released open-source Python framework/library for adding programmable guardrails to LLM and agent applications.
- Preserve its primary application-development role: input, retrieval, dialog, execution, and output rails; Colang; custom actions; guardrail catalogs; local/server deployment; evaluation; tracing/observability; and provider integrations belong to one software identity unless upstream later establishes an independently durable peer product.
- Keep NeMo Guardrails distinct from guardrail/safety models such as Nemotron safety classifiers, NVIDIA NIM services, NeMo Platform, generic policy concepts, API gateways, complete agent runtimes, and hosted AI-security services.
- Preserve lifecycle/version boundaries from current stable release documentation; development-branch behavior must not be presented as released functionality.
- Treat Python/runtime support, provider integrations, rail catalogs, Colang syntax, server/API behavior, built-in classifiers, optional extras, deployment methods, OpenTelemetry support, privacy/data-flow behavior, release versions, and compatibility matrices as freshness-sensitive.
- Preserve the exact enforcement boundary: guardrails can allow, block, transform, inspect, or govern configured application flows, but they do not by themselves provide complete OS sandboxing, credential isolation, network isolation, regulatory compliance, or universal application safety.
- Attribute safety/evaluation performance claims to NVIDIA or the cited evaluator and preserve the exact rail/model/configuration used.
- Preserve NVIDIA producer provenance.

## Validation

- The node remains an application-development guardrails framework rather than a hosted security service or trained safety model.
- Colang and built-in guardrail components are not duplicated as peer canonical products by default.
- Stable-release facts are not inferred from the repository development branch.
- Producer provenance resolves bidirectionally to NVIDIA.
