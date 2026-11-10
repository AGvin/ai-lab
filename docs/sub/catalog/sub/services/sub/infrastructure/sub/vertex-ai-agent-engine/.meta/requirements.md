# Documentation Requirements

## Requirements

- Present Agent Runtime on Gemini Enterprise Agent Platform as Google Cloud's generally available managed runtime/platform for deploying, operating, scaling, monitoring, and governing production AI agents.
- Preserve its managed-service boundary across agent runtime, sessions, memory, code execution, evaluation/monitoring, framework integration, and production infrastructure.
- Keep Google Agent Development Kit (ADK), Google Agents CLI, Gemini Enterprise Agent Platform, Google Agent Registry, underlying model identities, and third-party frameworks such as LangGraph/CrewAI separate from Agent Runtime.
- Preserve the March 4, 2025 GA service lifecycle and keep capability-level preview/GA distinctions source-scoped; later GA of Sessions/Memory Bank or preview integrations does not create peer service identities by default.
- Treat regions, pricing, quotas, supported frameworks/models, session/memory/code-execution behavior, monitoring, IAM/networking, and product integration state as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

- Preserve Vertex AI Agent Engine as the former-name alias. The documented rename to Agent Runtime on Gemini Enterprise Agent Platform does not create another service or merge the runtime with the broader platform.

## Validation

- Agent Runtime on Gemini Enterprise Agent Platform remains a producer-hosted managed runtime/platform rather than an installable agent framework.
- Gemini Enterprise registration/integration does not collapse Agent Runtime into the Gemini Enterprise product identity.
- Producer provenance resolves bidirectionally to Google Cloud.

## Scoped original-source qualification — 2026-11-06

- Google Cloud's current name-change table explicitly maps the former Vertex AI Agent Engine identity to Agent Runtime on Gemini Enterprise Agent Platform. Retain the existing canonical service and former-name alias; do not treat the rename as another accepted candidate or merge Agent Runtime into the umbrella enterprise agent platform.
- The original Agent Platform scale documentation distinguishes managed Agent Runtime from Sessions, Memory Bank, Code Execution, agent evaluation and other integrated services. Feature-level lifecycle, IAM permissions and regional/data-residency restrictions vary; for example, customer-managed encryption key support differs between single-region and multi-region deployed endpoints.
- Managed deployment and framework integrations do not transform ADK, models, LangGraph/CrewAI or Agent Registry into Google-owned trained-model artifacts. No authenticated runtime, production isolation or independent governance audit is implied by source qualification.
- Verified first-party source 1: https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes
- Verified first-party source 2: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale
- Gate scope is inherited source identity and current publisher-documented version/rights/operational boundaries, not independent production testing, full freshness/security/legal review, metadata or reader-repair credit, root-wide schema/cache/CI/render, clean pass, final delivery or merge.
