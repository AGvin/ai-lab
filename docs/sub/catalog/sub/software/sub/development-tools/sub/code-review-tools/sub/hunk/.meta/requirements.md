# Documentation Requirements

## Requirements

- Identify Hunk as an open-source local terminal diff/review viewer for human inspection of agent-authored or human-authored changesets.
- Keep its canonical role distinct from autonomous AI pull-request reviewers such as CodeRabbit or Qodo; Hunk presents diffs, annotations, and review sessions rather than independently establishing review correctness.
- Preserve durable integration surfaces at a high level: Git, Jujutsu, Sapling, direct-file/patch review, pager/difftool use, watch mode, inline agent annotations, live local review sessions, and the Hunk review skill.
- Preserve useful legacy trust boundaries: review visibility does not replace tests/static/security analysis; agent annotations can be wrong; live agent/session control and local loopback services need sandbox/network review; global pager configuration and evolving command/session interfaces are operational concerns.
- Keep exact installation commands, release behavior, version-control edge cases, command inventory, and UI features source-backed when expanded.
- Render the standard `entity-relations` block from the validated current-entity relation projection.
- Include current Hunk site and repository.

## Validation

- Hunk is not described as an autonomous code-review agent.
- Agent integration is represented as an external-participant/review-session surface.
- The `entity-relations` block matches the validated current-entity relation projection and every rendered destination resolves to a canonical node.
