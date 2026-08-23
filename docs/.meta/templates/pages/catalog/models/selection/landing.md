# Model Selection Landing Page

## Description

Entry page for model-specific decision support.

## Purpose

Explain how AI Lab approaches model selection and route readers to the correct materialized decision journey: task/need, combined user situation, or fixed/owned hardware.

## Use When

Use for `catalog/models/selection/`.

## Do Not Use When

Do not use for canonical model reference facts, one concrete selection guide, one user scenario, one hardware target, hardware purchasing, complete deployment architecture, or a generic catalog category.

## Owns

- selection methodology at orientation level;
- assignment-first decision framing where applicable;
- the distinction among `decision-guides/`, `user-scenarios/`, and `hardware/`;
- evidence-state and exact-identity expectations;
- child-navigation placement and reader wording for materialized direct selection areas;
- boundary back to canonical Model Reference.

## Does Not Own

- direct-child membership or ordering, which come from the validated current-node navigation projection;
- complete model, hardware, software, or service profiles;
- universal rankings;
- copied mutable pricing/availability as durable facts;
- full evaluation results belonging to specific guides;
- hardware purchase or whole-solution infrastructure decisions.

## Expected Inputs

Requirement-approved methodology summary, authorization for the primary child-navigation block, validated current-node direct-child projection, explicit Model Reference boundary/link, common evidence/decision principles, and concise descriptions of the materialized reader journeys.

## Composition

1. default header;
2. concise model-selection orientation;
3. reader-question routing among task/need, combined situation, and fixed hardware;
4. common evidence and exact-identity principles;
5. primary `child-navigation` to materialized direct selection areas using the validated direct-child projection;
6. explicit link back to canonical reference facts.

## Variants

The number of materialized selection journeys may change only through selected architecture. Only reviewed, materialized direct areas appear through the canonical navigation projection; empty conceptual skeletons are not rendered.

## Representative Example

- `docs/sub/catalog/sub/models/sub/selection/`

## Anti-patterns

- enumerating direct selection areas in page requirements when the standard child-navigation block is intended;
- filtering direct selection areas inside the template instead of using the canonical navigation projection;
- collapsing combined user scenarios or fixed-hardware selection into task guides;
- presenting one universal best-model list;
- duplicating canonical model or hardware descriptions;
- treating provider claims as independent AI Lab evidence;
- turning the hardware journey into a hardware-buying guide.
