# Documentation Requirements

## Requirements

- Identify IFEvalCode as a published controlled-code-generation evaluation benchmark, not Google IFEval, a language-model API or a standalone hosted inference service.
- The pinned first-party README points to a JSONL benchmark file under data/benchmark and separates inference (infer_models.py) from evaluation (eval_models.py). These scripts implement the task; they do not create additional independent dataset identities.
- Record exact prompt, input split, constraint types, model revision, decoding parameters, evaluation script and allowed tools before comparing scores. Do not treat satisfaction of constraints as proof of code correctness or safety.
- The pinned upstream repository has no root LICENSE. Public checkout access does not establish permission to redistribute or commercially reuse the data/code; confirm exact artifact and third-party source terms before use.
- Generated code and evaluator dependencies must be treated as untrusted. Any execution should happen in a restricted environment without privileged credentials or production connectivity.
- No model inference, generated-program execution, evaluation score, complete data audit, rights clearance or whole-catalog clean pass was performed.

## Validation

- Match one frozen dataset candidate with a canonical indexed entity and pinned first-party evidence.
- Do not count benchmark data as proof of legal rights, runtime evaluation or repository-wide clean validation.
