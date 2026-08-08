# Produced Items Component

## Description

Renders reverse catalog links for entities that reference the current producer.

## Parameters

- `entity-id`: required stable producer entity ID;
- `relationship-index`: required repository relationship index;
- `entity-index`: required canonical entity index;
- `title`: default `Produced items`;
- `heading-level`: integer, default `2`;
- `kinds`: optional entity-kind filter;
- `roles`: optional producer-role filter;
- `group-by-kind`: boolean, default `true`;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-incoming-relationships
  target-id="{{ component.attributes.entity-id }}"
  relationship-index="{{ component.attributes.relationship-index }}"
  entity-index="{{ component.attributes.entity-index }}"
  relation-types="{{ ['producer'] }}"
  roles="{{ component.attributes.roles }}"
  kinds="{{ component.attributes.kinds }}"
  title="{{ component.attributes.title | default: 'Produced items' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  group-by-kind="{{ component.attributes.group-by-kind | default: true }}"
  include-summaries="{{ component.attributes.include-summaries | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
