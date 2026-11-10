# Documentation Requirements

## Requirements

- Identify Windows 365 for Agents as Microsoft's generally available managed Cloud PC service purpose-built for agentic workloads.
- Preserve its infrastructure identity: it supplies secure managed execution environments that agent users can check out, sign in to, and use for automated or assisted workflows.
- Keep Agent 365 as the separate management/control-plane identity that governs access and permissions; do not collapse the two products because they integrate closely.
- Treat pool management, security baselines, Intune/Entra integrations, regional availability, licensing, quotas, and preview/GA feature state as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The entity remains managed infrastructure rather than an agent framework, assistant, or AI-management control plane.
- Feature-level preview status does not override the product-level GA evidence.
- Producer provenance resolves to Microsoft.

## Scoped original-source qualification — 2026-11-06

- Microsoft's official June 2026 release notes identify Windows 365 for Agents as generally available from the week of June 1, 2026, delivering managed Cloud PCs for agentic workflows. Agent users can check out, sign in to and use Cloud PCs, while Agent 365 remains the separate permission/control-plane service.
- The same publisher notes describe Microsoft Entra Conditional Access integration: device-compliance rules can prevent agents using noncompliant Cloud PCs. The product's GA does not imply every pool-management, security, or orchestration feature is GA or available in every region.
- Actual Cloud PC allocation, licenses, Intune/Entra policies, session isolation, identity delegation, accessible corporate resources and retention require tenant-scoped security/admin validation. Treat Microsoft's 'secure' wording as a provider claim rather than an independent agent isolation audit.
- Verified first-party source 1: https://learn.microsoft.com/en-us/windows-365/agents/whats-new
- Verified first-party source 2: https://learn.microsoft.com/en-us/windows-365/agents/overview
- Accept only the present managed infrastructure service identity and source-scoped lifecycle/authorization boundaries. No new entity/metadata, reader repair, independent security/legal/runtime audit, full freshness, whole-repository schema/cache/CI/render, clean pass, final delivery or merge.
