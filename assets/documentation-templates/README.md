# AI Lab Documentation Template Package

This directory is the distributable copy of the authoritative runtime registry under [`docs/templates/`](../../docs/templates/).

The package preserves registry-relative paths so it can be copied or synchronized into another repository's `docs/templates/` directory.

The renderer produces Markdown. HTML-like tags are declarative template instructions, not HTML output.

## Package Groups

- `pages/` — page templates;
- `layouts/` — outer page compositions;
- `partials/` — reusable composition fragments;
- `components/` — isolated parameterized renderable units;
- `manifest.yml` — package identity, inventory, source revision, and destination.

The files in this package must remain content-equivalent to the active AI Lab registry for the same package version.
