# Pipeline Architecture

A pipeline architecture processes an input through a predefined sequence of bounded stages, where each stage consumes a declared artifact and produces the next artifact.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Status

Established workflow pattern.

## Core idea

```text
input -> prepare -> extract -> transform -> validate -> review -> publish
```

The stage order and contracts are known before execution. Models may implement selected stages, but deterministic workflow code owns the sequence, validation, retries, and terminal state.

## Distinguish related patterns

- **Pipeline:** fixed linear or mostly linear stages known in advance.
- **Prompt chaining:** a pipeline whose stages are primarily LLM calls and whose outputs feed later prompts.
- **Graph or DAG:** supports branches, joins, loops, dynamic edges, and more general dependencies.
- **Planner-executor:** a planner dynamically creates or revises the steps.
- **Orchestrator-worker:** a coordinator dynamically delegates work based on the specific task.

Prefer a pipeline when the process is stable and predictable. Do not add a dynamic agent where explicit code paths are sufficient.

## Pipeline contract

Record:

```text
Pipeline ID and version:
Input and terminal output schemas:
Stage order and versions:
Artifact contract between stages:
Validation gates:
Side effects and approval points:
Retry and fallback policy by stage:
Checkpoint and resume policy:
Failure and partial-result policy:
Latency and cost budget:
Terminal acceptance criteria:
```

Each artifact should identify its source stage, version, schema, checksum where relevant, and validation status.

## Stage contract

Every stage should define:

- purpose and supported inputs;
- exact input and output schema;
- model, tool, runtime, prompt, and parameters;
- deterministic preparation and validation;
- permitted data and side effects;
- timeout, retry, fallback, and escalation;
- artifact persistence;
- quality ceiling and common failure modes;
- success, failure, skip, and abstention semantics.

Avoid implicit transformations between stages. Normalization, truncation, translation, summarization, and redaction should be explicit stages or declared parts of a contract.

## Validation gates

Place gates where downstream execution would amplify or hide an error:

- file decode and schema validation before model input;
- terminology, protected-token, or source-evidence checks after transformation;
- tests after code generation;
- dimensions, duration, and codec checks after media generation;
- human approval before publication or irreversible side effects;
- artifact persistence before resource teardown.

A later fluent stage must not silently repair or conceal an invalid earlier artifact without preserving the original failure and correction.

## Stage selection

Use the simplest implementation that meets each contract:

- deterministic parser, formatter, calculator, or validator;
- specialized model;
- general model with bounded prompt and schema;
- hosted service;
- human review or approval.

The entire pipeline need not use one model. Select and evaluate each stage within the complete end-to-end workload.

## Error propagation

Track whether a defect originates from:

- source input;
- preparation or conversion;
- model perception or extraction;
- transformation;
- validation;
- review or approval;
- publication or external side effect.

Preserve stage-level artifacts and evidence so a downstream failure can be traced without rerunning the complete pipeline.

Do not score only the final output. A pipeline may produce a plausible terminal artifact while losing source evidence, altering protected content, or hiding an earlier hallucination.

## Retry and fallback

Retry only the failed or invalid stage when its inputs remain valid. Define:

- transient versus semantic failure;
- maximum attempts;
- whether parameters may change;
- stronger model or alternative tool;
- manual correction path;
- downstream invalidation;
- terminal failure and partial-result behavior.

A retry must not create duplicate external side effects. Use idempotency and reconcile ambiguous outcomes.

## Checkpoint and resume

Checkpoint after expensive, validated, or externally sourced stages. On resume:

1. load the exact pipeline and artifact versions;
2. validate checkpoints and dependencies;
3. reconcile external jobs and side effects;
4. resume at the first incomplete or invalid stage;
5. invalidate downstream artifacts when an upstream artifact changed;
6. preserve earlier accepted outputs when still valid.

Do not resume a pipeline with changed stage logic without explicit compatibility or migration rules.

## Parallelism

A simple pipeline is sequential, but safe optimizations may include:

- processing independent items concurrently within one stage;
- batching compatible inputs;
- prefetching deterministic dependencies;
- running independent validators in parallel;
- using a map-reduce subworkflow inside a stage.

Preserve ordering and item identity. Do not introduce parallelism where stages share mutable state or require validated prior output.

## Suitable uses

- document ingestion, extraction, normalization, and indexing;
- translation, terminology checking, review, and publishing;
- code generation, formatting, testing, security scanning, and merge preparation;
- image, video, or audio preparation, generation, validation, and export;
- speech transcription, diarization, normalization, and caption packaging;
- high-volume stable workflows with observable intermediate artifacts.

## Poor fits

Avoid or generalize to a graph when:

- execution requires many conditional branches or joins;
- tasks and dependencies cannot be known in advance;
- an agent must explore and select tools dynamically;
- repeated correction loops dominate the process;
- stages require shared deliberation rather than artifact transformation;
- one deterministic operation is sufficient.

## Strengths

- predictable and inspectable control flow;
- clear stage ownership and artifacts;
- easy deterministic validation and testing;
- local retries and failure isolation;
- straightforward latency and cost attribution;
- simpler than a general graph or autonomous agent.

## Limitations

- rigid order can be inefficient for variable tasks;
- upstream errors propagate downstream;
- stage boundaries add serialization and latency;
- schema changes require compatibility management;
- excessive stages create operational overhead;
- a pipeline cannot adapt beyond its declared routes without explicit fallback.

## Evaluation metrics

Record:

- end-to-end terminal acceptance;
- first-pass success by stage;
- defect origin and propagation;
- retries, fallbacks, and manual corrections by stage;
- stage and total latency;
- cost and resource use by stage;
- checkpoint and resume success;
- duplicate side effects;
- artifact-validation and traceability failures;
- cost per accepted terminal result.

Measure pipeline performance on representative complete inputs. Optimizing one stage can reduce end-to-end quality if its output no longer fits downstream contracts.

## Evidence and established usage

Anthropic documents prompt chaining as a workflow that decomposes a task into a sequence of calls, where each call processes the previous output and programmatic gates may validate intermediate stages. The broader pipeline pattern also includes deterministic and human stages.

Source:

- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## Related concepts

- [Multi-Agent Systems](../..)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Planner-Executor Architecture](../planner-executor/)
- [Router-Specialist Architecture](../router-specialist/)
- [Evaluator-Optimizer Architecture](../evaluator-optimizer/)
- [Human Approval Gates](../human-approval-gates/)
