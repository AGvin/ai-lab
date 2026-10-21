# Documentation Requirements

## Identity and currentness

- Preserve two distinct 470M-class TurboCTC model identities: the standard Granite Speech 5.0 checkpoint and the NC checkpoint.
- Record the standard model's 21 October 2026 card state as multilingual with seven explicitly listed languages: English, French, German, Spanish, Portuguese, Italian and Japanese.
- Keep the NC checkpoint English-only unless its own first-party card changes; do not inherit the standard model's multilingual update.

## Operational decision boundaries

- The standard weights state Apache 2.0; the NC weights state CC-BY-NC-SA-4.0. Hosted availability does not alter downloaded-weight rights.
- Both are automatic speech-recognition models; punctuation/capitalization behavior, accuracy, latency, streaming fit, accents and noise robustness require representative audio evaluation.
- Revision history is not a new model identity: the standard card's earlier English-only state remains historical revision state.

## Validation

- Family membership resolves exactly to the standard and NC 470M checkpoints.
- Producer provenance resolves to IBM.
- Language and license statements remain attached to the exact checkpoint rather than generalized across the family.
- This assessment grants no runtime, benchmark-reproduction, cache or final-render credit.
