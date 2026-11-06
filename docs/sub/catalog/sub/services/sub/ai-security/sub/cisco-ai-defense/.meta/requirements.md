# Documentation Requirements

## Requirements

- Present Cisco AI Defense as Cisco's distinct AI-security product for securing AI applications and AI infrastructure against AI-specific threats.
- Keep generic Cisco security-suite capabilities outside this profile unless they are explicitly part of the current AI Defense product surface.
- Treat module names, supported deployment/integration surfaces, availability, licensing, and protection claims as freshness-sensitive.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- Cisco AI Defense remains AI-security-first rather than a generic cybersecurity-suite profile.
- Producer provenance resolves to Cisco.

## Scoped original-source qualification — 2026-11-06

- Cisco AI Defense's official data sheet documents one AI-specific security suite: cloud/asset visibility, model/MCP supply-chain scanning, model/application validation, and runtime protections for prompts, responses and agent tool actions. Current Cisco DevNet Management API separately documents model-validation endpoints and runtime policies, with MCP connection management explicitly beta.
- Cisco's deployment models distinguish protected traffic in customer VPC/AI POD and management-plane telemetry; a network- or API-level guardrail does not intrinsically inspect all external tools, all runtime paths or all privately retained data without correctly deployed enforcement.
- Model-specific tests, automated red-team counts, standards mappings and vendor-stated threat detection are not independent proof of universal coverage or regulatory compliance. Licensing, placement, policy setup and supported MCP features are mutable.
- Verified first-party source 1: https://www.cisco.com/c/en/us/products/collateral/security/ai-defense/ai-defense-ds.html
- Verified first-party source 2: https://developer.cisco.com/docs/ai-defense-management/
- Accept only source-bounded existing service identity and documented protection/deployment boundaries. This is not an independent security/privacy/compliance evaluation, vulnerability test, model validation result, new metadata/entity, reader repair, root-wide schema/cache/CI/render, clean pass, final delivery or merge.
