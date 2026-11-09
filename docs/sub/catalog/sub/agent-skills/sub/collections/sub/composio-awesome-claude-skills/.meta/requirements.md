# Documentation Requirements

## Requirements

- Identify Composio Awesome Claude Skills as the ComposioHQ-maintained, community-contributed repository for curated Claude/Agent Skills, separately from the existing Composio agent integration service, Composio producer and individual linked skills.
- Scope this node to the one distributed collection identity. Do not count its external skill links, embedded skill directories, app-automation recipes, integration plugins, skill instructions or individual third-party publishers as additional collection nodes.
- Pin the inspected upstream source to Git commit `be2a406907dbc61b73e6827ded415c96139d13a2` on original `master`; upstream GitHub Releases returned no release entries at inspection, so do not invent a stable version.
- State the upstream README's Apache-2.0 license declaration accurately, while explaining that the inspected Git tree has no repository-root `LICENSE` and GitHub's license metadata is null. No blanket legal clearance is inferred; individual skill directories, bundled third-party media, scripts, source links and dependencies may have different terms.
- Distinguish Composio's repository maintenance from third-party contributors' authorship. The original CONTRIBUTING guide requests attribution; acceptance here does not certify every contribution's origin, functionality or license.
- Warn that downloaded Agent Skills can include executable scripts, external tool calls, prompt instructions and privileged access. Review the exact selected folder and pin the revision; isolate execution, constrain secrets, filesystem/network permissions, and confirm external actions before adopting in production.
- Distinguish the `connect-apps` plugin and service-backed per-app workflows from a self-contained, offline-safe local skill. Composio connectivity may require a vendor account, API key, OAuth scopes and third-party processing; restrict and audit permissions and data sharing separately.
- Preserve the already materialized Composio producer and integration-service entities. Use one `produced-by` relation to the existing producer, with a matching `produces` inverse; this means collection distribution/maintenance, not original authorship of all linked projects.
- Keep full corporate/ultimate-beneficial-owner and third-party licensing/supply-chain assessment pending; assign no unsupported nationality-based threat tier.

## Pinned plugin, authorization and rights evidence

- Pin the original [connect-apps SKILL.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/connect-apps/SKILL.md) and separate [plugin README](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/connect-apps-plugin/README.md) when describing app integrations. These can send messages, create issues and mutate connected resources after API-key and OAuth setup; counts of supported apps are publisher claims and differ by route.
- Require explicit account, scope, data-sharing and write-action approval; distinguish installed instruction files, an authorized Composio account and authorization of a particular external effect.
- The pinned [CONTRIBUTING.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/be2a406907dbc61b73e6827ded415c96139d13a2/CONTRIBUTING.md) requests attribution and testing; this is not evidence of independently verified dependencies, third-party license grants or safe execution for every bundled skill. A stated repository Apache-2.0 license with no root LICENSE remains a recorded rights limitation.
- This is a bounded read-only source review; no live OAuth session, service call, permission validation or independent code audit was completed.

## Validation

- Exactly one new canonical `skill-collection` node is created, with one matching existing-producer inverse; do not duplicate Composio service, producer, individual skills or plugins.
- Parent collection index links to this materialized child once; all new reader links resolve to materialized destinations.
- Source version, license declaration vs missing root license, external execution/privacy boundaries, and review limitations are visible on the reader page.
- Scope validation to the touched files and required relations; do not assert global catalog reader, cache, schema, CI, renderer or beneficial-owner validation.
