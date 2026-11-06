# Documentation Requirements

## Requirements

- Scope ClassEval as a concrete class-level code-generation benchmark dataset; do not treat individual classes, methods, reference solutions, leaderboard records or the source test runner as new benchmark identities.
- The official README describes 100 manually crafted class-level Python tasks containing 100 classes and 410 methods, with an average of 33.1 unit-test cases per class. It references official v1.0.0 release from January 2024.
- Preserve method dependencies between fields, other methods, standalone logic and third-party libraries. The task-level and method-level pass criteria are not interchangeable.
- The pinned root LICENSE is MIT for covered source, without implied rights to external packages, code copied from third parties or future hosted submissions.
- Generated Python is untrusted code and must be evaluated in a sandbox with no secrets/network access and bounded CPU, memory, filesystem and execution time; do not execute against developer workstations or production systems.
- Record dataset revision, dependencies, unit-test version, model sampling and execution limits to compare scores. No code generation run, test execution or complete source and data rights audit was performed.

## Validation

- One canonical dataset identity, pinned upstream publisher sources and a resolvable index link.
- Keep distinct code/data/right boundaries; no runtime, security, complete citation audit or clean-group gate is inferred.
