# Catalog Producer Template

## Description

Template for canonical organization and individual producer profiles.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    suppress-sections-when-generated="Official resources:resources;Resources:resources;Produced items:produced-items;Agent Skill collections:produced-items;Selected Agent Skills:produced-items"/>

  <component id="entity-facts"/>
  <component id="resources"/>
  <component id="produced-items"/>
</layout>
```
