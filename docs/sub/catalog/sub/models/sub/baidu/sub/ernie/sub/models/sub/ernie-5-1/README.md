# ERNIE 5.1

ERNIE 5.1 is Baidu's released model described in the official article dated 9 May 2026. It is derived from ERNIE 5.0 through elastic sub-network extraction and additional agentic post-training, creating a distinct trained model rather than a provider alias. [Primary source](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

## Release and trained lineage

The official release article dated 9 May 2026 identifies ERNIE 5.1 as derived from 5.0 by selecting an elastic sub-network and applying further agentic post-training. It remains a distinct trained model in the same ERNIE family. Baidu reports roughly one-third of 5.0's total parameters and half of its active parameters; those relative statements do not disclose exact absolute counts. [Release and technical lineage](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

## Hosted access

The Qianfan catalog updated 18 October 2026 lists `ernie-5.1` with 128K context, 119K maximum input and up to 65,536 output tokens. These are current provider limits, not family-wide intrinsic limits. The audited release and provider sources do not establish a downloadable public-weight license or a self-hosting route for 5.1. [Current ERNIE endpoint table](https://cloud.baidu.com/doc/qianfan/s/rmh4stp0j)

## Evaluation boundary

Baidu's agentic, reasoning and search claims depend on release-specific tests, tools and evaluation settings. Compare the exact endpoint on representative tasks and keep data access and tool authorization outside generated instructions. Do not treat a benchmark position, a preview endpoint name or a model-family name as an operational guarantee. [Vendor evaluation scope](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/)

## Relations

- Derived from: [ERNIE 5.0](../ernie-5-0/README.md)
- Member of: [ERNIE](../../../../README.md)

## Official resources

- <https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/>
- <https://cloud.baidu.com/doc/qianfan/s/rmh4stp0j>
