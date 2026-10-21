# Documentation Requirements

## Requirements

- Represent TSPulse R1 as a model series because the official release contains three separately pretrained variants.
- Preserve the exact variants and intended roles: `tspulse-hybrid-allhead-512-p8-r1` for anomaly detection, `tspulse-hybrid-dualhead-512-p8-r1` for imputation/search, and `tspulse-block-dualhead-512-p16-r1` for classification.
- Treat branch/revision selectors as distribution mechanics, not aliases. Do not add child nodes until a later intake establishes durable per-variant catalog ownership.
- Keep context, minimum-input guidance, parameter count, task support, benchmarks, and license freshness-sensitive.

## Validation

- Membership resolves to Granite Time Series.
- The canonical ID is unchanged and the taxonomy correction adds no Model denominator node.
