# Crawl4AI

[Crawl4AI](https://github.com/unclecode/crawl4ai) is an open-source, Apache-2.0 Python crawler for gathering web pages and producing LLM-oriented Markdown, HTML and structured extracts for downstream agents, document indexing and RAG. Its primary catalog identity is an **independently installable web-data ingestion library**, not the [RAGFlow](../ragflow/) indexing/agent engine or the provider-operated Crawl4AI Cloud service.

## Release and deployment boundary

Original [v0.9.5](https://github.com/unclecode/crawl4ai/releases/tag/v0.9.5), dated **2026-10-14**, is a non-prerelease version. The tagged package declares Python **>=3.10** and a **Beta** classifier, not independently verified production readiness. Python library, self-hosted browser/API container, and separate [Crawl4AI Cloud](https://crawl4ai.com/) have different security, costs and operators; the original tagged release stated that Docker images were still being built, not verified available.

Crawl4AI supports local or remote browser sessions, JavaScript-rendered content, Markdown conversion, CSS/XPath and optional LLM extraction, and multi-page crawling. It does **not** own RAGFlow's graph/indexing workflow: the tagged RAGFlow v0.27.3 explicitly depends on a narrower Crawl4AI 0.9.2 range, so upgrading that dependency to 0.9.5 requires separate compatibility testing.

## Security, licensing and maintenance

Untrusted websites and uploaded HTML can contain prompt-injection instructions or sensitive content. Set strict allowed domains and URL/file/localhost restrictions, enforce authenticated Docker API endpoints, isolate browser profiles/cookies and API keys, constrain concurrency and data retention, and obtain permission for every target site. Server `/execute_js` and screenshot/PDF endpoints require especially careful exposure review; stealth options do not authorize bypassing access controls. External model, proxy and cloud fees are not included in the code's Apache-2.0 grant.

The original tagged [legacy `setup.py`](https://github.com/unclecode/crawl4ai/blob/v0.9.5/setup.py) clears the local `.crawl4ai/cache` directory **when that script executes**. Check installation/build workflows and preserve important local cache first; do not assume all standard installations invoke this script. The project's v0.9.5 `pyproject.toml` retains a **Beta** classifier while legacy setup metadata says Alpha. Neither classifier is proof of independent production audit.

## Producer and service boundary

- Original Python-package author: [Unclecode](../../../../../../../producers/sub/u/sub/unclecode/) (pseudonymous original maintainer).
- Cloud operation: [CONTEXT4AI PTE LTD](https://crawl4ai.com/legal/) is named in the current hosted-service terms; this does not independently prove ownership of the original author or grant an additional software-producer identity.

## Official resources

- [Original source repository](https://github.com/unclecode/crawl4ai)
- [v0.9.5 release](https://github.com/unclecode/crawl4ai/releases/tag/v0.9.5)
- [Tagged package metadata](https://github.com/unclecode/crawl4ai/blob/v0.9.5/pyproject.toml)
- [Tagged source version](https://github.com/unclecode/crawl4ai/blob/v0.9.5/crawl4ai/__version__.py)
- [Tagged legacy installer](https://github.com/unclecode/crawl4ai/blob/v0.9.5/setup.py)
- [Documentation](https://docs.crawl4ai.com/)
- [Hosted-service legal terms](https://crawl4ai.com/legal/)
