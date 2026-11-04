# Documentation Requirements

## Requirements

- Identify BIG-Bench Hard (BBH) as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `suzgunmirac/BIG-Bench-Hard@9ee07bd481feebf959a6b59d61ea57bdcf30964d` (blob `f046e5e03d9df0b0e3f36dc2047424665ebd5ca0`) and the actual source-license record where present.
- The pinned README identifies 23 originally challenging BIG-Bench tasks, with task files in bbh/ and accompanying chain-of-thought prompts in cot-prompts/.
- Published historical findings describe the effect of chain-of-thought prompting on then-evaluated models; they are not guarantees for modern models.
- Few-shot prompt, chain-of-thought visibility, scoring, model revision and task-set versions materially affect results.
- Repository source includes MIT LICENSE, but upstream tasks and prompts can have additional provenance and attribution needs.
- Do not present the 23-task subset as all BIG-Bench or promote published historical model outputs to independent AI Lab evaluations. No run or complete rights audit.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
