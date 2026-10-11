# Documentation Requirements

## Requirements

- Identify `tau3-bench` (τ³-bench) as Sierra Research's publicly released successor evaluation suite for policy-constrained tool-using conversational agents, with simulated users, domain APIs, task goals, grading and reproducible trajectory evaluation.
- Preserve historical lineage: original τ-bench evaluated text-only agent/user/tool interactions in airline and retail; τ² introduced dual-control evaluation; the current τ³ release expands to real-time voice and knowledge-retrieval tasks, fixes legacy tasks and retains compatibility boundaries. The upstream repository remains named `sierra-research/tau2-bench`, but repository slug is not evidence that τ² is the current named release.
- The official July 2026 **v1.0.1** grading correction changes `banking_knowledge` task outcomes; scores before and after v1.0.1 must not be treated as directly comparable for that domain. Keep exact version, task split, evaluator implementation, model/user simulator, API provider, and text-versus-full-duplex-voice modality explicit when explaining benchmark scores.
- Distinguish current customer-service tool-policy benchmark from WebArena-style browser navigation, Terminal-Bench shell tasks, GAIA general assistant tasks, knowledge-only QA datasets, agent-evaluation software frameworks and third-party leaderboards. Domain examples and simulator components are not separate canonical benchmark identities.
- Treat downloadable task inventories, evolving domain count, task fixes, compatible inference providers, optional dependencies and releases as mutable, verifiable upstream facts.
- Keep Sierra as the primary benchmark producer with reciprocal `produced-by` / `produces` metadata, without confusing third-party model providers used for simulations with benchmark authors.

## Validation

- Latest released τ³ name/version, task corpus, change log and current source repository correspond to first-party evidence.
- Any numerical comparison pins grading version, domain/task split, model/harness and conversation modality.
- No separate duplicate canonical τ, τ² and τ³ nodes are created from historical release names alone.
- The Sierra `produces` relation reciprocates this dataset's `produced-by` target.
