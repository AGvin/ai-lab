# Hunk

Hunk is an open-source, review-first terminal diff viewer for interactively inspecting changesets, including changes authored by coding agents. Its canonical role is a **local code-review/diff tool**, not an autonomous review agent.

## Review boundary

Hunk can review Git, Jujutsu, Sapling, direct-file, and patch changes; it supports pager/difftool workflows, watch mode, inline agent annotations, and agent-controlled local review sessions. Those capabilities improve visibility but do not establish correctness or security.

Treat external-agent annotations, live session control, the local loopback/session surface, global pager configuration, and generated changes as review boundaries. Retain tests, static analysis, security review, and human approval for consequential changes.

## Related

- [Modem](../../../../../../../producers/sub/m/sub/modem/) — canonical producer/sponsor.

## Official resources

- [Hunk](https://www.hunk.dev/)
- [Hunk repository](https://github.com/modem-dev/hunk)
- [Agent workflows](https://github.com/modem-dev/hunk/blob/main/docs/agent-workflows.md)
