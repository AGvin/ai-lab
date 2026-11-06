# Mind2Web 2

Mind2Web 2 is the NeurIPS 2025 Datasets and Benchmarks evaluation of long-horizon agentic search. Tasks require complex, time-varying information synthesis and answers supported by source URLs.

## Evaluation method

Agent-as-a-Judge evaluates answer quality and the grounding of cited evidence. The repository records the release of evaluation scripts for both development and test sets on 2025-10-23. The dataset, scripts, judge prompts, webpage cache, and evaluated agent or model are distinct parts of a run.

Preserve the task split, complete answer and citation artifacts, captured webpages and their collection time, evaluation-script revision, explicit `--eval_version`, judge/provider configuration, and any task-specific tool dependencies. Cached cited pages help keep inference and evaluation evidence consistent. Pages that change or cannot be retrieved, and revisions to judge scripts, can change the meaning of a score.

## Scope boundaries

Use this benchmark to assess search and grounded synthesis. [Mind2Web](../mind2web/) evaluates offline UI actions, and [Online-Mind2Web](../online-mind2web/) measures live browser task completion. Their metrics are not substitutes for Mind2Web 2 answer evaluation.

## Provenance

- Produced by: [Ohio State NLP Group](../../../producers/sub/o/sub/osu-nlp-group/)

The group publishes the first-party project; paper authorship and contributing affiliations remain separate from that stewardship and from the ownership of evaluated systems.

## Official resources

- [Mind2Web 2 repository and evaluation instructions](https://github.com/OSU-NLP-Group/Mind2Web-2)
- [Mind2Web 2 project site](https://osu-nlp-group.github.io/Mind2Web-2/)
