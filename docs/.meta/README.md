# Documentation Control Registry

This directory is the root documentation node's canonical control bundle and repository registry root.

## Files and Directories

- `defaults.yml` — canonical pre-root metadata baseline;
- `schemas/` — metadata and structured-content schemas;
- `templates/` — the repository's single active documentation template registry;
- `node.yml` — optional sparse root-node configuration;
- `content.yml` — optional structured content for the root page;
- `requirements.md` — optional root documentation requirements;
- `assets/` — optional assets referenced by root content or requirements.

Create optional files and directories only when they contain real configuration, content, requirements, or referenced assets.

## Node Bundle

Regular documentation nodes use:

```text
.meta/
├── node.yml
├── content.yml
├── requirements.md
└── assets/
```

- `node.yml` owns schema, template, layout, inheritance, localization, and processing configuration.
- `content.yml` owns stable current-node title, summary, identity, relations, resources, dependencies, facts, and structured section inputs.
- `requirements.md` owns sparse documentation-requirement deltas.
- `assets/` is optional and must not be created empty.

## Configured Paths

Canonical defaults declare node-scoped paths relative to each target node's `.meta/` directory:

```yaml
node:
  content:
    path: content.yml

  requirements:
    path: requirements.md
```

Inherited paths remain symbolic and are re-resolved for every target node.

## Ownership Boundary

Stable entity data must not be stored in `node.local`. That object is reserved for temporary current-node processing context such as an explicitly approved favorite marker.

Templates consume validated `content.*` values. They must not use implicit `source.title`, `source.summary`, or `source-body` extraction.
