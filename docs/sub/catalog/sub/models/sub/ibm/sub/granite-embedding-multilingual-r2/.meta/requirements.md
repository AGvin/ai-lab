# Documentation Requirements

## Requirements

- Identify Granite Embedding Multilingual R2 as IBM's April 2026 multilingual embedding release family.
- Materialize the 97M and 311M checkpoints separately because they trade throughput/size against retrieval quality.
- Preserve multilingual support, context length, embedding dimensions, benchmark claims, and runtime support only from current model cards.
- Keep rerankers, older English-only variants, and hosted retrieval services separate unless specifically materialized.

## Validation

- Producer provenance resolves to IBM.
- Family membership includes the two multilingual R2 checkpoints.
