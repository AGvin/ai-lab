# Code Review Tools

Non-agent tools for visualizing, navigating, inspecting, annotating, and reviewing code diffs and changesets in AI-assisted development workflows.

## Tools

- [`hunk/`](./sub/hunk/) — review-first terminal diff viewer for agent-authored and human-authored changesets.

## Scope

Use this node when the tool's primary role is presenting or supporting code review rather than independently acting as a review agent.

Keep agent-like review systems such as CodeRabbit and Qodo under [`agents/`](../../../agents/). Keep lifecycle tooling that defines specifications, plans, tasks, or quality gates under [`development-workflows/`](../development-workflows/).
