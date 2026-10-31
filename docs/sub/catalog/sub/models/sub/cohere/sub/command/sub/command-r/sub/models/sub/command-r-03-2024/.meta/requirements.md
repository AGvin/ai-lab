# Documentation Requirements

## Identity and provenance

- Command R 03-2024 is the separately released March 2024 original 35B text model for RAG and tool-using text generation. The published unquantized checkpoint is `CohereLabs/c4ai-command-r-v01`; The August 2024 R is a separate 32B model. [Official weight card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).
- Cohere's historical API used `command-r-03-2024`, with undated `command-r` as its alias. Both were deprecated September 15, 2025; no active route is claimed. [Historical API table](https://docs.cohere.com/v1/docs/models) [Deprecations](https://docs.cohere.com/docs/deprecations).
- The first-party card explicitly credits both Cohere and Cohere Labs. The Cohere Command namespace is retained; Cohere Labs has an exact non-exclusive co-producer relation rather than ownership of the entire commercial family. [Weight card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).

## Decision and operating boundaries

- The original research card reports 35B parameters, 128K text context, and ten optimized/evaluated languages, not uniformly verified quality. The historical API table lists a 4K maximum hosted output, which is not a guaranteed self-hosted runtime limit. [Weight card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Historical API table](https://docs.cohere.com/v1/docs/models).
- Published weights are access-gated under CC-BY-NC 4.0 and a Cohere Labs acceptable-use policy. No unrestricted commercial permission, current hosted availability, downloaded-weight execution or independent benchmark has been established. [Weight card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Terms](https://cohere.com/cohere-labs-cc-by-nc-license).
- Tool calls and citations require compatible templates, application-side execution and validation. Current corporate beneficial ownership was not independently verified; no unsupported geographic or control attribution is inferred. [Weight card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).

## Validation

- Preserve a distinct historical trained-model identity; exclude serving aliases, quantization duplicates and unsupported parent-weight edges.
- Check source identity, current deprecation, reciprocal relations, local reader links, and exact restrictions; no global CI or runtime validation is credited.
