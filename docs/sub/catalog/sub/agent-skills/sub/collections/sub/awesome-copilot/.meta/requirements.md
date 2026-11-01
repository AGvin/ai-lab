# Documentation Requirements

## Requirements

- Identify Awesome GitHub Copilot as a GitHub-organization-maintained, community-contributed repository that includes an independently usable Agent Skills collection.
- Scope this canonical identity to the Agent Skills collection within `github/awesome-copilot`; its custom agents, instructions, plugins, hooks and cookbook are other asset classes, not additional peer skill collections.
- Treat the upstream `skills/` directory and `docs/README.skills.md` as authoritative mutable inventory, rather than freezing counts, skill names or CLI compatibility.
- Preserve the distinction between GitHub's maintenance/distribution provenance and individual third-party contributors' authorship. A GitHub-organization source is not a guarantee that every contributed skill was authored, audited or endorsed by GitHub.
- Record repository-root MIT licensing without assuming that every third-party embedded script, dataset, media asset, dependency or external service is independently rights-cleared.
- Keep the official GitHub CLI skill-install workflow conditional on the current CLI version and host support. Distinguish installation of skills from the separate Copilot plugin marketplace and GitHub Copilot product.
- Warn that skills may contain executable scripts, tool permissions, subprocesses, network requests or secrets access. Inspect each selected skill, verify its origin and license, pin the reviewed revision where practical, and authorize execution/deployment separately.
- Do not infer ultimate beneficial-owner identities, nationality-based risk or supply-chain safety from hosting alone.

## Validation

- Exactly one skill-collection node represents this upstream collection; individual skills and non-skill asset classes are not duplicated as collections.
- `produced-by` resolves to GitHub, Inc. as collection maintainer, with a matching `produces` relation, not a claim that GitHub authored each community contribution.
- Official repository and Agent Skills documentation links resolve; runtime counts and license/CLI compatibility remain freshness-sensitive.
