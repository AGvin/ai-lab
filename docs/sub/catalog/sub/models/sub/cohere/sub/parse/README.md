# Parse

Parse is Cohere’s document-parsing model family, currently represented here by Parse 5.

## Identity and provenance

The family owns model identity for visual document understanding. The Parse API, Compass and managed deployment services are separate access or application surfaces. [Parse model documentation](https://docs.cohere.com/v2/docs/parse) [Parse release](https://docs.cohere.com/changelog/parse).

## Decision and operating boundaries

- Parse 5 extracts layout-aware Markdown/HTML, tables and visual locations from supported documents. Select the concrete model for its 8K context, supported inputs and language coverage; do not treat a family page as a complete parsing service contract. [Parse model documentation](https://docs.cohere.com/v2/docs/parse) [Parse release](https://docs.cohere.com/changelog/parse).
- The documentation’s North Micro architecture reference does not establish identical weights, an alias or Apache licensing for Parse. Parsing output also lacks several downstream features, including structured JSON and confidence scores. [Parse model documentation](https://docs.cohere.com/v2/docs/parse).

## Catalog relations

- [Cohere](../../../../../producers/sub/c/sub/cohere/) — producer.
- [Parse 5](sub/models/sub/parse-v5-0/) — member.

## Official resources

- [Parse model documentation](https://docs.cohere.com/v2/docs/parse).
- [Parse release](https://docs.cohere.com/changelog/parse).
