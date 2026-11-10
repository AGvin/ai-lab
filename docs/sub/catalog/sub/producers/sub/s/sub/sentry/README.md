# Sentry

Sentry is a developer debugging and application-observability platform for detecting, investigating and fixing software errors, performance regressions and related application issues. Its first-party `getsentry` repositories also publish two distinct collections of Agent Skills.

## Agent Skills publishing

**Sentry Skills** is a repository of Sentry-team engineering and development practices, including code review, commit workflows, security review and documentation guidance. The first-party README identifies Sentry employees as its primary audience. Its publication does not make these instructions a substitute for an organization's own engineering policy.

**Sentry for AI** is the source of user-facing skills that help compatible agents set up Sentry SDKs, investigate errors, configure alerts and connect monitoring workflows. The repository is **not itself the installable plugin**; its build pipeline publishes generated agent-specific plugins through separate distribution repositories and direct hosted skill delivery.

The two projects have separate source lifecycles and licenses: Apache-2.0 for Sentry Skills and MIT for Sentry for AI. Installing instructions does not authorize access to production Sentry projects or monitored user data. Use approved account credentials, limited tool permissions and controlled handling of traces and error records.

## Relations

- Produces: [Sentry Skills](../../../../../agent-skills/sub/collections/sub/sentry-skills/)
- Produces: [Sentry for AI](../../../../../agent-skills/sub/collections/sub/sentry-for-ai/)

## Official resources

- [Sentry](https://sentry.io/)
- [Sentry platform source](https://github.com/getsentry/sentry)
- [Sentry Skills source](https://github.com/getsentry/skills)
- [Sentry for AI source](https://github.com/getsentry/sentry-for-ai)
