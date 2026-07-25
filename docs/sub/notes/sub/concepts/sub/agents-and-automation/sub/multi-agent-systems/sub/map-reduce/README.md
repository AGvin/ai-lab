# Map-Reduce Agent Architecture

A map-reduce agent architecture partitions a workload into independent map tasks, executes them in parallel, groups their structured intermediate results, and combines them through one or more reduce stages.

## Translations

- English

## Status

Established parallel-processing pattern adapted for agent workflows.

## Core idea

```text
input corpus -> partition -> map workers -> normalized intermediate records
                                      -> group or shuffle -> reducer -> verified result
```

The pattern is useful when the workload can be divided without requiring every worker to see or modify the complete shared state.

## Distinguish related patterns

- **Map-reduce:** repeat one bounded map contract over partitions and aggregate normalized records through a reduce contract.
- **Parallelization:** broader category that includes independent sectioning or repeated voting without map and reduce semantics.
- **Orchestrator-worker:** an orchestrator may dynamically create heterogeneous tasks; map tasks are normally homogeneous or contract-compatible.
- **Graph or DAG:** can represent map-reduce and more general dependencies.
- **Pipeline:** map-reduce may be one parallel stage inside a larger fixed pipeline.

Do not call arbitrary multi-agent parallel work map-reduce when partition completeness, intermediate schemas, grouping, and reduction are undefined.

## Workload contract

Record:

```text
Job ID and version:
Input dataset and immutable snapshot:
Partition strategy and partition manifest:
Map function, model, prompt, tools, and version:
Intermediate record schema and keys:
Grouping, shuffle, and ordering rules:
Combiner policy:
Reduce function, model, prompt, tools, and version:
Validation and evidence requirements:
Retry, straggler, and partial-failure policy:
Terminal acceptance criteria:
```

The partition manifest should prove which input units were assigned, duplicated deliberately, excluded, or left unprocessed.

## Partitioning

Partition by a stable unit such as:

- document, page range, file, repository module, record range, time window, image set, audio segment, or video shot;
- semantic section with explicit source spans;
- deterministic hash or key;
- risk, language, modality, or domain class when map contracts remain compatible.

Define:

- complete coverage;
- overlap and deduplication;
- item identity and source order;
- maximum partition size and context budget;
- cross-partition dependencies;
- treatment of malformed or oversized items.

A semantic partitioner can omit or distort material content. Preserve source references and validate coverage independently.

## Map contract

Each map worker should receive:

- one declared partition and partition ID;
- bounded task and acceptance criteria;
- exact output schema;
- source and evidence requirements;
- model, tool, permission, and data boundary;
- timeout, retry, and resource envelope.

Each intermediate record should include:

```text
Job and partition ID:
Source unit and span:
Intermediate key:
Structured value:
Evidence or artifact reference:
Producer and model version:
Validation status:
Uncertainty and abstention:
```

Map workers should not invent global conclusions that require unseen partitions. They should report local findings and explicit missing context.

## Grouping and shuffle

Before reduction:

- validate intermediate schemas;
- reject or quarantine malformed records;
- deduplicate stable record IDs;
- group by declared keys;
- preserve source provenance;
- reconcile ordering where it matters;
- identify missing or failed partitions;
- enforce memory and size limits.

The grouping layer should be deterministic where possible. Do not ask a language model to infer which records exist when the manifest can establish it exactly.

## Combiner stage

A local combiner may reduce records before the global reduce stage when the operation is associative and semantically safe.

Examples include:

- deterministic counts or sums;
- deduplicated key sets;
- local summaries with preserved source references;
- top candidates under a declared scoring rule.

Do not use a lossy summary combiner when rare evidence, minority findings, exact quotations, or cross-partition contradictions matter.

## Reduce contract

The reducer should:

- receive normalized grouped records and the partition manifest;
- verify completeness and unresolved failures;
- combine facts under explicit rules;
- detect contradictions, duplicates, and missing evidence;
- preserve source traceability;
- distinguish aggregate fact, inference, recommendation, and unknown;
- run deterministic validators;
- abstain or escalate when the aggregate is insufficient.

For complex synthesis, use hierarchical reduction: bounded local reducers produce structured records for a final reducer. Evaluate information loss at every level.

## Deterministic and model reducers

Prefer deterministic reducers for:

- counts, sums, min or max, set operations, grouping, exact joins, schema validation, and source coverage.

Use model reducers for:

- semantic synthesis;
- contradiction analysis;
- thematic organization;
- evidence-grounded narrative or recommendation.

A model reducer should not recompute exact aggregate values from prose when structured records are available.

## Retry, stragglers, and partial failure

Define:

- maximum map attempts;
- idempotent output location and record IDs;
- speculative duplicate execution for stragglers, if allowed;
- winner and duplicate-result policy;
- timeout and cancellation;
- required versus optional partitions;
- minimum coverage for partial results;
- fallback model or human review;
- terminal failure when missing input is material.

Do not silently reduce only successful partitions and present the result as complete.

## Context and cost control

Map-reduce can reduce per-call context but increase total tokens, model calls, storage, and aggregation overhead.

Measure:

- partition count and size distribution;
- duplicated context or overlap;
- map and reduce token or media use;
- cold starts and queueing;
- intermediate storage and transfer;
- failed and duplicate attempts;
- human review and correction;
- total cost per accepted result.

Use larger partitions when dispatch overhead dominates and smaller partitions when context limits, parallelism, or failure isolation justify them.

## Security and data boundaries

- Partition after applying data-class and provider policy.
- Do not distribute secrets or complete private context to every mapper.
- Preserve tenant and source isolation.
- Restrict mapper tools and side effects; map functions should normally be read-only.
- Validate intermediate records as untrusted input to reducers.
- Prevent prompt injection in one partition from changing the global reduce policy.
- Apply human approval before consequential terminal actions.

## Suitable uses

- repository, document, log, record, or media corpus analysis;
- parallel extraction and evidence collection;
- translation or transformation of independent items;
- test generation or evaluation across many cases;
- large-scale classification and tagging;
- summarization with explicit source coverage;
- voting or repeated sampling when the reduce rule is declared.

## Poor fits

Avoid or simplify this pattern when:

- the input is small enough for one reliable call or deterministic tool;
- partitions have strong sequential dependencies;
- every mapper needs complete global context;
- the reduce step cannot recover information lost during mapping;
- side effects require strict serial control;
- dispatch and aggregation cost exceed parallel benefit.

## Strengths

- scales independent work horizontally;
- isolates partition failures;
- reduces per-worker context;
- supports deterministic coverage and aggregation;
- permits heterogeneous infrastructure under one record contract;
- provides clear map and reduce cost attribution.

## Limitations

- partitioning can lose cross-boundary context;
- reducers can become bottlenecks or hide missing partitions;
- duplicate and straggler handling add complexity;
- lossy intermediate records limit final quality;
- total model calls and cost can exceed one-pass processing;
- model outputs are less deterministic than classical map functions.

## Evaluation metrics

Record:

- input and partition coverage;
- map first-pass and terminal success;
- missing, duplicate, malformed, and stale intermediate records;
- straggler and speculative-execution rate;
- reducer correctness, evidence-grounding, and contradiction handling;
- information loss versus full-context baseline;
- speedup, throughput, queueing, and reducer bottleneck;
- token, infrastructure, storage, transfer, and human cost;
- terminal acceptance and cost per accepted result.

Compare against sequential processing, one larger-context call, and a simple parallel workflow. Adopt map-reduce only when partitioned execution improves the complete workload.

## Evidence and established usage

Google's original MapReduce work defines map functions that emit intermediate key-value pairs and reduce functions that merge values associated with the same key, with the runtime handling partitioning, scheduling, communication, and failures. Anthropic documents sectioning as a parallelization workflow for independent subtasks; agent map-reduce adds explicit intermediate and reduction contracts.

Sources:

- [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

## Related concepts

- [Multi-Agent Systems](../..)
- [Graph or DAG Workflow](../graph-dag-workflow/)
- [Pipeline Architecture](../pipeline/)
- [Orchestrator-Worker Architecture](../orchestrator-worker/)
- [Blackboard Architecture](../blackboard/)
- [Task Decomposition](../../../task-decomposition/)
