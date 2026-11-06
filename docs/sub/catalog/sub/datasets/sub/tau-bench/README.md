# τ-bench

τ-bench is Sierra’s maintained benchmark family for customer-service agents interacting with simulated users, policies and tools. Task and environment state determine success. The original τ-bench, τ² dual-control evaluation, τ³ knowledge/voice work and current 2.0 release describe versioned evaluation setups within this family.

## Version and score boundaries

Current upstream 2.0 introduces multilingual evaluation across six languages and separates frozen text and voice benchmark definitions. English inputs and grading also changed, so 2.0 scores are not comparable to the 1.x leaderboard. Use the v1.0.1 release for legacy comparisons. Its July 22, 2026 release corrected banking_knowledge grading and task data; results on that domain from before the correction require separate treatment. Record the exact release, task set, modality, language, user simulator, model and judges.

## Domains and operation

Retail, airline, telecom and banking-knowledge scenarios simulate service policies and tool actions; they are not real Sierra banking or travel products. Full-duplex voice adds provider-specific audio and caller-voice setup, while text uses a turn-based interaction. Current repository voice identifiers can be Sierra-internal and require replacement with the evaluator’s own configuration. MIT licensing applies to the repository; model and voice APIs can have separate accounts, costs and data terms. A dry run can inspect the planned calls before a paid evaluation.

## Relations

- Produced by: [Sierra](../../../producers/sub/s/sub/sierra/)

## Official resources

- [Official benchmark site](https://taubench.com/)
- [τ-bench upstream](https://github.com/sierra-research/tau2-bench)
- [τ³ knowledge research](https://sierra.ai/resources/research/tau-3-bench-knowledge)
- [Legacy v1.0.1 grading correction](https://github.com/sierra-research/tau2-bench/releases/tag/v1.0.1)
- [Repository license](https://github.com/sierra-research/tau2-bench/blob/main/LICENSE)
