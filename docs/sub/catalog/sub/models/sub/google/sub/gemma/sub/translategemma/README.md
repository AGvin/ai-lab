# TranslateGemma

Open translation-focused Gemma series with released 4B, 12B, and 27B variants covering 55 languages; it is separate from the Google Translate product.

## Relations

- Member of: [Gemma](../../)

## Source-scoped operating boundaries

- The documented direct-translation template supports text or image text extraction/translation with a 2K input context. It uses only User and Assistant roles and requires supported source_lang_code and target_lang_code values. [TranslateGemma model and prompt contract](https://huggingface.co/google/translategemma-4b-it).
- Other prompting patterns such as translation post-editing are not officially supported by that template. Keep language-pair evaluation and review of consequential translations separate from Google's aggregate quality claims. [Supported template boundary](https://huggingface.co/google/translategemma-4b-it).

## Official resources

- <https://ai.google.dev/gemma/docs/releases>
- <https://deepmind.google/models/gemma/>
- <https://huggingface.co/google/translategemma-4b-it>
