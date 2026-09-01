# Documentation Template Registry

Repository-owned semantic template registry for AI Lab reader-facing documentation.

## Canonical Location

```text
docs/.meta/templates/
```

This is AI Lab's single active template registry. Template IDs are derived from paths relative to their registry group and omit `.md`; for example, `pages/catalog/models/reference/model.md` has page-template ID `catalog/models/reference/model`.

## Design Principle

Templates are selected by reader job and semantic ownership, not by physical folder depth. Reuse a shared page family when representative nodes have the same reader goal and information hierarchy; specialize only when the page owns materially different information or decision behavior.

The registry uses a hybrid composition model:

- **layouts** wrap the page body;
- **partials** own repeated structural composition without domain semantics;
- **components** own reusable semantic blocks with explicit inputs;
- **page templates** own reader journey, section order, domain-specific boundaries, and page-level semantic responsibility.

Do not create a component merely to avoid a few repeated headings. Domain-specific sections such as scope boundaries, capabilities, installation/access, lineage, or collection descriptions remain page-template composition unless a stable reusable semantic contract is demonstrated.

## Semantic Contract Format

Every page template documents the same decision contract so a maintainer or AI renderer can select it without relying on repository history:

- **Purpose** — the reader job the page serves;
- **Use when** — node roles that should select the template;
- **Do not use when** — nearby cases owned by another family;
- **Owns** — information the page may present as its responsibility;
- **Does not own** — information delegated to another canonical owner;
- **Expected inputs** — requirement-approved information needed to compose the page;
- **Composition** — intended section order and reusable primitives;
- **Variants** — differences allowed without creating another template;
- **Representative examples** — concrete AI Lab nodes that exercise the family;
- **Anti-patterns** — common misuse the template must prevent.

These labels describe semantic requirements; they do not create new runtime fields. Reader-facing wording must still be authorized by validated applicable requirements and supported canonical inputs.

## Reader-Experience Gate

Evaluate each family from several reader perspectives before treating representative renders as complete:

- a general reader arriving from search should quickly understand what the subject is and whether the page is relevant;
- a developer should be able to reach practical technical details and canonical resources without reading unrelated background;
- an AI specialist should find precise identity, provenance, capability, version, artifact, and ownership boundaries;
- UX and information-architecture review should prioritize orientation, scanability, progressive disclosure, navigation continuity, and low cognitive load;
- SEO/discoverability review should use clear titles, natural introductory wording, recognizable terminology, descriptive internal links, and accurate headings without keyword stuffing or weakened technical precision.

Internal metadata vocabulary remains an authoring/rendering concern. Reader-facing pages should expose it only when the concept itself is useful to the reader.

## Registry Structure

```text
docs/.meta/templates/
├── README.md
├── layouts/
│   └── default.md
├── partials/
│   └── default/
│       ├── header.md
│       └── footer.md
├── components/
│   ├── translations.md
│   ├── child-navigation.md
│   ├── official-resources.md
│   ├── entity-relations.md
│   └── discovery-resources.md
└── pages/
    └── catalog/
        ├── landing.md
        ├── domain.md
        ├── category.md
        ├── child-index.md
        ├── alphabetical-index.md
        ├── producers/
        │   └── profile.md
        ├── models/
        │   ├── landing.md
        │   ├── reference/
        │   │   ├── landing.md
        │   │   ├── producer.md
        │   │   ├── family.md
        │   │   ├── series.md
        │   │   ├── model.md
        │   │   ├── version.md
        │   │   └── artifact.md
        │   └── selection/
        │       ├── landing.md
        │       ├── guide.md
        │       ├── user-scenarios/
        │       │   ├── index.md
        │       │   └── scenario.md
        │       └── hardware/
        │           ├── index.md
        │           └── target.md
        ├── agent-skills/
        │   ├── collection.md
        │   └── registry.md
        ├── integrations/
        │   └── integration.md
        ├── services/
        │   └── service.md
        └── software/
            └── software.md
```

Concrete canonical dataset and hardware **profile** templates remain deferred until representative concrete catalog entities justify them. `catalog/models/selection/hardware/*` is not a canonical hardware-profile family; it is model-specific decision support for a fixed hardware target.

## Shared Page Families

- `catalog/landing` — canonical catalog orientation across entity domains.
- `catalog/domain` — one canonical domain's ownership boundary and primary navigation.
- `catalog/category` — conceptual grouping inside a domain, independent of physical depth.
- `catalog/child-index` — typed navigation such as models, versions, or artifacts under a parent identity.
- `catalog/alphabetical-index` — lookup-oriented alphabetical partition, such as `Producers — N`.

## Specialized Page Families

Specialized families exist only where reader goals or ownership differ materially: canonical producer profiles; model reference producer/family/series/model/version/artifact identities; task/portfolio model-selection decision support; combined-context model user scenarios; hardware-constrained model selection; Agent Skill collections and registries; product-specific integrations; hosted services; and installable/self-managed software.

The three model-selection template families remain siblings under the same semantic owner:

- `catalog/models/selection/guide` — task/need/portfolio or model-first bounded decisions;
- `catalog/models/selection/user-scenarios/*` — combined-context reader situations;
- `catalog/models/selection/hardware/*` — device-first model selection for owned/fixed compute.

## Output Boundary

A render is constrained by validated global context, effective node metadata, validated current-node entity data, applicable requirements, selected registry definitions, and explicit authored fragments when used. Templates must not scrape reader-facing facts from an existing `README.md`, infer presentation solely from entity-field presence, or invent undocumented children, relations, claims, recommendations, or resources.

The complete `README.md` remains renderer-owned. Durable corrections belong in canonical inputs or template definitions and are applied through the normal validation/render/check workflow when executable support is available. A target-specific migration-phase render deferral may temporarily postpone that workflow without transferring README ownership.

## Selection Boundary

Template definitions and `node.template` selectors are separate canonical inputs. A bounded migration may introduce or update both together when the semantic contract and representative nodes are reviewed in the same package. Changing a template definition does not by itself authorize unrelated selector migration, generated README edits, or broader taxonomy materialization.
