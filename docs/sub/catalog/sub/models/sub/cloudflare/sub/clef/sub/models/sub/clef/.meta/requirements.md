# Documentation Requirements

## Requirements

- Identify Clef as Cloudflare's separately released 27B flagship decision model, published under the Clef family.
- Preserve the released model's 27B parameter identity and text/JSON and image/video input supported by the documented Workers AI model routes; distinguish typed decision/probability outputs from natural-language response generation.
- Treat 27B parameter count and open-weight Apache 2.0 announcement as upstream model facts, while hosted 64K context and Workers AI price remain mutable service configuration.
- Evaluate use cases (routing, safety classification, structured workflow choice) against the defined typed question schema, confidence/calibration needs, failure handling, and required human review rather than inferring safe autonomous action.
- Keep Cloudflare Workers AI alias, pricing, quotas, task-specific model selector and provider latency benchmarks with hosted service/runtime owners; vendor benchmark tables are evidence inputs, not independent AI Lab rankings.
- Treat the exact model card, weights/distribution, licensing and self-hosting compatibility as current-source facts that may change by release.

## Validation

- One separately trained model identity appears under Clef, not as a duplicated API endpoint or pricing tier.
- `member-of` and `has-member` relations are reciprocal.
- Parameter counts, modality and runtime capability claims are scoped to authoritative, dated sources.
