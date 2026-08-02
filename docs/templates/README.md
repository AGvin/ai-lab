# Documentation Template Registry

This is the authoritative runtime registry for AI Lab documentation rendering.

The renderer produces Markdown. HTML-like tags are declarative template instructions, not HTML output.

## Groups

- `pages/` — page templates selectable through `node.template`;
- `layouts/` — outer page compositions;
- `partials/` — reusable composition fragments;
- `components/` — isolated parameterized renderable units.

## Language Boundary

Definitions use interpolation, layout selection, partial inclusion, component invocation, named slots, and approved declarative render primitives.

They do not use general-purpose loops, conditionals, mutation, or side effects. Components receive all node, relation, localization, and parameter values explicitly through attributes or slots.

The distributable copy under `assets/documentation-templates/` mirrors this registry and is not a second runtime registry.
