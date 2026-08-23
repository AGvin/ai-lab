# User Scenario Page

## Description

Reusable decision-support page for one concrete combined-context user scenario.

## Purpose

Lead a reader from a recognizable situation and constraints through credible routes, trade-offs, boundaries, and escalation triggers while linking canonical entity and model-selection owners instead of duplicating them.

## Use When

Use when persona or operating scale plus multiple tasks, hardware, budget, skills, privacy/data boundaries, services, deployment, or operational constraints materially change the recommended route.

## Do Not Use When

Do not use when one bounded model task alone determines the decision, when the page is primarily a canonical entity profile, or when it is complete implementation architecture for a broader solution.

## Owns

- who the scenario is for and the typical starting environment;
- material goals, constraints, and success criteria;
- recommended starting route and credible alternatives when they materially differ;
- route-level trade-offs, data-boundary implications, cost/operational burden, review needs, and escalation triggers;
- verification boundaries for mutable recommendation inputs.

## Does Not Own

- canonical model/software/service/hardware identity or intrinsic facts;
- generic model rankings owned by model-specific decision guides;
- complete RAG, data-platform, contact-center, security, infrastructure, or other solution architecture;
- claims unsupported by canonical inputs or applicable requirements.

## Expected Inputs

- applicable scenario requirements;
- canonical entity links and model-specific decision-guide links when material;
- current, source-backed mutable evidence when recommendations depend on availability, pricing, limits, or provider terms.

## Composition

1. standard header and scenario fit;
2. starting environment, goals, and constraints;
3. recommended route and materially different alternatives;
4. trade-offs, data boundary, operations, cost, and verification needs;
5. escalation/change-route triggers;
6. links to canonical entities and applicable model-specific decision guides.

## Variants

Scenario depth may vary with decision scale, but the ownership boundary remains the same.

## Representative Examples

- `docs/sub/decision-support/sub/user-scenarios/sub/personal/sub/home-lab-owner/`
- `docs/sub/decision-support/sub/user-scenarios/sub/professionals/sub/software-engineer-without-local-gpu/`
- `docs/sub/decision-support/sub/user-scenarios/sub/organizations/sub/internal-ai-platform/`

## Anti-Patterns

- treating one named product/model as the scenario itself;
- copying complete catalog profiles or model-specific ranking tables;
- assuming self-hosted/local is automatically cheaper, private, or operationally simpler;
- materializing a scenario whose route is not materially distinct from an existing sibling;
- presenting mutable recommendation inputs without their verification boundary.
