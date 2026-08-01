# Agent Skills

> **Temporary catalog summary:** This overview is a placeholder for the RC structure and will be replaced by a reviewed Agent Skills catalog introduction.

Agent Skills are portable, named packages of procedural instructions and optional scripts, references, and assets that a compatible AI host can discover and load for repeatable work.

This catalog separates individual skills from named repositories or curated collections that distribute several skills. Plugins and host-specific packages are delivery or integration mechanisms unless they have a distinct canonical identity.

## Child pages

- [`skills/`](./sub/skills/) — individual Agent Skills.
- [`collections/`](./sub/collections/) — named catalogs and coordinated skill collections.

## Relationship requirements

Every selected skill and collection should link bidirectionally:

- skill → collection;
- collection → selected skills;
- skill or collection → canonical producer;
- producer → produced collections and selected skills.

Every skill profile must also describe verified dependencies, distinguishing required Agent Skills, collection or setup requirements, runtime/tool dependencies, bundled resources, and reverse dependants where useful.

## Legacy content preservation

The existing documentation under `docs/sub/notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/` contains substantial educational and operational content, including definitions, skill anatomy, discovery and activation behavior, portability, security, usage, creation, testing, platform support, source evaluation, examples, and English/Ukrainian localization.

The current catalog pages do **not** replace that material. Do not delete, collapse, or overwrite the legacy Agent Skills documentation until non-catalog ownership and item-level migration mapping are approved and the unique content and translations are preserved.

## Official standard

- [Agent Skills](https://agentskills.io/)
- [Agent Skills specification](https://agentskills.io/specification)
