# Documentation Requirements

## Requirements

- Present Application Development as the canonical software index for frameworks, SDKs, libraries, and common abstraction layers whose primary role is integrating generative-AI capabilities into applications.
- List every materialized direct child exactly once with a concise, source-backed description of its primary application-development role.
- Keep framework-specific APIs, supported languages and runtimes, integrations, provider support, deployment options, and mutable compatibility facts with child software profiles.
- Preserve the primary-role boundary: frameworks whose primary identity is agent orchestration belong under `catalog/software/agent-frameworks/`, while retrieval-first frameworks belong under the sibling Data and Retrieval category even when application-development frameworks expose agents or RAG features themselves.
- Do not classify a framework solely by one capability such as tools, RAG, agents, streaming, or structured output when its broader supported application-development surface is the primary identity.

## Content Specification

- Explain the Application Development primary-role boundary before the child list.
- Describe Vercel AI SDK, Genkit, Spring AI, LangChain4j, Mirascope, and Microsoft.Extensions.AI from current official sources.
- Link Agent Frameworks and Data and Retrieval as adjacent canonical owners where their primary roles differ from this category.

## Validation

- Navigation matches the materialized direct children.
- The index remains category-level and does not duplicate child profiles.
- Agent and retrieval capabilities inside a general application framework do not by themselves cause duplicate ownership across categories.
- Product summaries remain consistent with current official documentation and canonical child requirements.
