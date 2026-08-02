# Entity Facts Component

## Description

Renders schema-approved structured facts as a Markdown definition list or table.

## Parameters

- `title`: default `Details`;
- `heading-level`: integer, default `2`;
- `groups`: optional fact-group filter;
- `fields`: optional field filter and order;
- `mode`: `definition-list` or `table`, default `definition-list`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<fact-block
  facts="{{ node.facts }}"
  groups="{{ parameters.groups }}"
  fields="{{ parameters.fields }}"
  mode="{{ parameters.mode | default: 'definition-list' }}"
  title="{{ parameters.title | default: 'Details' }}"
  heading-level="{{ parameters.heading-level | default: 2 }}"
  hide-when-empty="{{ parameters.hide-when-empty | default: true }}"/>
```
