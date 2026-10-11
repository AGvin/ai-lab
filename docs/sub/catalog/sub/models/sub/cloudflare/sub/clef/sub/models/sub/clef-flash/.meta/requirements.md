# Documentation Requirements

## Requirements

- Identify Clef-flash as Cloudflare's separately released 9B low-latency decision model, published under the Clef family.
- Preserve the released model's 9B parameter identity and text/JSON and supported visual media input; distinguish typed decision/probability outputs from natural-language response generation.
- The October 9, 2026 hosted context window changed from 64K to 24K without changing the weights; self-hosted weights may support a longer context. Do not describe hosted endpoint limitations as intrinsic model architecture.
- Evaluate use cases (routing, safety classification, structured workflow choice) against the defined typed question schema, confidence/calibration needs, failure handling, and required human review rather than inferring safe autonomous action.
- Keep Cloudflare Workers AI alias, pricing, quotas, task-specific model selector and provider latency benchmarks with hosted service/runtime owners; vendor benchmark tables are evidence inputs, not independent AI Lab rankings.
- Treat the exact model card, weights/distribution, licensing and self-hosting compatibility as current-source facts that may change by release.

## Validation

- One separately trained model identity appears under Clef, not as a duplicated API endpoint or pricing tier.
- `member-of` and `has-member` relations are reciprocal.
- Parameter counts, modality and runtime capability claims are scoped to authoritative, dated sources.
