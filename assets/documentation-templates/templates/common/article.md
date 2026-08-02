# Common Article Template

## Description

Content-first page template for project overviews, policies, and reference articles.

## Parameters

- `show-children`: boolean, default `false`;
- `children`: parameter object forwarded to `children`;
- `show-resources`: boolean, default `true`.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    suppress-sections-when-generated="Child pages:children;Official resources:resources;Resources:resources"/>

  <if test="{{ parameters.show-children | default: false }}">
    <component id="children" parameters="{{ parameters.children }}"/>
  </if>

  <if test="{{ parameters.show-resources | default: true }}">
    <component id="resources"/>
  </if>
</layout>
```
