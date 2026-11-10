# Redis Agent Skills

**PROVENANCE/OWNERSHIP REVIEW PENDING.** Publisher attribution does not complete ownership/control-chain review or establish adoption clearance. See the [provenance policy](../../../../../../../project/sub/policies/sub/russia-linked-ai/).

Redis Agent Skills is Redis's official MIT-licensed collection of portable instructions for coding agents. The upstream repository covers Redis data structures, connections, search, semantic caching, clustering, security, observability and Iris development. These are instruction packages for working with Redis products, rather than a database deployment or a managed memory service. [Official collection](https://github.com/redis/agent-skills).

## Scope and operating boundaries

At the [inspected first-party revision](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md), the collection lists **14 skills**: seven Redis topics (`redis-core`, `redis-connections`, `redis-search`, `redis-semantic-cache`, `redis-clustering`, `redis-security`, `redis-observability`), `redis-docs-mcp`, and six Iris integration skills (`add-redis-iris`, `add-agent-memory`, `add-agent-playbooks`, `add-context-gateway`, `add-intent-router`, `add-lens`). The earlier `iris-development` entry is not in the current inspected directory list. Counts and names are mutable, not enduring guarantees.

The documented portable installation is `npx skills add redis/agent-skills`; this does **not** install the Redis Docs MCP server. The Claude Code, ChatGPT/Codex and Cursor plugin packages can bundle the public, read-only server at `https://redis.io/mcp`. **Every MCP search/fetch/ask query sends its text to redis.io**. Avoid including confidential content or credentials in those queries; disable `redis-docs` in the client's MCP settings if data policy forbids this transmission. Read-only documentation retrieval is not database authorization, nor does it guarantee absence of transferred data.

Review the instructions and database actions before enabling them. A skill cannot grant a missing credential, provision a deployment merely by being installed or guarantee that every Redis feature is available in the selected server or cloud plan. The repository's MIT license applies to these resources; the database, hosted service and connected tools retain their own licenses and permissions. [Collection scope](https://github.com/redis/agent-skills).

## Produced by

- [Redis](../../../../../producers/sub/r/sub/redis/)

## Source interpretation

Redis's MIT collection provides Redis instruction resources and client plugin packaging. Client plugins include a public documentation MCP server; standalone Agent Skills CLI installation does not carry that MCP component. Documentation access requires no Redis credentials, while database commands still need scoped access and version-appropriate review.

[Reviewed original README](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/README.md). Licensing is scoped to the inspected distribution; no skill or script was installed or executed. The complete selected Git tree was separately checked on 2026-11-10; live services and external packages were not audited.

## Complete selected-source freshness — 2026-11-10

The entire first-party Git tree at `74708dab4b3f81a9845803c3f642a4f7d443af69` matches current upstream HEAD: **203 identical tracked file blobs**, including source skills, plugin mirrors, scripts, evaluation material and manifests. No path or blob drift was found. This inventories the complete selected repository, not the separately installed Redis products, remote MCP contents, npm packages or live runtime behavior. A subsequent bounded static tooling and skill data-flow review is recorded below; third-party rights, installed behavior and independent full-profile review remain open.

## Static execution and data-flow review — 2026-11-10

The selected revision contains **14 source skill entrypoints and 58 skill files**; all 58 plugin mirror files have matching Git blob hashes. This is source correspondence, not a guarantee about an installed client or separately downloaded package.

### Repository tooling

The root [package manifest](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/package.json) has a `prepare: husky` lifecycle. Its [pre-commit hook](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/.husky/pre-commit) runs plugin synchronization and stages generated skill copies. The [synchronizer](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/scripts/sync-plugin-skills.mjs) deletes and rebuilds `plugins/redis-development/skills` in normal mode; `--check` compares without those writes. Run either from the intended checkout. This maintainer tooling is distinct from installing a skill-only bundle.

The [structure wrapper](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/scripts/validate-skill-structure.mjs) invokes an external Go `skill-validator`, can append to `GITHUB_STEP_SUMMARY`, and skips locally with success when the binary is absent; CI treats absence as a failure. CI installs the version named in the manifest. A local successful exit therefore does not by itself prove structure was checked. The inspected npm lockfile also marks `esbuild` and optional `fsevents` as having install scripts; dependency metadata is not an audit of downloaded package bytes.

The [evaluation runner](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/packages/redis-development-build/src/eval/anthropic-matrix.ts) launches configured Claude and Python executables with the inherited process environment. It sends generation and judge prompts, may retry each up to three attempts, and writes prompts, answers, grading and raw CLI-result/usage artifacts under `eval-workspaces`. `--no-session-persistence` on Claude does not prevent those repository artifacts. `--dry-run` returns before model commands and run-artifact writes, but the surrounding npm/runtime invocation still has its own dependency boundary. `--force` permits selected output overwrites; baseline promotion separately copies/writes committed benchmark summaries. Publisher benchmark files were not independently reproduced.

### Skill-directed actions

| Surface | Boundary at the inspected revision |
| --- | --- |
| Documentation MCP | The [docs skill](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/redis-docs-mcp/SKILL.md) states that all query text reaches Redis and `ask` also reaches the model provider behind its gateway. Public read-only documentation is distinct from database access. |
| Database guidance | Core/search/security/observability examples include data writes, index/alias changes, ACL/configuration/firewall changes and `SLOWLOG RESET`. They are instructions, not permission to act on an existing deployment. |
| Agent Memory | The [memory skill](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/add-agent-memory/SKILL.md) records user/assistant turns and supports shared namespaces and erasure. Its exclusion prompt is guidance rather than a guarantee: session content still reaches the model provider and direct `remember()` bypasses that exclusion. Decide retention, sharing and forbidden content before enabling write-back. |
| Agent Playbooks | [Runtime integration](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/add-agent-playbooks/references/integration.md) can submit uncovered answers unchanged as proposals; application privacy/quality gates remain necessary when that path is chosen. [Background extraction](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/add-agent-playbooks/references/memory-extraction.md) binds a whole memory store, with no namespace selection. Proposal creation is separate from publication. |
| Context Gateway | The [Gateway skill](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/add-context-gateway/SKILL.md) moves upstream secrets and tool traffic behind the Gateway and can retain results in caches/handles. It explicitly says `acl_field_mappings` is rejected and every key granted that Surface can read every record of it; do not assume per-record tenant isolation. Its `service create` has no dry-run, unlike several other Iris provisioning commands. |
| Intent Router / LangCache | Router examples upload route phrases and send runtime messages for matching; the semantic-cache examples send prompts and store responses in the selected service. Local instruction installation is distinct from enabling either data path. |
| Lens | The [Lens skill](https://github.com/redis/agent-skills/blob/74708dab4b3f81a9845803c3f642a4f7d443af69/skills/add-lens/SKILL.md) adds client instrumentation and exports turn/retrieval/prompt-related spans to a configured endpoint. Existing application OpenTelemetry exporters can receive those spans, content included. Inspect capture, destinations and retention in the selected SDK/deployment before private use; defaults were not independently tested. |

Iris instructions separate runtime, authoring/content and administrative credentials and warn that JSON key creation without a destination file prints the secret. Treat service creation, key minting, content publication, database operations and client-configuration rewrites as separately scoped actions. Python Iris/LangCache/framework dependencies, model services, external validator and actual host permissions require their own review.

No repository tooling, installer, database command, model evaluation, MCP session or Iris service operation was executed. This bounded static review maps the original implementation and instruction boundaries; ownership/control-chain, selected third-party/service rights, installed-code behavior and independent full-profile conclusion remain open.

## Official resources

- [Official collection](https://github.com/redis/agent-skills)
