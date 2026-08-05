# Catalog Producer Template

## Description

Template for canonical producer profiles, including organizations, teams, communities, and individual creators.

The template consumes entity data from `.meta/entity.yml`, processing configuration from `.meta/node.yml`, and reader-facing rules from `.meta/requirements.md` plus repository-global requirements.

## Template

```html
<layout id="{{ layout.id | default: 'default' }}">
  <source-body
    exclude="title,summary"
    generated-sections="entity-facts,parent-organization,sub-organizations,resources,produced-items"
  />

  <component
    id="entity-facts"
    facts="{{ entity.facts }}"
  />

  <component
    id="parent-organization"
    entity-id="{{ entity.id }}"
    relations="{{ entity.relations }}"
    entity-index="{{ repository.entity-index }}"
  />

  <component
    id="sub-organizations"
    entity-id="{{ entity.id }}"
    relationship-index="{{ repository.relationship-index }}"
    entity-index="{{ repository.entity-index }}"
  />

  <component
    id="resources"
    references="{{ entity.references }}"
  />

  <component
    id="produced-items"
    entity-id="{{ entity.id }}"
    relationship-index="{{ repository.relationship-index }}"
    entity-index="{{ repository.entity-index }}"
  />
</layout>
```

## Requirements boundary

- the template defines reusable composition, not the exact visible title, section wording, or included reference classes;
- effective requirements decide which optional sections are rendered and may override their titles or filters;
- empty optional components render nothing;
- entity metadata does not imply that every fact, reference, or relation must appear in the generated document;
- incremental updates preserve unaffected authored and generated content unless full regeneration is explicitly required.

## Relationship behavior

- `parent-organization` reads the producer's outgoing `parent-organization` relation;
- `sub-organizations` derives incoming `parent-organization` relations from the repository relationship index;
- `produced-items` derives incoming production relations instead of duplicating product lists on producer entities;
- relation targets resolve through documentation-node directories and the canonical entity index.
