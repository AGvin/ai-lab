# Default Header Partial

## Description

Renders the primary page heading, short description, and translation links.

## Template

```html
<component
  id="page-intro"
  title="{{ source.title }}"
  description="{{ source.summary }}"
/>

<component
  id="translations"
  default-locale="{{ localization.default_locale }}"
  locales="{{ localization.locales }}"
  current-locale="{{ render.locale }}"
  page="{{ node.reference }}"
/>
```
