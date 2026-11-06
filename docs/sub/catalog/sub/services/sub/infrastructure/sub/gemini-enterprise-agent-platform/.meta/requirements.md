# Documentation Requirements

## Requirements

- Identify Gemini Enterprise Agent Platform as Google's managed enterprise platform for developing, orchestrating, deploying, and operating agents at organizational scale.
- Preserve its relationship to Gemini Enterprise while keeping the platform identity distinct from the Gemini model family, Gemini end-user assistant application, Google ADK software, and individual managed agents/features.
- Treat the 2026-10-08 Gemini agent announcement as the current universal work-agent surface of Gemini Enterprise / the broader managed enterprise agent platform rather than a new peer service: its cross-Workspace execution, skills/tools, business-context access, model selection, security, administration, and cost controls are platform capabilities unless Google later establishes an independent product/service lifecycle.
- Preserve the current Agent Registry boundary: Google Agent Registry is a separate generally available governed registry/discovery service with dedicated product documentation and API lifecycle; Gemini Enterprise Agent Platform integrates with Registry but does not own its canonical identity.
- Keep Agent Gateway, sandboxes, runtime/orchestration capabilities, and other platform features inside the platform identity unless first-party evidence establishes an independently durable product/service boundary.
- Treat supported models, connectors, governance controls, deployment/runtime capabilities, billing, quotas, integrations, and feature availability as mutable source-scoped facts.
- Keep preview-only platform features out of the stable contract unless their lifecycle changes.

## Validation

- The service is not conflated with Google ADK, Gemini models, or Google Agent Registry.
- Enterprise product bundling does not erase independently meaningful service boundaries documented by Google Cloud.
- Mutable capability and availability claims retain freshness boundaries.

## Scoped original-source qualification — 2026-11-06

- Google Cloud's original Gemini Enterprise Agent Platform documentation combines managed agent development, runtime/orchestration, enterprise connectivity, observation and governance. The broader platform is distinct from separately canonical Agent Runtime (formerly Vertex AI Agent Engine), Gemini models/Apps, the ADK developer framework and Agent Registry's governed discovery/control service.
- The publisher describes Agent Gateway security and registry integrations as version- and deployment-dependent; separate preview, public-release and generally available status applies at feature level. The October 2026 enterprise work-agent announcement is part of the wider Gemini Enterprise product surface, not proof of an independent new trained model or unconditional new peer service.
- Treat regional routing, IAM/identity, data access, connectors, model selection, API maturity, billing and retention as contract- and workload-specific. Google-operated control surfaces are not an independently verified certification of every customer's agent.
- Verified first-party source 1: https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview
- Verified first-party source 2: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry
- Verified first-party source 3: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview
- Gate scope is inherited source identity and current publisher-documented version/rights/operational boundaries, not independent production testing, full freshness/security/legal review, metadata or reader-repair credit, root-wide schema/cache/CI/render, clean pass, final delivery or merge.
