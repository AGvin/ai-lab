# Children Component

## Description

Renders structural descendants as a Markdown list or tree.

## Parameters

- `root`: required documentation-node reference;
- `enabled`: boolean, default `true`;
- `title`: default `Child pages`;
- `heading-level`: integer, default `2`;
- `start-level`: integer, default `1`;
- `depth`: integer, default `1`;
- `mode`: `list` or `tree`, default `list`;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-documentation-children
  root="{{ component.attributes.root }}"
  enabled="{{ component.attributes.enabled | default: true }}"
  title="{{ component.attributes.title | default: 'Child pages' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  start-level="{{ component.attributes.start-level | default: 1 }}"
  depth="{{ component.attributes.depth | default: 1 }}"
  mode="{{ component.attributes.mode | default: 'list' }}"
  include-summaries="{{ component.attributes.include-summaries | default: false }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```
