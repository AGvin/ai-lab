# Documentation Requirements

## Requirements

- Describe Sentry Skills as a Sentry-authored collection of engineering and development Agent Skills and its associated Claude plugin marketplace, principally meant for the Sentry team. Do not confuse it with the separate user-facing Sentry for AI distribution source or the hosted Sentry service.
- Pin first-party `getsentry/skills` source commit `e94f22214528d69899d09c627b3315ddc3544816` (source inspected 2026-11-09) for the README, Apache-2.0 LICENSE, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, and example `skills/code-review/SKILL.md`. Avoid a fixed inventory count or claims about currently installed versions.
- Explain that the marketplace registers the `sentry-skills` plugin from repository root. The canonical `skills/` and `agents/` folders live at repo root; `.agents/skills` is a local mirror. An individual bundled skill does not automatically qualify as an independent AI Lab catalog entry.
- Ground installation in the published Claude Code marketplace/plugin commands and the optional skills.sh-compatible `npx skills add getsentry/skills` flow. Host compatibility, client policy, skills and dependencies may change.
- Note that Sentry engineering workflows (commit, code review, security reviews, PR iteration and configuration) can read files, run tools, touch remote repositories or obtain credentials. Installation does not authorize production access, code changes or operations in a different organization; require scoped user approval, least privilege and local review.
- Preserve the newly indexed collection-owned `browse-local-sentry` skill and its two different data boundaries: `dev-ui` uses the user's signed-in Chrome session and may access **production sentry.io data as the user**, including staff privileges; the full devserver uses a local database. Treat a local hostname as insufficient proof of isolation. Use only the nominated organization, avoid any create/edit/delete action without specific approval, do not bypass certificate warnings or request credentials, and do not read or alter pre-existing user tabs. Client MCP configuration changes require approval.
- Separate Apache-2.0 source licensing from included third-party vendored materials, underlying Sentry service accounts, private monitored data and other independently governed repositories.
- Preserve one reciprocal producer relationship to Sentry and one parent collection index entry. Do not duplicate bundled skills or the separate Sentry for AI source/build pipeline.

## Bounded source and safety reconciliation — 2026-11-09

- Compared the [old official source](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/README.md) to the [newer source](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/README.md): exactly one added `browse-local-sentry` inventory row. Inspected its [original SKILL.md](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/browse-local-sentry/SKILL.md); root Apache-2.0 LICENSE, marketplace manifest and plugin descriptor blobs are unchanged between the compared revisions.
- No browser session, production Sentry organization, private credentials or local devserver was accessed by AI Lab. This is not a full client installation, dependency/security or repository freshness audit.

## Validation

- [Official source](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/README.md), [manifest](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/.claude-plugin/marketplace.json), [plugin descriptor](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/.claude-plugin/plugin.json), [license](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/LICENSE), and [code review skill](https://github.com/getsentry/skills/blob/e94f22214528d69899d09c627b3315ddc3544816/skills/code-review/SKILL.md) establish source and packaging.
- The collection is indexed once and reciprocal `produced-by` / `produces` links resolve.
- No installed plugins, authenticated Sentry calls, user or production data access, complete dependencies audit, CI, or whole-catalog clean pass is claimed.
