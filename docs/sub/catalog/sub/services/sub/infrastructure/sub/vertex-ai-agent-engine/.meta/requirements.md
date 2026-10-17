# Documentation Requirements

## Requirements

- Present Vertex AI Agent Engine as Google Cloud's generally available managed runtime/platform for deploying, operating, scaling, monitoring, and governing production AI agents.
- Preserve its managed-service boundary across agent runtime, sessions, memory, code execution, evaluation/monitoring, framework integration, and production infrastructure.
- Keep Google Agent Development Kit (ADK), Google Agents CLI, Gemini Enterprise Agent Platform, Google Agent Registry, underlying model identities, and third-party frameworks such as LangGraph/CrewAI separate from Agent Engine.
- Preserve the March 4, 2025 GA service lifecycle and keep capability-level preview/GA distinctions source-scoped; later GA of Sessions/Memory Bank or preview integrations does not create peer service identities by default.
- Treat regions, pricing, quotas, supported frameworks/models, session/memory/code-execution behavior, monitoring, IAM/networking, and product integration state as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Vertex AI Agent Engine remains a producer-hosted managed runtime/platform rather than an installable agent framework.
- Gemini Enterprise registration/integration does not collapse Agent Engine into the Gemini Enterprise product identity.
- Producer provenance resolves bidirectionally to Google Cloud.
