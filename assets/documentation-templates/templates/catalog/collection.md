# Catalog Collection Template

## Description

Template for meaningful collections, families, catalogs, and distribution bundles.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    suppress-sections-when-generated="Details:entity-facts;Dependencies:dependencies;Installation and dependencies:dependencies;Producer:producer-card;Producers:producer-card;Selected skills:relations;Members:relations;Official resources:resources;Resources:resources;Child pages:children"/>

  <component id="entity-facts"/>
  <component id="dependencies"/>
  <component id="relations"
             types="{{ ['collection', 'member', 'contains', 'family', 'lineage', 'model', 'skill'] }}"
             direction="both"
             title="Members"/>
  <component id="children"/>
  <component id="producer-card"/>
  <component id="resources"/>
</layout>
```
