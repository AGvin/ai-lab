# Hunk

Hunk is an open-source, review-first terminal diff viewer designed for interactively inspecting multi-file changesets, including changes authored by coding agents.

## Metadata

```text
Resource type: Terminal code-review and diff-viewing tool
Primary use case: Review agent-authored or human-authored changesets interactively before accepting, committing, or merging them
Access model: Open-source local CLI and terminal UI
Cost model: Free
License: MIT
Source model: Open source
Operational requirement: Node.js 18+ for npm installation; macOS, Linux, or Windows; Git recommended; optional Homebrew or Nix packaging
Integration modes: Git, Jujutsu, Sapling, direct file comparison, patch input, pager and difftool workflows, live agent-controlled review sessions, agent-context sidecars, and an embeddable OpenTUI component
Source: https://github.com/modem-dev/hunk
Risk notes: Hunk improves changeset visibility but does not establish correctness or security. Retain tests, static analysis, security review, and human approval. Live agent control uses a local loopback session service, so verify sandbox and local-network boundaries before granting an agent access.
Last verified: 2026-07-17
```

## Overview

Hunk renders a changeset as an interactive terminal review stream rather than plain diff text. It provides sidebar navigation across files, syntax highlighting, split and stacked layouts, keyboard and mouse controls, inline agent annotations, and watch mode for automatically refreshing active reviews.

Hunk is not itself a code-review agent. It presents changes and annotations for inspection, while analysis and review decisions remain with a human or an external agent.

## Core capabilities

- Review multi-file working-tree changes and commits in one navigable interface.
- Include untracked files in Hunk-managed Git working-tree reviews.
- Switch between split, stacked, and responsive automatic layouts.
- Reload Git-backed and direct-file reviews through watch mode.
- Display inline AI or agent notes beside the relevant diff location.
- Operate through keyboard, mouse, pager, and Git difftool workflows.
- Detect Git, Jujutsu, and Sapling workspaces and use their native revision syntax.
- Compare direct file pairs or render patches supplied through standard input.
- Expose the diff renderer as an OpenTUI component for other applications.

## Installation

Install the `hunkdiff` npm package globally:

```bash
npm install --global hunkdiff
```

The installed executable is `hunk`. Homebrew users can install the maintained formula:

```bash
brew install hunk
```

Nix users can use the package exported by the repository's `flake.nix`.

Verify the installation:

```bash
hunk --version
hunk
```

## Review workflows

### Git working tree and commits

```bash
hunk diff
hunk diff --watch
hunk show
hunk show HEAD~1
```

`hunk diff` reviews current repository changes and includes untracked files by default. `hunk show` reviews a commit, with the latest commit used when no revision is supplied.

### Direct files and patches

```bash
hunk diff before.ts after.ts
hunk diff before.ts after.ts --watch
git diff --no-color | hunk patch -
```

These modes are useful for reviewing generated outputs, exported patches, or files outside a normal Git changeset.

### Jujutsu and Sapling

Hunk auto-detects Jujutsu and Sapling workspaces. In those repositories, `hunk diff` and `hunk show` accept native revsets. The selected version-control backend can also be overridden in configuration.

## Agent-assisted review

Hunk can expose a running terminal review to an external coding agent:

1. Open `hunk diff` or `hunk show` in a user-controlled terminal.
2. Run `hunk skill path` and make the returned Hunk review skill available to the agent.
3. Ask the agent to inspect and control the live Hunk session through `hunk session` commands.

Typical non-interactive agent commands include:

```bash
hunk session list
hunk session get --repo .
hunk session review --repo . --json
hunk session navigate --repo . --file src/App.tsx --hunk 2
hunk session comment add --repo . --file src/App.tsx --new-line 42 --summary "Check this boundary condition"
```

The agent can inspect review structure, navigate the visible UI, reload its contents, and add inline notes. Raw patch inclusion is optional and should be requested only when the agent needs the full unified diff.

As an alternative to a live session, `--agent-context` can load prewritten agent annotations from a JSON sidecar file.

## Configuration

Hunk reads user-level or repository-level TOML configuration from:

```text
~/.config/hunk/config.toml
.hunk/config.toml
```

Configurable behavior includes theme, layout mode, version-control backend, watch mode, untracked-file handling, line numbers, wrapping, menu visibility, agent notes, and transparent terminal backgrounds.

Hunk can also be configured as the Git pager:

```bash
git config --global core.pager "hunk pager"
```

Using Hunk's own `hunk diff` command remains preferable when untracked-file inclusion is required, because Git itself controls what is sent to a pager.

## Strengths

- Provides a focused human review surface for large agent-generated changesets.
- Keeps navigation, syntax highlighting, and annotations inside the terminal workflow.
- Separates code generation from explicit review instead of automatically accepting agent changes.
- Supports several version-control systems and raw patch input.
- Allows an agent to guide a live review while the user retains control of the visible session.
- Can be adopted as an opt-in command without replacing the existing editor or coding agent.

## Trade-offs and limitations

- Hunk is a presentation and review tool, not a substitute for tests, linters, static analysis, or security scanning.
- Inline agent notes may still be incomplete, noisy, or incorrect and require human judgment.
- It does not provide structural diffing comparable to syntax-aware tools such as Difftastic.
- Live session control depends on a local loopback service that may be inaccessible from a restricted agent sandbox.
- Watch behavior differs by version-control backend; Jujutsu and Sapling reviews may rely on polling.
- Global pager configuration changes normal Git output behavior and should be tested before broad adoption.
- The project is evolving, so commands, packaging, and session interfaces should be checked against the installed release.

## Fit for AI Lab

Hunk belongs under `development/code-review-tools/` because its primary role is interactively presenting and annotating code changesets. Its agent integration allows an external agent to participate in review, but Hunk does not independently behave as a code-review agent.

Use this page as a reference for:

- human review of coding-agent changes;
- terminal-based diff and changeset navigation;
- agent annotations attached to exact diff locations;
- Git, Jujutsu, and Sapling review workflows;
- comparisons with Lumen, Difftastic, Delta, and other diff-viewing tools.

## References

- Repository and primary documentation: https://github.com/modem-dev/hunk
- Agent workflow guide: https://github.com/modem-dev/hunk/blob/main/docs/agent-workflows.md
- Hunk review skill: https://github.com/modem-dev/hunk/blob/main/skills/hunk-review/SKILL.md
- OpenTUI component guide: https://github.com/modem-dev/hunk/blob/main/docs/opentui-component.md
- License: https://github.com/modem-dev/hunk/blob/main/LICENSE
