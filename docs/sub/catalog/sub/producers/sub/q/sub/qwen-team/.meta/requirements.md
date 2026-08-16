# Documentation Requirements

## Requirements

- Identify Qwen Team as the canonical producer team for the Qwen model series represented in the catalog.
- Preserve the team's validated `part-of` relationship to Alibaba Cloud without inferring ownership or a stronger parent/child relation.
- Represent the current physical `produces` edges to the Qwen root family and the represented Qwen2.5-Coder, Qwen3-Coder, and Qwen3 series.
- Keep concrete model, version, artifact, deployment, and provider details in their corresponding canonical model or service owners.

## Content Specification

- Use `Qwen Team` as the page title.
- State concisely that Qwen Team develops the represented Qwen models at Alibaba Cloud.
- Link Alibaba Cloud through the canonical `part-of` relation.
- Link the canonical Qwen root family plus Qwen2.5-Coder, Qwen3-Coder, and Qwen3 from the physically materialized `produces` relations.
- Include the official Qwen website and official Qwen GitHub organization.

## Validation

- The Qwen Team/Alibaba Cloud `part-of` / `has-part` relation pair is physically present at both endpoints and semantically consistent.
- The Qwen Team/Qwen, Qwen Team/Qwen2.5-Coder, Qwen Team/Qwen3-Coder, and Qwen Team/Qwen3 `produces` / `produced-by` relation pairs are physically present at both endpoints and semantically consistent.
- The page does not infer `owned-by`, `parent-of`, or another stronger organizational relation from the documented `part-of` relationship.
- Model details remain in model-domain pages rather than being duplicated here.
- Every internal relation/navigation link resolves to a canonical documentation node.
