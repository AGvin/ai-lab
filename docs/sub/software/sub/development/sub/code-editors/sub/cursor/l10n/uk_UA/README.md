<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:bb6d427c7ac187c26260589c1369447183a72783
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

<!-- doc-anchor: cursor-data-safety; target: next-heading -->
<a id="cursor-data-safety"></a>
## Шлях даних і приватність

Перевірено 2026-07-26.

Cursor документує, що AI requests проходять через інфраструктуру Cursor навіть тоді, коли користувач указує окремий API key постачальника моделі. Запити можуть містити історію розмови, нещодавно переглянуті файли та релевантний код, після чого можуть передаватися вибраному inference provider.

Privacy Mode змінює гарантії зберігання та використання для навчання, але не робить шлях запиту прямим або повністю локальним. Під час індексації codebase фрагменти коду також завантажуються для обчислення embeddings, а embeddings і пов’язані metadata можуть зберігатися відповідно до поточної архітектури сервісу.

Для чутливих repositories:

- за потреби примусово ввімкніть Privacy Mode на рівні workspace;
- погодьте Cursor, вибраного model provider, subprocessors, regions і retention terms;
- видаліть secrets і виключіть контент, якому заборонено залишати device;
- окремо перевірте indexing, background requests, plugins, skills, MCP servers і remote execution;
- не використовуйте Cursor, якщо політика організації забороняє third-party processing або посередника в шляху до моделі.

Перед упровадженням повторно перевірте актуальну product behavior і contracts, оскільки routing, providers, retention і enterprise controls можуть змінюватися.

## Примітки щодо оцінювання

Зафіксуйте точну surface і version Cursor, вибрану model, repository access, увімкнені skills і plugins, MCP servers, remote або background execution, approval behavior і дату перевірки. Desktop, CLI, SSH та hosted surfaces можуть надавати різні capabilities.

## Джерела

- Cursor: https://cursor.com/
- Документація Cursor: https://cursor.com/docs
- Використання даних і приватність Cursor: https://cursor.com/data-use
- Безпека Cursor: https://cursor.com/security
- Agent Skills: https://cursor.com/docs/skills
- Plugins: https://cursor.com/docs/plugins