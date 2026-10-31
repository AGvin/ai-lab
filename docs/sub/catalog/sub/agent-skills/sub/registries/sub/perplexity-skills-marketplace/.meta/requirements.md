# Documentation Requirements

## Requirements

- Identify Perplexity Skills Marketplace as Perplexity AI's public/enterprise marketplace and discovery surface for reusable Perplexity Computer Skills.
- Preserve registry/marketplace ownership rather than treating the marketplace itself as a publisher-owned skill collection: users and organizations can discover, install, create/upload, share, and govern reusable skills through the marketplace/workspace surface.
- Keep individual public, personal, and organization skills with their source/owner context; marketplace presence does not justify creating standalone AI Lab nodes for every skill.
- Keep Perplexity Computer, Portable Computer, connectors, Brain, models, and subscription/workspace controls as separate product capabilities or dependencies rather than registry identities.
- Treat inventory, categories, ranking/search behavior, install flow, enterprise sharing, approval policy, organization-skill governance, plan eligibility, and marketplace UI as freshness-sensitive.
- Do not treat marketplace availability or installation approval as proof that a skill is safe, correct, compatible, or suitable for a target repository/workflow.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The Marketplace remains a registry/discovery identity rather than a first-party fixed collection.
- Individual indexed skills are not duplicated automatically.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity Skills Marketplace is a discovery and installation registry for reusable Computer skills, including public and organization-managed skills.
- Decision and deployment boundary: Public browsing and Enterprise administration are different access levels. Inspect the selected skill's publisher, instructions and requested access; organization approval does not establish code safety or grant unrelated application permissions.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace>.
