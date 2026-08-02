# Page Intro Component

## Description

Renders the primary Markdown heading and normalized short description.

## Parameters

- `title`: required string;
- `description`: optional string;
- `heading-level`: integer, default `1`;
- `description-max-length`: integer, default `240`;
- `description-overflow-marker`: string, default `…`;
- `hide-description-when-empty`: boolean, default `true`.

## Template

```html
<render-page-intro
  title="{{ component.attributes.title }}"
  description="{{ component.attributes.description }}"
  heading-level="{{ component.attributes.heading-level | default: 1 }}"
  description-max-length="{{ component.attributes.description-max-length | default: 240 }}"
  description-overflow-marker="{{ component.attributes.description-overflow-marker | default: '…' }}"
  hide-description-when-empty="{{ component.attributes.hide-description-when-empty | default: true }}"
/>
```
