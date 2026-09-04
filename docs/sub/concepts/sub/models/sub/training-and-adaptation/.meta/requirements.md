# Documentation Requirements

## Requirements

- Use the reader-facing title `Model Training and Adaptation`.
- Present this domain as canonical reusable knowledge about learning model parameters or trainable adaptation components from data, feedback, objectives, or interaction so model behavior/capability changes persist beyond one inference context.
- Distinguish training/adaptation from prompting, retrieval augmentation, tool use, context construction, decoding controls, and runtime execution. Those inference/system mechanisms can alter current behavior without necessarily changing trained model parameters or learned adaptation state.
- Keep `pretraining/`, `fine-tuning/`, and `preference-optimization/` as distinct selected descendants. Fine-tuning can include full-parameter, partial-parameter, or parameter-efficient adaptation; preference optimization uses preference/feedback objectives after or alongside other training stages.
- Explain that training stages are lifecycle roles rather than universal chronological labels. A model can undergo continued pretraining, several fine-tuning stages, preference optimization, distillation, or other adaptation in different sequences, and terminology must be scoped to the specific training lineage.
- Distinguish the base/foundation model from resulting checkpoints, adapters, or derivatives. Concrete model identities and artifacts remain catalog-owned even when this domain explains the adaptation method.
- Explain that training outcomes depend on data, objective/loss, sampling, optimizer, schedule, regularization, architecture, initialization/base checkpoint, numerical precision, distributed strategy, and evaluation conditions; no single training-stage label predicts quality or safety.
- Make clear that adaptation can improve target behavior while degrading other capabilities, calibration, robustness, or safety; regression evaluation and held-out evidence remain separate from the method definition.
- Render the standard direct-child navigation from the validated materialized child set when reader-facing rendering is activated.
- Keep concrete datasets, licenses/provenance, checkpoints, hyperparameter recipes, compute infrastructure, training logs, experiment results, and model-selection decisions with their applicable catalog, evidence, engineering, learning, or decision owners.

## Validation

- Training/adaptation is not equated with prompting, RAG, context injection, or decoding controls.
- Pretraining, fine-tuning, preference optimization, pruning/distillation, and inference optimization are not treated as synonyms.
- Lifecycle stage names are not assumed to imply one mandatory universal pipeline order.
- Concrete model artifacts, datasets, and experiment results remain with their own owners.
- Direct-child navigation contains only currently materialized selected descendants.
