# Documentation Requirements

## Requirements

- Teach Pretraining as base-model training before downstream adaptation, with objective, modality, architecture, data, scale, and implementation choices treated as explicit design dimensions rather than one universal recipe.
- Verify the exact data mixture/version, tokenizer or processor, architecture/configuration, objective, optimizer/schedule, precision, distributed topology, checkpoint format, monitoring, and recovery plan before expensive stages.
- Evaluate meaningful checkpoints for optimization stability, capability trends, contamination/leakage indicators, bias/safety regressions, and data-quality failures while preserving a sufficiently independent acceptance boundary.
- Compare scaling, curriculum, or data-mixture changes against matched baselines and record compute/data/objective/implementation differences explicitly.
- Record training-data lineage and material rights/restrictions, run ownership, compute budget, artifact destinations, incident/restart history, and the exact checkpoint promoted downstream.
- Link general dataset engineering and governance to Data and Knowledge rather than duplicating those owners here.

## Validation

- Pretraining remains distinct from continued pretraining and post-training adaptation.
- Repeatedly observed benchmarks are not silently promoted into the final independent acceptance set.
- Promoted checkpoints remain traceable to the run state, data lineage, and evaluation evidence that produced them.
