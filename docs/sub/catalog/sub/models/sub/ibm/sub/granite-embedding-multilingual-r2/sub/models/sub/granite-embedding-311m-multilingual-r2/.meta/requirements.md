# Documentation Requirements

## Identity and provenance

- Identify Granite Embedding 311M Multilingual R2 as the larger concrete R2 embedding checkpoint.
- Preserve its reciprocal has-derivative relation to Granite Embedding 97M Multilingual R2 because the 97M card explicitly documents the reduction from this checkpoint.

## Operational decision boundaries

- Preserve the documented 32,768-token maximum sequence length, 768-dimensional default embeddings and Matryoshka outputs at 768, 512, 384, 256 and 128 dimensions.
- Broad multilingual coverage is not a guarantee of uniform retrieval quality; evaluate representative query/document pairs and the selected embedding dimension.
- Weights state Apache 2.0. ONNX/OpenVINO conversions and endpoint implementations remain artifacts or runtimes.

## Validation

- Membership resolves to Granite Embedding Multilingual R2.
- has-derivative resolves reciprocally to the 97M node's derived-from relation.
- This assessment grants no runtime or benchmark-reproduction credit.
