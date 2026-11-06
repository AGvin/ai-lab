# Documentation Requirements

## Requirements

- Identify ARC as the original 2018 Ai2 Reasoning Challenge, a concrete grade-school science multiple-choice question dataset, not the unrelated ARC-AGI abstraction benchmark, ARC Prize Foundation work, or a general AI-reasoning concept.
- Preserve 7,787 released questions and the exact separate Easy/Challenge configurations. The official publisher dataset card lists ARC-Challenge as 1,119 train + 299 validation + 1,172 test (2,590) and ARC-Easy as 2,251 train + 570 validation + 2,376 test (5,197); these sum to 7,787 and are not new independently produced benchmark families.
- The Challenge set was curated from questions missed by both a retrieval baseline and a word co-occurrence baseline. This historical filtering does not establish that every current LLM finds every Challenge item difficult or that an accuracy metric captures all reasoning.
- Ai2's original open-data description also references a 14-million-science-sentence corpus; keep that supplemental knowledge corpus distinct from the 7,787-question ARC evaluation dataset and its variants.
- Scope the current Hugging Face card license to its metadata declaration of CC-BY-SA-4.0 for the dataset. The same card's narrative licensing section contains incomplete placeholder language; do not claim a complete independent third-party question-rights clearance. The Apache-2.0 license in the Ai2 Aristo leaderboard repository applies to source code/tools and must not overwrite data licensing.
- Attribute the dataset to Ai2, now styled Ai2 / Allen Institute for AI, using an exact reciprocal Ai2 producer relation. Historical paper authorship is not proof every source question was originally written by an individual Ai2 employee or that a different ARC acronym shares ownership.
- Treat original public questions, mirrors, test splits, prompting, answer normalization, evaluation scoring and published leaderboard values as version-/protocol-sensitive; contamination risk means no uncontaminated current-model score can be inferred from public availability.
- Report current Ai2 public source page, official dataset card, original paper, original Ai2 leaderboard/tool repository and separate Apache-2.0 software license. No model run, scores, production deployment, data transfer or comprehensive data-rights/beneficial-ownership audit was performed.
- Render standard current-entity relations through the validated entity relation projection; require all canonical links to resolve.

## Validation

- Exactly one ARC source-dataset identity; Easy/Challenge are internal split configurations, not separate producer or dataset entities.
- Ai2 produced-by / produces must resolve bidirectionally and remain distinct from ARC Prize/ARC-AGI.
- The data-code license boundary, counts and contamination caveat are accurate and source-backed.
- Full schema/cache/CI/global reader/render and clean eight-root research passes must not be claimed from a scoped addition.
