# Documentation Requirements

## Requirements

- Use the reader-facing title `Reproducibility`.
- Define reproducibility for this repository as the ability to reconstruct and repeat an evaluation, experiment, benchmark run, or workflow from sufficiently specified artifacts, configuration, data, and operating conditions and obtain results that are consistent within the declared deterministic, statistical, or decision-relevant tolerance.
- Explicitly note terminology variation. Scientific and computing communities use `reproducibility`, `repeatability`, and `replicability` with different conventions; when citing an external source, preserve that source's convention and state how it maps to this repository's operational use rather than claiming one vocabulary is universal.
- Distinguish reproducibility from byte-identical determinism. Exact outputs can be appropriate for deterministic checks, while stochastic generation, parallel/distributed execution, floating-point kernels, sampling, asynchronous systems, or mutable services can require distributional, metric-level, or tolerance-based reproducibility instead.
- Distinguish reproducibility from validity and representativeness. A flawed or unrepresentative evaluation can be reproduced precisely, and reproducibility alone does not prove that the method measures the intended real-world property.
- Require the evaluated unit and artifact identities to be recorded at the level needed to reconstruct the run: model/checkpoint/adapters, code/commit, prompt/instruction/templates, schemas, tool definitions, retrieval corpus/index, datasets, references/rubrics, configuration, and evaluation method versions as applicable.
- Require data and evaluation artifacts to be versioned or content-identified where material. Dataset cases, labels/qrels, preprocessing, chunking/indexing, benchmark rules, judge prompts, and aggregation code can change results even when the model name is unchanged.
- Record runtime/environment conditions that materially affect results: dependency/library/compiler versions, operating system/container/environment, numerical precision/quantization, hardware/topology, drivers/firmware, parallelism, concurrency/load, cache/warm state, and resource limits where applicable.
- Record randomness controls such as seeds, sampling parameters, data shuffling, initialization, and randomized evaluation order when they exist, while making clear that a seed does not guarantee identical behavior across different runtimes, kernels, model/service versions, or execution schedules.
- Treat hosted/provider systems as potentially mutable dependencies. Record explicit model/version/snapshot identifiers when available plus provider/service/API version, date/time or evaluation window, region/configuration, and relevant feature flags; a stable marketing/model alias is not proof of a frozen backend.
- Preserve raw outputs, retrieved items, logs/traces, intermediate measurements, failures/timeouts, and per-example judgments needed to audit aggregate results when feasible. Aggregate scores alone can hide changes in sample membership, parsing, retry logic, or failure handling.
- Define the acceptable reproduction criterion before interpreting reruns where possible: exact match, metric tolerance, confidence interval/distribution overlap, ordering/ranking stability, pass/fail agreement, or another decision-relevant criterion. `Comparable` must not remain undefined when conclusions depend on it.
- Explain that repeated runs can be necessary to characterize stochastic variance. A single matching rerun does not establish stability if the method has substantial run-to-run variation, while a non-identical output can still reproduce the same measured conclusion within a justified tolerance.
- Distinguish artifact availability from reproducibility. Public code/data/container images improve the ability to reproduce a result but do not prove the artifacts are complete, executable, faithful to the reported run, or sufficient to recreate the result.
- Explain that containers, lockfiles, environment managers, workflow systems, infrastructure-as-code, experiment trackers, and archived artifacts are useful implementation mechanisms rather than universal requirements; the requirement is sufficient recoverable specification of material dependencies/conditions.
- Where artifacts cannot be shared because of privacy, licensing, security, contractual, or provider constraints, document the unavailable dependency, access/recreation procedure, relevant hashes/metadata, and resulting limitation on independent verification rather than claiming full reproducibility.
- Distinguish reproducing an evaluation result from replicating a finding under new data, independently reimplemented methods, or changed operating conditions. The latter can strengthen generalization evidence but should be named according to the terminology of the governing field/source rather than silently treated as the same procedure.
- Keep concrete experiment manifests, containers, lockfiles, seeds, model snapshots, datasets, hardware inventories, raw result archives, run IDs, CI/workflow configurations, and reproduction reports with their applicable project/evidence/catalog owners.
- Use the canonical entity references as research inputs for terminology variation, artifact completeness, independent result reproduction, and documented AI-evaluation conditions when reader-facing rendering is activated.

## Validation

- Reproducibility is not equated with byte-identical output, fixed random seeds, artifact availability, or evaluation validity.
- External `reproducibility`/`replicability` terminology is preserved/mapped rather than universalized across disciplines.
- Model/data/prompt/tool/evaluation/runtime identities and material operating conditions are versioned enough to reconstruct the claimed run.
- Hosted mutable service aliases are not assumed to identify immutable backends.
- Raw failures and per-example evidence are not silently lost when they can change aggregate interpretation.
- A tolerance-based reproduction criterion is explicit when exact equality is neither expected nor required.
- Concrete run manifests, artifacts, environments, hardware, and reproduction reports remain outside the reusable reproducibility concept owner.
