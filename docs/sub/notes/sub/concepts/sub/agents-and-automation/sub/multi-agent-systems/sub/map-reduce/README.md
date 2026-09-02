# Map-Reduce Agent Architecture

Legacy residual retained for map/reduce-specific workflow pedagogy, partition/aggregation contracts, and exact foundational provenance because the selected workflow-fundamentals learning owner is not yet materialized on the active branch.

> **Migration note:** Generic MapReduce/fan-out/fan-in workflow semantics and the exact Anthropic `Building effective agents` research source are already preserved in `docs/sub/concepts/sub/agents-and-autonomy/sub/workflows-and-orchestration/`. The readiness design routes substantive composition teaching to workflow-fundamentals/manager-worker learning as appropriate, but the selected `learning/areas/agents-and-automation/workflows-and-orchestration/workflow-fundamentals/` node is currently absent on the active AI Lab ref. Preserve the map/reduce-specific material and the non-duplicated Google MapReduce provenance below until its learning/evidence owners are ready.

## Translations

- English
- [Українська](./l10n/uk_UA/)

## Workload and partition residual

Map-reduce is useful when one bounded map contract can process partitions independently and normalized intermediate records can be combined under an explicit grouping/reduction contract. Arbitrary parallel multi-agent work is not map-reduce when partition completeness, intermediate schemas, grouping, and reduction are undefined.

For a non-trivial job, record where relevant:

- job/version identity and immutable input snapshot;
- partition strategy and manifest;
- map implementation/model/prompt/tools/version;
- intermediate record schema and keys;
- grouping/shuffle/ordering and optional combiner policy;
- reduce implementation/model/prompt/tools/version;
- validation/evidence requirements;
- retry/straggler/partial-failure policy;
- terminal acceptance criteria.

The partition manifest should establish which source units were assigned, intentionally duplicated, excluded, failed, or left unprocessed. Preserve stable item identity/source spans and validate semantic partitioning independently because a model-derived partition can omit or distort coverage.

## Map and intermediate-record residual

A mapper should receive one declared partition, bounded task/acceptance criteria, exact output schema, source/evidence requirements, permissions/data boundaries, and a resource/retry envelope.

Intermediate records should preserve enough structure to support deterministic aggregation, for example job/partition identity, source unit/span, grouping key, structured value, evidence/artifact reference, producer/model version, validation status, uncertainty, and abstention.

Map workers should report local findings and missing context rather than inventing global conclusions that require unseen partitions.

## Grouping, combiner, and reduce residual

Before reduction, validate schemas, reject/quarantine malformed records, deduplicate stable IDs, group by declared keys, preserve provenance/order where material, identify missing/failed partitions, and enforce memory/size limits. Prefer deterministic grouping when the manifest and keys can establish membership exactly.

A local combiner is safe only when its reduction is semantically compatible with later aggregation. Deterministic counts/sums/sets or explicitly loss-aware local summaries can be appropriate; lossy summarization is dangerous when rare evidence, minority findings, exact source text, or cross-partition contradictions matter.

A reducer should receive normalized grouped records plus the partition manifest, verify completeness/unresolved failures, apply declared combination rules, detect contradiction/duplication/missing evidence, preserve source traceability, distinguish aggregate fact from inference/recommendation/unknown, and abstain or escalate when the aggregate is insufficient.

Use deterministic reducers for exact aggregation/join/schema/coverage operations and model reducers for semantic synthesis or contradiction analysis. Do not ask a model to recompute exact aggregates from prose when structured records already contain the values.

Hierarchical reduction can keep context bounded, but every additional summarization/reduction layer needs explicit information-loss evaluation.

## Straggler, partial-result, and cost residual

Define map attempt limits, stable output/record identities, whether speculative duplicate execution is allowed, winner/duplicate policy, timeout/cancellation, required versus optional partitions, minimum coverage for partial results, fallback/escalation, and terminal failure when missing input is material.

Do not silently reduce only successful partitions and label the result complete.

Map-reduce can lower per-call context while increasing total calls/tokens, queueing, storage, transfer, duplicate work, and aggregation overhead. Tune partition size against context limits, parallelism, dispatch overhead, failure isolation, and accepted-result quality rather than assuming finer partitioning is cheaper or faster.

## Security and evaluation residual

Apply data-class/provider policy before partitioning; avoid distributing unnecessary secrets or full private context to every mapper; preserve tenant/source isolation; keep mapper effects bounded; validate intermediate records as untrusted reducer input; and prevent content in one partition from changing the global aggregation/control policy.

Evaluate source/partition coverage, mapper first-pass/terminal success, missing/duplicate/malformed/stale records, straggler/speculative-execution rate, reducer correctness/evidence grounding/contradiction handling, information loss versus fuller-context baselines, throughput/queueing/reducer bottlenecks, complete token/infrastructure/storage/transfer/human cost, and terminal acceptance/cost per accepted result.

Compare against sequential processing, one larger-context call, and simpler parallel workflows; use map-reduce only when its explicit partition/aggregation structure improves the complete workload.

## Legacy evidence-provenance residual

The legacy source used Google's original MapReduce work for the foundational map/intermediate-key/reduce/runtime contract:

- [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)

The legacy Anthropic source is already preserved exactly in the canonical Workflows and Orchestration entity and is therefore not duplicated here solely for provenance.

These map/reduce-specific pedagogical and evidence fragments remain migration source material until their selected learning/evidence owners are ready.
