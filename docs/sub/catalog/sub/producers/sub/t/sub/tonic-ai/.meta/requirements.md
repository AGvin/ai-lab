# Documentation Requirements

## Requirements

- Identify Tonic.ai as the producer identity for Tonic Fabricate.
- Keep Fabricate distinct from other Tonic products unless separately materialized.
- Render the standard `entity-relations` block from validated current-entity relations.
- Preserve this source-backed identity and provenance context: Tonic.ai is the producer identity for Tonic Fabricate. Its official documentation separates Fabricate's generation of relational data, unstructured datasets and mock APIs from the distinct Tonic Structural and Tonic Textual products.
- Explain the following operating and decision boundary: Choose the product that matches the data workflow: generating new synthetic data, transforming existing structured data and redacting unstructured material have different inputs and controls. Do not transfer a privacy or capability claim between Tonic products solely because they share a producer. Review the selected product's data inputs, connected systems, output validation and subscription terms before using generated data in a development or AI workflow.
- Support the producer context with these first-party sources: <https://www.tonic.ai/products/fabricate>, <https://www.tonic.ai/docs>.

## Validation

- `produces` is the inverse of Tonic Fabricate `produced-by`.
