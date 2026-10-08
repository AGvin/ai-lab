# Documentation Requirements

## Requirements

- Identify AILuminate as MLCommons' family of released generative-AI safety and security benchmarks, with the general-purpose chatbot safety benchmark as the established core evaluation surface.
- Preserve AILuminate Safety v1.1 as the current released safety revision only while supported by current MLCommons material; keep language coverage, hazard taxonomy, personas, prompt inventory, evaluator composition, grading thresholds, supported interaction modes, official/practice-test boundaries, and published results freshness-sensitive.
- Preserve the benchmark's end-to-end system-under-test boundary: a tested chatbot system may include models, prompts, guardrails, retrieval, and other workflow components, so results must not automatically be attributed to the underlying base model alone.
- Keep safety, jailbreak, and future AILuminate benchmark variants within the family boundary unless their independent lifecycle and reader value justify separate canonical nodes.
- Keep individual prompts, evaluator models, vendor systems, policies, safety frameworks, and generic AI-risk concepts separate from the AILuminate identity.
- Preserve MLCommons producer provenance through the canonical relation.
- Do not interpret a favorable AILuminate grade as proof that a system is risk-free, clinically safe, unbiased, or safe outside the benchmark's tested hazards, languages, personas, and interaction scope.

## Validation

- The node remains the AILuminate benchmark-family identity rather than one vendor system, evaluator, prompt set, or generic safety concept.
- Safety-version facts and language availability remain tied to the exact released revision.
- MLCommons provenance resolves bidirectionally.
- Reported grades remain scoped to the tested fixed system and benchmark configuration.
