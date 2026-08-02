# Resources Component

## Description

Renders structured official, reference, and community resource links.

## Parameters

- `resources`: required resource array;
- `enabled`: boolean, default `true`;
- `title`: default `Resources`;
- `heading-level`: integer, default `2`;
- `scopes`: optional allowed scopes;
- `types`: optional allowed resource types;
- `group-by-scope`: boolean or `auto`, default `auto`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-resource-links
  resources="{{ component.attributes.resources }}"
  enabled="{{ component.attributes.enabled | default: true }}"
  title="{{ component.attributes.title | default: 'Resources' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  scopes="{{ component.attributes.scopes }}"
  types="{{ component.attributes.types }}"
  group-by-scope="{{ component.attributes.group-by-scope | default: 'auto' }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
