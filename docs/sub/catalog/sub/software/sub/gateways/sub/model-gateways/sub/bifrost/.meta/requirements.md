# Documentation Requirements

## Requirements

- Identify Maxim Bifrost as an open-source AI model gateway that provides a unified interface across multiple model providers and supports routing/operational gateway concerns.
- Preserve its primary placement under `gateways/model-gateways`; Bifrost mediates model-provider access rather than acting as a model provider itself.
- Preserve both direct Go-package and HTTP/gateway usage as implementation modes without turning packaging into separate catalog identities.
- Avoid repeating vendor benchmark or throughput claims as stable catalog facts; keep provider counts, performance figures, cluster behavior, and other mutable implementation details source-backed when expanded.
- Include current official Bifrost documentation and repository references.

## Validation

- The page identifies the intended `maximhq/bifrost` AI gateway rather than unrelated projects with the same name.
- Vendor benchmark claims are not presented as independent AI Lab evaluation.
- Official resource links match canonical entity metadata.
- The page contains no temporary-placeholder wording.
