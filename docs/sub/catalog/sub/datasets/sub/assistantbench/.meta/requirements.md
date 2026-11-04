# Documentation Requirements

## Requirements

- Define AssistantBench as a web-agent benchmark dataset assessing real-world information-seeking tasks rather than a web browsing service, a self-hosted autonomous agent implementation, or a live website inventory.
- First-party README links the canonical AssistantBench Hugging Face dataset and leaderboard; SeePlanAct (SPA) is a separately described proposed agent approach, not an independent dataset or proof that full source is available in this checkout.
- Benchmark evaluation depends on exact question, reference answers, test date, location/time-sensitive websites, browser and search permissions, model configuration and grading. Public web changes can make originally correct answers stale.
- Root LICENSE is AI Pubs OpenRAIL-S (responsible-use conditions), not plain permissive MIT/Apache. Verify the license of the exact Hugging Face dataset snapshot, associated media and live websites separately.
- Review scraping terms, robots policies, authenticated account rights, sensitive personal data, browser sandboxing and cost controls before replaying agent tasks; never treat source benchmark prompts as authorization to access external systems.
- Do not claim an actual browsing run, benchmark success, model API usage, page scraping, current leaderboard accuracy, complete rights audit or whole-catalog clean pass.

## Validation

- Exactly one canonical dataset identity, pinned publisher sources, and a resolvable dataset index link.
- Distinguish repository and benchmark data rights; do not award runtime, complete source audit or whole-catalog clean-pass credit.
