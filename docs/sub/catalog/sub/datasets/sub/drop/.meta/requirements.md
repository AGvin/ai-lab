# Documentation Requirements

## Requirements

- Represent DROP (Discrete Reasoning Over the content of Paragraphs) as one independently released Ai2 2019 English passage-grounded reading-comprehension dataset requiring reference resolution and operations such as counting, addition and sorting. Do not duplicate an AllenNLP reader, NAQANet model, score, leaderboard, or ARC/OpenBookQA data identity.
- Reconcile the original publisher's **approximately 96,000** questions over about 6,700 passages, with **77,409 train and 9,536 dev** examples documented by TFDS 2.0.0 plus an approximately **9,500-question hidden test** partition. Dataset and evaluator versions must be pinned for comparison; hidden test labels are not available via the public TFDS train/dev builder.
- Explain the **55,000-question count in the final NAACL 2019 abstract** versus the original publisher's 96,000-question release claim as separate original source-scope statements, not an unqualified contradiction resolution.
- Cite Ai2 current open-data listing, the original archived AllenNLP publisher page, original NAACL 2019 paper, Ai2-managed AWS registry and TFDS 2.0.0 builder.
- Preserve the original publisher's express **CC BY-SA 4.0** dataset statement, while noting that the Ai2-managed AWS registry says **CC BY**. Before reuse, determine exact dataset-file licensing, attribution/share-alike obligations, and underlying external passage rights; third-party package, site or code licenses do not override those rights.
- Separate the historical dataset, hidden test, AllenNLP/NAQANet implementation and benchmark metrics. Do not assert current best-model ranking, security certification, or model execution.
- Reuse canonical `catalog/producers/a/ai2` and add one exact reciprocal `produced-by` / `produces` pair. Preserve Ai2's existing ARC and OpenBookQA pairs and the original organization's accepted evidence.
- Reader should include the identity, scope disagreement, source rights, public/hidden split, valid source links and producer provenance; review dependent decision support without unrelated changes.

## Validation

- Exactly one new canonical dataset at `catalog/datasets/drop`, three new authored files, and a dataset-index link.
- Existing Ai2 entity, requirements and reader agree on three original datasets and the reciprocal edge resolves without duplicates.
- Scoped catalog readback is not a complete eight-root clean cycle, final cache/render/schema/CI verification, model run, or comprehensive upstream data-rights audit.

## Scoped original-source qualification — 2026-11-08

- **DROP** is Ai2's originally published 2019 paragraph-based reading comprehension task requiring discrete reasoning. The archived publisher page describes a **~96,000-question** released corpus, with ~77K public train, ~9.5K public dev and similar hidden test. The **55K** statement in the original NAACL paper abstract describes a distinct paper-era scope, not a reason to overwrite released counts.
- Dataset usage rights are **not unambiguously normalized**: the first-party archival source says **CC BY-SA 4.0**, whereas the Ai2-managed AWS registry summarizes the license as **CC BY**. Also distinguish source passage rights, hidden scoring, AllenNLP dataset reader and NAQANet baseline implementation.
- Original sources: https://github.com/allenai/allennlp-website/blob/master/drop.html ; https://allenai.org/open-data ; https://aclanthology.org/N19-1246/ ; https://registry.opendata.aws/allenai-drop/
- The scoped gate accepts only this existing original dataset identity and source-reported release/split/license boundaries. No independent rights/legal/privacy/security audit, hidden test access, model evaluation, global schema/cache/CI/render, clean or final gate.
