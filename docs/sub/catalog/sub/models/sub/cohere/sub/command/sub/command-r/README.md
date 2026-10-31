# Command R

The Command R series groups original March/April 2024 R/R+, August 2024 refreshes, December 2024 Command R7B, and the February 2025 Arabic research checkpoint.

## Identity and provenance

Six dated models are now materialized. The original 35B March Command R and 104B April Command R+ are distinct trained releases from the August 2024 updates. Their old hosted API IDs and unversioned aliases were deprecated on September 15, 2025. [Historical identifiers](https://docs.cohere.com/v1/docs/models) [Deprecations](https://docs.cohere.com/docs/deprecations) [Original R card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Original R+ card](https://huggingface.co/CohereLabs/c4ai-command-r-plus). [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models) [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

Command R7B Arabic is a separate Cohere/Cohere Labs gated-weight research checkpoint emphasizing Modern Standard Arabic and English, with a 128K context and approximately 8B total parameters (7B transformer and 1B embeddings). Cohere's release note accidentally displays the December 2024 ID, so the separately published 2025 model card is the exact identification source. No trained-from relation is asserted. [Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025) [Arabic release note](https://docs.cohere.com/changelog/command-r7b-arabic).

## Decision and operating boundaries

- The original 2024 R/R+ model cards specify 128K text context and gated CC-BY-NC-4.0 research weights. The historical API table lists a 4K maximum hosted output; deprecated routes are unsuitable for new integration. Local inference limits and benchmark quality have not been independently verified. [Original R card](https://huggingface.co/CohereLabs/c4ai-command-r-v01) [Original R+ card](https://huggingface.co/CohereLabs/c4ai-command-r-plus) [Historical model table](https://docs.cohere.com/v1/docs/models).
- The August R card reports 32B parameters, R+ reports 104B, and R7B uses a 7B-class name. The three earlier models advertise a 128K context and the current API table lists a 4K maximum output; the Arabic research release separately has 128K context without proof of that API output cap; those limits are not a guarantee of quality throughout the window. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024) [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- The weight cards state CC-BY-NC research terms and model-specific templates for grounded generation and tools. A tool-capable model requests actions; connected application software performs them. [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024) [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024) [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- Choose exact version and deployment from current documentation. August release throughput and latency comparisons are provider measurements, not reproduced runtime results. [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).

## Catalog relations

- [Command](../../) — series or family.
- [Command R 03-2024](sub/models/sub/command-r-03-2024/) — historical member.
- [Command R+ 04-2024](sub/models/sub/command-r-plus-04-2024/) — historical member.
- [Command R 08-2024](sub/models/sub/command-r-08-2024/) — member.
- [Command R+ 08-2024](sub/models/sub/command-r-plus-08-2024/) — member.
- [Command R7B](sub/models/sub/command-r7b-12-2024/) — member.
- [Command R7B Arabic](sub/models/sub/command-r7b-arabic-02-2025/) — member.

## Official resources

- [Original Command R card](https://huggingface.co/CohereLabs/c4ai-command-r-v01).
- [Original Command R+ card](https://huggingface.co/CohereLabs/c4ai-command-r-plus).
- [Historical API model table](https://docs.cohere.com/v1/docs/models).
- [Deprecations](https://docs.cohere.com/docs/deprecations).
- [Cohere model lifecycle and API identifiers](https://docs.cohere.com/docs/models).
- [Command R7B documentation](https://docs.cohere.com/docs/command-r7b).
- [Command August 2024 refresh](https://docs.cohere.com/changelog/command-gets-refreshed).
- [Command R 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-08-2024).
- [Command R+ 08-2024 model card](https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024).
- [Command R7B model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024).
- [Command R7B Arabic model card](https://huggingface.co/CohereLabs/c4ai-command-r7b-arabic-02-2025).
- [Command R7B Arabic release](https://docs.cohere.com/changelog/command-r7b-arabic).
