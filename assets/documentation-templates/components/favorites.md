# Favorites Component

## Description

Selects descendants whose effective local context contains `local.favorites: true`.

## Parameters

- `title`: default `Favorites`;
- `heading-level`: integer, default `2`;
- `start-level`: integer, default `1`;
- `depth`: integer, default `1`;
- `hide-when-empty`: boolean, default `true`.

## Body Sections

- `custom`: literal authored Markdown;
- `generated`: requirements for generated Markdown;
- `favorites`: generated result placement.

## Template

```html
<set name="favorite-nodes"
     value="{{ descendants(node,
                           start-level: parameters.start-level | default: 1,
                           depth: parameters.depth | default: 1)
              | where-effective: 'local.favorites', true }}"/>

<if test="{{ favorite-nodes | not-empty
             or component.body | produces-content
             or parameters.hide-when-empty == false }}">
  <md-heading level="{{ parameters.heading-level | default: 2 }}">
    {{ parameters.title | default: 'Favorites' }}
  </md-heading>

  <render-component-body default-slot="favorites">
    <slot-renderer name="custom" mode="literal-markdown"/>
    <slot-renderer name="generated" mode="generated-markdown"/>
    <slot-renderer name="favorites">
      <entity-link-list entities="{{ favorite-nodes }}"/>
    </slot-renderer>
  </render-component-body>
</if>
```
