# Documentation Requirements

## Requirements

- Identify TranslateGemma as Google's released translation-focused Gemma model series in 4B, 12B, and 27B parameter sizes.
- Preserve current language coverage, model-size inventory, translation task boundary, open-weight distribution, and customization/deployment guidance only while supported by first-party sources.
- Keep TranslateGemma distinct from general-purpose Gemma models, hosted Gemini translation behavior, Google Translate products/services, and downstream fine-tuned derivatives.
- Treat language inventory, artifacts, licenses, runtime support, quantization, context limits, hardware fit, quality metrics, and provider comparisons as freshness-sensitive.
- Do not turn provider translation-quality claims into a universal language-pair ranking.

## Validation

- TranslateGemma remains a model series rather than one universal checkpoint.
- Size-specific deployment facts are not generalized across every series member.

## Verified identity and provenance

Open translation-focused Gemma series with released 4B, 12B, and 27B variants covering 55 languages; it is separate from the Google Translate product.

## Source-scoped operating boundaries

- The documented direct-translation template supports text or image text extraction/translation with a 2K input context. It uses only User and Assistant roles and requires supported source_lang_code and target_lang_code values. [TranslateGemma model and prompt contract](https://huggingface.co/google/translategemma-4b-it).
- Other prompting patterns such as translation post-editing are not officially supported by that template. Keep language-pair evaluation and review of consequential translations separate from Google's aggregate quality claims. [Supported template boundary](https://huggingface.co/google/translategemma-4b-it).

## Source evidence

- <https://huggingface.co/google/translategemma-4b-it>
- <https://ai.google.dev/gemma/docs/releases>
