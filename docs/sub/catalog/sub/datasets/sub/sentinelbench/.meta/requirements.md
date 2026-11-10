# Documentation Requirements

## Requirements

- Present SentinelBench as Microsoft Research's open-source benchmark for long-running monitoring agents operating in time-evolving environments where useful progress may depend on waiting for external state changes.
- Preserve its released scope of 100 tasks across ten synthetic web environments and its evaluation dimensions of completion, reaction time, and resource use.
- Keep waiting strategies, browser-agent harnesses, evaluated models, synthetic applications, and monitoring-agent architectures separate from the benchmark identity.
- Treat scenario inventory, event timelines, harness versions, metrics, and reported results as freshness-sensitive.

## Validation

- SentinelBench remains a benchmark/dataset identity rather than a monitoring agent implementation.
- Cost/pass-rate claims remain tied to the cited benchmark release and run configuration.

## Scoped original-source qualification — 2026-11-08

- **SentinelBench** is Microsoft Research's originally released **June 2026** benchmark for agents that must monitor environments evolving independently of their actions. Its **100 tasks across ten synthetic web apps** replay scripted event timelines for email, chat, social, finance, calendar, code-hosting, entertainment and search. These are artificial controlled websites, not live production inboxes or financial accounts.
- Scoring covers task completion, reaction time and resource/token use under specific models and browser harnesses. The Microsoft study evaluates a wait-condition tool versus repeated timed sleep; the author's comparisons do not prove general autonomous monitoring performance, real notification delivery, compliance or cost predictability. Benchmark data, scenario timelines, generation code, model and harness results are distinct; avoid unattended tests with live service credentials.
- First-party sources: https://www.microsoft.com/en-us/research/articles/sentinelbench-a-benchmark-for-long-running-monitoring-agents/ ; https://www.microsoft.com/en-us/research/publication/sentinelbench-a-benchmark-for-long-running-monitoring-agents/ ; https://github.com/microsoft/sentinel_environments
- Source acceptance is restricted to the existing original June 2026 dataset release, 100/10 synthetic environment scope and evaluation dimensions. No replayed environments, independent runtime monitoring, comprehensive third-party data/rights/privacy/security audit, repository-wide schema/cache/CI/render, clean or final gate.
