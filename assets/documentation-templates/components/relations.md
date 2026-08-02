# Relations Component

## Description

Renders configurable non-structural relationships between catalog entities.

## Parameters

- `entity-id`: required stable current entity ID;
- `relations`: required outgoing relation array;
- `relationship-index`: required for incoming or bidirectional rendering;
- `entity-index`: required canonical entity index;
- `types`: required relation-type array;
- `roles`: optional role filter;
- `direction`: `outgoing`, `incoming`, or `both`, default `outgoing`;
- `title`: optional title;
- `heading-level`: integer, default `2`;
- `group-by`: optional grouping field;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-entity-relationships
  entity-id="{{ component.attributes.entity-id }}"
  relations="{{ component.attributes.relations }}"
  relationship-index="{{ component.attributes.relationship-index }}"
  entity-index="{{ component.attributes.entity-index }}"
  types="{{ component.attributes.types }}"
  roles="{{ component.attributes.roles }}"
  direction="{{ component.attributes.direction | default: 'outgoing' }}"
  title="{{ component.attributes.title }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  group-by="{{ component.attributes.group-by }}"
  include-summaries="{{ component.attributes.include-summaries | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
