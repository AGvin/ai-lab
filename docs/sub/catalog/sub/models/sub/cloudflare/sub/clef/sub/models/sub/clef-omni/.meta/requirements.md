# Documentation Requirements

## Requirements

- Identify Clef-omni as Cloudflare's separately released multi-modal MoE decision model, published under the Clef family.
- Preserve the released model's 30B total / 3B active MoE parameter identity and text/JSON, images, audio, video; distinguish typed decision/probability outputs from natural-language response generation.
- Keep 30B total vs 3B active parameter semantics explicit. October 9, 2026 Workers AI access includes audio/video; do not infer that every alternative backend currently exposes identical media I/O.
- Evaluate use cases (routing, safety classification, structured workflow choice) against the defined typed question schema, confidence/calibration needs, failure handling, and required human review rather than inferring safe autonomous action.
- Keep Cloudflare Workers AI alias, pricing, quotas, task-specific model selector and provider latency benchmarks with hosted service/runtime owners; vendor benchmark tables are evidence inputs, not independent AI Lab rankings.
- Treat the exact model card, weights/distribution, licensing and self-hosting compatibility as current-source facts that may change by release.

## Validation

- One separately trained model identity appears under Clef, not as a duplicated API endpoint or pricing tier.
- `member-of` and `has-member` relations are reciprocal.
- Parameter counts, modality and runtime capability claims are scoped to authoritative, dated sources.
