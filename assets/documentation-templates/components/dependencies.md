# Dependencies Component

## Description

Renders structured catalog, setup, runtime, tool, bundled-resource, optional, and reverse dependency data.

## Parameters

- `title`: default `Dependencies`;
- `heading-level`: integer, default `2`;
- `classes`: optional dependency-class filter;
- `include-reverse`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<dependency-groups
  dependencies="{{ node.dependencies }}"
  classes="{{ parameters.classes }}"
  include-reverse="{{ parameters.include-reverse | default: false }}"
  title="{{ parameters.title | default: 'Dependencies' }}"
  heading-level="{{ parameters.heading-level | default: 2 }}"
  hide-when-empty="{{ parameters.hide-when-empty | default: true }}"/>
```
