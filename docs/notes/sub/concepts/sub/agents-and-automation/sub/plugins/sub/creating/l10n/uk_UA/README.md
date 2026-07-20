<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:479360a9061bfad04b6eb9ab83efeb9f47c66c45
  mode: translated
-->

# Створення AI plugins

Цей tutorial пояснює, як проєктувати й створювати AI plugin, коли standalone Agent Skill недостатньо. Спочатку він описує спільну architectural model, а потім показує повний приклад для Claude Code, оскільки plugin manifests залежать від платформи.

## Переклади

- [English](../../)
- Українська

## Навчальні цілі

Після завершення цього guide ви повинні вміти:

- визначати, чи потрібен plugin;
- відокремлювати portable skills від host-specific adapters;
- проєктувати manifest і package layout;
- безпечно об’єднувати skills, commands, hooks і MCP configuration;
- тестувати installation, activation, update і removal;
- публікувати через marketplace, не представляючи формат одного host як universal.

## 1. Спочатку виберіть target host

Не починайте з generic directory `plugin/`. Спочатку визначте host і його official schema:

```text
Target host:
Minimum supported version:
Plugin manifest format:
Supported components:
Marketplace or direct-install mechanism:
Permission model:
Update mechanism:
```

Claude Code plugin, OpenAI plugin, Cursor plugin і OpenCode plugin можуть надавати подібні capabilities, але використовують різні manifests і runtime contracts.

## 2. Переконайтеся, що plugin виправданий

Використовуйте standalone skill, коли package містить лише одну portable procedure.

Створюйте plugin, коли потрібна одна або кілька таких можливостей:

- кілька skills потрібно встановлювати й version разом;
- host потребує custom commands або agents;
- мають виконуватися lifecycle hooks;
- потрібно налаштувати MCP server або connector;
- потрібні marketplace distribution і managed updates;
- namespacing запобігає collisions commands;
- installation потребує host-specific UI metadata.

## 3. Відокремте portable і host-specific layers

Рекомендований source layout:

```text
engineering-workflows/
├── skills/
│   ├── clarify-requirements/
│   │   └── SKILL.md
│   └── review-change/
│       └── SKILL.md
├── mcp-servers/
│   └── project-status/
├── adapters/
│   ├── claude-code/
│   ├── openai/
│   ├── cursor/
│   └── opencode/
├── tests/
└── README.md
```

Portable files `SKILL.md` залишаються canonical. Кожен adapter пакує їх відповідно до правил конкретного host.

## 4. Визначте plugin contract

Перед написанням manifest задокументуйте:

```text
Plugin name:
Target users:
Problems solved:
Bundled skills:
Bundled commands or agents:
Hooks and trigger events:
MCP servers or connectors:
Required runtimes:
Required credentials:
Filesystem access:
Network access:
Consequential actions:
Approval points:
Update and rollback policy:
Uninstall cleanup:
```

## 5. Створіть мінімальний package

Мінімальний plugin повинен містити лише files, потрібні вибраному host, і documentation.

Conceptual example:

```text
plugin-root/
├── manifest
├── README.md
└── skills/
    └── clarify-requirements/
        └── SKILL.md
```

Переконайтеся, що package встановлюється, перш ніж додавати hooks, executable code або external integrations.

## 6. Спроєктуйте manifest

Manifest зазвичай визначає:

- stable plugin identifier;
- display name і description;
- version;
- publisher і source repository;
- license;
- minimum host version;
- component entrypoints;
- requested capabilities або dependencies;
- marketplace metadata.

Зберігайте manifest declarative. Не приховуйте installation behavior у недокументованих scripts.

## 7. Повний приклад Claude Code

Claude Code plugins використовують manifest `.claude-plugin/plugin.json` і conventional component directories.

```text
engineering-workflows-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── clarify-requirements/
│   │   └── SKILL.md
│   └── review-change/
│       └── SKILL.md
├── commands/
│   └── prepare-review.md
├── hooks/
│   └── hooks.json
├── scripts/
│   └── verify-clean-tree.sh
└── README.md
```

Приклад `.claude-plugin/plugin.json`:

```json
{
  "name": "engineering-workflows",
  "description": "Reusable requirement clarification and change-review workflows.",
  "version": "1.0.0",
  "author": {
    "name": "Example Engineering Team"
  },
  "repository": "https://github.com/example/engineering-workflows-plugin",
  "license": "MIT"
}
```

Приклад `skills/clarify-requirements/SKILL.md`:

```markdown
---
name: clarify-requirements
description: Interview the user to resolve ambiguous product or engineering requirements before implementation. Use when scope, constraints, terminology, acceptance criteria, or tradeoffs remain unclear.
---

# Clarify requirements

1. Restate the current goal and known constraints.
2. Ask one high-impact question at a time.
3. Record decisions, rejected alternatives, and unresolved risks.
4. Stop when acceptance criteria and boundaries are explicit.
5. Present the resulting specification for approval before implementation.
```

Приклад command `commands/prepare-review.md`:

```markdown
Review the current change set against the accepted requirements and repository standards. Report blocking issues first. Do not modify files unless explicitly asked.
```

Приклад `hooks/hooks.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/verify-clean-tree.sh"
          }
        ]
      }
    ]
  }
}
```

Приклад `scripts/verify-clean-tree.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Working tree contains unreviewed changes." >&2
  exit 2
fi
```

Цей hook навмисно strict для demonstration. Реальні hooks повинні документувати, коли вони запускаються, що блокують і як users можуть діагностувати failures.

## 8. Додавайте MCP лише за потреби

Plugin може налаштовувати MCP server, але server залишається окремою trust boundary.

Документуйте:

- command або URL;
- transport;
- required environment variables;
- authentication scopes;
- exposed tools, resources і prompts;
- write effects;
- startup і shutdown behavior;
- version pinning.

Не зберігайте production secrets у plugin repository.

## 9. Hooks потребують найретельнішої перевірки

Hooks можуть виконуватися без явного invocation skill користувачем. Для кожного hook визначте:

```text
Event:
Matcher:
Command or handler:
Inputs received:
Files or services accessed:
Failure result:
Timeout:
User-visible diagnostics:
Disable procedure:
```

Віддавайте перевагу read-only validation hooks. Вимагайте explicit approval, перш ніж hooks зможуть виконувати external writes або destructive actions.

## 10. Протестуйте локально

Тестуйте ці layers незалежно.

### Package validation

- manifest parse успішно;
- required files існують;
- identifiers і versions valid;
- referenced paths залишаються всередині package;
- executable files мають documented runtimes.

### Installation

- installation у clean profile успішне;
- expected components з’являються;
- repeated installation є idempotent або завершується з чітким failure;
- unsupported host versions відхиляються.

### Skills і commands

- positive і negative discovery tests проходять;
- namespaces коректні;
- supporting references і scripts resolve;
- output і approval requirements observable.

### Hooks і MCP

- кожен event matcher протестовано;
- denied permissions fail safely;
- timeouts і unavailable dependencies visible;
- startup і shutdown не залишають orphaned processes;
- unexpected network або filesystem access відсутній.

### Removal і rollback

- uninstall видаляє package registration;
- skills, commands, agents, hooks і MCP entries зникають;
- external credentials revoke окремо, коли це потрібно;
- попередню pinned version можна відновити.

## 11. Створіть marketplace repository

Для host, який підтримує third-party marketplaces, публікуйте окремий marketplace index або host-required metadata навколо plugin package.

Marketplace entry повинен містити:

- plugin identifier і display name;
- current version;
- source і package location;
- description і categories;
- license;
- compatibility;
- publisher identity;
- changelog або release notes;
- security contact;
- installation і removal instructions.

Marketplace не повинен без повідомлення перенаправляти existing plugin identifier на unrelated package.

## 12. Version behavior, а не лише files

Використовуйте semantic versioning як communication tool:

- patch: clarification або compatible fix, що не розширює permissions;
- minor: новий compatible skill, command або optional integration;
- major: змінений activation behavior, removed capability, нова mandatory dependency, expanded privilege або incompatible manifest change.

Розглядайте changes instructions як behavioral changes. Оновлення одного рядка `SKILL.md` може істотно змінити commands або approval requirements.

## 13. Multi-platform publication

Не стверджуйте, що один package є universal лише тому, що bundled skills portable.

Для кожного host:

1. створіть dedicated adapter;
2. validate його за official schema;
3. протестуйте install і uninstall у clean profile;
4. задокументуйте unsupported components;
5. publish host-specific package version;
6. синхронізуйте shared skills через generation або explicit release process.

## 14. Поширені помилки

### Копіювання manifest одного host в інший

Result: partial installation або ignored components. Fix: підтримуйте thin validated adapters.

### Розміщення essential workflow rules лише в plugin metadata

Result: portable clients завантажують incomplete skills. Fix: зберігайте essential behavior у `SKILL.md`.

### Додавання hooks до validation базового package

Result: startup failures приховують packaging errors. Fix: додавайте по одному component class за раз.

### Auto-update privileged plugins без review

Result: permissions або behavior можуть змінюватися непомітно. Fix: pin versions і review diffs.

### Uninstall без cleanup credentials

Result: external tokens залишаються valid. Fix: документуйте revocation окремо.

## Контрольний список публікації

- [ ] Plugin потрібен понад можливості standalone skill.
- [ ] Target host і minimum version визначені явно.
- [ ] Portable і host-specific layers розділено.
- [ ] Manifest validates за official schema.
- [ ] Skills, commands, hooks, MCP, connectors, code і assets інвентаризовано.
- [ ] Permissions і approval gates задокументовано.
- [ ] Clean install, update, rollback і uninstall tests проходять.
- [ ] Version і changelog описують behavioral changes.
- [ ] Marketplace metadata ідентифікує справжнього publisher і source.
- [ ] Security contact і reporting process доступні.

## Джерела

- [Концепція plugins](../../../../l10n/uk_UA/)
- [Використання Plugins](../../../using/l10n/uk_UA/)
- [Створення Agent Skills](../../../../../agent-skills/sub/creating/l10n/uk_UA/)
- Створення OpenAI plugins: https://developers.openai.com/codex/plugins/create-plugin
- Plugins Claude Code: https://code.claude.com/docs/en/plugins
- Marketplaces plugins Claude Code: https://code.claude.com/docs/en/plugin-marketplaces
- Plugins Cursor: https://cursor.com/docs/plugins
- Plugins OpenCode: https://opencode.ai/docs/plugins/
