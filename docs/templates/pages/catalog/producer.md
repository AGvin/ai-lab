# Catalog Producer Template

## Description

Template for canonical organization and individual producer profiles.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="entity-facts,resources,produced-items"
  />

  <component id="entity-facts" facts="{{ node.facts }}"/>
  <component id="resources" resources="{{ node.resources }}"/>

  <component
    id="produced-items"
    entity-id="{{ node.entity.id }}"
    relationship-index="{{ repository.relationship-index }}"
    entity-index="{{ repository.entity-index }}"
  />
</layout>
```
