# Documentation Requirements

## Requirements

- Identify Topoteretes as the current upstream GitHub Organization owning the Cognee repository for catalog provenance.
- Do not infer a differently named corporate entity without authoritative evidence.
- Render the standard `entity-relations` block from validated current-entity relations.
- Preserve this source-backed identity and provenance context: Topoteretes is the upstream GitHub organization publishing the represented Cognee repository. This is a source-backed publishing identity; the repository handle alone does not establish a differently named legal company or ownership of every Cognee integration and dependency.
- Explain the following operating and decision boundary: Distinguish the open-source installation from Cognee Cloud and the configured model providers. The current upstream README supports local extraction and embedding without an LLM key, but enabling a hosted model provider introduces provider calls. For shared deployments, review authentication, persistent storage and file-ingestion permissions; a local demonstration configuration does not establish a safe multi-user operating posture.
- Support the producer context with these first-party sources: <https://github.com/topoteretes/cognee>, <https://www.cognee.ai/>.

## Validation

- `produces` is the inverse of Cognee `produced-by`.
