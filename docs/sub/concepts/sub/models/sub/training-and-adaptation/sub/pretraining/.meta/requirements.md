# Documentation Requirements

## Requirements

- Use the reader-facing title `Pretraining`.
- Define pretraining as an initial or foundational training stage in a model lineage that learns broadly reusable representations, capabilities, or predictive structure from a relatively broad training distribution before later task/domain specialization.
- Avoid defining pretraining solely by dataset size, compute scale, self-supervision, or one modality. Large-scale self-supervised learning is central to many modern foundation models, but supervised, multimodal, generative, contrastive, masked-prediction, autoregressive, or other objectives can participate depending on the model family.
- Distinguish pretraining from fine-tuning by lifecycle role and intended generality rather than by one universal token/data/step threshold. Continued pretraining can start from an already pretrained checkpoint and further train on broad or domain-shifted data while still serving a pretraining-like adaptation role.
- Distinguish pretraining from ordinary inference-time prompting, retrieval augmentation, context injection, and tool use. Those mechanisms do not update the pretrained model parameters by themselves.
- Explain that pretraining can create a base/foundation checkpoint whose downstream behavior is later changed through fine-tuning, instruction tuning, preference optimization, parameter-efficient adaptation, distillation, or other stages; no one downstream sequence is mandatory.
- Make clear that broad pretraining data can encode useful regularities as well as bias, error, duplication, contamination, stale information, harmful content, privacy risks, or licensing/provenance issues; broad scale is not automatic evidence of quality or safety.
- Explain that a pretrained model's apparent knowledge is not an authoritative or current database and that training-cutoff/provenance limits differ across concrete models and datasets.
- Distinguish the abstract pretraining method from concrete pretraining datasets, corpus mixtures, model checkpoints, compute runs, training frameworks, and experiment evidence, which retain their applicable catalog/evidence/project owners.
- Treat tokenizer/representation, architecture, objective/loss, optimizer/schedule, data mixture, filtering/deduplication, precision, distributed strategy, and evaluation as important design dimensions without turning one modern LLM recipe into the universal pretraining definition.
- Keep exact training-token counts, datasets, licenses, compute budgets, hyperparameters, contamination audits, model-specific curricula, and current provider training claims with their applicable catalog, evidence, engineering, governance, or project owners.
- Use the canonical entity references as research inputs for current pretraining terminology and foundation-model lifecycle boundaries when reader-facing rendering is activated.

## Validation

- The page does not define pretraining by one universal minimum dataset, parameter count, compute budget, or number of steps.
- Self-supervision or next-token prediction is not presented as the only possible pretraining objective.
- Pretraining is distinguished from fine-tuning by role/context rather than simply `larger scale`.
- Prompting, RAG, context injection, and tool use are not mislabeled as pretraining.
- Broad pretraining is not presented as evidence of current, attributable, unbiased, legally usable, or safe knowledge.
- Concrete datasets/checkpoints/training runs remain outside the abstract concept owner.
