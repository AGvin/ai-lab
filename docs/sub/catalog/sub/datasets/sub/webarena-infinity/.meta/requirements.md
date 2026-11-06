# Documentation Requirements

## Requirements

- Identify WebArena-Infinity as the separately released WebArena-x research benchmark approach and materialized evaluation suite for automatically generated, realistic browser environments with verifiable tasks, with first-party source at `web-arena-x/webarena-infinity` and the March 2026 project publication.
- Distinguish its **generated and potentially evolving task distribution** from original WebArena's fixed 812 annotated tasks, VisualWebArena's 910 visual tasks and ServiceNow's WebArena-Verified corrected evaluator. WebArena-Infinity's app generators, coding-agent pipeline and web UI execution harness support the benchmark; they are not evidence that all generated environments share a stable fixed-size public test split.
- Preserve reproducibility boundaries: pin the exact repo revision, app/environment manifest, generated application state and data, task/verifier definitions, evaluation scripts, agent/model/runtime versions, random seeds where provided and reset policy before comparing results.
- The first-party project currently includes runnable pre-built environments and generation scripts, with environment count and downloadable trajectories evolving independently. Do not treat a rolling default branch or hosted environment hub as an immutable normative benchmark version.
- The full automatic generation workflow invokes coding agents with privileged code-editing capabilities, including a `--dangerously-skip-permissions` option documented upstream. Require sandboxed/disposable execution and least-privilege credentials; do not imply it is safe to run unrestricted against an ordinary workstation or production infrastructure.
- Keep the WebArena-x first-party producer link reciprocal. Research contributors and underlying agent API providers are not the owners of generated benchmark identity.

## Validation

- The official released research artifact includes reproducible runnable/verifiable tasks rather than merely announcing an unimplemented future concept.
- WebArena-Infinity and the original/Visual/Verified WebArena suites are not conflated in versioned result comparisons.
- The WebArena-x producer has the inverse `produces` relation; the canonical node is not duplicated under software solely because the benchmark offers generation tooling.
