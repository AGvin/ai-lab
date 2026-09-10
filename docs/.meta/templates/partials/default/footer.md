# Default Footer Partial

## Description

Stable shared extension point appended by the default layout after the page-template body.

## Purpose

Reserve one canonical place for future repository-wide footer behavior without forcing page templates to own or duplicate it.

## Current Output

The partial intentionally emits no reader-facing content.

## Rules

- do not add page-specific navigation, references, ownership notes, or boilerplate here;
- introduce shared footer output only when it is genuinely repository-wide and owner-reviewed;
- page-template completeness must never depend on hidden footer content.
