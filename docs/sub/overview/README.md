# Overview

Practical AI lab for models, tools, local inference, benchmarks, hardware notes, and automation workflows.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Documentation Layout

Use `docs/` as the repository-level documentation container.

Use `sub/` for child documentation nodes inside a named documentation node.

Do not create `docs/README.md`.

## Documentation Nodes

- [`docs/sub/software/`](../software/) — AI-related software, development tooling, inference tools, workflow engines, agents, assistants, automation tools, platforms, and models.
- [`docs/sub/notes/`](../notes/) — concepts, benchmarks, comparisons, and practical AI notes.

## Current Software Areas

- [`development/`](../software/sub/development/) — software used to create, structure, inspect, and review changes in AI-assisted development workflows.
  - [`code-editors/`](../software/sub/development/sub/code-editors/) — code editors and editor extension ecosystems.
  - [`development-workflows/`](../software/sub/development/sub/development-workflows/) — tools that structure AI-assisted software delivery through durable specifications, plans, tasks, validation, and implementation stages.
  - [`code-review-tools/`](../software/sub/development/sub/code-review-tools/) — non-agent tools for inspecting, navigating, annotating, and reviewing code changesets.
- [`inference/`](../software/sub/inference/) — local and self-hosted model execution.
- [`workflow-engines/`](../software/sub/workflow-engines/) — AI workflow engines and UIs.
- [`agents/`](../software/sub/agents/) — agent-like AI systems.
- [`agent-orchestration/`](../software/sub/agent-orchestration/) — systems, frameworks, runtimes, and control planes for coordinating or running AI agents.
- [`assistants/`](../software/sub/assistants/) — conversational AI assistants.
- [`automation/`](../software/sub/automation/) — automation tools relevant to AI-adjacent workflows.
- [`model-platforms/`](../software/sub/model-platforms/) — model, dataset, and AI tooling platforms.
- [`models/`](../software/sub/models/) — model families and individual AI models.

## Current Notes Areas

- [`concepts/`](../notes/sub/concepts/) — AI concept explanations.
- [`benchmarks/`](../notes/sub/benchmarks/) — benchmark and leaderboard references.
- [`comparisons/`](../notes/sub/comparisons/) — decision-support comparisons across models, tools, workflows, platforms, and AI systems.

## Assets

Store reader-facing assets next to the documentation node that uses them.

Default-locale source assets belong under `assets/default/`. Localized reader-facing variants belong under `assets/<locale-id>/` only when the asset materially differs by language or region. Keep processing and control inputs separate under `.meta/assets/`; those files are not reader-facing assets.

Prefer typed subdirectories inside each reader-facing locale directory:

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

Folder roles:

- `images/` — general images used by documentation.
- `screenshots/` — UI screenshots.
- `diagrams/` — diagrams, charts, schemas, and visual explanations.
- `pdf/` — PDF files.
- `samples/` — small sample inputs, configs, prompts, datasets, or examples.
- `exports/` — exported artifacts produced by tools or workflows.
- `files/` — other supporting files that do not fit the typed folders.

Example:

```text
docs/sub/software/sub/development/sub/code-editors/sub/vs-code/
  README.md
  assets/
    default/
      images/
        interface.png
      screenshots/
        extension-settings.png
      pdf/
        reference.pdf
      files/
        uncommon-reference-file.ext
```

Guidelines:

- Store default-locale reader-facing assets under `assets/default/`.
- Store a localized reader-facing asset under `assets/<locale-id>/` only when a language- or region-specific variant is needed.
- Use typed asset folders inside the applicable locale directory instead of placing files directly in `assets/`, `assets/default/`, or `assets/<locale-id>/`.
- Use `files/` for rare or miscellaneous file types instead of creating one-off folders.
- Keep `.meta/assets/` for control inputs referenced by canonical metadata or requirements, not for reader-facing files.
- Create only folders that contain real files.
- Use shared parent-level assets only when the same file is reused by multiple child pages.

## Expansion Rules

Create new documentation nodes only when real content exists.

Create reader-facing asset directories and typed subdirectories only when a documentation node has real supporting files.

Use `assets/default/files/` for uncommon default-locale supporting files that do not justify a dedicated typed folder. Use the corresponding `assets/<locale-id>/files/` path only for a materially localized variant.

Use one canonical page per product, model, platform, assistant, agent, editor, extension, or tool. Add child nodes only when a specific usage scenario has enough content to justify a separate page.
