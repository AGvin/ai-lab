# DOCX

> **Temporary catalog summary:** This short description is a placeholder for a future reviewed skill profile.

DOCX is an Anthropic document skill for creating, reading, editing, validating, redlining, commenting on, and visually checking Word documents.

## Collection

- [`Anthropic Skills`](../../../collections/sub/anthropic-skills/)

## Producer

- [`Anthropic`](../../../../../producers/sub/a/sub/anthropic/)

## Dependencies

- Required Agent Skills: none.
- Collection/setup requirement: selectively installable; the complete skill directory and bundled scripts must remain together.
- Runtime/tool dependencies: Node.js with `docx`, `pandoc`, LibreOffice, Poppler (`pdftoppm`), ZIP tools, and Python for bundled helpers; exact needs vary by operation.
- Bundled resources: office conversion and validation, XML run merging, comments, tracked-change acceptance, and related helpers.
- Used by: Word-document tasks; no selected catalog skill depends on it.

## Official resources

- [Official skill source](https://github.com/anthropics/skills/tree/main/skills/docx)
