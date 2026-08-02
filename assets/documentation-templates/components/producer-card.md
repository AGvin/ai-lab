# Producer Card Component

## Description

Renders compact outgoing producer, publisher, maintainer, or operator relations.

The summary is derived from the canonical producer page and is not duplicated in item metadata.

## Parameters

- `title`: singular or plural default selected automatically;
- `heading-level`: integer, default `2`;
- `roles`: default producer-like roles;
- `summary-max-length`: integer, default `180`;
- `show-role`: boolean or `auto`, default `auto`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<set name="producer-relations"
     value="{{ outgoing-relations(node)
              | roles: parameters.roles | default: producer-like }}"/>

<relationship-cards
  relations="{{ producer-relations }}"
  title="{{ parameters.title }}"
  heading-level="{{ parameters.heading-level | default: 2 }}"
  summary-max-length="{{ parameters.summary-max-length | default: 180 }}"
  show-role="{{ parameters.show-role | default: 'auto' }}"
  hide-when-empty="{{ parameters.hide-when-empty | default: true }}"/>
```
