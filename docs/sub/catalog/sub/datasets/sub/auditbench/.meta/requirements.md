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

## Scoped original-source qualification — 2026-11-08

- **AuditBench** is Anthropic's original **2026-03-10** release for assessing investigator-agent performance in alignment audits, with **56 deliberately fine-tuned target language models representing 14 hidden-behavior categories**. The target model checkpoints, implanted hidden behavior types, auditor tool configurations and evaluator are components of this one benchmark/testbed, not 56 independent AI Lab dataset identities or evidence of widespread real-world hidden behavior.
- The original research separately compares investigator tools across **13 evaluation tool configurations**, with black-box prompt generation, controlled tests and white-box interpretability surfaces. Publisher results depend on the injected target model, audit agent, generated test prompts and grading rubric; detected behavior is not proof that a commercial production model exhibits the same hidden tendencies or that an auditor can guarantee disclosure.
- First-party sources: https://alignment.anthropic.com/2026/auditbench/ ; https://arxiv.org/abs/2602.22755 .
- Scoped source gate covers the existing research benchmark's original publisher, 56/14/13 evaluation scope and methodological limits only; no trained checkpoints downloaded or audited, executable evaluator run, independent model-risk assurance, full redistribution/legal/security/privacy review, missing reader reconstruction, global CI/render, clean or final credit.
