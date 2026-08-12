# Documentation Requirements

## Requirements

- Explain the current documentation architecture without reproducing the exhaustive physical tree.
- State that repository `README.md` is the concise landing page, `project/navigation/catalog/` is curated descriptive discovery, and `project/navigation/tree/` is the exhaustive implemented hierarchy.
- Describe `docs/` as the documentation container and `sub/` as the child-node container used by the canonical node structure.
- Describe the two currently materialized top-level domains: `catalog/` for documented entities and decision-support catalogs, and `project/` for repository-owned navigation, policies, and overview material.
- Preserve the useful legacy asset rule: reader-facing assets stay beside the documentation node that consumes them; default-locale assets use `assets/default/`, localized variants use `assets/<locale-id>/` only when materially different, and control/processing assets belong under `.meta/assets/` rather than reader-facing asset directories.
- Preserve typed reader-facing asset categories such as `images/`, `screenshots/`, `diagrams/`, `pdf/`, `samples/`, `exports/`, and `files/`, creating only categories that contain real files.
- Preserve the no-placeholder expansion principle: create documentation nodes and asset directories only when real reviewed content or real supporting files justify them.
- State that one canonical owner should exist for each documented entity or concept; child nodes are added when the narrower subject has enough distinct content to justify independent ownership.
- Link readers to the curated Documentation Catalog and exhaustive Documentation Tree instead of embedding large duplicated navigation maps.

## Validation

- The overview reflects the current `catalog/` + `project/` architecture rather than the superseded `software/` + `notes/` legacy layout.
- It does not duplicate the exhaustive Documentation Tree.
- Legacy asset guidance is retained only where compatible with the current documentation-node contract.
- No obsolete `docs/sub/software/sub/models/` or legacy model-selection ownership is presented as canonical.
