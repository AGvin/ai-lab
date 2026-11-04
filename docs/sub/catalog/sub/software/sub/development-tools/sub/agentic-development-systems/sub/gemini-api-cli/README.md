# Gemini API CLI

**Gemini API CLI** (`gemini-api`) is Google's stateless command-line client for accessing [Gemini API](https://ai.google.dev/gemini-api/docs) models, multimodal analysis and media generation, and managed agent capabilities from an existing coding agent, shell or CI system. It is **not** the general interactive Gemini CLI or Google Agents CLI.

## Interface and deployment

The [pinned first-party README](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/README.md) documents a Go-based CLI with Windows, Linux and macOS installation options, agent-readable command schemas, JSON/TOON output and the `--dry-run` option. Dry-run resolves and validates a request without contacting the Gemini API, and prints credentials in redacted form. Agentic workflows can call the binary and consume returned artifacts, but the CLI itself is stateless; externally managed agents operate on Google's services rather than locally.

The [pinned Go module](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/go.mod) targets Go 1.26.10. Check a selected release's dependencies, platform support and change log rather than treating a pinned source snapshot as a tested binary.

## Operational and rights boundaries

The official README labels the client **beta** and warns that breaking changes may occur. Pin release versions in automated workflows. Keep API keys and generated output out of public logs, use least-privilege access where supported, and plan for remote data transfer, quotas, media rights and provider billing. A local CLI does not include free inference or imply that hosted models and managed agent services carry the CLI's license.

The [CLI source is Apache-2.0 licensed](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/LICENSE). No installation, Gemini API request, managed-agent run, cross-platform test, full license audit or whole-catalog clean pass is claimed.

## Official sources

- [Gemini API CLI repository](https://github.com/google-gemini/gemini-api-cli)
- [Pinned README](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/README.md)
- [Pinned Go module](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/go.mod)
- [Pinned Apache-2.0 LICENSE](https://github.com/google-gemini/gemini-api-cli/blob/3197748d387c025604ec80f9f87d6f499bd7d7f7/LICENSE)
