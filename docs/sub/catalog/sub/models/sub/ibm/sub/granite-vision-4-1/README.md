# Granite Vision 4.1

Granite Vision 4.1 is IBM's April 2026 document-focused vision-language family, represented in the catalog by the 4B checkpoint.

The model card emphasizes structured document understanding: chart extraction, table extraction, semantic key-value extraction, and general image-to-text use. Task tags and output formats are prompting contracts of the same model rather than additional trained identities.

The 4B checkpoint is fine-tuned on the canonical [Granite 4.1 3B instruction-tuned model](../granite-4-1/sub/models/sub/granite-4-1-3b/), with reciprocal provenance relations recorded on those two concrete model nodes. It is not based on the distinct Granite 4.1 3B Base identity. Docling and other document-processing software remain separate artifacts.

## License and evaluation boundaries

The represented 4B checkpoint is released under Apache 2.0 according to its [IBM model card](https://huggingface.co/ibm-granite/granite-vision-4.1-4b). This does not establish licensing for separate datasets or integrations. The card evaluates chart outputs with an LLM judge and table extraction with TEDS, separating cropped-table and full-page settings. These source-reported comparisons do not establish lossless extraction or accuracy on arbitrary documents. Validate the chosen prompts, output format, input data, and runtime integration for the intended workflow. Image-to-text support does not imply image generation; no runtime or benchmark reproduction is claimed here.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Vision 4.1 4B](sub/models/sub/granite-vision-4-1-4b/) — member.

## Official resources

- <https://huggingface.co/ibm-granite/granite-vision-4.1-4b>
