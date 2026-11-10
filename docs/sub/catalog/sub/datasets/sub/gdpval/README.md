# GDPval

GDPval is OpenAI's benchmark of economically valuable knowledge-work tasks. The first release spans 44 occupations and nine sectors, with 1,320 tasks in the full set and 220 tasks in the public gold subset. The OpenAI Hugging Face distribution provides that public subset, not the full private evaluation.

## Tasks and judging

Tasks supply instructions and reference files and ask for professional deliverables such as documents, slides, or spreadsheets. The published method uses blind expert comparisons with human-created work, supported by task-specific rubrics. Automated grading is a separate approximation of expert judgment.

Pin the task inventory, reference files, gold deliverables, rubric revision, grading method, human-comparison protocol, and model/tool configuration. Public-subset results and full-set results are different scopes. The original one-shot setup also excludes much of the clarification and iteration present in workplace tasks.

## Access and lifecycle

OpenAI's search-indexed official notice states that its hosted GDPval leaderboard is no longer active and directs readers to grading guidance. The public dataset remains available. A guidance link does not establish an active hosted grading service.

Leaderboard retirement does not retire the benchmark. GDPval measures work-product performance, not GDP impact, occupation replacement, hiring prospects, or universal productivity.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

## Official resources

- [GDPval release and methodology](https://openai.com/index/gdpval/)
- [OpenAI GDPval public dataset](https://huggingface.co/datasets/openai/gdpval)
- [GDPval grading guidance](https://evals.openai.com/gdpval/grading)
- [OpenAI-hosted leaderboard status](https://evals.openai.com/gdpval/leaderboard?curius=2011)
