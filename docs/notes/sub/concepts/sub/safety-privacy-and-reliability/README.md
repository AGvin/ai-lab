# Safety, Privacy, and Reliability

Concepts for controlling model behavior, protecting data, and reducing operational risk in AI systems.

## Translations

- English — current
- [Українська](./l10n/uk_UA/)

Concepts are grouped by practical priority. Priority affects reading order, not thematic placement.

## Essential

- [`prompt-injection/`](./sub/prompt-injection/) — Input designed to override or manipulate an AI system's intended instructions.
- [`indirect-prompt-injection/`](./sub/indirect-prompt-injection/) — Malicious or conflicting instructions embedded in external content processed by an AI system.
- [`trust-boundaries/`](./sub/trust-boundaries/) — Explicit separation between trusted instructions, trusted systems, users, and untrusted data.
- [`least-privilege/`](./sub/least-privilege/) — Granting an AI system only the permissions required for its current task.
- [`sandboxing/`](./sub/sandboxing/) — Isolating execution so failures or malicious behavior have limited impact.
- [`secret-handling/`](./sub/secret-handling/) — Protecting credentials, tokens, keys, and other sensitive operational data.
- [`data-privacy/`](./sub/data-privacy/) — Controlling how personal, confidential, or sensitive data is collected, processed, retained, and shared.
- [`retrieval-poisoning/`](./sub/retrieval-poisoning/) — Manipulating indexed knowledge so retrieval supplies misleading or malicious context.

## Useful

- [`guardrails/`](./sub/guardrails/) — Controls that validate, restrict, or monitor model inputs, outputs, and actions.
- [`data-residency/`](./sub/data-residency/) — The geographic or jurisdictional location where data is stored or processed.
- [`provenance/`](./sub/provenance/) — Information about the origin, ownership, transformation, and custody of data or model artifacts.
- [`content-moderation/`](./sub/content-moderation/) — Detecting or restricting content according to safety, legal, or platform policies.

## Specialized

- [`jailbreaking/`](./sub/jailbreaking/) — Attempts to bypass a model's configured safety or policy constraints.
- [`model-alignment/`](./sub/model-alignment/) — Shaping model behavior toward intended goals, values, policies, or preferences.
- [`data-poisoning/`](./sub/data-poisoning/) — Corrupting training or adaptation data to degrade or manipulate model behavior.
