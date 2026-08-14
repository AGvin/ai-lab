# Translations Component

## Description

Reusable locale-navigation block linking the current page to available equivalent localized representations.

## Purpose

Give readers a predictable way to change language without making every page template understand localization mechanics.

## Inputs

The renderer supplies the current output locale and validated repository locale configuration through the approved localization context. Callers do not pass complete metadata objects.

## Rendering Rules

- render only available equivalent locale targets;
- exclude the current output locale;
- use human-readable locale labels when available rather than raw locale codes;
- preserve the equivalent page and section when the localization contract supports it;
- omit the block when no alternative representation is available;
- missing or stale localized representations remain governed by the repository localization boundary and are not repaired by this component.

## Anti-patterns

- inventing links to non-materialized localized pages;
- exposing localization control metadata to readers;
- independently selecting or reapplying a page template for the localized output.
