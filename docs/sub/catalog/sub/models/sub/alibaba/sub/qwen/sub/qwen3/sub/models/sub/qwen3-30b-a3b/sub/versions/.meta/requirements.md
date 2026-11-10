# Documentation Requirements

## Requirements

- Explain that this node is the version index for the Qwen3 30B-A3B concrete model.
- List only represented chronological releases that retain the same concrete-model identity.
- Keep model-wide architecture and parameter facts on the parent model page.
- Keep version-specific naming, behavior, context, and release changes on the corresponding version pages.

## Content Specification

- Use `Qwen3 30B-A3B Versions` as the page title.
- Link the parent Qwen3 30B-A3B model.
- Link the represented `Initial release` and `2507` version pages.
- Explain briefly that versions are separate release revisions rather than different parameter-size model identities.

## Decision and Operational Boundaries

- This catalog index navigates represented children of Qwen3 30B-A3B; it does not define another trained-model identity.
- Keep model/revision-specific modality, license, context, and operational/security facts on canonical children.
- List only materialized child pages, maintain the parent route, and do not present navigation order as a quality or deployment ranking.

Use the current primary references in `entity.yml` for these boundaries; mutable service values are not intrinsic identity guarantees.

## Validation

- The index does not duplicate the parent model profile.
- Every listed child has a canonical `version-of` relation to Qwen3 30B-A3B.
- No prospective or empty version nodes are listed as implemented documentation.

## Reader Projection

- Render the current entity's validated visible relations with resolved canonical links and preserve relation ordering; project the sourced identity and operational boundaries into the reader page.
