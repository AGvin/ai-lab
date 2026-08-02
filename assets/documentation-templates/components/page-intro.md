# Page Intro Component

## Description

Renders the primary Markdown heading and the page's short description.

The default title and description are read from the source document. Other components may reuse the normalized short description.

## Parameters

- `title`: optional title override;
- `heading-level`: integer, default `1`;
- `description`: optional description override;
- `description-max-length`: integer, default `240`;
- `description-overflow-marker`: string, default `…`;
- `hide-description-when-empty`: boolean, default `true`.

## Template

```html
<md-heading level="{{ parameters.heading-level | default: 1 }}">
  {{ parameters.title | default: source.title }}
</md-heading>

<md-paragraph
  value="{{ parameters.description | default: source.summary }}"
  max-length="{{ parameters.description-max-length | default: 240 }}"
  overflow-marker="{{ parameters.description-overflow-marker | default: '…' }}"
  hide-when-empty="{{ parameters.hide-description-when-empty | default: true }}"/>
```
