# AbstentionBench

**AbstentionBench** tests when a language model appropriately declines to give a definitive answer rather than guessing. The first-party authors evaluate abstention under insufficient, ambiguous, stale or otherwise unanswerable information.

## Benchmark and scoring

The [official repository](https://github.com/facebookresearch/AbstentionBench/blob/e29184174c69bc95139b8c33dcca09aacab9442a/README.md) describes **20 component datasets** across **six abstention scenarios**, including three newly designed underspecified reasoning challenges. Its released evaluation tools use model inference and human-validated judging to assess both whether answers should be withheld and whether a supplied answer is correct.

A benchmark score depends on the task mixture, whether the answer was knowable, prompt formulation and judge/model version. The authors' published model findings are research results, not independent AI Lab measurements or general deployment guarantees.

## Licensing and limitations

The root [CC BY-NC 4.0 license](https://github.com/facebookresearch/AbstentionBench/blob/e29184174c69bc95139b8c33dcca09aacab9442a/LICENSE) places a noncommercial condition on covered material. The README additionally warns about independently licensed third-party datasets: the repository's license does not override their rights. Guard prompt contents, evaluation logs, private examples and provider API keys.

No test suite, inference call, judge audit, source-dataset rights audit or whole-catalog clean pass was executed.

## Official source snapshot

- [Publisher repository](https://github.com/facebookresearch/AbstentionBench)
- [Pinned README](https://github.com/facebookresearch/AbstentionBench/blob/e29184174c69bc95139b8c33dcca09aacab9442a/README.md)
- [Pinned LICENSE](https://github.com/facebookresearch/AbstentionBench/blob/e29184174c69bc95139b8c33dcca09aacab9442a/LICENSE)
