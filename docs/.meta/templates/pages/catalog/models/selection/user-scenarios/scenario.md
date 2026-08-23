# Model User Scenario Page

## Description

Combined-context model-selection page for one concrete user scenario.

## Purpose

Lead a reader from a recognizable situation and constraints through credible model routes, trade-offs, boundaries, and escalation triggers while linking canonical owners instead of duplicating them.

## Use When

Use when persona/scale plus multiple tasks, hardware, budget, skills, privacy/data boundaries, services, deployment preferences, or operational constraints materially change the recommended model route.

## Do Not Use When

Do not use when one bounded model task determines the choice, fixed hardware alone is the primary starting question, the page is a canonical entity profile, or it is full solution architecture.

## Owns

- scenario fit and starting environment;
- material goals, constraints, and success criteria;
- recommended starting model route and credible alternatives;
- route-level trade-offs, data-boundary implications, cost/operations/review needs;
- escalation/change-route triggers;
- verification boundaries for mutable recommendation inputs;
- a hardware-specific continuation block when requirements declare fixed/owned hardware material.

## Does Not Own

- canonical model/software/service/hardware identity or intrinsic facts;
- generic model rankings;
- detailed hardware-fit analysis owned by sibling `hardware/`;
- complete RAG/data-platform/contact-center/security/infrastructure architecture.

## Expected Inputs

Scenario requirements, canonical links, applicable decision-guide/hardware links, and current source-backed mutable evidence when recommendations depend on availability, pricing, limits, runtime support, or provider terms.

## Composition

1. standard header and scenario fit;
2. starting environment, goals, and constraints;
3. recommended route and materially different alternatives;
4. trade-offs, data boundary, operations, cost, and verification needs;
5. optional hardware-specific model-selection continuation;
6. escalation/change-route triggers;
7. canonical entity and sibling selection links.

## Variants

Scenario depth varies with decision scale; ownership does not.

## Representative Examples

- `.../user-scenarios/sub/personal/sub/home-lab-owner/`
- `.../user-scenarios/sub/professionals/sub/mac-developer-or-creator/`
- `.../user-scenarios/sub/organizations/sub/internal-ai-platform/`

## Anti-patterns

- one named model/product as the scenario itself;
- copying catalog profiles or hardware-fit matrices;
- assuming local/self-hosted is automatically cheaper/private/simpler;
- mutable recommendations without verification boundary.
