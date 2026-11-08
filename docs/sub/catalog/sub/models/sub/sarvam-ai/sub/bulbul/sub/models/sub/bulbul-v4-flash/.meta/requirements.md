# Documentation Requirements

## Identity and original source

- Sarvam introduced **Bulbul V4 Flash** on **2026-10-13** as a separately trained/distilled real-time text-to-speech model. The release details Indian-language speech pretraining, a V4 research line, more efficient Flash weights and streaming optimizations. Model identity is not merely a serving flag for V3. [Publisher launch](https://www.sarvam.ai/blogs/bulbul-v4-flash) [model catalog](https://www.sarvam.ai/models).
- Use explicit identifier `bulbul:v4-flash` when integrating. The official model guide says omitting `model` still selects V3, and V4 accepts persona-style speaker identifiers rather than V3's short names. [Bulbul model guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul) [speaker selection](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/how-to/change-the-speaker-voice).
- Rest, HTTP streaming and WebSocket are delivery modes of the same model, not separate trained releases. Version, account/region availability, latency, voice ID formats, codec and sample rates must be checked for the selected endpoint. [Model guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul) [REST API](https://docs.sarvam.ai/api-reference/text-to-speech/convert).

## Versioned capability and evidence boundaries

- The 2026-10-13 launch advertised **83 voices / 224 voice-and-style combinations, 11 languages, <250 ms production time-to-first-audio and ₹20 per 10,000 characters**. These are dated provider descriptions, not static contract terms or independent AI Lab measurements. [Original launch](https://www.sarvam.ai/blogs/bulbul-v4-flash).
- Current published developer docs diverge: the Bulbul guide describes **200+ persona voices / 222 catalog IDs**, and its V4 language list omits Malayalam and Odia. A separate getting-started page lists ten language/locale categories including English-Hindi code mixing. An API best-practice page inconsistently enumerates 11 language codes while noting missing Malayalam/Odia V4 voice personas. Preserve the conflict and validate endpoint availability for a specific account/voice instead of asserting one immutable coverage figure. [Bulbul guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul) [model selection](https://docs.sarvam.ai/api/getting-started/models) [best practices](https://docs.sarvam.ai/api/api-guides-tutorials/text-to-speech/best-practices).
- Publisher cost/speed gains compared with Bulbul V3 are not independently reproduced. The still-previewed **V4 Pro** is not an available confirmed concrete model based on the launch alone; persona/style voice IDs likewise create no extra model gate.
- This review establishes hosted API access only. No downloadable weights or general open-weights license is inferred. Keep content, pronunciation, generated likeness, consent, voice impersonation, personal data, billing and retention as deployment-specific rights and safety checks.

## Validation

- Exact `member-of` to the existing model family, reciprocal family `has-member`, and distinct canonical Sarvam producer relations must resolve.
- Only the frozen released V4 Flash model earns metadata+source acceptance. Family navigation repairs, pricing checks, full rights/legal/security audits, CI/render/cache, inference/latency tests, clean-group and final gates are uncredited.
