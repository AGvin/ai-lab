# Granite Docling 258M

Granite Docling 258M is IBM's 258M-class image-and-text checkpoint for structured document conversion. The trained weights are a model identity distinct from the Docling software pipeline and separately distributed runtime artifacts.

## Architecture and capabilities

The checkpoint uses an Idefics3 architecture with a SigLIP2 vision encoder and a Granite language component. It converts document images into structured representations of layouts, tables, equations and text. English is the primary supported language; experimental Japanese, Arabic and Chinese capabilities must not be interpreted as general multilingual certification.

## Validation and deployment boundaries

- Test full-page and region extraction on representative document layouts, checking both transcription accuracy and output schema/structure.
- Pin the exact checkpoint and compatible runtime. Measure memory, latency and conversion quality for the intended workload; do not infer deployment suitability from the 258M label alone.
- The published model weights use **Apache-2.0**. Hosted-service terms and converted or runtime-specific artifacts may have separate conditions.
- Published benchmark results are producer claims; they do not establish independent reproduction or deployed performance here.

## Family and official resource

- [Granite Docling family](../../../../)
- [Official IBM checkpoint](https://huggingface.co/ibm-granite/granite-docling-258M)
