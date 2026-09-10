# Default Header Partial

## Description

Shared structural header for ordinary AI Lab pages. It renders the requirement-approved page title, an optional short orientation summary, and locale navigation without owning domain-specific page semantics.

## Purpose

Keep the H1/intro/translation shell consistent while allowing each page template to decide what the title and summary must communicate.

## Parameters

### `title`

- Type: `string`
- Required: yes
- Description: Exact reader-facing page title authorized by the applicable requirements.

### `summary`

- Type: `string | null`
- Required: no
- Description: Short introductory orientation text authorized by the applicable requirements.

## Composition

1. Render `title` as the page H1.
2. When `summary` is present and non-empty, render it as one concise introductory paragraph directly below the H1.
3. Invoke `translations` after the intro so locale navigation is consistently discoverable without interrupting the subject explanation.

## Rules

- title and summary are explicit caller inputs; this partial does not substitute `entity.name` or scrape an existing README;
- the summary is orientation, not a miniature profile or SEO filler;
- absence of a summary produces no empty paragraph or placeholder;
- domain-specific scope, ownership, capabilities, navigation, and resources remain page-template responsibilities;
- the partial does not expose internal metadata vocabulary merely because it exists in canonical inputs.
