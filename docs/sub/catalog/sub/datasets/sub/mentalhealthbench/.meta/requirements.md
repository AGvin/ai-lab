# Documentation Requirements

## Requirements

- Identify MentalHealthBench as OpenAI's open benchmark for evaluating AI responses in realistic mental health conversations, developed with licensed mental health experts.
- Preserve the current first-party benchmark scope across everyday mental health situations and more urgent scenarios, including the documented adult, teen, caregiver, and clinician personas only while supported by current OpenAI material.
- Preserve the benchmark's expert-defined behavior evaluation boundary, including safety, context seeking, user agency, and actionable guidance, without turning those dimensions into general clinical claims.
- Keep MentalHealthBench distinct from ChatGPT product safeguards, policy documents, individual evaluated models, model scores, crisis-response procedures, and generic mental-health safety concepts.
- Treat expert-participant counts, represented countries, persona definitions, behavior dimensions, evaluation methodology, evaluated-model roster, scores, and released artifacts as freshness-sensitive.
- Preserve OpenAI producer provenance through the canonical relation.
- Do not generalize benchmark performance into a claim that an AI system is a substitute for professional mental-health care or is clinically validated outside the benchmark's stated evaluation scope.

- Render the complete visible current-node relation set through the standard `entity-relations` component as a provenance block; preserve relation semantics and canonical target identities.
- Render an `official-resources` block with this explicit selection from canonical references: [MentalHealthBench release and expert rubric methodology](https://openai.com/index/introducing-mentalhealthbench/).

## Validation

- MentalHealthBench remains a concrete released benchmark/dataset identity rather than a generic mental-health safety concept.
- OpenAI provenance resolves bidirectionally.
- Quantitative and comparative claims remain scoped to the exact benchmark revision and evaluation setup.
- Reader-facing wording preserves the distinction between benchmarked conversational behavior and clinical efficacy.

## Scoped original-source qualification — 2026-11-08

- **MentalHealthBench** is OpenAI's original **2026-09-23** open conversational-behavior benchmark developed with **over 80 licensed mental-health experts across 22 countries**. It consists of **1,215 synthetic conversations**, split into **650 non-acute, 221 high-acuity and 344 emergent** scenarios, covering adult, explicitly age-identified teen, caregiver and clinician personas; these are research examples and not patient medical records or live therapy sessions.
- Expert-written and cross-reviewed weighted rubrics evaluate responses to the **final user turn**, rewarding safety, eliciting context, preserving agency and context-appropriate guidance. The original grading uses an automated judge pinned to a specific model/revision and evaluation setup; results do not certify the model as a psychotherapist, guarantee appropriate crisis intervention, or establish the clinical efficacy of a deployed conversational product.
- First-party publisher sources: https://openai.com/index/introducing-mentalhealthbench/ ; https://deploymentsafety.openai.com/gpt-6-1-terra/mentalhealthbench .
- Scoped original-source acceptance covers this pre-existing synthetic dataset identity, release, expert rubric and acuity/persona boundaries only. No patient data processing, actual therapeutic or clinical evaluation, independently rerun grader/model, complete privacy/legal/security and component-rights audit, full CI/renderer, clean or final acceptance.
