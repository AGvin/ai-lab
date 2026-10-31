# Documentation Requirements

## Requirements

- Present the concrete Qwen3-Coder models currently represented in the migrated catalog.
- Keep this page as navigation rather than duplicating line-wide or concrete-model facts.
- Preserve legacy concrete models when their model ownership is already selected.

## Content Specification

- Use `Qwen3-Coder Models` as the page title.
- Link the parent Qwen3-Coder model line.
- List Qwen3-Coder 30B-A3B Instruct, Qwen3-Coder 480B-A35B Instruct, and Qwen3-Coder-Next with short identity-level descriptions.
- Do not repeat concrete parameter tables, hosted aliases, model-selection advice, runtime guidance, frontier/ecosystem classifications, or deployment conclusions.

## Decision and Operational Boundaries

- This catalog index navigates represented children of Qwen3-Coder; it does not define another trained-model identity.
- Keep model/revision-specific modality, license, context, and operational/security facts on canonical children.
- List only materialized child pages, maintain the parent route, and do not present navigation order as a quality or deployment ranking.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- Every listed child resolves to a canonical documentation node.
- The index contains no temporary placeholder wording.
- The page does not act as a second Qwen3-Coder line profile.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
