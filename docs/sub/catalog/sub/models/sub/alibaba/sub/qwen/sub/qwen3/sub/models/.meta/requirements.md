# Documentation Requirements

## Requirements

- Present the concrete Qwen3 models currently represented in the catalog.
- Keep this page as model navigation rather than duplicating family-wide or concrete-model facts.
- List only implemented child nodes.

## Content Specification

- Use `Qwen3 Models` as the page title.
- Link the parent Qwen3 generation page.
- List Qwen3 8B, Qwen3 14B, Qwen3 30B-A3B, and Qwen3 32B with short identity-level descriptions.
- Distinguish dense models from the Qwen3 30B-A3B Mixture of Experts (MoE) model when useful for navigation.
- Do not repeat parameter tables, model-selection advice, hardware-fit recommendations, or deployment guidance from child pages.

## Decision and Operational Boundaries

- This catalog index navigates represented children of Qwen3; it does not define another trained-model identity.
- Keep model/revision-specific modality, license, context, and operational/security facts on canonical children.
- List only materialized child pages, maintain the parent route, and do not present navigation order as a quality or deployment ranking.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Every listed child resolves to a canonical documentation node.
- The index contains no temporary placeholder wording.
- The page does not act as a second Qwen3 family profile.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
