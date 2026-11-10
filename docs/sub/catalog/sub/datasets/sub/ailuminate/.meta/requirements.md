# Documentation Requirements

## Requirements

- Identify AILuminate as MLCommons' family of released generative-AI safety and security benchmarks, with the general-purpose chatbot safety benchmark as the established core evaluation surface.
- Preserve versioned AILuminate Safety releases, including current Safety v1.2 (2026-09-09), and keep each revision's languages, hazard taxonomy, personas, prompt inventory, evaluator composition, grading scale, interaction modes, official/practice-test boundaries and results separate. Do not treat v1.1 scores or the old model-based judge as current v1.2 protocol.
- Preserve the benchmark's end-to-end system-under-test boundary: a tested chatbot system may include models, prompts, guardrails, retrieval, and other workflow components, so results must not automatically be attributed to the underlying base model alone.
- Keep safety, jailbreak, and future AILuminate benchmark variants within the family boundary unless their independent lifecycle and reader value justify separate canonical nodes.
- Keep individual prompts, evaluator models, vendor systems, policies, safety frameworks, and generic AI-risk concepts separate from the AILuminate identity.
- Preserve MLCommons producer provenance through the canonical relation.
- Do not interpret a favorable AILuminate grade as proof that a system is risk-free, clinically safe, unbiased, or safe outside the benchmark's tested hazards, languages, personas, and interaction scope.

- Reconcile the reader with the source-backed identity, access and interpretation context in canonical `entity.identity_note`.
- Render the standard `entity-relations` block from the validated current-entity relation projection.

## Validation

- The node remains the AILuminate benchmark-family identity rather than one vendor system, evaluator, prompt set, or generic safety concept.
- Safety-version facts and language availability remain tied to the exact released revision.
- MLCommons provenance resolves bidirectionally.
- Reported grades remain scoped to the tested fixed system and benchmark configuration.

## Scoped original-source qualification — 2026-11-08

- **AILuminate Safety** is MLCommons' continuing original safety-benchmark family, with **Safety 1.2 released on 2026-09-09** after the older v1.1 English/French-era catalog profile. The new 1.2 benchmark updates **all three core measurement components**: an MLCommons-trained evaluator rather than changing third-party general-model judges, a **3,900-prompt Problem Set 2.0** selected from the previous 12,000 official prompts, and a fixed-reference **0–100 rating scale** rather than the previous relative Poor-to-Excellent categories.
- Results under v1.1 and v1.2 are not interchangeable, even for the same system/model. A tested system may include prompts, retrieval, filtering, guardrails, model API settings and a complete interaction configuration; a result is not universal safety certification, clinical suitability or an intrinsic base-model score. Official testing, public practice examples and published submitted-system records have different rules and access.
- The pre-existing entity note and reader still describe v1.1 as current, so canonical metadata/current reader must be reconciled separately with version, language and evaluator evidence; this scoped original-source gate does not claim that repair or any clean pass.
- First-party publisher sources: https://mlcommons.org/ailuminate/safety/ ; https://mlcommons.org/benchmarks/ailuminate/ .
- Source qualification covers one previously materialized MLCommons benchmark family and original release/version/protocol changes only. No real model tested, public prompt pack copied, independent safety/legal/security audit, entity/reader repair, whole-repo schema/cache/CI/render, clean or final credit.
