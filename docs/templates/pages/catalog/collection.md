# Catalog Collection Template

## Description

Template for meaningful collections, families, catalogs, and distribution bundles.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="entity-facts,dependencies,relations,children,producer-card,resources"
  />

  <component id="entity-facts" facts="{{ node.facts }}"/>

  <component
    id="dependencies"
    dependencies="{{ node.dependencies }}"
    entity-id="{{ node.entity.id }}"
    relationship-index="{{ repository.relationship-index }}"
  />

  <component
    id="relations"
    entity-id="{{ node.entity.id }}"
    relations="{{ node.relations }}"
    relationship-index="{{ repository.relationship-index }}"
    entity-index="{{ repository.entity-index }}"
    types="{{ ['collection', 'member', 'contains', 'family', 'lineage', 'model', 'skill'] }}"
    direction="both"
    title="Members"
  />

  <component id="children" root="{{ node.reference }}"/>

  <component
    id="producer-card"
    relations="{{ node.relations }}"
    entity-index="{{ repository.entity-index }}"
  />

  <component id="resources" resources="{{ node.resources }}"/>
</layout>
```
