# Agent Skills Sources and Collections

Legacy residual for Agent Skills source material that has not yet been fully assigned to the final documentation structure. Generic source-trust/adoption guidance, collection facts, workflow examples, and collection-selection guidance have moved to existing canonical learning/catalog owners.

> **Migration note:** This legacy page is intentionally fragmentary during the active consolidation. The former `Agent Skills standard` section was removed after its useful specification and portability content was verified in the existing [Agent Skills](../../) owner. The remaining `skills.sh` block stays here because no approved existing canonical destination has been verified yet.

Last verified: 2026-07-19.

## Translations

- English
- [Українська](./l10n/uk_UA/)

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

- skills.sh: https://skills.sh/
- skills.sh CLI: https://www.skills.sh/docs/cli
