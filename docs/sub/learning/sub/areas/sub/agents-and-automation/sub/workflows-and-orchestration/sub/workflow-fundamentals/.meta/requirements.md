# Documentation Requirements

## Requirements

- Teach workflow fundamentals through explicit stages, transitions, state, artifacts, validation gates, failure paths, deterministic control, and composition before introducing more specialized orchestration patterns.
- Use fixed pipelines as the simplest worked orchestration shape: input moves through a predefined sequence of bounded stages whose order and artifact contracts are known before execution, while models/tools may implement individual stages without owning overall control flow.
- For non-trivial workflows, make pipeline/workflow version, input and terminal-output schemas, stage identities/versions, artifact contracts, validation/approval gates, side effects, local retry/fallback behavior, checkpoint/resume policy, latency/cost budget, and terminal acceptance criteria explicit where material.
- Define each stage by purpose, accepted input/output schema, implementation/model/tool/runtime parameters, deterministic preparation/validation, permitted data/effects, timeout/retry/fallback/escalation behavior, artifact persistence, characteristic failure modes, and success/failure/skip/abstention semantics.
- Make transformations such as normalization, truncation, translation, summarization, redaction, parsing, or format conversion explicit rather than hiding them between stages. Preserve artifact identity, version/schema, provenance, and validation state when later diagnosis/resume depends on them.
- Place validation where a bad intermediate artifact would be amplified or hidden downstream. Teach examples such as schema validation before model use, source/terminology checks after transformation, tests after code generation, media validation before export, approval before consequential publication, and artifact persistence before resource teardown.
- Do not let a later fluent/model-generated stage silently conceal an invalid earlier artifact. Preserve the failure/correction path and enough evidence to attribute defects to source input, preparation/conversion, perception/extraction, transformation, validation, review/approval, or publication/side effect.
- Choose the simplest implementation that satisfies each stage contract: deterministic code, specialized/general model, hosted service, or qualified human review. A workflow does not need one model for every stage, and each stage must be evaluated within end-to-end workload behavior.
- Distinguish transient failures from semantic/validation failures. When authoritative inputs remain valid, retry or replace only the failed stage where possible; define attempt limits, allowed model/tool/parameter changes, manual correction/escalation, downstream invalidation, and partial/terminal failure behavior.
- Keep consequential side effects under the canonical idempotency/reconciliation contract. A workflow retry or resume must not duplicate an external write merely because a stage was retried.
- Checkpoint after expensive, validated, or externally sourced stages when interruption/recovery matters. On resume, require compatible workflow/stage/artifact versions, validate checkpoint dependencies, reconcile external jobs/effects, restart from the first incomplete/invalid stage, and invalidate downstream artifacts when authoritative upstream input changed.
- Do not silently resume persisted artifacts under incompatible stage logic without an explicit compatibility or migration rule.
- Explain that a linear workflow may still use bounded parallelism inside a stage, batching of compatible items, deterministic dependency prefetch, concurrent independent validators, or an embedded bounded fan-out/fan-in subworkflow. Preserve item identity/order and define a conflict contract before parallel writes to shared mutable state.
- Teach pattern fit: fixed pipelines suit stable staged processes such as ingestion/extraction/indexing, translation/review/publishing, code generation/testing/scanning, and media preparation/generation/validation/export where intermediate artifacts are useful.
- Route readers to graph/DAG or other explicit orchestration when conditional branches/joins, repeated loops, dynamic dependencies, or adaptive dispatch dominate. Prefer one deterministic operation when staging adds no useful control, recovery, or observability.
- Evaluate both terminal acceptance and intermediate behavior: stage first-pass success, defect origin/propagation, retries/fallbacks/manual corrections, per-stage and total latency/cost/resource use, checkpoint/resume success, duplicate side effects, artifact-validation/traceability failures, and cost per accepted terminal result.
- Keep generic workflow ownership, retry/idempotency/recovery, human approval, routing, manager-worker, evaluator-optimizer, event-driven, graph/DAG, and other specialized pattern semantics with their canonical concept or dedicated learning owners rather than duplicating them here.
- Use the canonical workflow concept's Anthropic `Building effective agents` source as supporting evidence rather than duplicating mutable framework/product claims inside this learning node.

## Validation

- Workflow control flow is never implicitly delegated to a model when the workflow contract is meant to be deterministic.
- Intermediate artifacts and validation state remain inspectable enough to diagnose upstream defects and resume safely.
- Resume never assumes compatibility after workflow/stage/schema changes without validation or migration.
- A fluent terminal artifact is not treated as proof that every upstream stage was correct.
- Specialized orchestration patterns are linked as continuations rather than collapsed into generic workflow fundamentals.
