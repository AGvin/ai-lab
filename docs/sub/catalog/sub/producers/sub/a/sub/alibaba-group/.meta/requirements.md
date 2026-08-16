# Documentation Requirements

## Requirements

- Identify Alibaba Group as the organization relevant to the producer hierarchy and Higress provenance represented in this catalog.
- Explain its structural relationship to Alibaba Cloud without implying ownership or production relations that are not independently supported.
- Preserve Higress as a product originating within Alibaba Group through the physically materialized `produces` relation when the reciprocal Higress `produced-by` relation resolves successfully.

## Content Specification

- Use `Alibaba Group` as the page title.
- Keep the introduction concise and producer-focused rather than providing a general corporate profile.
- Link Alibaba Cloud from the physically materialized `has-part` relation when the reciprocal Alibaba Cloud `part-of` relation resolves successfully.
- Link Higress from the physically materialized `produces` relation when the reciprocal Higress `produced-by` relation resolves successfully.
- Include authoritative Alibaba Group identity material and keep Higress-specific provenance with the Higress entity.

## Validation

- The Alibaba Group/Alibaba Cloud `has-part` / `part-of` relation pair is physically present at both endpoints and semantically consistent.
- The Alibaba Group/Higress `produces` / `produced-by` relation pair is physically present at both endpoints and semantically consistent.
- Every internal producer/product link resolves to a canonical node.
- The page does not imply additional ownership, hierarchy, or production relations beyond validated entity relations.
