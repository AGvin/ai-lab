# Online-Mind2Web

Online-Mind2Web is the COLM 2025 benchmark for end-to-end web-agent execution on live websites. Its published scope is 300 tasks across 136 websites.

## Changing tasks and evaluation

The maintainers replace invalid or outdated tasks, including tasks affected by website changes or CAPTCHAs. The history records 36 replacements on 2025-11-03 and further changes in 2026. Record exact task IDs, repository or dataset revision, execution date, website availability, and relevant browser state; the task collection is not immutable.

The v2 trajectory-submission schema was announced on 2026-05-23. It records structured steps and supporting screenshots. Pin the schema and submission artifacts, and state whether results use human review or automatic WebJudge evaluation, including the judge configuration. Website access restrictions and changing content can prevent historical reproduction even with the same agent.

## Choosing the protocol

Use the benchmark for live-site task completion. [Mind2Web](../mind2web/) measures offline action prediction; [Mind2Web 2](../mind2web-2/) evaluates grounded search answers. WebArena's separately hosted, resettable environment is another distinct evaluation protocol. Scores across these settings answer different questions.

## Provenance

- Produced by: [Ohio State NLP Group](../../../producers/sub/o/sub/osu-nlp-group/)

The first-party repository lists Ohio State and UC Berkeley coauthors. The catalog steward relation does not imply exclusive institutional authorship or permission to operate third-party websites.

## Official resources

- [Online-Mind2Web repository, task updates, and submission schema](https://github.com/OSU-NLP-Group/Online-Mind2Web)
- [WebArena environment comparison](https://github.com/web-arena-x/webarena)
