# Resources Component

## Description

Renders structured entity references as reader-facing resource links when the applicable requirements permit them.

The component consumes `entity.references`. Presence in entity metadata does not by itself require rendering; page requirements and component filters control the visible result.

## Parameters

- `references`: required entity reference array;
- `enabled`: boolean, default `true`;
- `title`: default `Resources`;
- `heading-level`: integer, default `2`;
- `authorities`: optional allowed authority values;
- `types`: optional allowed semantic reference types;
- `platforms`: optional allowed platforms;
- `purposes`: optional allowed reference purposes;
- `group-by`: optional `authority`, `type`, or `platform`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-reference-links
  references="{{ component.attributes.references }}"
  enabled="{{ component.attributes.enabled | default: true }}"
  title="{{ component.attributes.title | default: 'Resources' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  authorities="{{ component.attributes.authorities }}"
  types="{{ component.attributes.types }}"
  platforms="{{ component.attributes.platforms }}"
  purposes="{{ component.attributes.purposes }}"
  group-by="{{ component.attributes.group-by }}"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```

## Rendering rules

- render nothing when no reference passes the active filters and `hide-when-empty` is true;
- render only references whose inclusion is permitted by the effective page requirements;
- use the reference source locator as the destination;
- derive a readable label from explicit metadata or the semantic type and platform without exposing internal enum values verbatim;
- preserve deterministic ordering defined by requirements or the canonical renderer policy;
- prefer a localized authoritative destination matching the current document locale when equivalent official variants are available;
- do not treat independent or community references as official;
- do not render research-only references when page requirements exclude them.
