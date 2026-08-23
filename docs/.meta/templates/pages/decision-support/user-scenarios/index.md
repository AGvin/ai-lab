# User Scenarios Index Page

## Description

Reusable index page for the user-scenario root and its audience-group indexes.

## Purpose

Help readers navigate from a combined real-world context to a materialized scenario whose constraints genuinely change the decision route.

## Use When

Use for `decision-support/user-scenarios/` and its audience-group nodes such as `personal/`, `professionals/`, `teams/`, and `organizations/`.

## Do Not Use When

Do not use for a concrete scenario leaf, a task-oriented model decision guide, or a canonical catalog entity.

## Owns

- the scenario method or audience-group boundary appropriate to the current node;
- concise orientation to the dimensions that distinguish scenarios;
- placement of validated child navigation.

## Does Not Own

- detailed recommendations belonging to child scenarios;
- canonical model, software, service, hardware, or other entity facts;
- child nodes that are only logical future destinations and have not been materialized.

## Expected Inputs

- applicable root or group requirements;
- validated visible direct-child projection.

## Composition

1. standard header;
2. scenario-method or audience-group orientation;
3. key scope/boundary guidance;
4. child navigation for materialized scenarios or groups.

## Variants

- **root index** — explains the combined-context method and the four decision-scale groups;
- **audience-group index** — explains one group's boundary and links only its materialized scenarios.

## Representative Examples

- `docs/sub/decision-support/sub/user-scenarios/`
- `docs/sub/decision-support/sub/user-scenarios/sub/personal/`

## Anti-Patterns

- turning an index into a second recommendation monolith;
- creating empty scenario children to mirror a logical taxonomy;
- grouping primarily by one cross-cutting property such as local/cloud, privacy, budget, or VRAM instead of the selected audience/decision-scale axis.
