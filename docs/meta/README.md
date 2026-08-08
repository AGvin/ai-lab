# Documentation Metadata Registry

This directory contains canonical defaults and JSON Schemas for AI Lab documentation metadata.

## Files

- `defaults.yml` — canonical pre-root metadata baseline;
- `schemas/root.schema.json` — repository-root metadata;
- `schemas/default.schema.json` — common metadata definitions and default node contract;
- `schemas/localized.schema.json` — localized source-hash metadata;
- specialized schemas — catalog index, item, collection, and producer contracts.

## Requirements Document

`docs/meta/defaults.yml` defines the inherited requirements-document location:

```yaml
node:
  requirements:
    path: requirements/README.md
```

The effective `node.requirements.path` is resolved relative to each documentation node directory. A nearer `meta.yml` may override the inherited path when a node intentionally uses a different location.

The configured path is a discovery location, not a declaration that the file must exist. If the file is absent, the node has no local requirements document and processing continues with any requirements inherited from ancestors.

Requirements-related assets may be stored under `requirements/assets/` and referenced directly by the requirement that uses them. They do not require a separate asset inventory section.

## Inheritance Boundary

Schema, requirements-document path, template, layout, template parameters, and `children` baselines are ordinary inheritable metadata.

Canonical entity-instance data is current-node-only and must be declared under `node.local`:

- `entity`;
- `relations`;
- `resources`;
- `dependencies`;
- `facts`.

The resolver overlays these values into the current effective node for rendering and repository indexing, then discards them before initializing descendants. This prevents an entity ID, producer relation, resource list, dependency set, or fact block from leaking into child pages.

`node.local.favorites` follows the same current-node-only boundary.
