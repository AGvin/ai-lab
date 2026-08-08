# Parent Organization Component

## Description

Renders the current producer's outgoing `parent-organization` relation as a compact optional organization link or list.

The component represents organizational containment, not ownership. Legal or factual ownership must use a distinct relation such as `owned-by` when required.

## Parameters

- `entity-id`: required stable current producer entity ID;
- `relations`: required outgoing relation array;
- `entity-index`: required canonical entity index;
- `title`: default `Parent organization`;
- `heading-level`: integer, default `2`;
- `include-summary`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-entity-relationships
  entity-id="{{ component.attributes.entity-id }}"
  relations="{{ component.attributes.relations }}"
  entity-index="{{ component.attributes.entity-index }}"
  types="{{ ['parent-organization'] }}"
  direction="outgoing"
  title="{{ component.attributes.title | default: 'Parent organization' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  include-summaries="{{ component.attributes.include-summary | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```

## Rendering rules

- render nothing when no matching relation exists and `hide-when-empty` is true;
- resolve relation targets through the canonical entity index;
- do not infer ownership from `parent-organization`;
- preserve support for more than one parent relation even though the normal producer case has one;
- page-specific wording belongs in requirements or explicit component parameters.
