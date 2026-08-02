# Resources Component

## Description

Renders structured official, reference, and community resource links.

## Parameters

- `title`: default `Resources`;
- `heading-level`: integer, default `2`;
- `scopes`: optional allowed scopes;
- `types`: optional allowed resource types;
- `group-by-scope`: boolean, default `auto`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<set name="resource-items"
     value="{{ node.resources
              | include-scopes: parameters.scopes
              | include-types: parameters.types }}"/>

<if test="{{ resource-items | not-empty
             or parameters.hide-when-empty == false }}">
  <md-heading level="{{ parameters.heading-level | default: 2 }}">
    {{ parameters.title | default: 'Resources' }}
  </md-heading>

  <resource-link-list
    resources="{{ resource-items }}"
    group-by-scope="{{ parameters.group-by-scope | default: 'auto' }}"/>
</if>
```
