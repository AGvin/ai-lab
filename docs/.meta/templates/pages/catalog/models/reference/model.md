# Concrete Model Page

## Description

Canonical profile for one concrete trained-model identity within a family or series.

## Purpose

Give readers the stable technical identity and intrinsic facts of one concrete model while delegating release deltas, artifacts, deployment conclusions, and recommendations to their correct owners.

## Use When

Use for exact concrete model identities such as Qwen3 30B-A3B.

## Do Not Use When

Do not use for a family, series, version/checkpoint, downloadable representation, hosted model route, or selection recommendation.

## Owns

- concrete model identity;
- parent family/series and producer relationships;
- architecture and parameter structure at model scope;
- stable licensing/training-stage facts when supported;
- model-scoped capability statements with source attribution boundaries;
- navigation to versions and artifacts.

## Does Not Own

- chronological release differences;
- quantization/package identity;
- runtime memory as inferred from artifact size;
- hardware-fit, workload suitability, rankings, or deployment strategy;
- mutable hosted-provider behavior unless explicitly scoped as external access context.

## Expected Inputs

Requirement-approved display values, canonical relations, stable model facts, source-scoped technical claims, version/artifact navigation, and authoritative resources.

## Composition

1. default header;
2. parent/producer relations;
3. model identity and architecture overview;
4. key stable technical facts in a scan-friendly structure when requirements justify them;
5. important interpretation boundaries and limitations;
6. navigation to versions/artifacts;
7. `official-resources`.

## Variants

Dense, MoE, multimodal, specialist, base, instruct, or derivative models reuse this family when they remain one concrete model identity. Specialized facts appear only when requirements and evidence support them.

## Representative Example

- Qwen3 30B-A3B.

## Anti-patterns

- treating active parameters as total model size or dense-model equivalence;
- flattening version deltas into the model page;
- using published file size as peak RAM/VRAM;
- inserting selection guidance as intrinsic model fact.
