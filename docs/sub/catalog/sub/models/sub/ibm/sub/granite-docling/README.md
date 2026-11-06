# Granite Docling

Granite Docling is IBM's document-conversion model family, represented by the separately released 258M image-text checkpoint. It converts document images to structured output, including layout, tables and equations.

## Boundaries

The trained model weights are distinct from the Docling software pipeline and runtime-specific distribution artifacts. Evaluate both transcription and structure on representative full pages and regions. English support is distinct from experimental Japanese, Arabic and Chinese capabilities. Published weights use Apache-2.0; hosted service terms are separate.

## Model and official source

- [Granite Docling 258M](./sub/models/sub/granite-docling-258m/)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-docling-258M)

## Deployment validation

Pin the exact checkpoint revision and compatible runtime version. Measure memory, latency and document-conversion quality on representative inputs. Check runtime-specific artifacts and hosted-service terms separately from the downloaded-weight license.

Published benchmark results are producer claims; this page does not establish independent benchmark reproduction or deployed performance.
