# Documentation Requirements

## Requirements

- Identify Perplexity Skills Marketplace as Perplexity AI's public/enterprise marketplace and discovery surface for reusable Perplexity Computer Skills.
- Preserve registry/marketplace ownership rather than treating the marketplace itself as a publisher-owned skill collection: users and organizations can discover, install, create/upload, share, and govern reusable skills through the marketplace/workspace surface.
- Keep individual public, personal, and organization skills with their source/owner context; marketplace presence does not justify creating standalone AI Lab nodes for every skill.
- Keep Perplexity Computer, Portable Computer, connectors, Brain, models, and subscription/workspace controls as separate product capabilities or dependencies rather than registry identities.
- Account for Perplexity's separately introduced 2026-11-06 **Agent Plugins** distribution: install skills and connectors together through a plugin or import compatible packages from GitHub/ZIP. Keep plugin packaging and connector authorization distinct from marketplace skill discovery, without multiplying identities.
- Preserve deployment permissions: plugin/skill installation is not blanket consent for connected-account reads/actions, and Enterprise admins can govern which roles may add plugins and use their connectors; eligible plans and enterprise access remain freshness-sensitive.
- Explain rights boundaries: regular service [Terms](https://www.perplexity.ai/en-GB/hub/legal/terms-of-service) cover user content licensing but explicitly exclude separate Enterprise and API terms. No Marketplace or plugin listing grants blanket copyright/security rights over all third-party skill files; check each publisher and customer deployment agreement.
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

## Scoped original-source qualification — 2026-11-08

- **Perplexity Skills Marketplace** is an independently identifiable vendor-operated discovery/installation **registry**, rather than a fixed publisher-authored collection of the individually published skills it lists. Perplexity's official 2026-09-21 launch notes describe a public browsable catalog even without sign-in and Enterprise-specific installation, sharing, organization skill creation and approval governance.
- Original first-party product/lifecycle evidence: https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace (Perplexity, checked 2026-11-08). Individual skills retain their own publisher and security/rights boundaries; a directory entry or Enterprise approval does not make third-party skill code safe or authorize unrelated credentials. Account, plan, admin policy, discovery UI and inventory may change.
- Accept **one previously uncredited existing-identity original-source gate** for this marketplace only. Preserve distinct Perplexity Computer, agent plugin packaging, individual skill collections, skill registries and the upstream open Agent Skills format. No new identity or metadata gate, source artifact redistribution, authenticated installation/enterprise permission test, complete license/security/privacy audit, root-wide reader/CI/render, clean or final acceptance.

## Marketplace and Agent Plugins freshness/rights — 2026-11-09

- Compared first-party [2026-09-21 Skills Marketplace launch](https://www.perplexity.ai/changelog/effort-mode-gpt-6-astra-and-skills-marketplace) to the newer [2026-11-06 Agent Plugins launch](https://www.perplexity.ai/changelog/teammates-fully-local-computer-on-mac-and-voice-mode). The November release documents bundled skills/connectors and import by GitHub repository or ZIP, with role-governed plugin/connector usage for qualifying Enterprise administrators. Marketplace registry identity is unchanged.
- [Consumer Terms](https://www.perplexity.ai/en-GB/hub/legal/terms-of-service) (2026-01-23) distinguish user content rights, service licensing and third-party materials; they explicitly do not govern Enterprise or API contracts. This records a **terms/rights boundary**, not permission to redistribute third-party skills, a definitive enterprise-license assessment or installation/security approval.
- No account-connected operations, plugin install/import, protected file upload, admin permission test or independent runtime verification performed.
