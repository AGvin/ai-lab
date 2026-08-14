# Child Navigation Component

## Description

Reusable semantic navigation block for an explicitly supplied set of materialized child destinations.

## Purpose

Present the next useful destinations consistently while keeping taxonomy ownership and child discovery outside the component.

## Inputs

Each supplied entry may contain a canonical reader-facing label, destination, short disambiguating description, and an optional approved semantic group. The caller supplies only entries already authorized by the page requirements and resolved navigation context.

## Rendering Rules

- preserve the caller's semantic grouping and order when they carry reader meaning;
- use descriptive link text rather than raw paths;
- keep descriptions short and decision-relevant;
- omit non-navigation implementation paths such as `.meta/`, assets, localization mirrors, and control-only nodes;
- render only materialized destinations unless requirements explicitly describe a non-link future state;
- scale presentation to entry count without turning a parent page into an exhaustive unbounded tree when a child index owns the complete list.

## Does Not Own

- taxonomy classification;
- child discovery or inference;
- canonical entity facts;
- selection ranking;
- decisions about whether a child should exist.

## Anti-patterns

- inventing children from model memory or naming conventions;
- flattening meaningful groups into one list;
- copying detailed child profiles into navigation descriptions;
- using opaque labels such as `click here` or raw folder slugs when a clear reader label exists.
