# Catalog Landing Page

## Description

Top-level orientation page for the canonical AI Lab entity catalog.

## Purpose

Help a reader understand what the Catalog contains, how its major domains differ, and which domain is the right next destination.

## Use When

Use for the single `catalog/` root that coordinates canonical entity domains such as models, producers, services, software, Agent Skills, datasets, and hardware.

## Do Not Use When

Do not use for a single domain, a taxonomy category, an alphabetical lookup page, or an individual entity profile.

## Owns

- concise explanation of the Catalog as the canonical entity/reference layer;
- high-level distinctions among materialized catalog domains;
- navigation to those domains;
- links to adjacent non-catalog journeys only when needed to prevent reader confusion.

## Does Not Own

- complete taxonomy or physical-tree reproduction;
- detailed entity facts;
- model-selection conclusions;
- installation, deployment, or workflow guidance owned elsewhere.

## Expected Inputs

A requirement-approved title and orientation, the currently materialized direct catalog domains, short domain descriptions, and any explicit boundary links to adjacent documentation journeys.

## Composition

1. default header;
2. short plain-language Catalog orientation;
3. primary domain navigation using `child-navigation`;
4. concise boundary note only where readers are likely to confuse Catalog with another documentation journey.

## Variants

The number of materialized domains may change. The page remains useful with a small or large domain set and must not invent empty domain branches.

## Representative Example

- `docs/sub/catalog/`

## Anti-patterns

- dumping the complete documentation tree;
- turning the landing page into an encyclopedia article;
- duplicating descriptions and facts owned by domain or entity pages;
- presenting recommendation guidance as canonical catalog fact.
