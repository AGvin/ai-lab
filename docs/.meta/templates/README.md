# Documentation Template Registry

Repository-owned template registry for AI Lab documentation rendering and reconciliation.

## Canonical Location

```text
docs/.meta/templates/
```

This is the repository's single active template registry. Do not create a synchronized registry under `docs/templates/`, `assets/documentation-templates/`, or node-local `.meta/` directories.

## Current Registry

```text
docs/.meta/templates/
├── README.md
├── layouts/
│   ├── default.md
│   └── empty.md
├── partials/
│   └── default/
│       ├── header.md
│       └── footer.md
└── components/
    ├── favorites.md
    ├── page-intro.md
    └── translations.md
```

Create `pages/`, `modifiers/`, or additional component groups only when reviewed definitions exist.

## Output Boundary

Reader output is derived conceptually from validated global context, effective node metadata, the current node's `.meta/entity.yml`, the current node's `.meta/requirements.md`, and explicitly selected registry definitions.

Templates must not infer reader-facing requirements from entity-field presence or scrape stable values from an existing `README.md`.

Do not assume:

```text
entity.name -> page title
entity.references -> rendered links
entity.relations -> rendered relation sections
```

Do not use `content`, `source`, `source.title`, `source.summary`, `source-body`, stable entity data in `node.local`, or another obsolete runtime representation.

## Current Definition Scope

The current registry contains only baseline definitions already compatible with the common documentation-template contract:

- `layouts/default` — renders the page-template body and shared footer without inferring title or summary;
- `layouts/empty` — pass-through page body;
- `partials/default/header` — receives explicit reader-facing title and optional summary and invokes translations;
- `partials/default/footer` — no-output shared extension point;
- `components/page-intro` — explicit page title and optional summary;
- `components/translations` — locale-variant navigation;
- `components/favorites` — approved favorite-node discovery and composition.

AI Lab page templates are intentionally not materialized yet. The requirements-to-output projection, authored-versus-generated ownership, repository indexes used by generated navigation/relation views, and representative specialized entity schemas remain design gates. A documentation node must not select an unresolved page-template ID.

## Validation Boundary

- only page templates may be selected through `node.template`;
- layouts, partials, and components must resolve inside this registry;
- components receive only explicit attributes and slots;
- entity fields render only when current-page requirements authorize the output;
- localized pages consume the composed default-locale result and do not independently select page templates;
- generated content must not replace useful authored content before equivalent output is verified.
