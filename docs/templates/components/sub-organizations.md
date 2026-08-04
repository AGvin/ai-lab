# Sub-organizations Component

## Description

Renders producer entities whose outgoing `parent-organization` relation targets the current producer.

The component represents organizational containment, not ownership. Legal subsidiaries, internal teams, brands, projects, and communities may require additional semantic distinctions in entity relations even when they are displayed together by this component.

## Parameters

- `entity-id`: required stable current producer entity ID;
- `relationship-index`: required repository relationship index;
- `entity-index`: required canonical entity index;
- `title`: default `Sub-organizations`;
- `heading-level`: integer, default `2`;
- `types`: optional producer-type filter;
- `group-by-type`: boolean, default `false`;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-incoming-relationships
  target-id="{{ component.attributes.entity-id }}"
  relationship-index="{{ component.attributes.relationship-index }}"
  entity-index="{{ component.attributes.entity-index }}"
  relation-types="{{ ['parent-organization'] }}"
  types="{{ component.attributes.types }}"
  title="{{ component.attributes.title | default: 'Sub-organizations' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  group-by-type="{{ component.attributes.group-by-type | default: false }}"
  include-summaries="{{ component.attributes.include-summaries | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```

## Rendering rules

- render nothing when no matching incoming relation exists and `hide-when-empty` is true;
- derive the list from the relationship index rather than duplicating child IDs on the parent entity;
- resolve source entities through the canonical entity index;
- use stable deterministic ordering;
- page-specific wording and grouping belong in requirements or explicit component parameters.
