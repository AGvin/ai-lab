# Documentation Requirements

## Requirements

- Identify AGIEval as one concrete frozen-source **dataset**, not a model, implementation library, hosted inference service or measured benchmark result.
- Pin the first-party README at `ruixiangcui/AGIEval@84ab72d94318290aad2e4ec820d535a95a1f7552` (blob `56780cb8df6dc547f2bae6d4f19a69a1b2b24251`) and the actual source-license record where present.
- The official pinned README describes v1.1 with 20 tasks, including 18 multiple-choice and two cloze tasks; v1.1 updated Gaokao sources and corrected labels.
- Question data can include passage, question, options, label and answer fields. Prompting, source exams, language, scoring and version differ by task.
- Original admissions, qualification and competition exams may have independent copyright and data licenses, as explicitly stated in the README.
- Use exact version, task, few-shot prompt and answer extraction for evaluation; public tasks can contaminate training sets.
- A repository MIT license does not override original exam publisher rights. No exams were redistributed, benchmark run, rights clearance made, or full clean pass performed.

## Validation

- Exactly one newly materialized dataset identity, one parent index link and no invented publisher or duplicate source entity.
- This scoped source review is not complete rights, schema/render closure, repository-wide CI or a whole-catalog clean pass.
