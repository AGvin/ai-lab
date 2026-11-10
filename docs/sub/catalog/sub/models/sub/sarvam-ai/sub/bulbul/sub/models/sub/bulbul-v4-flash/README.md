# Bulbul V4 Flash

**Bulbul V4 Flash** is Sarvam AI's released text-to-speech model, introduced **13 October 2026** for expressive, low-latency speech in Indian-language applications. The publisher reports distilling a larger V4 research effort into a smaller production model, distinct from Bulbul V3 and from the still-previewed V4 Pro. [Original announcement](https://www.sarvam.ai/blogs/bulbul-v4-flash).

## Choosing the exact model

For production routing, request `model=bulbul:v4-flash` explicitly. Sarvam's current [Bulbul API guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul) says **Bulbul V3 remains the API default** if the field is omitted. V4 Flash accepts persona-style speaker IDs; old V3 short speaker identifiers cannot automatically be reused. REST, HTTP streaming and WebSocket are delivery routes, not three trained models.

## What the publisher reports

The launch describes expressive native speech, Indian-English/code-mixed phrasing, contextual number/name pronunciation, and real-time voice-agent applications. It advertised 83 named voices, 224 styles, 11 languages and first audio under 250 ms at launch. Those voice, latency, pricing and language-coverage values are vendor claims and mutable.

Current first-party documentation shows **different voice counts and language coverage** (including V4-specific exclusions for Malayalam and Odia), so do not assume the full dated launch inventory is currently selectable for every endpoint. Revalidate the chosen `language_code`, persona ID, transport, account access and current terms. [Model guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul) [model-selection docs](https://docs.sarvam.ai/api/getting-started/models).

## Safety and rights

The available evidence documents provider-operated API access, not downloadable V4 Flash weights or license grants for local redistribution. Protect API credentials, obtain voice likeness/content consent where required, and check data retention, privacy policy, sample-rate/codec behavior and commercial terms per integration. Claims about speed and quality were not independently reproduced by AI Lab.

## Relations

- Member of: [Bulbul](../../../../README.md)

## Sources

- [Sarvam launch](https://www.sarvam.ai/blogs/bulbul-v4-flash)
- [Sarvam model catalog](https://www.sarvam.ai/models)
- [Current Bulbul API guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul)
- [Sarvam TTS endpoint reference](https://docs.sarvam.ai/api-reference/text-to-speech/convert)
