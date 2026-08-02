# Dependencies Component

## Description

Renders structured catalog, setup, runtime, tool, bundled-resource, optional, and reverse dependency data.

## Parameters

- `dependencies`: required dependency array;
- `entity-id`: optional current entity ID;
- `relationship-index`: optional repository relationship index;
- `title`: default `Dependencies`;
- `heading-level`: integer, default `2`;
- `classes`: optional dependency-class filter;
- `include-reverse`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-dependencies
  dependencies="{{ component.attributes.dependencies }}"
  entity-id="{{ component.attributes.entity-id }}"
  relationship-index="{{ component.attributes.relationship-index }}"
  title="{{ component.attributes.title | default: 'Dependencies' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  classes="{{ component.attributes.classes }}"
  include-reverse="{{ component.attributes.include-reverse | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
