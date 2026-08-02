# Common Index Template

## Description

Taxonomy and navigation template that preserves authored Markdown and generates structural navigation.

## Parameters

- `show-favorites`: boolean, default `false`;
- `favorites`: optional favorite-component settings;
- `children`: optional child-component settings;
- `show-resources`: boolean, default `true`.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="favorites,children,resources"
  />

  <component
    id="favorites"
    root="{{ node.reference }}"
    enabled="{{ parameters.show-favorites | default: false }}"
    title="{{ parameters.favorites.title }}"
    heading-level="{{ parameters.favorites.heading-level }}"
    start-level="{{ parameters.favorites.start-level }}"
    depth="{{ parameters.favorites.depth }}"
  />

  <component
    id="children"
    root="{{ node.reference }}"
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
