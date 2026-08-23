# Hardware-Constrained Model Selection Index Page

## Description

Index/orientation page for the device-first model-selection journey and its first-level hardware groups.

## Purpose

Help a reader who already owns or has a fixed compute target identify the correct hardware ecosystem route before selecting model candidates.

## Use When

Use for `catalog/models/selection/hardware/` and first-level groups `mobile/`, `computers/`, `single-board/`, `embedded/`, and `servers/`.

## Do Not Use When

Do not use for canonical hardware profiles, hardware purchasing, task-first model guides, user scenarios, or a concrete compute ecosystem target.

## Owns

- the device-first selection method or one first-level group boundary;
- explanation of the axis used to choose among children;
- common fit cautions: runtime/format support, memory/context, modality, thermals/power, concurrency, measured performance, accepted-result quality;
- validated child navigation.

## Does Not Own

- canonical hardware identity/specifications;
- specific model profiles;
- runtime/software profiles;
- hardware purchase recommendations;
- children absent from canonical inputs.

## Expected Inputs

Applicable requirements, validated child projection, current first-party compatibility evidence where group routing depends on mutable platform support.

## Composition

1. standard header;
2. target-identification/routing method;
3. material fit dimensions and anti-traps;
4. child navigation;
5. sibling model-selection continuation where useful.

## Variants

Root explains all five hardware classes; group pages explain how to choose the correct ecosystem child.

## Representative Examples

- `.../selection/sub/hardware/`
- `.../selection/sub/hardware/sub/single-board/`

## Anti-patterns

- TOPS or nominal memory as universal rank;
- using edge/cloud/local as hardware classes;
- duplicating a hardware catalog;
- materializing vendor children without distinct runtime/compatibility routes.
