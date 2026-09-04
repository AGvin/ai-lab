# Documentation Requirements

## Requirements

- Present Decoding and Sampling as the model-inference learning group for turning model scores into outputs through deterministic/search decoding, stochastic sampling, sampling controls, constrained generation, and schema/grammar-oriented generation.
- Use canonical generation-control concepts for stable semantics; this group teaches how to choose, configure, compare, validate, and debug decoding strategies for concrete workloads.
- Explain that the current materialized subset focuses on `sampling-parameters/` and `constrained-generation/` because both have source-backed legacy tuning/validation teaching ready for migration.
- Do not imply that unmaterialized selected siblings `greedy-and-beam-search/`, `sampling/`, or `structured-generation/` are absent from the logical architecture; standard navigation reflects only physical children.
- Distinguish decoding configuration from upstream task definition. Missing evidence/context, unclear instructions, invalid schemas, unsupported tool/action contracts, or model capability limits are not repaired merely by changing sampling parameters or adding a grammar.
- Require controlled comparison where configuration effects matter: record the full decoding configuration and relevant model/runtime/version/workload identity, vary intentional factors, and evaluate on representative cases rather than attributing hidden configuration differences to the model.
- Treat syntactic/grammar/schema validity as different from semantic/domain validity, safety, authorization, factuality, or appropriateness. Application validation and policy controls remain explicit after decoding.
- Keep provider-specific parameter names/defaults/order, grammar/schema support subsets, deterministic-mode behavior, seed guarantees, APIs, and benchmark measurements with catalog/evidence owners.

## Validation

- Decoding configuration is not treated as a substitute for task/evidence/schema/authorization correctness.
- Syntactically constrained output is not automatically semantically valid or authorized.
- Current navigation exposes only materialized selected children.
- Mutable provider/runtime decoding behavior remains evidence/catalog-owned.
