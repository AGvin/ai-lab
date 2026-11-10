# Composio Awesome Claude Skills

[ComposioHQ's Awesome Claude Skills repository](https://github.com/ComposioHQ/awesome-claude-skills) is a maintained, community-contributed directory and bundle of Claude/Agent Skills, resource links and automation plugins. It contains `SKILL.md`-based workflows, local skill directories and links to external contributors. The publisher also includes Composio-backed app-automation recipes and a `connect-apps` plugin. This catalog entry describes **one collection**, not every embedded or linked skill as a separate accepted identity.

## Collection and release boundary

The inspected [`master` source snapshot](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2) is pinned to commit `be2a406907dbc61b73e6827ded415c96139d13a2`. No public GitHub Releases were found at inspection. The README's claimed number of skills/integrations and platform support are publisher statements subject to changes and per-skill compatibility; a directory entry is not an installation or execution test.

Composio maintains the repository and distributes collection content, but community contributors and linked external projects retain their own authorship. The collection is distinct from [Composio's hosted integration service](../../../../../services/sub/agent-integration-platforms/sub/composio/) and the Anthropic/other publishers' separate collections.

## Licensing, security and privacy boundaries

The [original README](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md#license) declares **Apache-2.0** for the repository and explicitly warns that individual skills may use different licenses. The inspected root contains **no `LICENSE` file**, and the GitHub repository license field was null; therefore this statement is not a verified blanket grant for every bundled skill, third-party asset or linked project. Inspect each selected skill and its own license before redistribution or commercial use.

Treat skills as untrusted instructions and code: review `SKILL.md`, shell/Python scripts, dependencies, allowed tools and write/network actions, and pin the reviewed revision. Do not expose credentials or sensitive workspace data by default. The `connect-apps` plugin and some per-app recipes rely on Composio's external service and may involve API keys, OAuth grants and third-party data processing; grant the minimum necessary scope and authorize external effects separately. No package install, skill execution, third-party code audit or complete beneficial-ownership investigation was performed.

## Verified app-action boundary

The pinned [`connect-apps` skill](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/connect-apps/SKILL.md) is not a read-only reference: after plugin installation, API-key setup and per-app OAuth consent, it can send email, publish chat messages and create issue-tracker records through an external tool router. The separately packaged [connect-apps plugin](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/connect-apps-plugin/README.md) also has a local-plugin installation route. Their advertised integration counts differ, so treat counts as vendor marketing rather than a tested inventory.

Before invoking a connected app, inspect the exact OAuth permissions, account/tenant, destination and information to be transmitted; require explicit approval for externally visible writes. Installation does not itself authorize any external service effect. The [original contributor rules](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/CONTRIBUTING.md) request attribution and testing, but do not prove every contributed script, dependency or linked skill was independently audited. The root of this pinned tree lacks a standalone `LICENSE` file even though its README advertises Apache-2.0; inspect per-skill terms instead of granting blanket redistribution rights. No live plugin, OAuth, app action or dependency was tested here.

## Relations

- Maintained/published by: [Composio](../../../../../producers/sub/c/sub/composio/)
- Distinct associated service: [Composio agent integration platform](../../../../../services/sub/agent-integration-platforms/sub/composio/)

## Original resources

- [Awesome Claude Skills repository](https://github.com/ComposioHQ/awesome-claude-skills)
- [Repository README and license declaration](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/README.md)
- [Contribution and attribution requirements](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/CONTRIBUTING.md)
- [Inspected source commit](https://github.com/ComposioHQ/awesome-claude-skills/commit/be2a406907dbc61b73e6827ded415c96139d13a2)
