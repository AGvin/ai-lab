# Documentation Requirements

## Requirements

- List only materialized concrete Gemini model identities for which no separate stable series node is required.
- Keep hosted aliases, API products, snapshots, and selection routes out of this collection unless they satisfy the canonical model/version taxonomy.

## Validation

- Every listed child is a concrete model identity.
- The collection does not invent an empty series level.

## Verified identity and provenance

Navigation index of concrete Gemini model identities, including released historical identities; it is not a trained model or a serving endpoint.

## Source-scoped operating boundaries

- Keep model IDs and lifecycle qualifications visible on linked profiles. Stable models, allowlisted GA variants, retired previews, and aliases that route to another model are different selection states. [Model inventory](https://ai.google.dev/gemini-api/docs/models) · [Lifecycle table](https://ai.google.dev/gemini-api/docs/deprecations).
- Capabilities and operational constraints belong to each concrete profile; an index entry does not imply uniform tools, Live API access, or media generation.

## Source evidence

- <https://ai.google.dev/gemini-api/docs/models>
- <https://ai.google.dev/gemini-api/docs/deprecations>
