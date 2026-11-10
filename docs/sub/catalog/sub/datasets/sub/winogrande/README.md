# WinoGrande

WinoGrande is a Winograd-style commonsense reasoning benchmark distributed with training sets of several sizes and separate validation/test splits. Its pinned v1.1 README notes that official test labels are withheld and leaderboard submission is required for test scores.

## Dataset and evaluation boundaries

The pinned README identifies WinoGrande v1.1 and a download script with several training sizes (xs, s, m, l, xl) plus validation and test JSONL files.
Official test labels are not included in the distributed test.jsonl; the original leaderboard handles test-set scoring.

## Licensing, reproducibility and responsible use

Apache-2.0 repository LICENSE; dataset packaging/terms separately reviewable. Avoid leaked test labels and represent hidden-test scores only with official measurement evidence. No files downloaded, model fine-tuned, evaluation executed or full clean pass.

## Official source snapshot

- [Original repository](https://github.com/allenai/winogrande)
- [Pinned README](https://github.com/allenai/winogrande/blob/727e837f77521ef38bcc56df3b275c8da43f45af/README.md)
- [Pinned LICENSE](https://github.com/allenai/winogrande/blob/727e837f77521ef38bcc56df3b275c8da43f45af/LICENSE)
