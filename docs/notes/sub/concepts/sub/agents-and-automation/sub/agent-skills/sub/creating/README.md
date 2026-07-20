# Creating Agent Skills

This tutorial teaches how to design, implement, test, and publish an Agent Skill. It assumes no previous experience with skills.

A good skill turns a repeatable way of working into a small, inspectable package. The goal is not to hide reasoning behind a large prompt. The goal is to make the workflow discoverable, predictable, maintainable, and safe.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Learning objectives

After completing this guide, you should be able to:

- decide whether a workflow should be a skill, prompt, tool, repository instruction, MCP server, or plugin;
- create a valid skill directory and `SKILL.md`;
- write discovery metadata that activates for the right tasks;
- separate core instructions from references, scripts, and assets;
- design approval gates and failure behavior;
- test discovery, activation, execution, and portability;
- version and publish a skill without surprising its users.

## 1. Decide whether a skill is the right abstraction

Create a skill when the same **procedure** should be reused across tasks or projects and loaded only when relevant.

Typical examples:

- diagnosing a difficult bug through a disciplined loop;
- preparing release notes from a defined source range;
- reviewing a pull request against repository standards;
- interviewing a user before producing a technical design;
- converting a recurring report into a consistent document.

Do not create a skill merely because a prompt is long.

| Need | Better fit |
|---|---|
| One-off instruction for the current conversation | Prompt |
| Facts and conventions that should always apply in one repository | Repository instructions such as `AGENTS.md` or `CLAUDE.md` |
| Deterministic operation the model must execute | Tool or script |
| Standard connection to external tools, resources, or prompts | MCP server |
| Installable platform-specific bundle containing skills and integrations | Plugin |
| Reusable procedure selected only for relevant tasks | Agent Skill |

A skill can call tools, read repository instructions, use MCP capabilities, and be distributed inside a plugin. These concepts complement one another.

## 2. Define the behavioral contract before writing files

Write a short design note with these fields:

```text
Name:
User problem:
Use when:
Do not use when:
Required inputs:
Expected outputs:
Available tools:
Side effects:
Approval points:
Failure behavior:
Success criteria:
```

Example:

```text
Name: release-notes
User problem: Maintainers need consistent, evidence-backed release notes.
Use when: Preparing a release, changelog, or summary of merged changes.
Do not use when: Writing marketing copy without a known change range.
Required inputs: Base and head revisions or a list of merged changes.
Expected outputs: Categorized Markdown release notes with source references.
Available tools: Git history and pull-request reader.
Side effects: None by default.
Approval points: Ask before publishing or creating a release.
Failure behavior: Stop when the release range cannot be established.
Success criteria: Every claim maps to an included change.
```

This contract prevents the skill from becoming an unbounded “do everything” instruction.

## 3. Create the minimum directory

A portable skill starts with one directory containing `SKILL.md`:

```text
release-notes/
└── SKILL.md
```

Use a lowercase name with single hyphens:

```text
release-notes       # good
ReleaseNotes        # avoid
release_notes       # avoid
release--notes      # avoid
```

The open format requires the directory entrypoint to be named exactly `SKILL.md`.

## 4. Write valid frontmatter

Start `SKILL.md` with YAML frontmatter:

```markdown
---
name: release-notes
description: Draft evidence-backed release notes from a known revision range or set of merged changes. Use when preparing a software release, changelog, or stakeholder change summary.
---
```

The required fields are:

- `name` — stable machine-readable identifier;
- `description` — discovery text explaining both what the skill does and when to select it.

The standard also defines optional fields:

```yaml
license: MIT
compatibility: Requires Git history or pull-request access.
metadata:
  author: example-team
  version: "1.0.0"
  category: release-management
```

Some clients recognize additional fields. Keep client-specific extensions optional and document what happens when another client ignores them.

### Write a discovery-quality description

A weak description describes only the output:

```yaml
description: Creates release notes.
```

A stronger description contains:

1. the task;
2. the qualifying context;
3. useful trigger language;
4. important exclusions when ambiguity is likely.

```yaml
description: Draft evidence-backed release notes from Git commits or merged pull requests. Use for release preparation, changelog generation, or stakeholder summaries when a concrete change range is available; do not use for speculative product marketing.
```

Do not put the entire workflow in the description. Discovery metadata should remain compact enough to appear in a skill catalog.

## 5. Write the instruction body

A beginner-friendly skill body normally contains:

```markdown
# Release notes workflow

## When to use

## Required inputs

## Workflow

## Output format

## Approval and safety rules

## Failure handling

## References
```

Prefer imperative, testable steps:

```markdown
## Workflow

1. Establish the exact base and head revisions.
2. Enumerate changes inside that range.
3. Exclude merges, formatting-only changes, and internal refactors unless they affect users.
4. Group retained changes by user impact.
5. Identify breaking changes and migrations explicitly.
6. Attach a source commit or pull request to every non-trivial claim.
7. Present the draft for review; do not publish it without explicit approval.
```

Avoid vague language such as “make it good,” “use best practices,” or “handle errors appropriately.” State the observable behavior.

## 6. Keep the entrypoint focused

The whole `SKILL.md` is loaded when the skill activates. Large background references should not consume context on every invocation.

Use this structure as complexity grows:

```text
release-notes/
├── SKILL.md
├── references/
│   ├── categories.md
│   └── style-guide.md
├── scripts/
│   └── collect-changes.py
└── assets/
    └── release-template.md
```

### `references/`

Use references for material the model should read only in specific situations:

- domain terminology;
- long classification rules;
- provider-specific instructions;
- examples and edge cases;
- API or file-format details.

Link references explicitly from `SKILL.md`:

```markdown
When classifying a change, read [`references/categories.md`](./references/categories.md).
```

### `scripts/`

Use scripts for deterministic or repeatedly error-prone operations:

- parsing logs;
- collecting Git history;
- validating schemas;
- checking links;
- generating a fixed report structure.

A script should:

- declare its runtime and dependencies;
- validate input;
- produce machine-readable or clearly delimited output;
- return a non-zero exit status on failure;
- avoid hidden network access or destructive defaults;
- support a dry-run mode for consequential changes where practical.

### `assets/`

Use assets for files copied or adapted into output:

- document templates;
- configuration skeletons;
- sample datasets;
- diagrams or images;
- style resources.

Assets are output resources, not instructions. Put behavioral guidance in `SKILL.md` or `references/`.

## 7. Example A: a minimal skill

Directory:

```text
friendly-release-notes/
└── SKILL.md
```

Complete `SKILL.md`:

```markdown
---
name: friendly-release-notes
description: Turn a supplied list of completed changes into concise, user-facing Markdown release notes. Use when the user provides a concrete release scope and wants readable notes; do not invent changes or publish automatically.
license: MIT
---

# Friendly release notes

## Required input

Obtain a concrete list of completed changes. If no reliable source is available, stop and ask for one.

## Workflow

1. Remove duplicates and implementation-only details that do not affect users.
2. Group changes under `Added`, `Changed`, `Fixed`, and `Deprecated` only when those groups contain content.
3. Rewrite each item in plain language while preserving technical accuracy.
4. Mark breaking changes with **Breaking** and include the required migration action.
5. Do not invent benefits, dates, issue numbers, or compatibility claims.

## Output

Return Markdown with a one-sentence summary followed by grouped bullets.

## Safety

Produce a draft only. Publishing, tagging, or creating a release requires explicit approval.
```

This skill is useful without tools. In a tool-enabled client it can be extended to gather the change list automatically, but that capability is not assumed.

## 8. Example B: a skill with references

Directory:

```text
sfcc-log-analyzer/
├── SKILL.md
└── references/
    └── error-classification.md
```

`SKILL.md`:

```markdown
---
name: sfcc-log-analyzer
description: Deduplicate Salesforce Commerce Cloud production errors, count occurrences, preserve representative stack traces, and rank investigation priority. Use when analyzing SFCC log exports or repeated application exceptions.
compatibility: Requires readable text logs; optional shell or scripting access improves large-file processing.
---

# SFCC log analysis

## Workflow

1. Preserve the original log as read-only evidence.
2. Normalize volatile request IDs, timestamps, and thread identifiers without removing class names, messages, controller routes, or stack frames.
3. Group records only when the normalized error signature and relevant stack root match.
4. Count all occurrences and retain one representative full stack trace.
5. Classify each group using [`references/error-classification.md`](./references/error-classification.md).
6. Rank by impact, frequency, reproducibility, and confidence.
7. Separate confirmed causes from hypotheses.

## Output

For every group provide signature, count, priority, representative stack trace, likely owner, evidence, and next diagnostic action.

## Safety

Redact credentials, tokens, personal data, session IDs, and customer payloads before reproducing log content.
```

`references/error-classification.md`:

```markdown
# Error classification

## Priority 1

Security exposure, checkout failure, data corruption, widespread authentication failure, or an exception blocking a critical customer journey.

## Priority 2

Repeated functional failure with a workaround, significant operational noise, or a defect affecting a limited segment.

## Priority 3

Low-frequency issue, recoverable integration failure, or warning without demonstrated user impact.

## Confidence

- Confirmed: directly supported by stack trace and surrounding evidence.
- Probable: multiple signals support one explanation but reproduction is missing.
- Unknown: evidence is insufficient; state the next observation required.
```

The classification document can evolve without making the activation instructions unnecessarily large.

## 9. Example C: a skill with a script

Directory:

```text
repository-link-checker/
├── SKILL.md
└── scripts/
    └── check-links.py
```

`SKILL.md`:

```markdown
---
name: repository-link-checker
description: Validate relative Markdown links in a documentation tree and report missing targets without modifying files. Use before documentation commits or pull requests.
compatibility: Requires Python 3.10 or newer.
---

# Repository link checker

1. Determine the documentation root.
2. Run `python3 scripts/check-links.py <root>`.
3. Treat non-zero exit status as a failed validation.
4. Report each broken source path, link target, and line number.
5. Do not rewrite links automatically unless the user explicitly requests fixes.
6. After fixes, rerun the checker and report the final count.
```

Simplified `scripts/check-links.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check-links.py <documentation-root>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    failures = 0
    for source in root.rglob("*.md"):
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for raw_target in LINK.findall(line):
                target = raw_target.split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (source.parent / target).resolve()
                if not resolved.exists():
                    failures += 1
                    print(f"{source}:{line_number}: missing {raw_target}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

The script performs deterministic checking. The skill provides judgment about scope, remediation, and reporting.

## 10. Design tool use and approvals

A skill never grants a tool by itself. Document required capabilities and handle their absence explicitly.

For each side effect, define:

- the operation;
- the data and system affected;
- whether it is reversible;
- the approval required;
- the verification after execution.

Example:

```markdown
Before creating a Git tag:

1. Show the exact tag name, target commit, and release notes.
2. Wait for explicit approval.
3. Create the tag only on the approved target.
4. Read the tag back and verify its commit.
```

Do not bury approval requirements at the end of a long document.

## 11. User-invoked and model-invoked behavior

The open specification does not require a universal invocation-mode field. Clients and collections may add conventions such as:

- explicit slash-command orchestration skills;
- automatically selected discipline skills;
- fields that disable model invocation;
- platform UI metadata.

Design broad interview or orchestration workflows for explicit invocation when automatic activation would be disruptive. Design narrow, clearly triggered disciplines for automatic discovery.

Keep the portable workflow valid even when a client ignores invocation-specific extensions.

## 12. Add client metadata only when needed

Some clients or plugin systems support additional files, for example an `agents/openai.yaml` presentation definition or plugin manifests.

Treat these files as adapters around the portable skill:

```text
release-notes/
├── SKILL.md
└── agents/
    └── openai.yaml
```

Do not move essential workflow rules exclusively into a client-specific file. Another Agent Skills client may never read it.

## 13. Test the skill

Test four layers separately.

### Structural validation

Verify:

- the directory and `name` match;
- `SKILL.md` uses exact capitalization;
- YAML parses;
- required fields exist;
- referenced paths exist;
- scripts run in a clean environment;
- licenses and dependencies are documented.

### Discovery tests

Write positive prompts that should expose or select the skill:

```text
Prepare user-facing release notes for commits v2.3.0..HEAD.
```

Write nearby negative prompts:

```text
Write a launch announcement for a feature that has not shipped yet.
```

The skill should match the first and not claim the second.

### Execution tests

Use representative fixtures and check observable invariants:

- required questions are asked;
- steps occur in the expected order;
- evidence is preserved;
- dangerous actions stop for approval;
- output follows the promised schema;
- failures do not silently produce partial success.

### Cross-client tests

When portability matters, run the same fixtures in every supported client. Record differences in:

- discovery;
- invocation syntax;
- path resolution;
- script execution;
- permissions;
- unsupported metadata;
- context or output limits.

## 14. Review common failure modes

### The description is too broad

Symptom: the skill activates for unrelated requests.

Fix: add qualifying context, narrow the task, and move broad orchestration to explicit invocation.

### The description is too vague

Symptom: the skill is never discovered.

Fix: include concrete tasks and language users naturally use.

### `SKILL.md` contains an entire handbook

Symptom: activation consumes excessive context and the model misses the operational steps.

Fix: keep the workflow in the entrypoint and move background material to `references/`.

### The skill assumes unavailable tools

Symptom: it fabricates tool results or stalls.

Fix: declare compatibility, detect capability availability, and define a conversational fallback or explicit stop condition.

### Scripts hide consequential behavior

Symptom: a short instruction launches opaque writes or network calls.

Fix: document inputs, outputs, dependencies, side effects, dry-run behavior, and approval gates.

### The happy path is tested but failure is not

Symptom: missing inputs or partial tool failures produce plausible but incorrect output.

Fix: test absent files, malformed data, denied permissions, network failures, and interrupted execution.

## 15. Version and publish

For a published skill:

1. choose a stable source repository;
2. include a license;
3. document supported clients and runtime dependencies;
4. tag releases or record immutable revisions;
5. maintain a changelog for behavioral changes;
6. treat instruction changes as code changes requiring review;
7. test upgrades from the previous published version;
8. avoid silently expanding permissions or network access.

A collection may be distributed by direct copy, an installer such as `skills.sh`, or a platform-specific plugin. See [Sources and collections](../sources/) and [Plugins](../../../plugins/).

## Creation checklist

- [ ] The problem is procedural and recurring.
- [ ] Use and non-use conditions are explicit.
- [ ] Inputs, outputs, tools, side effects, approvals, and failures are defined.
- [ ] `name` and directory match.
- [ ] `description` passes positive and negative discovery tests.
- [ ] The entrypoint is focused.
- [ ] References, scripts, and assets have clear roles.
- [ ] Scripts validate input and fail visibly.
- [ ] Consequential actions require explicit approval.
- [ ] Structural, discovery, execution, failure, and cross-client tests pass.
- [ ] License, compatibility, source revision, and update policy are documented.

## References

- Agent Skills specification: https://agentskills.io/specification
- Skill creation overview: https://agentskills.io/skill-creation
- Optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Using Agent Skills: ../using/
- Platform support: ../platform-support/
