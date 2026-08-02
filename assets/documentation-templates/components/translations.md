# Translations Component

## Description

Renders links to alternative localized variants of the composed default-locale page.

Localized pages do not reapply page templates.

## Parameters

- `default-locale`: defaults to the repository localization context;
- `locales`: defaults to configured localization locales;
- `title`: default `Translations`;
- `heading-level`: integer, default `2`;
- `hide-when-empty`: boolean, default `true`.

## Template

```html
<set name="available-locales"
     value="{{ locale-set(parameters.default-locale, parameters.locales)
              | exclude: render.locale }}"/>

<if test="{{ available-locales | not-empty
             or parameters.hide-when-empty == false }}">
  <md-heading level="{{ parameters.heading-level | default: 2 }}">
    {{ parameters.title | default: 'Translations' }}
  </md-heading>

  <md-list>
    <for each="locale in available-locales">
      <md-list-item>
        <md-link href="{{ localized-page-url(node, locale) }}">
          <locale-label
            locale="{{ locale }}"
            output-locale="{{ render.locale }}"
            form="translation-target"/>
        </md-link>
      </md-list-item>
    </for>
  </md-list>
</if>
```

## Label Rule

The `translation-target` form produces locale-natural wording, including `Українською`, `Англійською`, and `Німецькою` in Ukrainian output.
