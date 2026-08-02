# Produced Items Component

## Description

Renders reverse catalog links for entities that reference the current producer.

## Parameters

- `title`: default `Produced items`;
- `heading-level`: integer, default `2`;
- `kinds`: optional entity-kind filter;
- `roles`: optional producer-role filter;
- `group-by-kind`: boolean, default `true`;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<set name="produced-entities"
     value="{{ incoming-relations(node.entity.id)
              | roles: parameters.roles | default: producer-like
              | entity-kinds: parameters.kinds }}"/>

<relationship-groups
  relations="{{ produced-entities }}"
  title="{{ parameters.title | default: 'Produced items' }}"
  heading-level="{{ parameters.heading-level | default: 2 }}"
  group-by-kind="{{ parameters.group-by-kind | default: true }}"
  include-summaries="{{ parameters.include-summaries | default: false }}"
  hide-when-empty="{{ parameters.hide-when-empty | default: true }}"/>
```
