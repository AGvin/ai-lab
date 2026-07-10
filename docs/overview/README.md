# Overview

Practical AI lab for models, tools, local inference, benchmarks, hardware notes, and automation workflows.

## Documentation Layout

Use `docs/` as the repository-level documentation container.

Use `sub/` for child documentation nodes inside a named documentation node.

Do not create `docs/README.md`.

## Documentation Nodes

- [`docs/software/`](../software/) — AI-related software, inference tools, workflow engines, development workflows, code editors, agents, assistants, automation tools, platforms, and models.
- [`docs/notes/`](../notes/) — concepts, benchmarks, comparisons, and practical AI notes.

## Current Software Areas

- [`inference/`](../software/sub/inference/) — local and self-hosted model execution.
- [`workflow-engines/`](../software/sub/workflow-engines/) — AI workflow engines and UIs.
- [`development-workflows/`](../software/sub/development-workflows/) — tools that structure AI-assisted software delivery through durable specifications, plans, tasks, validation, and implementation stages.
- [`code-editors/`](../software/sub/code-editors/) — code editors and editor extension ecosystems.
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

Use `assets/` inside a documentation node for supporting files used by that node.

Prefer typed subdirectories:

```text
assets/
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
docs/software/sub/code-editors/sub/vs-code/
  README.md
  assets/
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

- Store assets next to the documentation node that uses them.
- Use typed asset folders instead of placing files directly in `assets/`.
- Use `files/` for rare or miscellaneous file types instead of creating one-off folders.
- Create only folders that contain real files.
- Use shared parent-level assets only when the same file is reused by multiple child pages.

## Expansion Rules

Create new documentation nodes only when real content exists.

Create `assets/` and typed asset subdirectories only when a documentation node has real supporting files.

Use `assets/files/` for uncommon supporting file types that do not justify a dedicated typed folder.

Use one canonical page per product, model, platform, assistant, agent, editor, extension, or tool. Add child nodes only when a specific usage scenario has enough content to justify a separate page.
