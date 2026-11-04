# StrongREJECT

**StrongREJECT** — measuring harmful-response refusal under adversarial prompts.

## Data and evaluation boundary

The publisher supplies an evaluation prompt dataset over six harmful-behavior categories, jailbreak transformations and two scorer variants: a model-graded rubric and a separately fine-tuned evaluator. Test prompts and derived outputs are distinct from the generated jailbreak methods, judge model and scored leaderboards.

The [pinned first-party source](https://github.com/dsbowen/strong_reject/blob/7a551d5b440ec7b75d4f6f5bb7c1719965b76b47/README.md) establishes the identity and release scope. Related model outputs, scoring programs, downloaded task materials and historical leaderboard measurements remain separate artifacts.

## Rights, limitations and safety

The MIT root LICENSE does not cover all reused prompt sources: the README explicitly lists external datasets including some with no license. Refusal-testing prompts should be restricted to controlled safety research, with no execution of harmful methods or unsafe model completions.

No benchmark datasets were downloaded and no evaluator, model, untrusted code, harmful safety prompt or physical experiment was executed. No full rights audit or repository-wide CI was run.

## Official source snapshot

- [Repository](https://github.com/dsbowen/strong_reject)
- [Pinned README](https://github.com/dsbowen/strong_reject/blob/7a551d5b440ec7b75d4f6f5bb7c1719965b76b47/README.md)
- [Pinned LICENSE](https://github.com/dsbowen/strong_reject/blob/7a551d5b440ec7b75d4f6f5bb7c1719965b76b47/LICENSE)
