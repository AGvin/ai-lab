# Translations Component

## Description

Renders links to alternative localized variants of the composed default-locale page.

Localized pages do not reapply page templates.

## Parameters

- `default-locale`: required locale ID;
- `locales`: required locale-ID array;
- `current-locale`: required locale ID;
- `page`: required canonical page reference;
- `title`: default `Translations`;
- `heading-level`: integer, default `2`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<render-translation-links
  default-locale="{{ component.attributes.default-locale }}"
  locales="{{ component.attributes.locales }}"
  current-locale="{{ component.attributes.current-locale }}"
  page="{{ component.attributes.page }}"
  title="{{ component.attributes.title | default: 'Translations' }}"
  heading-level="{{ component.attributes.heading-level | default: 2 }}"
  label-form="translation-target"
  hide-when-empty="{{ component.attributes.hide-when-empty | default: true }}"
/>
```

## Label Rule

The semantic `translation-target` form produces locale-natural wording, including `Українською`, `Англійською`, and `Німецькою` in Ukrainian output.
