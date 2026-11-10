# Perplexity API Platform Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Perplexity API Platform Skills is the official repository-backed collection for API migration and search-development workflows. Its portable skill files and plugin packaging are distinct from the public Computer Skills Marketplace.

## Documentation MCP and data boundary

The pinned [first-party MCP configuration](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/mcp.json) connects plugin-capable clients to **`https://docs.perplexity.ai/mcp`** using `streamable-http`. This is a remote documentation server: when the client invokes it, document queries and any accompanying text are transmitted to that external host. The publicly accessible docs MCP does not require a Perplexity API key, but that is *not* permission to transmit confidential data, an offline mode, or entitlement to paid Search, Sonar or Agent API operations.

An Agent Plugin or supported Claude/Codex plugin can include both local instructions and this docs MCP connection. Skills-only installation can omit the MCP component. Review outbound-data policy and client settings before enabling the integration; do not paste keys, private source code or sensitive customer material into documentation queries. Any paid API use or application migration requires separate credentials, cost review and user authorization.

## Use and deployment boundaries

The repository declares Apache-2.0. Pin and inspect the selected revision, skill scripts and optional documentation integration before use. Installing instructions or a docs integration does not provide paid API access or permission to change an application's data.

## Producer

- [Perplexity AI](../../../../../producers/sub/p/sub/perplexity-ai/README.md).

## Source interpretation

Perplexity's Apache-2.0 repository distributes API-development skill guidance and plugin packaging, separate from the Computer Skills Marketplace. The optional public docs MCP server requires no API key; this does not establish paid search/API entitlement. Inspect scripts and authorize application migration or network calls independently.

[Reviewed original README](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. The complete selected repository tree was separately compared with current HEAD on 2026-11-10; external releases and live services remain outside that freshness check.

## Static source and execution review — 2026-11-10

The complete selected upstream Git tree matches the current HEAD at `78f568a867bc7bc44ce625318b60ac0d86802c5f` (**62 identical tracked files**). The three skill entrypoints are migration, CLI and Search SDK guidance; this comparison establishes repository-source currentness, not live API behavior or the identity of separately downloaded packages.

The [migration scanner](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/migrate-sonar-to-agent-api/scripts/scan_sonar_usage.py) uses Python's standard library, recursively reads selected source/notebook files and prints matching paths, line numbers and up to 60 characters of source per finding. Its inspected code has no network or file-write calls. Scope the input directory and protect its output: snippets may expose private source or embedded secrets, and reading is not sandboxed by the skill.

The [CLI skill](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-cli/SKILL.md) recommends a shell installer from the mutable latest release of a separate repository and an in-place updater. The publisher describes checksum verification, but the installer, released binary and stored-key protection were not independently audited here. The skill documents a local `credentials.json` or `PERPLEXITY_API_KEY`, with the environment taking precedence. The [Search SDK skill](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-search-sdk/SKILL.md) recommends an unpinned `pip install pplx-srch-sdk`; its stated Python/platform support and per-request billing are publisher claims, not reproduced compatibility tests.

Search/Agent API examples send prompts, queries and requested URLs to external services using a key. The [fan-out example](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-search-sdk/examples/fanout_research.py) also writes `results.jsonl` and `errors.jsonl`, preserving request specifications. The [evaluation grader](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/evals/migrate-sonar-to-agent-api/check.sh) is static by default; `--live` executes target application scripts and redirects their output to `/tmp/eval-run.out`. Migration instructions ask for production smoke calls when a key exists; possession of a key alone is not authorization to transmit data or incur costs.

No installer, scanner, SDK, migration or live evaluation was executed. External package provenance, dependency rights, hosted-service retention and ownership/control-chain review remain unresolved; no full-profile or adoption clearance follows from this static review.

## Official resources

- [Official skills repository](https://github.com/perplexityai/api-platform-developers).
- [API documentation](https://docs.perplexity.ai/docs/search/quickstart).
