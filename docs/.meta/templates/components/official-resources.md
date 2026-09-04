# Official Resources Component

## Description

Reusable block for requirement-approved authoritative or upstream resources relevant to the current page.

## Purpose

Make canonical source material easy to find without causing every profile template to reinvent resource-list presentation.

## Inputs

The caller supplies an explicit set of approved resource entries. Each entry contains a reader-facing label and destination and may carry a source role such as official site, documentation, repository, model card, technical report, or upstream collection.

## Rendering Rules

- prefer clear source-role labels over bare URLs;
- preserve distinctions between official/upstream resources and independent AI Lab evidence;
- omit the block when the page requirements do not authorize any resources;
- do not infer that every entity reference belongs in reader output;
- do not silently turn mutable third-party mirrors into canonical resources.

## Does Not Own

Source authority, reference identity, claim support, and freshness remain canonical-data and requirements concerns. This component only presents explicitly supplied reader-facing resources.
