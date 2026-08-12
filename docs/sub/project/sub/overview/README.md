# Overview

AI Lab's documentation separates reader-facing catalog content from repository-owned navigation, policies, and overview material.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Documentation architecture

The documentation lives under `docs/` and uses `sub/` for child documentation nodes.

Its currently materialized top-level domains are:

- [`catalog/`](../../catalog/) — documented entities, tools, services, software, models, and task-oriented catalog guidance;
- [`project/`](../..) — repository-owned navigation, policies, and overview material.

Navigation has three distinct responsibilities:

- [`README.md`](../../../../README.md) — concise repository landing page;
- [`navigation/catalog/`](../navigation/sub/catalog/) — curated descriptive discovery;
- [`navigation/tree/`](../navigation/sub/tree/) — exhaustive implemented hierarchy.

The overview does not duplicate the complete tree. Use the curated catalog to discover useful areas and the tree when the exact physical hierarchy matters.

## Documentation nodes

Each documentation node owns one coherent subject. Use one canonical owner for an entity or concept and add a child node only when the narrower subject has enough distinct reviewed content to justify independent ownership.

Do not pre-create empty taxonomy merely because a category might exist later. Materialize nodes when real content, evidence, or supporting files require them.

## Reader-facing assets

Keep reader-facing assets beside the documentation node that uses them.

Default-locale assets belong under `assets/default/`. Create a localized `assets/<locale-id>/` variant only when the asset materially differs for that locale. Processing or control assets referenced by canonical metadata belong under `.meta/assets/` instead of reader-facing asset directories.

Use typed directories when needed:

```text
assets/
  default/
    images/
    screenshots/
    diagrams/
    pdf/
    samples/
    exports/
    files/
  <locale-id>/
    images/
    screenshots/
    diagrams/
    pdf/
    samples/
    exports/
    files/
```

Create only directories that contain real files. Use `files/` for uncommon supporting files that do not justify a dedicated type.

## Expansion rule

Grow the documentation from actual reader value rather than an empty desired taxonomy. A new page should have a clear owner, real content or evidence, and a reason to exist independently of its parent.

For navigation, continue to the [Documentation Catalog](../navigation/sub/catalog/) or [Documentation Tree](../navigation/sub/tree/).
