<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:2b6d7d3b85be4555ac19ecb7d391c5427ecd32fd
  mode: translated
-->

# Плагіни ШІ

Плагін ШІ — це встановлюваний платформоспецифічний пакет, який розширює AI application однією або кількома можливостями, наприклад Agent Skills, connectors, MCP servers, agents, commands, hooks, templates або metadata інтерфейсу користувача.

На відміну від Agent Skills і Model Context Protocol, **plugin не є єдиним універсальним кросплатформним форматом**. OpenAI, Claude Code, Cursor, OpenCode та інші hosts визначають різні структури пакетів, manifests, lifecycle hooks, permissions і marketplaces.

## Переклади

- [English](../../)
- Українська

## Шлях навчання

- [Використання плагінів](../../sub/using/l10n/uk_UA/) — оцінювання, встановлення, оновлення, вимкнення, видалення й аудит сторонніх plugins.
- [Створення плагінів](../../sub/creating/l10n/uk_UA/) — проєктування та створення платформоспецифічного plugin із повними прикладами й кроками перевірки.
- [Agent Skills](../../../agent-skills/l10n/uk_UA/) — переносні процедурні workflows, які plugin може поширювати.
- [Model Context Protocol](../../../model-context-protocol/l10n/uk_UA/) — стандартний protocol, який plugin може налаштовувати або постачати.

## Навіщо потрібні plugins

Окремий skill може навчити модель workflow, але багатьом integrations потрібно більше, ніж instructions:

- керований механізм встановлення й оновлення;
- кілька пов’язаних skills, установлених як один продукт;
- connectors або OAuth configuration;
- визначення MCP server;
- custom agents або commands;
- lifecycle hooks;
- application-specific UI presentation;
- organization policy і marketplace metadata;
- namespacing для уникнення collisions.

Plugin пакує ці host-specific аспекти навколо повторно використовуваних capabilities.

## Типові компоненти

Plugin може містити деякі або всі такі компоненти:

| Компонент | Призначення |
|---|---|
| Manifest | Ідентифікує package, version, author, description, compatibility та entrypoints. |
| Skills | Повторно використовувані workflows `SKILL.md`, які завантажуються за релевантності. |
| Agents | Попередньо налаштовані спеціалізовані roles, prompts, models, tools і permissions. |
| Commands | Явні операції, які викликає користувач, або slash commands. |
| Hooks | Код або commands, що виконуються під час lifecycle events. |
| MCP configuration | Визначення локальних або віддалених MCP servers. |
| Connectors | Керовані платформою підключення до зовнішніх services та accounts. |
| App templates | Повторно використовуваний UI або application scaffolding. |
| Assets | Icons, screenshots, templates і documentation. |
| Marketplace metadata | Інформація, потрібна для discovery, review та встановлення package. |

Точні назви й розташування компонентів відрізняються залежно від host.

## Plugin і Agent Skill

| Agent Skill | Plugin |
|---|---|
| Переносна папка, зосереджена навколо `SKILL.md` | Host-specific installable package |
| Передусім процедурні знання | Межа поширення й інтеграції |
| Може працювати без executable code | Може містити code, hooks, connectors і configuration |
| Виявляється та активується за релевантністю задачі | Встановлюється, вмикається, оновлюється й видаляється як package |
| Зазвичай один сфокусований workflow | Може об’єднувати багато skills і capabilities |
| Відкрита специфікація Agent Skills | Немає єдиної універсальної plugin specification |

Plugin може містити skills. Skill не потребує plugin.

Використовуйте standalone skill, коли користувачам потрібен прозорий і переносний workflow. Використовуйте plugin, коли потрібне кероване поширення або host-specific integration.

## Plugin і MCP

| MCP | Plugin |
|---|---|
| Client-server interoperability protocol | Механізм установлення й пакування |
| Надає tools, resources і prompts | Може налаштовувати або поширювати MCP server |
| Може обслуговувати кілька сумісних hosts | Зазвичай орієнтований на один host або plugin ecosystem |
| Має semantics lifecycle та transport протоколу | Має semantics установлення, оновлення й marketplace package |

Установлення plugin, який посилається на MCP server, створює дві межі довіри:

1. plugin package і його installation behavior;
2. MCP server, credentials, data access і tool effects.

Перевіряйте обидві окремо.

## Plugin, prompt, tool і connector

- **Prompt** надає instructions або context. Plugin може поширювати prompts чи commands.
- **Tool** виконує operation. Plugin може реєструвати або надавати tools.
- **Connector** підключає platform до зовнішнього service, часто з керованою authentication. Plugin може оголошувати connector dependencies, якщо platform це підтримує.
- **Skill** пояснює моделі, коли і як застосовувати procedure. Plugin може встановлювати кілька skills разом.

## Межа переносності

Не припускайте, що directory з назвою `plugins/` є переносною.

Приклади платформоспецифічних відмінностей:

- filename і schema manifest;
- layout кореня package;
- marketplace registration;
- namespaces і command syntax;
- hook events;
- підтримувані executable languages;
- connector declarations;
- форма MCP configuration;
- permission і approval policy;
- вимоги signing і publication.

Мультиплатформний проєкт має зберігати повторно використовувані skills і MCP servers у нейтральних source directories, а потім генерувати або підтримувати тонкі host adapters.

```text
project/
├── skills/                  # Portable source skills
├── mcp-servers/             # Portable or separately deployable services
└── adapters/
    ├── claude-code-plugin/
    ├── openai-plugin/
    ├── cursor-plugin/
    └── opencode-plugin/
```

## Життєвий цикл установлення

Керований plugin зазвичай проходить такі етапи:

1. **Discovery** — користувач або administrator знаходить package у marketplace чи repository.
2. **Review** — перевіряються source, publisher, permissions, components і version.
3. **Installation** — files і configuration реєструються в host.
4. **Enablement** — bundled skills, agents, hooks, connectors або MCP servers стають доступними.
5. **Execution** — capabilities працюють у межах permissions і approvals host.
6. **Update** — нова package version змінює instructions, code або dependencies.
7. **Disablement or removal** — host вивантажує components і очищає package state.
8. **Credential cleanup** — непотрібні tokens або external authorizations відкликаються.

Установлення не є остаточним security decision. Кожне оновлення може змінити поведінку.

## Безпека й межа довіри

Перед установленням plugin перевірте:

- identity publisher і source repository;
- package version та update channel;
- повний manifest і bundled files;
- skills і приховані instruction surfaces;
- executable hooks і commands;
- MCP servers і network destinations;
- connectors та запитані account scopes;
- filesystem і shell permissions;
- secrets, environment variables і credential storage;
- telemetry та external asset loading;
- approval gates для writes або інших consequential actions;
- uninstall behavior і residual configuration.

Віддавайте перевагу least privilege, pinned versions, reproducible builds, explicit update review та isolated testing для незнайомих packages.

## Коли створювати plugin

Створюйте plugin, коли виконується хоча б одна умова:

- кілька capabilities мають установлюватися й версіонуватися разом;
- workflow потребує host-specific hooks, agents, connectors або UI;
- користувачам потрібні кероване marketplace installation та updates;
- для уникнення collisions потрібен namespacing;
- organization administrators потребують centralized distribution або policy controls.

Не створюйте plugin лише для поширення одного переносного `SKILL.md`, коли достатньо прямого встановлення skill.

## Джерела

- Plugins OpenAI: https://developers.openai.com/codex/plugins
- Створення plugin OpenAI: https://developers.openai.com/codex/plugins/create-plugin
- Plugins Claude Code: https://code.claude.com/docs/en/plugins
- Marketplaces plugins Claude Code: https://code.claude.com/docs/en/plugin-marketplaces
- Plugins Cursor: https://cursor.com/docs/plugins
- Plugins OpenCode: https://opencode.ai/docs/plugins/
- Agent Skills: ../../../agent-skills/l10n/uk_UA/
- Model Context Protocol: ../../../model-context-protocol/l10n/uk_UA/
