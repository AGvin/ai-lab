# IFEvalCode

**IFEvalCode** is a benchmark for **controlled code generation**, testing whether a model follows specified constraints while producing code.

## Benchmark and tooling

The [first-party README](https://github.com/CSJianYang/IFEvalCode/blob/13c3e775b42e061f2f23e4d6740874ec47bebcb4/README.md) describes the project's benchmark stored as a JSONL task set and separate `infer_models.py` and `eval_models.py` scripts. These are the dataset's inference/evaluation interfaces; they do not make the project a hosted model provider or a copy of the general instruction-following IFEval benchmark.

Reported scores require the precise task snapshot, constraints, prompt, model/version, decoding settings and evaluator code. Even code satisfying a surface instruction constraint may be incorrect or unsafe when executed.

## Rights and execution safety

No root LICENSE file was found at the pinned commit. Do not infer unrestricted redistribution rights. Source training examples and independently obtained model files may have additional conditions. Model-generated programs are untrusted and should only be run in isolated sandboxes with no credentials, restricted network and explicit resource limits.

No model or code evaluation, rights audit, dataset download or whole-catalog clean pass was performed.

## Official source snapshot

- [Publisher repository](https://github.com/CSJianYang/IFEvalCode)
- [Pinned README](https://github.com/CSJianYang/IFEvalCode/blob/13c3e775b42e061f2f23e4d6740874ec47bebcb4/README.md)
