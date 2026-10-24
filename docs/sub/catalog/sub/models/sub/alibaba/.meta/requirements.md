# Documentation Requirements

## Requirements

- Provide model-domain navigation for the distinct Qwen and Wan model families associated with Alibaba Cloud, Qwen Team, and Wan Team.
- Keep producer identity and detailed producer descriptions in canonical producer pages.

## Content Specification

- Use `Alibaba models` as the page title.
- Include only a short explanation of why this producer grouping exists in the model catalog.
- Link the canonical Alibaba Cloud and Qwen Team producer pages.
- Link the Qwen model-family child page.

## Decision and Operational Boundaries

- Alibaba models is a producer-oriented navigation view containing the distinct Qwen and Wan model families.
- Do not attach a shared model license, input/output contract, deployment guarantee, or security policy to this navigation view.
- Keep Qwen Team and Wan Team as canonical producer identities and keep Alibaba Cloud Model Studio as a hosting service.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The page does not duplicate detailed producer descriptions or organizational histories.
- Canonical producer links resolve under `catalog/producers/`.
- Model-family links resolve within the model subtree.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
