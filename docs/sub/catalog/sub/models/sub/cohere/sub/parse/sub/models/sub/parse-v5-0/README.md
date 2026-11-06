# Parse 5

Parse 5 is Cohere’s 2.3B document-parsing model, served under the identifier parse-v5.0.

## Identity and provenance

The release establishes a 2.3B multimodal parsing model with an 8K context and approximately 4.6GB model size. Current documentation labels its architecture proprietary north-micro-vision-instruct; that architecture reference does not prove identity, derivation or a shared weight license with the separately released North Micro model. [Parse release](https://docs.cohere.com/changelog/parse) [Parse model documentation](https://docs.cohere.com/v2/docs/parse) [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).

## Decision and operating boundaries

- The documented inputs include PDF, PPT and base64 JPEG. Outputs are Markdown/HTML with reading-order text, HTML tables, forms, page boundaries, bounding boxes and image descriptions; the service does not promise structured JSON or confidence scores. [Parse model documentation](https://docs.cohere.com/v2/docs/parse) [Parse release](https://docs.cohere.com/changelog/parse).
- The documentation lists nine stable input languages: Arabic, English, French, German, Italian, Japanese, Korean, Portuguese and Spanish. Other languages are described as zero-shot with variable accuracy. Header/footer and font-hierarchy classification are not provided. [Parse model documentation](https://docs.cohere.com/v2/docs/parse).
- The model is available through the Parse API and documented managed deployment routes. No public open-weight license was established here. Validate reading order, tables and locations before downstream retrieval or extraction; parsing is not itself a guarantee of factual interpretation. [Parse model documentation](https://docs.cohere.com/v2/docs/parse) [Parse release](https://docs.cohere.com/changelog/parse).

## Catalog relations

- [Parse](../../../../) — series or family.

## Official resources

- [Parse model documentation](https://docs.cohere.com/v2/docs/parse).
- [Parse release](https://docs.cohere.com/changelog/parse).
- [North Micro Vision model card](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct).
