# Documentation Requirements

## Requirements

- Present Code Intelligence as the canonical development-tools category for software whose primary purpose is to build, index, query, navigate, or analyze structural or semantic representations of software codebases.
- Explain the category in terms of codebase understanding: symbols, definitions, calls, imports, dependencies, references, architecture, paths, impact, and repository context may be represented or queried, but no single implementation technique is mandatory.
- Keep the category technology-neutral. AST parsing, static analysis, knowledge graphs, embeddings, lexical indexes, databases, language servers, and model-assisted extraction are implementation choices rather than defining requirements.
- Exclude products whose primary identity is a code editor, coding agent, code-review tool, spec/workflow system, or general graph/data platform merely because they expose code-intelligence features.
- Treat assistant/editor/MCP integrations as capabilities of the concrete product unless an integration artifact has an independently justified canonical identity.
- Use the validated direct-child projection for navigation and list every materialized direct child exactly once.
- Keep product-specific setup, security/privacy behavior, supported languages/integrations, benchmarks, versions, and other mutable claims with the concrete child profile.

## Validation

- Every direct child has codebase intelligence as its primary product identity rather than a secondary feature.
- Navigation matches the materialized direct children.
- The page remains category-level and does not duplicate concrete product profiles.
- The category does not imply that every product uses knowledge graphs, embeddings, LLMs, or any other single implementation technique.
