# Agent Skills Sources and Collections

Legacy residual for Agent Skills source material that has not yet been fully assigned to the final documentation structure. Generic source-trust/adoption guidance, collection facts, workflow examples, and collection-selection guidance have moved to existing canonical learning/catalog owners.

Last verified: 2026-07-19.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Agent Skills standard

The portable specification is published at `agentskills.io`.

Use it as the canonical source for:

- the required directory and `SKILL.md` entrypoint;
- YAML frontmatter fields;
- naming and description constraints;
- progressive disclosure;
- optional `scripts/`, `references/`, and `assets/` directories;
- client implementation guidance;
- validation expectations.

A skill that follows the specification can be portable, but a client may still differ in installation paths, invocation syntax, permissions, optional metadata, and supported tools. See [Platform support](../platform-support/).

## skills.sh

Website and CLI: `skills.sh` and `vercel-labs/skills`

`skills.sh` is a discovery index, leaderboard, and installer for public Agent Skills repositories. A common command is:

```bash
npx skills@latest add owner/repository
```

The CLI discovers skill directories in the source and asks which clients should receive them.

Important operational notes:

- the CLI copies skills into selected client roots;
- copied skills can be edited locally;
- updates require another installation or a managed process;
- popularity is based partly on aggregated installation telemetry;
- telemetry can be disabled with `DISABLE_TELEMETRY=1`;
- registry presence and security scanning do not guarantee quality or safety.

Recommended use:

- discover public collections;
- install the same skill into several compatible clients;
- compare popularity and ecosystem adoption;
- bootstrap editable project-local copies.

For consequential workflows, pin a reviewed commit instead of blindly following the latest repository state.

## References

- Agent Skills: https://agentskills.io/
- skills.sh: https://skills.sh/
- skills.sh CLI: https://www.skills.sh/docs/cli
