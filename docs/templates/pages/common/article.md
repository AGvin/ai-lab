# Common Article Template

## Description

Content-first page template for project overviews, policies, and reference articles.

## Parameters

- `show-children`: boolean, default `false`;
- `children`: optional child-component settings;
- `show-resources`: boolean, default `true`.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="children,resources"
  />

  <component
    id="children"
    root="{{ node.reference }}"
    enabled="{{ parameters.show-children | default: false }}"
    title="{{ parameters.children.title }}"
    heading-level="{{ parameters.children.heading-level }}"
    start-level="{{ parameters.children.start-level }}"
    depth="{{ parameters.children.depth }}"
    mode="{{ parameters.children.mode }}"
    include-summaries="{{ parameters.children.include-summaries }}"
  />

  <component
    id="resources"
    resources="{{ node.resources }}"
    enabled="{{ parameters.show-resources | default: true }}"
  />
</layout>
```
