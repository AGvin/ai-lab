# Hardware-Constrained Model Selection Target Page

## Description

Device/ecosystem-first model-selection page for a concrete local compute route.

## Purpose

Turn an exact fixed hardware/runtime boundary into a practical shortlist/evaluation route while preventing load-success, file-size, TOPS, or nominal-memory shortcuts from masquerading as model fit.

## Use When

Use for a selected hardware ecosystem or specialization such as `computers/nvidia/`, `single-board/jetson/`, or `single-board/raspberry-pi/hailo-10h/`.

## Do Not Use When

Do not use for hardware purchasing, canonical hardware profiles, generic runtime documentation, or task-only model rankings.

## Owns

- exact target-identification prerequisites;
- supported execution routes and current compatibility boundary;
- hardware-specific constraints that materially change model fit;
- suitable model classes/candidates or evaluation procedure when evidence supports them;
- practical-fit measurement checks;
- common traps and fallback/escalation route;
- child navigation when the target has selected specializations.

## Does Not Own

- canonical hardware/software/model facts already owned elsewhere;
- unsupported compatibility claims;
- infrastructure architecture beyond frozen conditions needed for model selection;
- hardware purchase recommendations.

## Expected Inputs

Target requirements; current first-party platform/runtime references; exact model/artifact links when candidates are named; evidence state; memory/context/modality/power/concurrency assumptions; verification/recheck triggers.

## Composition

1. standard header and who this target applies to;
2. exact hardware/runtime identification checklist;
3. what materially changes model fit;
4. supported execution routes/current compatibility;
5. model classes/candidates or bounded evaluation route;
6. practical-fit measurement checklist;
7. common traps;
8. fallback/escalation and related selection journeys;
9. freshness/recheck boundary.

## Variants

An intermediate target such as Android or Raspberry Pi may include child navigation after explaining the shared platform boundary.

## Representative Examples

- `.../hardware/sub/computers/sub/apple/`
- `.../hardware/sub/single-board/sub/raspberry-pi/sub/hailo-10h/`
- `.../hardware/sub/servers/sub/nvidia/`

## Anti-patterns

- “it loads” as practical-fit proof;
- summing multi-GPU memory without supported sharding;
- generic vendor support transferred across OS/device generations;
- recommendation by parameter count/TOPS alone;
- buying advice disguised as model selection.
