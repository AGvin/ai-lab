# Using Agent Skills

This guide explains how to adopt an existing Agent Skill safely, verify that it is available, invoke it, and maintain it over time.

## Before installation

1. Confirm that the target client supports Agent Skills or the collection's plugin format.
2. Read the skill's `SKILL.md` and any bundled scripts.
3. Check its license, maintenance status, compatibility requirements, and update mechanism.
4. Identify every tool, credential, network destination, and writable path it may use.
5. Decide whether the skill should be project-local or user-global.

Use a project-local installation when the workflow belongs to one repository and should be reviewed with the code. Use a user-global installation for personal workflows that are safe and useful across unrelated projects.

## Installation models

### Copy a skill directory

The most portable installation is to copy one complete skill directory into a location scanned by the client:

```text
<client-skill-root>/release-notes/
├── SKILL.md
├── references/
└── scripts/
```

Do not copy only `SKILL.md` when it references supporting files.

### Use an installer

Community installers such as `skills.sh` can copy selected skills into supported clients:

```bash
npx skills@latest add owner/repository
```

An installer reduces manual path work but does not make the source trustworthy. Review the selected version and resulting files before granting broad permissions.

### Install a plugin

Some products distribute collections as managed plugins. A plugin may provide skills together with hooks, agents, MCP servers, or configuration. Plugin commands are platform-specific; see [Using Plugins](../../../plugins/sub/using/).

## Explicit and automatic invocation

### Explicit invocation

Use the platform's command, mention, or skill picker when you need a specific workflow:

```text
/grill-me
```

```text
Use the diagnosing-bugs skill for this failure.
```

Explicit invocation is preferable when:

- the task is high impact;
- several skills could plausibly match;
- you need a user-invoked orchestration flow;
- you are testing a new skill;
- automatic discovery is unreliable.

### Automatic invocation

A client may select a skill automatically when the task matches its description. A good test prompt should express the real task rather than naming the skill:

```text
Investigate why this test fails intermittently. Reproduce it, isolate the cause, and add a regression test before changing production code.
```

If the diagnostic skill activates correctly, the response should follow its defined process rather than immediately guessing at a fix.

## Confirming activation

Clients expose activation differently. Use one or more of these checks:

- inspect the UI for an active skill indicator;
- ask the client which skill instructions it loaded;
- verify that the expected workflow steps appear;
- inspect logs or tool calls where the client exposes them;
- temporarily add an unmistakable but harmless test instruction;
- disable the skill and compare behavior.

Do not rely only on the final answer sounding similar. Test observable workflow requirements.

## Combining skills

Skills can compose when responsibilities remain clear. A practical engineering flow might use:

1. `grill-with-docs` to resolve requirements and terminology;
2. `to-spec` to capture the agreed design;
3. `tdd` during implementation;
4. `code-review` before commit.

Avoid activating several skills that each claim ownership of the same stage. Conflicting instructions increase context use and make behavior harder to audit.

## Updating

Choose one update model:

- **Managed subscription** — the plugin or marketplace updates the installed package.
- **Pinned copy** — keep a reviewed version in the repository and update through normal code review.
- **Forked copy** — maintain local adaptations and periodically reconcile upstream changes.

For consequential workflows, record the source repository and revision. Review diffs before updating because a Markdown-only change can still alter commands, permissions, or data handling.

## Removing or disabling

Depending on the client, remove the skill directory, uninstall its plugin, disable it in the Skills UI, or deny access through the client's skill permission rules.

After removal:

- restart or reload the client when required;
- confirm the skill no longer appears in discovery metadata;
- remove hooks or MCP configuration installed by a plugin;
- revoke credentials that were created only for the skill.

## Troubleshooting

### The skill is not discovered

Check:

- directory location;
- exact uppercase filename `SKILL.md`;
- valid YAML frontmatter;
- required `name` and `description` fields;
- directory name matching the skill name;
- client permissions and disabled patterns;
- whether a restart or plugin reload is required.

### The skill does not activate automatically

Improve the description so it includes concrete tasks and trigger phrases. Test both positive prompts that should activate it and nearby negative prompts that should not.

### The skill activates too often

Narrow the description. State the qualifying condition and exclude adjacent tasks in the body. Use explicit invocation for broad orchestration skills.

### A script fails

Verify the runtime, working directory, executable permission, dependency versions, environment variables, and network access. The skill should fail with a clear message rather than silently continuing with partial results.

### Different clients behave differently

The open format does not standardize every client behavior. Compare installation paths, supported frontmatter extensions, tool names, permission models, and invocation syntax in [Platform support](../platform-support/).

## Safe adoption checklist

- [ ] Source and revision recorded.
- [ ] `SKILL.md` reviewed.
- [ ] Scripts and dependencies reviewed.
- [ ] Required permissions minimized.
- [ ] Positive activation test passes.
- [ ] Negative activation test passes.
- [ ] Failure and rollback behavior tested.
- [ ] Update policy selected.

## References

- Agent Skills specification: https://agentskills.io/specification
- Optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Platform support: ../platform-support/
- Sources and collections: ../sources/
