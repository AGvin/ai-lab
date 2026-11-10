# Documentation Requirements

## Requirements

- Identify Perplexity API Platform Skills as Perplexity AI's official repository-backed collection of portable Agent Skills for Perplexity API Platform development workflows.
- Preserve the collection boundary: the repository currently packages skills for Sonar-to-Agent-API migration, Perplexity CLI search, and Perplexity Search SDK workflows and is designed to grow over time; do not create one peer catalog entity per skill by default.
- Keep the repository's Claude Code plugin marketplace packaging, Agent Plugin packaging, Codex plugin flow, ecosystem installers, docs MCP server, CLI/SDK packages, and API endpoints as distribution/access surfaces rather than separate skill-collection identities.
- Keep the Perplexity Skills Marketplace separate as the multi-source/user-and-organization marketplace/registry surface; this collection is a publisher-owned first-party skill set.
- Treat exact skill inventory, client compatibility, install commands, bundled MCP/configuration, invocation names, plugin metadata, and release state as freshness-sensitive.
- Distinguish local skill-only installation from Agent Plugin/Claude/Codex plugin paths that bundle a remote **Perplexity documentation MCP** connection. The reviewed `mcp.json` specifies `https://docs.perplexity.ai/mcp` with `streamable-http`. Even though the public docs MCP needs no API key, requests and submitted query text leave the local environment for Perplexity's documentation host; never include confidential API keys, customer data or internal source text without an approved data-processing basis.
- Do not imply that this documentation MCP provides authenticated Search/Sonar/Agent API entitlement or can perform paid customer searches; authentication and billing for actual APIs are distinct. Ask for approval before client config changes, account API calls or code migrations that modify app behavior.
- Preserve the repository-level Apache-2.0 distribution boundary while requiring path-specific license verification if future bundled assets establish different terms.
- Render the standard `entity-relations` block from validated current-entity relations.

## Documentation MCP network boundary — 2026-11-09

- The pinned [first-party README](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/README.md) describes plugin installation with docs MCP and standalone skill-only installations. The pinned [MCP config](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/mcp.json) uses `streamable-http` to connect to `https://docs.perplexity.ai/mcp`; no API key is required for that public documentation surface.
- Public documentation access is not offline or privacy-neutral, nor does it imply authorization to use paid Perplexity Search or Agent APIs. This is source and configuration inspection only: no network MCP session, customer API call, runtime compatibility test, or telemetry/retention verification occurred.

## Validation

- The collection remains distinct from the Perplexity Skills Marketplace registry.
- Individual repository skill directories are not duplicated as standalone AI Lab nodes without independent identity.
- Producer provenance resolves bidirectionally to Perplexity AI.

## Source-backed reader scope — 2026-10-20

- Identity and provenance: Perplexity API Platform Skills is the official repository-backed collection for API migration and search-development workflows. Its portable skill files and plugin packaging are distinct from the public Computer Skills Marketplace.
- Decision and deployment boundary: The repository declares Apache-2.0. Pin and inspect the selected revision, skill scripts and optional documentation integration before use. Installing instructions or a docs integration does not provide paid API access or permission to change an application's data.
- Render every visible current relation using canonical target names, explicit order first and alphabetical order within each relation group. Keep metadata paths out of reader navigation.
- Recheck account eligibility, exact artifact access, versions and terms before deployment. This source review does not certify runtime performance.
- Reviewed sources: <https://github.com/perplexityai/api-platform-developers>, <https://docs.perplexity.ai/docs/search/quickstart>.

## Scoped source interpretation — 2026-11-05

- Render the source-specific licensing, lifecycle, distribution and authorization boundaries from the current entity note.
- Use the pinned original README and applicable license paths; this bounded source qualification does not establish all contained skills, dependency versions, ownership clearance or runtime safety.
- Keep provenance/ownership review visibly pending. No blanket redistribution or execution permission follows from catalog inclusion.

## Static source and execution review — 2026-11-10

The complete selected upstream Git tree matches the current HEAD at `78f568a867bc7bc44ce625318b60ac0d86802c5f` (**62 identical tracked files**). The three skill entrypoints are migration, CLI and Search SDK guidance; this comparison establishes repository-source currentness, not live API behavior or the identity of separately downloaded packages.

The [migration scanner](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/migrate-sonar-to-agent-api/scripts/scan_sonar_usage.py) uses Python's standard library, recursively reads selected source/notebook files and prints matching paths, line numbers and up to 60 characters of source per finding. Its inspected code has no network or file-write calls. Scope the input directory and protect its output: snippets may expose private source or embedded secrets, and reading is not sandboxed by the skill.

The [CLI skill](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-cli/SKILL.md) recommends a shell installer from the mutable latest release of a separate repository and an in-place updater. The publisher describes checksum verification, but the installer, released binary and stored-key protection were not independently audited here. The skill documents a local `credentials.json` or `PERPLEXITY_API_KEY`, with the environment taking precedence. The [Search SDK skill](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-search-sdk/SKILL.md) recommends an unpinned `pip install pplx-srch-sdk`; its stated Python/platform support and per-request billing are publisher claims, not reproduced compatibility tests.

Search/Agent API examples send prompts, queries and requested URLs to external services using a key. The [fan-out example](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/skills/pplx-search-sdk/examples/fanout_research.py) also writes `results.jsonl` and `errors.jsonl`, preserving request specifications. The [evaluation grader](https://github.com/perplexityai/api-platform-developers/blob/78f568a867bc7bc44ce625318b60ac0d86802c5f/evals/migrate-sonar-to-agent-api/check.sh) is static by default; `--live` executes target application scripts and redirects their output to `/tmp/eval-run.out`. Migration instructions ask for production smoke calls when a key exists; possession of a key alone is not authorization to transmit data or incur costs.

No installer, scanner, SDK, migration or live evaluation was executed. External package provenance, dependency rights, hosted-service retention and ownership/control-chain review remain unresolved; no full-profile or adoption clearance follows from this static review.
