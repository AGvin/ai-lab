# Documentation Requirements

## Requirements

- Teach Privacy and Licensing as dataset-use constraints that must be evaluated from the actual source, permissions, consent, legal/license terms, sensitive-data handling, and downstream distribution/use context.
- Preserve source/license/permission/consent metadata with the dataset version when it materially affects training, evaluation, sharing, publication, or derived artifacts.
- Review synthetic data for reproduced personal, confidential, copyrighted, secret, or otherwise restricted content; generated data is not automatically anonymous or redistribution-safe.
- When sensitive source data are used, assess the concrete privacy mechanism and disclosure risk separately from superficial similarity or the label `synthetic`.
- Treat changes in consent, access, takedown status, or licensing as lifecycle events that may require deprecation, removal, retraining, or re-evaluation of downstream artifacts.

## Validation

- Public availability is not treated as permission for every downstream use.
- Privacy claims are tied to concrete mechanisms and evidence.
- Dataset rights/privacy state remains traceable across versions and derived artifacts.
