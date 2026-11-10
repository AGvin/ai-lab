# Documentation Requirements

## Requirements

- Identify Bulbul as Sarvam AI's **text-to-speech model family**, not an alias of general chat/reasoning, speech recognition (Saaras), document intelligence (Sarvam Vision), the Sarvam API product, or a speaker persona.
- Preserve released V4 Flash as one concrete member. Sarvam's original launch describes **Bulbul V4 Pro as coming later**; do not grant a released model identity based on a preview demonstration. [Launch](https://www.sarvam.ai/blogs/bulbul-v4-flash).
- Model version and speaker persona/style identifiers are different kinds of identifiers. Do not count HTTP/streaming/WebSocket transports or hosted endpoint contracts as separate trained models. [Bulbul API guide](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul).
- Keep V3 as the documented API default when the `model` request field is omitted; V4 Flash requires explicit `bulbul:v4-flash` selection for consistent routing. [Bulbul docs](https://docs.sarvam.ai/api/api-guides-tutorials/models/bulbul).
- Reciprocal Sarvam AI producer relation and exact member-of / has-member relationships must resolve to canonical model nodes.

## Validation

- One released concrete model child, one family source/control and exact parent reader navigation.
- Family support entity receives no additional frozen metadata or original-source gate; only V4 Flash is a frozen candidate model.
