<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:ca206d82f99cb0b0df1aa435d05140bd85c839e0
  mode: translated
-->

# Джерела й колекції Agent Skills

Agent Skills можуть надходити з офіційних vendor catalogs, open standards, community repositories, installation indexes або platform-specific plugin marketplaces. Ці sources розв’язують різні задачі й не повинні вважатися рівнозначними trust signals.

Остання перевірка: 2026-07-19.

## Переклади

- [English](../../)
- Українська

## Типи джерел

| Тип source | Основна роль | Чого він не гарантує |
|---|---|---|
| Specification | Визначає portable format і behavior model | Quality, safety, maintenance або client support конкретного skill |
| Vendor catalog | Публікує skills, які підтримує або курує platform чи technology vendor | Придатність для кожного environment або permission policy |
| Community collection | Пакує workflows і погляди author | Independent review, long-term compatibility або organizational approval |
| Installer або leaderboard | Допомагає знаходити й копіювати skills у clients | Що popularity означає correctness або safety |
| Plugin marketplace | Поширює host-specific managed package | Portability до іншого host або transparency кожної runtime behavior |

Перед adoption skill перевірте source revision, повний `SKILL.md`, scripts, dependencies, license, network use, writable paths, credentials і update model. Див. [Використання Agent Skills](../../../using/l10n/uk_UA/).

## Стандарт Agent Skills

Portable specification опублікована на `agentskills.io`.

Використовуйте її як canonical source для:

- required directory і entrypoint `SKILL.md`;
- YAML frontmatter fields;
- naming і description constraints;
- progressive disclosure;
- optional directories `scripts/`, `references/` і `assets/`;
- guidance для client implementations;
- validation expectations.

Skill, що відповідає specification, може бути portable, але clients усе одно можуть відрізнятися installation paths, invocation syntax, permissions, optional metadata і supported tools. Див. [Підтримка платформ](../../../platform-support/l10n/uk_UA/).

## Каталог OpenAI Skills

Repository: `openai/skills`

Каталог OpenAI містить skills для Codex і відповідає стандарту Agent Skills. Repository розділяє skills на категорії, зокрема:

- `.system` — skills, bundled із поточними distributions Codex;
- `.curated` — reviewed skills, які можна встановити за name через `$skill-installer`;
- `.experimental` — examples і workflows, що потребують explicit source selection та додаткового evaluation.

Типова installation у Codex:

```text
$skill-installer gh-address-comments
```

Або з конкретного repository path:

```text
$skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/create-plan
```

Restart Codex після installation, якщо цього потребує поточна surface.

Розглядайте license і trust boundary окремо для кожного skill. Каталог OpenAI явно дозволяє окремим skills мати власні license files.

Рекомендоване використання:

- вивчення актуальних OpenAI-specific skill patterns;
- installation curated workflows Codex;
- дослідження `agents/openai.yaml` та іншої OpenAI presentation metadata;
- порівняння system, curated і experimental distribution policies.

## Repository Anthropic Skills

Repository: `anthropics/skills`

Public repository Anthropic поєднує:

- examples Agent Skills;
- specification і template material;
- creative та design examples;
- development і technical examples;
- enterprise і communication examples;
- complex document skills для DOCX, PDF, PPTX та XLSX.

Багато examples мають open source, а деякі production document implementations є source-available за власними terms. Перевіряйте license у відповідному path, а не припускайте одну license для всього catalog.

Claude Code може зареєструвати repository як plugin marketplace:

```text
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
```

Document collection можна встановити окремо:

```text
/plugin install document-skills@anthropic-agent-skills
```

Рекомендоване використання:

- вивчення простих і складних skill structures;
- дослідження production-scale використання scripts, references і assets;
- використання template як starting point;
- порівняння standalone skills із packaging plugin Claude Code.

## Verified skills NVIDIA

Repository: `NVIDIA/skills`

NVIDIA публікує catalog skills для NVIDIA libraries, AI Blueprints і platform tools. Skills підтримуються в product repositories і mirrored у catalog через automated pipeline.

Catalog додає governance artifacts понад базовий Agent Skills format, зокрема:

- `skill-card.md` для identity і governance documentation;
- detached signatures `skill.oms.sig`;
- evaluation datasets;
- generated benchmark reports, де вони доступні;
- published trust anchor для signature verification.

Установлення через Skills CLI:

```bash
npx skills add nvidia/skills
```

Installer запитує selected skills і destination clients.

Cryptographic verification може підтвердити, що published files відповідають signed NVIDIA package. Вона не доводить, що skill придатний для конкретного repository, credential scope або production environment. Окремо перевіряйте capabilities і permissions.

Рекомендоване використання:

- guidance щодо NVIDIA CUDA-X і AI platform;
- вивчення signed skill distribution і provenance;
- вивчення skill cards, evaluation artifacts та governance controls;
- organization-level allow-listing на основі verified revisions.

## skills.sh

Website і CLI: `skills.sh` та `vercel-labs/skills`

`skills.sh` — discovery index, leaderboard і installer для public repositories Agent Skills. Типова command:

```bash
npx skills@latest add owner/repository
```

CLI знаходить skill directories у source і запитує, які clients мають їх отримати.

Важливі operational notes:

- CLI копіює skills у selected client roots;
- copied skills можна редагувати локально;
- updates потребують повторної installation або managed process;
- popularity частково базується на aggregated installation telemetry;
- telemetry можна disable через `DISABLE_TELEMETRY=1`;
- наявність у registry і security scanning не гарантують quality або safety.

Рекомендоване використання:

- пошук public collections;
- installation того самого skill у кілька compatible clients;
- порівняння popularity і ecosystem adoption;
- bootstrap editable project-local copies.

Для consequential workflows pin reviewed commit замість blind tracking latest repository state.

## `obra/superpowers`

Repository: `obra/superpowers`

Superpowers — opinionated software-development methodology, реалізована як composable skills і bootstrap instructions. Вона наголошує на clarification перед implementation, detailed planning, isolated worktrees, test-driven development, reviews і verification перед completion.

Вона підтримує кілька agent harnesses через mixture plugins, marketplaces, native skills і host-specific installation instructions. Установлюйте її окремо для кожного harness і перевіряйте, які components є host adapters, а які — portable skills.

### Базовий workflow

1. `brainstorming`
2. `using-git-worktrees`
3. `writing-plans`
4. `subagent-driven-development` або `executing-plans`
5. `test-driven-development`
6. `requesting-code-review`
7. `finishing-a-development-branch`

### Повний список skills

#### Testing

- `test-driven-development` — enforce implementation loop red-green-refactor.

#### Debugging

- `systematic-debugging` — досліджувати root causes через structured multi-phase process.
- `verification-before-completion` — вимагати evidence, що fix або task справді complete.

#### Collaboration і delivery

- `brainstorming` — уточнювати idea через questions і design validation.
- `writing-plans` — створювати detailed small implementation tasks із verification steps.
- `executing-plans` — виконувати approved plans batches із checkpoints.
- `dispatching-parallel-agents` — координувати independent tasks concurrently.
- `requesting-code-review` — готувати й запитувати structured review.
- `receiving-code-review` — оцінювати й опрацьовувати review feedback.
- `using-git-worktrees` — створювати isolated workspaces для feature work.
- `finishing-a-development-branch` — перевіряти completion і вибирати disposition branch.
- `subagent-driven-development` — виконувати tasks із fresh subagents і staged review.

#### Meta

- `writing-skills` — створювати й тестувати skills за methodology collection.
- `using-superpowers` — bootstrap і пояснення workflow Superpowers.

### Рекомендований starting set

Почніть із цих skills, а не вмикайте всю methodology без перевірки:

- `brainstorming` — висока цінність, коли requirements неповні;
- `writing-plans` — перетворює accepted design на testable work;
- `test-driven-development` — додає rapid evidence loop під час implementation;
- `systematic-debugging` — зменшує speculative fixes;
- `verification-before-completion` — запобігає unsupported completion claims;
- `requesting-code-review` — додає explicit review gate.

Додавайте worktree, subagent і branch-finishing skills лише тоді, коли selected client і repository workflow підтримують їхні assumptions.

## `mattpocock/skills`

Repository: `mattpocock/skills`

Ця collection надає small composable engineering і productivity workflows. Вона явно розрізняє:

- **user-invoked skills** — orchestration flows, доступні лише після вибору user;
- **model-invoked skills** — повторно використовувані disciplines, які model може вибирати автоматично, коли вони relevant.

Це distinction є convention collection, а не required field open Agent Skills specification.

Установіть editable copies через `skills.sh`:

```bash
npx skills@latest add mattpocock/skills
```

Collection також надає managed plugin Claude Code:

```text
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

### Повний список skills

#### Engineering: user-invoked

- `ask-matt` — route situation до appropriate workflow.
- `grill-with-docs` — інтерв’ювати user під час створення domain documentation і architectural decisions.
- `triage` — проводити issues через structured triage process.
- `improve-codebase-architecture` — знаходити й обговорювати opportunities поглиблення architecture.
- `setup-matt-pocock-skills` — налаштовувати repository-specific issue tracking, labels і documentation paths.
- `to-spec` — перетворювати current discussion на durable specification.
- `to-tickets` — декомпозувати plan або specification на dependency-aware tasks.
- `implement` — реалізовувати accepted specification із TDD seams і review.
- `wayfinder` — планувати body of work, надто великий для одного agent session, як investigation tickets.

#### Engineering: model-invoked

- `prototype` — створювати disposable prototype для відповіді на design question.
- `diagnosing-bugs` — reproduce, minimize, hypothesize, instrument, fix і regression-test.
- `research` — досліджувати primary sources і зберігати cited findings.
- `tdd` — реалізовувати по одному vertical slice через red-green-refactor.
- `domain-modeling` — підтримувати project terminology, edge cases і architectural decisions.
- `codebase-design` — design deep modules за small testable interfaces.
- `code-review` — independently review diff щодо standards і specification fidelity.
- `resolving-merge-conflicts` — resolve conflicts через tracing intent обох сторін.

#### Productivity: user-invoked

- `grill-me` — інтерв’ювати user, доки plan або decision не буде sufficiently resolved.
- `handoff` — compact current session у continuation document.
- `teach` — керувати multi-session learning workflow.
- `writing-great-skills` — пояснювати principles predictable skill authoring.

#### Productivity: model-invoked

- `grilling` — reusable interview discipline, що лежить в основі explicit grilling workflows.

### Рекомендований starting set

Для documentation і software engineering:

- `grill-me` — уточнювати idea без assumptions щодо repository workflow;
- `grill-with-docs` — уточнювати architecture зі збереженням decisions у documentation;
- `grilling` — reusable questioning behavior для інших skills;
- `domain-modeling` — створювати й підтримувати shared terminology;
- `diagnosing-bugs` — досліджувати до зміни code;
- `tdd` — реалізовувати з immediate executable feedback loop;
- `code-review` — перевіряти engineering standards і specification fidelity;
- `to-spec` — зберігати agreed solution перед implementation;
- `implement` — поєднувати approved specification з implementation і review.

Установіть `setup-matt-pocock-skills` перед repository-dependent workflows, якщо дотримуєтеся documented setup model collection.

## Вибір між двома engineering collections

| Потреба | Superpowers | Skills Matt Pocock |
|---|---|---|
| End-to-end prescribed development methodology | Strong fit | Compose selected workflows manually |
| Small independently adoptable practices | Available, але methodology-oriented | Primary design goal |
| Explicit requirement interviews | `brainstorming` | `grill-me`, `grill-with-docs`, `grilling` |
| Domain vocabulary і ADR maintenance | Indirect | `domain-modeling`, `grill-with-docs` |
| TDD | `test-driven-development` | `tdd` |
| Debugging | `systematic-debugging` | `diagnosing-bugs` |
| Review | Pair requesting/receiving review | Two-axis `code-review` |
| Subagent execution | Core workflow option | `implement` може orchestrate supporting disciplines |
| Large multi-session planning | Detailed plans і execution | `wayfinder`, tickets, specifications |

Не встановлюйте обидві complete methodologies із automatic activation overlapping workflows без testing precedence. Віддайте перевагу small reviewed subset із clear ownership кожного stage.

## Контрольний список adoption

Для кожного source або collection:

- [ ] Визначено, чи це standard, catalog, installer, collection або plugin marketplace.
- [ ] Зафіксовано repository, revision, license і maintainer.
- [ ] Перевірено всі selected skills і bundled scripts.
- [ ] Підтверджено supported clients і installation roots.
- [ ] Визначено, чи updates pinned, copied, forked або managed.
- [ ] Протестовано positive і negative activation prompts.
- [ ] Узгоджено ownership overlapping workflows.
- [ ] Обмежено tools, credentials і writable paths.
- [ ] Перевірено removal і rollback.

## Джерела

- Agent Skills: https://agentskills.io/
- OpenAI Skills: https://github.com/openai/skills
- Anthropic Skills: https://github.com/anthropics/skills
- NVIDIA Skills: https://github.com/NVIDIA/skills
- skills.sh: https://skills.sh/
- CLI skills.sh: https://www.skills.sh/docs/cli
- Superpowers: https://github.com/obra/superpowers
- Skills Matt Pocock: https://github.com/mattpocock/skills
- [Використання Agent Skills](../../../using/l10n/uk_UA/)
- [Plugins](../../../../../plugins/l10n/uk_UA/)
