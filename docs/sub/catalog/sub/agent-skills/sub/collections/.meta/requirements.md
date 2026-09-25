# Documentation Requirements

## Requirements

- Present this node as the canonical index of the currently selected Agent Skill collections.
- List each materialized direct child exactly once from the validated direct-child projection; do not maintain a second hand-written fixed inventory in this requirement.
- Describe each collection briefly enough to distinguish its producer, scope, or distribution role without duplicating its detailed selected-skill content.
- Treat each collection page as the canonical owner of collection identity, distribution context, and the selected collection-owned skills represented in AI Lab.
- Do not create or imply standalone skill nodes merely because the collection exposes separately addressable skill directories.
- Treat direct-child inventory as generated/navigation-sensitive state: when a collection is added or removed, update this index requirement in the same authored change package.

## Validation

- Navigation matches the validated materialized direct-child projection exactly, including Stripe Agent Skills and any later accepted collection additions.
- Every listed collection resolves to one canonical direct child and no materialized direct child is omitted.
- The index contains no temporary or RC placeholder wording.
- Detailed skill dependencies, runtime requirements, bundled resources, and source paths remain on the owning collection pages.
