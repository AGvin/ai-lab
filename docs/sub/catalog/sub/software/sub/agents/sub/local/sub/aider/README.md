# Aider

Aider is an open-source terminal-based AI pair-programming tool that works directly with local Git repositories. It edits repository files, understands codebase context, and integrates changes into the ordinary Git workflow, including automatic commits that can be inspected, diffed, managed, or undone with standard Git tooling.

## Execution boundary

Aider runs as a user-controlled local CLI and can connect to cloud or local model backends. Model-provider choice therefore determines important privacy, credential, and data-flow boundaries; local model support does not make every Aider workflow offline by default.

Because Aider can modify source files and can be used alongside generated-code execution workflows, protect repository secrets, scope provider credentials, review diffs before push or publication, and isolate untrusted generated code when appropriate.

## Official resources

- [Aider website](https://aider.chat/)
- [Aider documentation](https://aider.chat/docs/)
- [Aider repository](https://github.com/Aider-AI/aider)
- [Aider AI](../../../../../../../producers/sub/a/sub/aider-ai/)
