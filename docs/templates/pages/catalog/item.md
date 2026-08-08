# Catalog Item Template

## Description

Reusable template for concrete software, service, skill, model, version, artifact, hardware, and dataset pages.

Components suppress equivalent manual sections only when their structured inputs produce output.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="entity-facts,dependencies,producer-card,relations,children,resources"
  />

  <component id="entity-facts" facts="{{ node.facts }}"/>

  <component
    id="dependencies"
    dependencies="{{ node.dependencies }}"
    entity-id="{{ node.entity.id }}"
    relationship-index="{{ repository.relationship-index }}"
  />

  <component
    id="producer-card"
    relations="{{ node.relations }}"
    entity-index="{{ repository.entity-index }}"
  />

  <component
    id="relations"
    entity-id="{{ node.entity.id }}"
    relations="{{ node.relations }}"
    relationship-index="{{ repository.relationship-index }}"
    entity-index="{{ repository.entity-index }}"
    types="{{ ['collection', 'family', 'lineage', 'version-of', 'artifact-of', 'compatible-with'] }}"
    direction="outgoing"
  />

  <component id="children" root="{{ node.reference }}"/>
  <component id="resources" resources="{{ node.resources }}"/>
</layout>
```
