# Documentation Requirements

## Requirements

- Use the reader-facing title `llms.txt` and explain it first as a concise Markdown discovery/index file that a website or documentation publisher can expose so AI agents can understand the site and find high-value machine-friendly resources without loading the whole corpus.
- State the current status accurately: `llms.txt` is an emerging community proposal/convention from Jeremy Howard, not a universally mandatory or ratified web standard. Keep exact normative details with `catalog/specifications/formats/llms-txt/` and re-check the current upstream revision before presenting changing syntax as fixed.
- Explain the core mental model as **index, not dump**. A good `llms.txt` provides project/site identity, a concise summary or interpretation guidance when useful, and curated groups of links with short descriptions; detailed content stays behind those links.
- Explain path scope: a root `/llms.txt` can cover the origin, while a path-specific file such as `/docs/llms.txt` can cover only that subtree. When several apply, the most specific applicable file should guide the agent.
- Explain the current high-level structure without duplicating every normative nuance: H1 project/site title; optional summary/details; H2 link groups; Markdown list links with optional descriptions; and the conventional `Optional` section for lower-priority resources.
- Explain how an agent should use the file:
  1. fetch the most specific applicable `llms.txt`;
  2. read the short project/site context and link descriptions;
  3. select only resources relevant to the task;
  4. prefer linked Markdown or otherwise low-noise canonical content where available;
  5. fetch additional resources only when needed and preserve source/provenance awareness.
- Explain how a publisher should apply it:
  1. choose the web path whose content the file describes;
  2. write a short, stable identity/summary rather than marketing filler;
  3. group the most useful canonical resources by reader/agent purpose;
  4. add short descriptions that clarify why each resource matters;
  5. place secondary material under `Optional` when useful;
  6. make linked machine-friendly representations directly fetchable where practical;
  7. test every link and keep the file synchronized with the published corpus.
- Recommend curation over exhaustive enumeration. Do not mechanically copy a full sitemap into `llms.txt`; prioritize authoritative entry points and task-relevant documentation that help an agent decide what to fetch next.
- Explain Markdown alternatives from the current proposal at a practical level: publishers can expose clean `.md` representations of pages and advertise them through standard link relations. Keep exact URL and `Link`/HTML relation syntax with the formal proposal artifact.
- Distinguish `llms.txt` from `llms-full.txt`: `llms.txt` is deliberately small and navigational; `llms-full.txt` is an ecosystem convention that aggregates much more or all documentation content in one file. The latter is useful in different context/ingestion scenarios and is not currently defined by llmstxt.org v2.
- Distinguish `llms.txt` from `robots.txt`: it provides context/discovery rather than crawler permission or prohibition. Respect actual access-control, crawler-policy, legal, and authorization boundaries independently.
- Distinguish `llms.txt` from `sitemap.xml`: the sitemap is primarily an enumeration for search/discovery systems, whereas `llms.txt` is curated and can point to agent-friendly or even relevant external resources with semantic descriptions.
- Distinguish `llms.txt` from RAG/search/vector indexes: the file is publisher-side discovery metadata/content; a consuming agent may use any retrieval architecture after fetching it.
- Distinguish `llms.txt` from MCP or another runtime integration protocol: the static file does not expose executable capabilities, negotiate a session, or authorize actions.
- Explain suitable use cases: software/API documentation, product knowledge, public knowledge bases, course/reference sites, or other content where an agent benefits from a reliable guided entry point.
- Explain when it adds little value: very small single-page sites, private content that should not be exposed, or environments where the consuming system already receives an equivalent tightly controlled canonical index through another mechanism.
- Include a compact example that follows the current proposal shape and demonstrates useful descriptions rather than a long URL dump.
- Include a practical validation checklist: raw file fetch succeeds; H1 exists; descriptions are concise; links resolve; linked content is public and intended for agents; high-priority links are canonical/current; lower-priority content is optional; file size/context remains intentionally small; and a test agent can answer representative navigation questions starting from the file alone.
- Treat adoption counts, client support, crawler behavior, SEO/answer-engine effects, and platform automation as mutable ecosystem evidence rather than guaranteed properties of the format.
- Preserve the trust boundary: an agent should not execute instructions, disclose secrets, or grant privileges merely because content is linked from `llms.txt`; normal source trust, prompt-injection defenses, authorization, and content validation still apply.
- Include the current llmstxt.org proposal and upstream repository as primary research sources, and provide a clear link to the formal AI Lab proposal artifact for readers who need exact current format rules.

## Validation

- The page teaches both what `llms.txt` is and how publishers/agents should use it without becoming the normative specification owner.
- `llms.txt` is presented as a concise curated index rather than a mandatory full-site dump.
- The page does not claim that `llms.txt` controls crawler access, replaces sitemaps, implements RAG, or provides runtime capabilities.
- `llms-full.txt` remains clearly separate and is not described as a current llmstxt.org v2 requirement.
- Mutable adoption/support/SEO claims are not treated as universal guarantees.
- Practical advice remains compatible with the current upstream proposal and preserves access-control and trust boundaries.
