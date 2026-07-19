<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:289d8a67b3fa4229f08437cf55d8298658a71772
  mode: translated
-->

# Підтримка Agent Skills на платформах

Agent Skills використовують переносний формат `SKILL.md`, але кожний host має власні discovery paths, installation UI, invocation syntax, permission model і plugin system.

Ця сторінка централізує platform-specific instructions, щоб product pages могли посилатися сюди, а не дублювати setup steps.

Остання перевірка: 2026-07-19.

## Переклади

- [English](../../)
- Українська

## Матриця підтримки

| Платформа | Native Agent Skills | Project-local skills | User-global skills | Explicit invocation | Automatic invocation | Plugin distribution |
|---|---:|---:|---:|---|---|---:|
| ChatGPT | Так, на відповідних plans і surfaces | Upload або створення в продукті замість repository scan | Personal і workspace-managed skills | Skill picker або direct request | Так | Так, на підтримуваних Work/Codex surfaces |
| OpenAI Codex | Так | `.agents/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | `$skill-name`, згадування skill або selector `/skills` | Так | Так |
| Claude Code | Так | `.claude/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | `/skill-name` | Так | Так, Claude Code-specific plugins |
| Cursor | Так, editor і CLI | `.cursor/skills/` або сумісні roots `.agents/skills/` | `~/.cursor/skills/` і підтримувані compatible roots | Slash-command menu | Так | Так, Cursor Marketplace |
| OpenCode | Так | `.opencode/skills/`, `.claude/skills/` або `.agents/skills/` | Відповідні user configuration roots | Попросити використати skill або дозволити agent викликати native tool `skill` | Так | Plugins OpenCode існують, але мають інший формат, ніж plugins OpenAI чи Claude Code |

Підтримка відрізняється навіть між surfaces одного product. Перед стандартизацією organization-wide installation перевірте актуальну product documentation.

## Переносна structure project

Для repositories, які використовують кілька сумісних agents, віддавайте перевагу neutral root Agent Skills, якщо його підтримує кожний вибраний client:

```text
project/
└── .agents/
    └── skills/
        └── release-notes/
            ├── SKILL.md
            ├── references/
            └── scripts/
```

Коли один client не scan neutral root, використовуйте один із підходів:

1. зберігайте canonical skill у `.agents/skills/` і створюйте reviewed symlinks із client-specific roots;
2. використовуйте installer, який копіює той самий source у кожний вибраний client;
3. пакуйте skill окремо у plugin format кожного client;
4. підтримуйте generated client adapters, залишаючи `SKILL.md` source of truth.

Не підтримуйте кілька manually edited copies без explicit synchronization і review process.

## ChatGPT

### Доступність

ChatGPT підтримує повторно використовувані personal і workspace skills на відповідних plans. Точна доступність залежить від plan, workspace settings, admin permissions, region і product surface.

Skills у ChatGPT відповідають open Agent Skills standard, але personal skills іноді потрібно додавати окремо на desktop і web/mobile surfaces, якщо synchronization недоступна.

### Створення або встановлення

Відкрийте розділ Skills в interface ChatGPT. Залежно від поточної surface він може бути розміщений у Plugin Directory або menu profile/workspace.

Підтримувані paths створення:

- попросити ChatGPT створити skill у conversation;
- використати Skills editor;
- upload наявний skill directory або archive;
- установити skill, яким поділився інший user або workspace;
- установити plugin, що містить skills, на підтримуваній surface.

Перед upload third-party skill перевірте весь його content, scripts, required connectors і network behavior. Product scanning є додатковим control, а не заміною source review.

### Виклик

Skill може activate автоматично, коли request відповідає його description. Щоб зробити вибір explicit, виберіть або згадайте skill, де це підтримує interface, чи прямо вкажіть skill name у prompt.

Приклад:

```text
Використай skill repository-link-checker, щоб перевірити цей documentation export.
```

### Керування

Використовуйте interface Skills, щоб inspect, share, download, disable або remove skill. Workspace admins можуть окремо контролювати:

- хто може створювати або використовувати skills;
- uploading;
- workspace sharing і publication;
- installation для інших members;
- access до apps або connectors, потрібних skill чи plugin.

### Обмеження

- доступність залежить від plan і workspace policy;
- skills і plugins доступні не в кожному ChatGPT mode або surface;
- skills не отримують connector або filesystem access автоматично;
- installed skill може поводитися по-різному в conversational і tool-enabled chats.

## OpenAI Codex

### Discovery paths

Codex читає repository skills із directories `.agents/skills` між current working directory і repository root:

```text
$CWD/.agents/skills/<name>/SKILL.md
$REPO_ROOT/.agents/skills/<name>/SKILL.md
```

User skills:

```text
$HOME/.agents/skills/<name>/SKILL.md
```

Shared machine або container skills:

```text
/etc/codex/skills/<name>/SKILL.md
```

Codex також містить system skills, bundled OpenAI.

### Manual installation

Копіюйте повний skill directory, а не лише `SKILL.md`:

```bash
mkdir -p .agents/skills
cp -R /path/to/release-notes .agents/skills/
```

Для personal installation:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R /path/to/release-notes "$HOME/.agents/skills/"
```

Codex слідує за symlinked skill directories. Використовуйте symlinks лише тоді, коли зрозуміла їхня update і trust model.

### Установлення через Codex

Codex надає вбудовані workflows створення й installation skills:

```text
$skill-creator
$skill-installer linear
```

Installer також може отримувати skills з інших repositories. Для consequential workflows фіксуйте source revision.

### Виклик

У CLI або IDE:

- запустіть `/skills`, щоб переглянути доступні skills;
- введіть `$`, щоб згадати skill;
- явно напишіть `$skill-name` у request;
- опишіть task і дозвольте implicit activation.

Приклад:

```text
$repository-link-checker перевір docs/ перед моїм commit.
```

### Увімкнення або вимкнення

Skill можна disable без видалення через `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/absolute/path/to/skill/SKILL.md"
enabled = false
```

Після зміни configuration restart Codex.

### OpenAI-specific metadata

Optional `agents/openai.yaml` може описувати presentation metadata, invocation policy і dependencies:

```yaml
interface:
  display_name: "Repository Link Checker"
  short_description: "Validate relative Markdown links"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI documentation access"
```

Зберігайте essential workflow instructions у `SKILL.md`; інші clients можуть ігнорувати цей file.

### Plugins

Plugins Codex можуть package skills разом із connectors, MCP configuration, hooks і presentation resources. Використовуйте desktop plugin browser ChatGPT або `/plugins` у Codex CLI, де це підтримується. Після installation почніть new session, щоб bundled skills стали доступними.

## Claude Code

### Discovery paths

Project skill:

```text
.claude/skills/<name>/SKILL.md
```

Personal skill:

```text
~/.claude/skills/<name>/SKILL.md
```

Plugin skill:

```text
<plugin-root>/skills/<name>/SKILL.md
```

Claude Code scan project skills від working directory через parent directories до repository root і може знаходити nested package skills, коли відкриваються relevant files.

### Manual installation

Project-local:

```bash
mkdir -p .claude/skills
cp -R /path/to/release-notes .claude/skills/
```

Personal:

```bash
mkdir -p "$HOME/.claude/skills"
cp -R /path/to/release-notes "$HOME/.claude/skills/"
```

Claude Code відстежує зміни в наявних skill roots. Якщо top-level skill directory створено після старту session і його не виявлено, restart session.

### Виклик

Використовуйте automatic selection або slash command, утворену з directory name:

```text
/release-notes
```

Plugin skills мають namespace:

```text
/plugin-name:release-notes
```

### Plugins

Додайте marketplace, а потім установіть plugin:

```text
/plugin marketplace add owner/repository
/plugin install plugin-name@marketplace-name
```

Equivalent non-interactive commands доступні через `claude plugin ...`.

Використовуйте standalone skills для personal, repository-local або experimental workflows. Використовуйте plugins Claude Code для managed distribution, namespacing, versioning і bundles, що містять agents, hooks, MCP servers або інші Claude-specific components.

## Cursor

### Discovery і invocation

Cursor підтримує Agent Skills в editor і CLI. Agents знаходять relevant workflows `SKILL.md` і можуть застосовувати їх автоматично. Skills також можна вибирати зі slash-command menu.

Використовуйте client-native project root:

```text
.cursor/skills/<name>/SKILL.md
```

Для portable project skills Cursor також підтримує Agent Skills-compatible roots, наприклад:

```text
.agents/skills/<name>/SKILL.md
```

Типовий personal root:

```text
~/.cursor/skills/<name>/SKILL.md
```

Точні compatible roots і parity між desktop, SSH, CLI та SDK surfaces можуть змінюватися. Тестуйте фактичну execution surface, а не припускайте, що desktop behavior застосовується всюди.

### Manual installation

Скопіюйте весь skill directory у вибраний project або personal root. Відкрийте settings Cursor для Rules, Commands або Skills, щоб підтвердити discovery, де UI це показує.

### Plugins

Plugins Cursor можуть package skills, rules, agents, commands, hooks і MCP configuration для installation через Marketplace. Installation можна почати з Marketplace або, де це підтримується, з Agent chat:

```text
/add-plugin plugin-name
```

Plugin format і behavior Cursor є platform-specific. Не припускайте, що directory plugin Claude Code або OpenAI установиться без змін.

## OpenCode

### Discovery paths

OpenCode розпізнає кілька project roots:

```text
.opencode/skills/<name>/SKILL.md
.claude/skills/<name>/SKILL.md
.agents/skills/<name>/SKILL.md
```

І відповідні global roots:

```text
~/.config/opencode/skills/<name>/SKILL.md
~/.claude/skills/<name>/SKILL.md
~/.agents/skills/<name>/SKILL.md
```

Для project-local paths OpenCode проходить від current working directory до Git worktree root.

### Виклик

OpenCode показує discovered metadata через native tool `skill`. Agent викликає:

```text
skill({ name: "release-notes" })
```

Users зазвичай описують task або просять OpenCode використати named skill. Full instructions завантажуються лише після виклику tool.

### Permissions

Контролюйте visibility skill і approval в `opencode.json`:

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

Значення:

- `allow` — завантажити одразу;
- `ask` — запросити approval;
- `deny` — приховати й відхилити access.

Skills також можна disable для конкретного agent, вимкнувши tool `skill`.

### Plugins

OpenCode підтримує plugins, але його plugin API і package model є OpenCode-specific. Для portable instructions віддавайте перевагу neutral directory Agent Skills. Використовуйте plugin OpenCode лише тоді, коли workflow потребує lifecycle hooks OpenCode, JavaScript/TypeScript extension code або іншої host-specific capability.

## Стратегія multi-platform maintenance

Для skill, що використовується в кількох clients:

1. виберіть один canonical source directory;
2. зберігайте portable workflow у `SKILL.md` і standard support folders;
3. ізолюйте host-specific metadata і manifests;
4. генеруйте або копіюйте installations через documented process;
5. pin або record source revision;
6. запускайте ті самі discovery і execution fixtures у кожному supported host;
7. документуйте known surface-specific limitations;
8. review update diffs перед deployment.

## Контрольний список перевірки

Для installation на кожній платформі:

- [ ] Skill з’являється в discovery list або UI платформи.
- [ ] Positive prompt активує його.
- [ ] Схожий negative prompt не активує його.
- [ ] Explicit invocation працює.
- [ ] Supporting files resolve коректно.
- [ ] Required scripts і tools доступні.
- [ ] Denied permissions fail visibly.
- [ ] Consequential actions зупиняються для approval.
- [ ] Removal або disabling прибирає skill із discovery.

## Джерела

- Стандарт Agent Skills: https://agentskills.io/
- Skills ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Skills Codex: https://developers.openai.com/codex/skills
- Plugins OpenAI: https://developers.openai.com/codex/plugins
- Skills Claude Code: https://code.claude.com/docs/en/skills
- Plugins Claude Code: https://code.claude.com/docs/en/plugins
- Agent Skills Cursor: https://cursor.com/docs/skills
- Agent Skills OpenCode: https://opencode.ai/docs/skills/
