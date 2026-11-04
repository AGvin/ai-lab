# XSTest

**XSTest** — over-refusal and exaggerated safety behavior testing.

## Data and evaluation boundary

The first-party release provides a prompt CSV and separate model completions/evaluation scripts, used to classify compliance and refusal. Original results distinguish safe prompts from contrast-style unsafe prompts; model outputs are historical evidence and not part of the prompt licensing grant.

The [pinned first-party source](https://github.com/paul-rottger/xstest/blob/d7bb5bd738c1fcbc36edd83d5e7d1b71a3e2d84d/readme.md) establishes the identity and release scope. Related model outputs, scoring programs, downloaded task materials and historical leaderboard measurements remain separate artifacts.

## Rights, limitations and safety

The source explicitly licenses XSTest prompts CC BY 4.0 but keeps model completions under the original Meta, Mistral and OpenAI licenses. Preserve attribution and do not republish generated completions under the prompt license. Test safety prompts without seeking harmful outputs.

No benchmark datasets were downloaded and no evaluator, model, untrusted code, harmful safety prompt or physical experiment was executed. No full rights audit or repository-wide CI was run.

## Official source snapshot

- [Repository](https://github.com/paul-rottger/xstest)
- [Pinned README](https://github.com/paul-rottger/xstest/blob/d7bb5bd738c1fcbc36edd83d5e7d1b71a3e2d84d/readme.md)
- [Pinned LICENSE](https://github.com/paul-rottger/xstest/blob/d7bb5bd738c1fcbc36edd83d5e7d1b71a3e2d84d/LICENSE)
