# Documentation Requirements

## Requirements

- Identify AuditBench as Anthropic's released benchmark/testbed for evaluating investigator-agent performance when auditing language models for hidden behaviors.
- Preserve the first-party benchmark boundary: the released suite contains 56 target language models with implanted hidden behaviors spanning 14 categories, and evaluates investigator-agent behavior across multiple tool configurations only while supported by the current official release.
- Keep the benchmark identity distinct from Anthropic's investigator agent implementation, the released target models, individual auditing tools, evaluation results, and general alignment-auditing methodology.
- Treat target-model counts, hidden-behavior categories, tool configurations, released artifacts, and reported results as version-sensitive facts that must be re-checked against current first-party evidence.
- Preserve the benchmark's intended research use as an auditing testbed without generalizing benchmark performance into claims about real-world model safety or audit completeness.

## Validation

- AuditBench is represented as a concrete benchmark/dataset identity rather than a generic alignment-auditing concept.
- The benchmark is not conflated with the investigator agent or with the hidden-behavior model collection as separate software/model products.
- Quantitative claims remain scoped to the released benchmark revision and evaluation setup.
