# Common Index Template

## Description

Taxonomy and navigation template that preserves authored Markdown and generates structural navigation.

## Parameters

- `show-favorites`: boolean, default `false`;
- `favorites`: parameter object forwarded to `favorites`;
- `children`: parameter object forwarded to `children`;
- `show-resources`: boolean, default `true`.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    suppress-sections-when-generated="Child pages:children;Official resources:resources;Resources:resources;Favorites:favorites"/>

  <if test="{{ parameters.show-favorites | default: false }}">
    <component id="favorites" parameters="{{ parameters.favorites }}"/>
  </if>

  <component id="children" parameters="{{ parameters.children }}"/>

  <if test="{{ parameters.show-resources | default: true }}">
    <component id="resources"/>
  </if>
</layout>
```
