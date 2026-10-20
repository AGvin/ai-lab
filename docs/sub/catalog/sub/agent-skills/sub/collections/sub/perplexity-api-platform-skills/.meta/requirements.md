# Documentation Requirements

## Requirements

- Identify Perplexity API Platform Skills as Perplexity AI's official repository-backed collection of portable Agent Skills for Perplexity API Platform development workflows.
- Preserve the collection boundary: the repository currently packages skills for Sonar-to-Agent-API migration, Perplexity CLI search, and Perplexity Search SDK workflows and is designed to grow over time; do not create one peer catalog entity per skill by default.
- Keep the repository's Claude Code plugin marketplace packaging, Agent Plugin packaging, Codex plugin flow, ecosystem installers, docs MCP server, CLI/SDK packages, and API endpoints as distribution/access surfaces rather than separate skill-collection identities.
- Keep the Perplexity Skills Marketplace separate as the multi-source/user-and-organization marketplace/registry surface; this collection is a publisher-owned first-party skill set.
- Treat exact skill inventory, client compatibility, install commands, bundled MCP/configuration, invocation names, plugin metadata, and release state as freshness-sensitive.
- Preserve the repository-level Apache-2.0 distribution boundary while requiring path-specific license verification if future bundled assets establish different terms.
- Render the standard `entity-relations` block from validated current-entity relations.

## Validation

- The collection remains distinct from the Perplexity Skills Marketplace registry.
- Individual repository skill directories are not duplicated as standalone AI Lab nodes without independent identity.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity API Platform Skills is the official repository-backed collection for API migration and search-development workflows. Its portable skill files and plugin packaging are distinct from the public Computer Skills Marketplace.
- Decision and deployment boundary: The repository declares Apache-2.0. Pin and inspect the selected revision, skill scripts and optional documentation integration before use. Installing instructions or a docs integration does not provide paid API access or permission to change an application's data.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://github.com/perplexityai/api-platform-developers>, <https://docs.perplexity.ai/docs/search/quickstart>.
