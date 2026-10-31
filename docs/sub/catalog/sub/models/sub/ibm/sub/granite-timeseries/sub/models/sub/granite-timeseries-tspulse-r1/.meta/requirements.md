# Documentation Requirements

## Requirements

- Represent TSPulse R1 as a model series because the official release contains three separately pretrained variants.
- Preserve the exact variants and intended roles: `tspulse-hybrid-allhead-512-p8-r1` for anomaly detection, `tspulse-hybrid-dualhead-512-p8-r1` for imputation/search, and `tspulse-block-dualhead-512-p16-r1` for classification.
- Treat branch/revision selectors as distribution mechanics, not aliases. Do not add child nodes until a later intake establishes durable per-variant catalog ownership.
- Preserve task-dependent input-length guidance from the current first-party card: anomaly detection requires roughly 1536–2048 points (3–4× the 512 base context), imputation and semantic search require at least 512 points, while classification accepts arbitrary input length and internally resamples/interpolates to 512.
- Keep parameter count, task support, benchmark claims, release notes, and license freshness-sensitive; do not treat source benchmark claims as independently reproduced results.

## Validation

- Membership resolves to Granite Time Series.
- The canonical ID is unchanged and the taxonomy correction adds no Model denominator node.
- Reader guidance does not collapse the distinct per-task input-length requirements into one universal 512-point minimum.