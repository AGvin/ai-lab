# Favorites Component

## Description

Renders descendants explicitly selected from the supplied root by their effective `local.favorites` state.

## Parameters

- `root`: required documentation-node reference;
- `enabled`: boolean, default `true`;
- `title`: default `Favorites`;
- `heading-level`: integer, default `2`;
- `start-level`: integer, default `1`;
- `depth`: integer, default `1`;
- `hide-when-empty`: boolean, default `true`.

## Slots

- `custom`: literal authored Markdown;
- `generated`: generation requirements, not final prose;
- `favorites`: placement of the generated favorite links.

## Template

```html
<render-favorites
  root="{{ component.attributes.root }}"
  enabled="{{ component.attributes.enabled | default: true }}"
  title="{{ component.attributes.title | default: 'Favorites' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  start-level="{{ component.attributes.start-level | default: 1 }}"
  depth="{{ component.attributes.depth | default: 1 }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
>
  <slot name="custom">
    <component-slot name="custom"/>
  </slot>
  <slot name="generated">
    <component-slot name="generated"/>
  </slot>
  <slot name="favorites">
    <component-slot name="favorites"/>
  </slot>
</render-favorites>
```
