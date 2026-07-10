# Data Residency

Data residency specifies the geographic or jurisdictional location where data is stored or processed.

## Core idea

AI workflows may transmit prompts, files, embeddings, logs, and backups across several services and regions. Residency requirements therefore apply to the entire processing chain, not only the primary model endpoint.

## Practical questions

- Where are prompts and uploaded files processed?
- Where are logs, caches, backups, and embeddings stored?
- Can support staff access data from another jurisdiction?
- Which subprocessors and regions are involved?
- Is regional failover allowed?

## Trade-offs and limitations

Restricting regions can reduce provider choice, availability, or performance. A regional endpoint may still rely on globally operated control systems unless the provider contract explicitly defines boundaries.

## Common mistakes

- Confusing data residency with data privacy or sovereignty.
- Checking only the model API and ignoring telemetry.
- Assuming a company address determines processing location.
- Failing to document backup and disaster-recovery regions.

## Related concepts

- [Safety, Privacy, and Reliability](../../)
- [Data Privacy](../data-privacy/)
- [Provenance](../provenance/)
- [Model Selection](../../../evaluation-and-operations/sub/model-selection/)
