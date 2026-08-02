# Producer Card Component

## Description

Renders compact outgoing producer, publisher, maintainer, or operator relations.

Producer summaries are derived from canonical producer pages and are not duplicated in item metadata.

## Parameters

- `relations`: required relation array;
- `entity-index`: required canonical entity index;
- `title`: automatically singular or plural when omitted;
- `heading-level`: integer, default `2`;
- `roles`: optional producer-like role filter;
- `summary-max-length`: integer, default `180`;
- `show-role`: boolean or `auto`, default `auto`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-producer-cards
  relations="{{ component.attributes.relations }}"
  entity-index="{{ component.attributes.entity-index }}"
  title="{{ component.attributes.title }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  roles="{{ component.attributes.roles }}"
  summary-max-length="{{ component.attributes.summary-max-length | default: 180 }}"
  show-role="{{ component.attributes.show-role | default: 'auto' }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
