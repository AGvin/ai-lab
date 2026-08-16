# Documentation Requirements

## Requirements

- Identify Microsoft as the canonical producer organization for the represented Phi model family and Microsoft-authored software entities in the catalog.
- Preserve GitHub, Inc. as a separately represented organization owned by Microsoft and link it through the canonical `owns` relation.
- Keep the GitHub ownership fact distinct from production: GitHub-produced product identities remain attributed to GitHub unless independent evidence supports an additional producer.
- Keep Phi family and concrete-model details in `catalog/models/` and keep framework, application-development, editor, and testing details in their corresponding software owners rather than duplicating them on the producer page.
- Represent the current Microsoft `produces` relations to Phi, AutoGen, Microsoft Agent Framework, Microsoft.Extensions.AI, Visual Studio Code, and Playwright.
- Keep Azure-hosted access, third-party inference providers, quantizations, runtime integrations, and deployment guidance with their corresponding canonical owners rather than inferring them from corporate association.

## Content Specification

- Use `Microsoft` as the page title.
- Describe Microsoft concisely as the producer organization for the represented Phi and Microsoft-authored software entities.
- Link GitHub, Inc. through the canonical `owns` relation while keeping its product provenance separate.
- Include the official Microsoft website, Microsoft Hugging Face organization, and official Microsoft acquisition record supporting the GitHub ownership fact.

## Validation

- GitHub ownership is not treated as evidence that Microsoft directly produces GitHub-authored catalog products.
- All represented entity links resolve to canonical catalog nodes.
