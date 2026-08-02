# Documentation Metadata Registry

This directory contains canonical defaults and JSON Schemas for AI Lab documentation metadata.

## Files

- `defaults.yml` — canonical pre-root metadata baseline;
- `schemas/root.schema.json` — repository-root metadata;
- `schemas/default.schema.json` — common metadata definitions and default node contract;
- `schemas/localized.schema.json` — localized source-hash metadata;
- specialized schemas — catalog index, item, collection, and producer contracts.

## Inheritance Boundary

Schema, template, layout, template parameters, and `children` baselines are ordinary inheritable metadata.

Canonical entity-instance data is current-node-only and must be declared under `node.local`:

- `entity`;
- `relations`;
- `resources`;
- `dependencies`;
- `facts`.

The resolver overlays these values into the current effective node for rendering and repository indexing, then discards them before initializing descendants. This prevents an entity ID, producer relation, resource list, dependency set, or fact block from leaking into child pages.

`node.local.favorites` follows the same current-node-only boundary.
