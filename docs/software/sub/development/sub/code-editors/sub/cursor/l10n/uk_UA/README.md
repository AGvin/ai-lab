<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:6b5af97b1dd1ba2d50291eb541bd1d231a34a443
  mode: translated
-->

# Cursor

Cursor — code editor із підтримкою ШІ та вбудованою AI integration.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: редактор коду з підтримкою ШІ
Основний сценарій використання: AI-assisted coding у спеціалізованому editor
Модель доступу: desktop application та/або hosted service
Операційні вимоги: локальна workstation і доступ до account/service
Режими інтеграції: desktop UI, editor workflow, model/provider integrations, Agent Skills, plugins і MCP
Джерело: https://cursor.com/
Примітки щодо ризиків: перед використанням із чутливим code перевірте pricing, source availability, data handling, model providers, repository access behavior, installed skills, plugins, MCP servers і approval policy.
```

## Призначення

Використовуйте Cursor для AI-assisted coding, навігації codebase, редагування й development workflows.

## Релевантність для ШІ

Cursor релевантний AI Lab як code editor із вбудованою AI functionality, а не як standalone AI agent.

## Skills, plugins і MCP

Cursor підтримує Agent Skills у editor та CLI workflows, поширює host-specific plugins через Cursor Marketplace і може налаштовувати MCP integrations.

Для переносних понять і детальних workflows використовуйте централізовані guides:

- [Agent Skills](../../../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/l10n/uk_UA/)
- [Установлення й виклик skills у Cursor](../../../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/l10n/uk_UA/#cursor)
- [Plugins](../../../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/l10n/uk_UA/)
- [Model Context Protocol](../../../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/)

Plugin packaging Cursor є platform-specific. Не припускайте, що plugin OpenAI, Claude Code або OpenCode встановлюється без змін лише тому, що містить переносні Agent Skills.

## Режими розгортання

- Локальна workstation
- Hosted SaaS або hybrid behavior: перевірте поточну product behavior

## Апаратне прискорення

- Зазвичай не стосується локального environment

## Режими інтеграції

- Desktop UI
- Editor та agent workflows
- Agent Skills і rules
- Plugins Cursor Marketplace
- MCP servers
- Model/provider integrations: перевірте поточні options

## Примітки щодо оцінювання

Зафіксуйте точну surface і version Cursor, вибрану model, repository access, увімкнені skills і plugins, MCP servers, remote або background execution, approval behavior і дату перевірки. Desktop, CLI, SSH та hosted surfaces можуть надавати різні capabilities.

## Джерела

- Cursor: https://cursor.com/
- Документація Cursor: https://cursor.com/docs
- Agent Skills: https://cursor.com/docs/skills
- Plugins: https://cursor.com/docs/plugins