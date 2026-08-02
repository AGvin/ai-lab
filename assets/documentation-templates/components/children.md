# Children Component

## Description

Renders structural child documentation nodes as a Markdown list or tree.

## Parameters

- `title`: default `Child pages`;
- `heading-level`: integer, default `2`;
- `start-level`: integer, default `1`;
- `depth`: integer, default `1`;
- `mode`: `list` or `tree`, default `list`;
- `include-summaries`: boolean, default `false`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<set name="child-nodes"
     value="{{ descendants(node,
                           start-level: parameters.start-level | default: 1,
                           depth: parameters.depth | default: 1) }}"/>

<if test="{{ child-nodes | not-empty
             or parameters.hide-when-empty == false }}">
  <md-heading level="{{ parameters.heading-level | default: 2 }}">
    {{ parameters.title | default: 'Child pages' }}
  </md-heading>

  <entity-link-list
    entities="{{ child-nodes }}"
    mode="{{ parameters.mode | default: 'list' }}"
    include-summaries="{{ parameters.include-summaries | default: false }}"/>
</if>
```
