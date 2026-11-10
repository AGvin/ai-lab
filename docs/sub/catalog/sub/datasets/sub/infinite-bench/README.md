# InfiniteBench

**InfiniteBench** is OpenBMB's long-context benchmark designed to evaluate model comprehension and reasoning on contexts of **100,000 tokens and above**.

## Task families

The [official README](https://github.com/OpenBMB/InfiniteBench/blob/51d9b37b0f1790ead936df2243abbf7f0420e439/README.md) describes **12 tasks**, spanning summarization, question answering and other long-context operations. It includes synthetic material such as substituted fictional books and real-world-derived texts. Task-specific input lengths and scoring procedures vary, so a single aggregate number cannot substitute for a documented task breakdown.

Reproducibility depends on exact dataset revision, tokenizer, context truncation, prompts, input/output budgets, selected model and answer scoring. Models with advertised large context windows may still differ substantially in usable retrieval and reasoning performance.

## Data rights and operations

The [repository LICENSE](https://github.com/OpenBMB/InfiniteBench/blob/51d9b37b0f1790ead936df2243abbf7f0420e439/LICENSE) is MIT for covered source. Underlying books, documents and derived test contexts may have separate copyright or reuse terms. Large-context inference also carries computational cost and privacy implications for submitted texts.

No dataset import, model invocation, score check, legal review or whole-catalog clean pass was performed.

## Official source snapshot

- [Publisher repository](https://github.com/OpenBMB/InfiniteBench)
- [Pinned README](https://github.com/OpenBMB/InfiniteBench/blob/51d9b37b0f1790ead936df2243abbf7f0420e439/README.md)
- [Pinned root LICENSE](https://github.com/OpenBMB/InfiniteBench/blob/51d9b37b0f1790ead936df2243abbf7f0420e439/LICENSE)
