# Documentation Requirements

## Requirements

- Identify Microsoft as the canonical producer organization for represented Microsoft model and software entities in the catalog.
- Preserve GitHub, Inc. as a separately represented organization owned by Microsoft without using ownership as a substitute for GitHub product provenance.
- Keep the GitHub ownership fact distinct from production: GitHub-produced product identities remain attributed to GitHub unless independent evidence supports an additional producer.
- Keep model-family and concrete-model details in `catalog/models/` and software details in their corresponding canonical owners rather than duplicating them on the producer page.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Keep Azure-hosted access, third-party inference providers, quantizations, runtime integrations, and deployment guidance with their corresponding canonical owners rather than inferring them from corporate association.

## Content Specification

- Use `Microsoft` as the page title.
- Describe Microsoft concisely as the producer organization for the represented Microsoft model and software entities.
- Include the official Microsoft website, Microsoft Hugging Face organization, and official Microsoft acquisition record supporting the GitHub ownership fact.

## Validation

- GitHub ownership is not treated as evidence that Microsoft directly produces GitHub-authored catalog products.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
