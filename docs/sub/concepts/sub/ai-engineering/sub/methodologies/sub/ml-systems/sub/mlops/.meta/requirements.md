# Documentation Requirements

## Requirements

- Use the reader-facing title `MLOps` and expand it as `Machine Learning Operations` on first use.
- Define MLOps as the engineering/operational discipline for managing the machine-learning lifecycle from development and experimentation through reproducible validation, release, deployment, monitoring, maintenance, governance, and retirement or replacement.
- Explain that MLOps adapts DevOps principles to ML-specific state and change surfaces such as data, features, training code, model artifacts, evaluation results, environments, lineage, and model behavior. It is not merely CI/CD for one model file.
- Cover automation and reproducibility across appropriate lifecycle stages: versioned code/configuration/data/model artifacts, repeatable pipelines/environments, automated testing/evaluation, controlled promotion/deployment, monitoring, rollback/recovery, and traceable lineage where material.
- Distinguish continuous integration, continuous delivery/deployment, and continuous training. A system can consume externally produced foundation models and therefore need no continuous-training pipeline while still benefiting from MLOps/LLMOps/GenAIOps lifecycle controls.
- Treat model/data drift and behavioral degradation as monitoring/evaluation triggers whose response may include investigation, prompt/retrieval/application changes, model upgrades, retraining, rollback, or no change depending on root cause; do not prescribe automatic retraining as universal remediation.
- Explain governance and provenance as operational evidence: teams should be able to identify which code, model, data/evaluation assets, configuration, environment, and approvals produced or promoted a deployed state to the degree required by risk and reproducibility needs.
- Explain that `LLMOps`, `FMOps`, and `GenAIOps` are ecosystem terms for specialized operational concerns around large/foundation/generative models. Treat them as contextual specializations/variants of the broader lifecycle discipline here unless future architecture separately selects an independent canonical concept.
- For generative-AI applications, cover prompt/context/retrieval configuration, model/provider upgrades, evaluation gates, cost/latency/quality monitoring, safety/security tests, and user-feedback loops as additional lifecycle surfaces where applicable.
- Keep concrete cloud products, model registries, pipeline engines, CI/CD systems, observability products, vendor maturity levels, deployment commands, and organization-specific operating processes with their applicable catalog or project owners.
- Use the canonical entity references as research inputs for current MLOps/GenAIOps terminology and lifecycle boundaries when reader-facing rendering is activated.

## Validation

- MLOps is lifecycle-wide and not reduced to deployment, monitoring, CI/CD, or retraining alone.
- ML-specific artifacts/state and ordinary software artifacts are both represented where relevant.
- Continuous training is not assumed necessary for systems that consume externally produced models.
- LLMOps/FMOps/GenAIOps are not materialized as duplicate peer concepts without a separate architecture decision.
- Drift does not automatically imply retraining, and automation does not remove governance/validation requirements.
- Concrete vendor tooling remains outside the reusable methodology owner.
