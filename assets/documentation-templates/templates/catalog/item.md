# Catalog Item Template

## Description

Reusable template for concrete software, service, skill, model, version, artifact, hardware, and dataset pages.

Components hide themselves when their structured data is absent.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    suppress-sections-when-generated="Details:entity-facts;Dependencies:dependencies;Producer:producer-card;Producers:producer-card;Collection:relations;Official resources:resources;Resources:resources;Child pages:children"/>

  <component id="entity-facts"/>
  <component id="dependencies"/>
  <component id="producer-card"/>
  <component id="relations"
             types="{{ ['collection', 'family', 'lineage', 'version-of', 'artifact-of', 'compatible-with'] }}"
             direction="outgoing"/>
  <component id="children"/>
  <component id="resources"/>
</layout>
```
