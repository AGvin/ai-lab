# Entity Facts Component

## Description

Renders schema-approved structured facts as a Markdown definition list or table.

## Parameters

- `facts`: required facts object;
- `title`: default `Details`;
- `heading-level`: integer, default `2`;
- `groups`: optional fact-group filter;
- `fields`: optional field filter and order;
- `mode`: `definition-list` or `table`, default `definition-list`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-entity-facts
  facts="{{ component.attributes.facts }}"
  title="{{ component.attributes.title | default: 'Details' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  groups="{{ component.attributes.groups }}"
  fields="{{ component.attributes.fields }}"
  mode="{{ component.attributes.mode | default: 'definition-list' }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
