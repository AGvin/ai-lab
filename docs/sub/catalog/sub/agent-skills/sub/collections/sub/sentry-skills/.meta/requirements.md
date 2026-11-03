# Documentation Requirements

## Requirements

- Describe Sentry Skills as a Sentry-authored collection of engineering and development Agent Skills and its associated Claude plugin marketplace, principally meant for the Sentry team. Do not confuse it with the separate user-facing Sentry for AI distribution source or the hosted Sentry service.
- Pin first-party `getsentry/skills` source commit `0c464f411bdfb8d4c12314b36264d06cb2f60270` (2026-11-02) for the README, Apache-2.0 LICENSE, `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, and example `skills/code-review/SKILL.md`. Avoid a fixed inventory count or claims about currently installed versions.
- Explain that the marketplace registers the `sentry-skills` plugin from repository root. The canonical `skills/` and `agents/` folders live at repo root; `.agents/skills` is a local mirror. An individual bundled skill does not automatically qualify as an independent AI Lab catalog entry.
- Ground installation in the published Claude Code marketplace/plugin commands and the optional skills.sh-compatible `npx skills add getsentry/skills` flow. Host compatibility, client policy, skills and dependencies may change.
- Note that Sentry engineering workflows (commit, code review, security reviews, PR iteration and configuration) can read files, run tools, touch remote repositories or obtain credentials. Installation does not authorize production access, code changes or operations in a different organization; require scoped user approval, least privilege and local review.
- Separate Apache-2.0 source licensing from included third-party vendored materials, underlying Sentry service accounts, private monitored data and other independently governed repositories.
- Preserve one reciprocal producer relationship to Sentry and one parent collection index entry. Do not duplicate bundled skills or the separate Sentry for AI source/build pipeline.

## Validation

- [Official source](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/README.md), [manifest](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/.claude-plugin/marketplace.json), [plugin descriptor](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/.claude-plugin/plugin.json), [license](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/LICENSE), and [code review skill](https://github.com/getsentry/skills/blob/0c464f411bdfb8d4c12314b36264d06cb2f60270/skills/code-review/SKILL.md) establish source and packaging.
- The collection is indexed once and reciprocal `produced-by` / `produces` links resolve.
- No installed plugins, authenticated Sentry calls, user or production data access, complete dependencies audit, CI, or whole-catalog clean pass is claimed.
