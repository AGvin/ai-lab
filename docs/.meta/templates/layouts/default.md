# Default Layout

## Description

Baseline layout for AI Lab Markdown documentation. It wraps a complete page-template body and leaves page-specific information hierarchy to the selected page family.

## Purpose

Provide one stable outer composition so page templates do not repeat footer handling or infer repository-wide chrome independently.

## Use When

Use for ordinary reader-facing documentation pages unless a future approved family demonstrates a materially different outer-layout requirement.

## Composition

```html
<layout-body/>
<partial id="default/footer"/>
```

## Rules

- the page-template body appears exactly once;
- the layout does not infer title, summary, entity facts, navigation, or relationships;
- the page template owns whether and how the default header is invoked;
- the shared footer is appended after the page body;
- a different layout requires a distinct reviewed reader-experience need, not cosmetic preference.
