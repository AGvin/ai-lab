# Documentation Requirements

## Requirements

- Identify Gemini API CLI (`gemini-api`) as Google's released stateless Go command-line client for using Gemini API models, media and managed agents from existing assistants or shell automation, not the broader interactive Gemini CLI, Google Agents CLI, or the API/service.
- Source snapshot: `3197748d387c025604ec80f9f87d6f499bd7d7f7`, first-party [README](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/README.md), [Go module](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/go.mod), and [Apache-2.0 LICENSE](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/LICENSE). `go.mod` identifies `github.com/google-gemini/gemini-api-cli` and a Go 1.26.10 toolchain target; that does not guarantee installed local compatibility or cross-platform testing.
- Describe a CLI with machine-readable schemas, structured output and an explicit `--dry-run` mode that validates resolved HTTP inputs and redacts credentials without issuing requests. Avoid describing these as tested local behaviors.
- Distinguish stateless local CLI execution from Gemini API network requests, managed-agent execution, external model terms, billing and any generated media/data rights.
- Warn that the project's official README calls this tool **beta**, recommends pinning release versions in CI due to breaking changes, and does not currently accept open pull requests.
- Document secret handling: Google API keys, shell environment and logs; never store credentials in scripts, CI output or checked-in configuration. Model calls, media requests and managed agent sessions require provider access and can generate charges.
- Do not claim installing the CLI, making API calls, generating media, executing remote agents, verifying all operating systems, whole-repository CI or a whole-catalog clean pass.

## Validation

- Pinned README, go.mod and license support installation and scope claims.
- One catalog entry indexed under Agentic Development Systems and differentiated from Google Agents CLI.
