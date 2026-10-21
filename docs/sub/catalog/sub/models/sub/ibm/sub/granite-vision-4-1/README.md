# Granite Vision 4.1

Granite Vision 4.1 is IBM's April 2026 document-focused vision-language family, represented in the catalog by the 4B checkpoint.

The model card emphasizes structured document understanding: chart extraction, table extraction, semantic key-value extraction, and general image-to-text use. Task tags and output formats are prompting contracts of the same model rather than additional trained identities.

The concrete checkpoint is fine-tuned on Granite 4.1 3B. That source model is not currently materialized as a canonical catalog node, so the lineage remains source-documented instead of creating a broken relation. Docling and other document-processing software remain separate artifacts.

## Catalog relations

- [IBM](../../../../../producers/sub/i/sub/ibm/) — producer.
- [Granite Vision 4.1 4B](sub/models/sub/granite-vision-4-1-4b/) — member.

## Official resources

- <https://huggingface.co/ibm-granite/granite-vision-4.1-4b>
