# GPT Image

GPT Image is OpenAI’s model family for generating and editing images from text and image inputs. Its represented releases are GPT Image 2 and the Sunburst and Flare members of GPT Image 2.5.

## Operating boundaries

The Image API selects an image model directly. In Responses, a supported mainline model calls the image-generation tool, whose model setting selects the image model; the orchestration model and image model are separate identities [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).

Organization verification, output settings, and content filtering are service conditions. Precise text placement, composition, and cross-image consistency still require reviewing the generated result [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).

## Child pages

- [Models](sub/models/README.md).

## Relations

- Member: [GPT-Image-2](sub/models/sub/gpt-image-2/README.md).
- Member: [GPT-Image-2.5 Flare](sub/models/sub/gpt-image-2-5-flare/README.md).
- Member: [GPT-Image-2.5 Sunburst](sub/models/sub/gpt-image-2-5-sunburst/README.md).
- Producer: [OpenAI](../../../../../producers/sub/o/sub/openai/README.md).

## Official resources

- [OpenAI model catalog](https://developers.openai.com/api/docs/models).
- [Image-generation guide](https://developers.openai.com/api/docs/guides/image-generation).
- [API changelog](https://developers.openai.com/api/docs/changelog).
