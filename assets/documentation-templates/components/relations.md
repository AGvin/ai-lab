# Relations Component

## Description

Renders configurable non-structural relationships between catalog entities.

## Parameters

- `types`: required relation types;
- `roles`: optional role filter;
- `direction`: `outgoing`, `incoming`, or `both`, default `outgoing`;
- `title`: optional title;
- `heading-level`: integer, default `2`;
- `group-by`: optional grouping field;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<relationship-groups
  relations="{{ relations(node,
                           types: parameters.types,
                           roles: parameters.roles,
                           direction: parameters.direction | default: 'outgoing') }}"
  title="{{ parameters.title }}"
  heading-level="{{ parameters.heading-level | default: 2 }}"
  group-by="{{ parameters.group-by }}"
  include-summaries="{{ parameters.include-summaries | default: false }}"
  hide-when-empty="{{ parameters.hide-when-empty | default: true }}"/>
```
