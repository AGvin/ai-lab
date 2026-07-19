<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:5d1deca1445da488f8b481c10707411ebc2c0b69
  mode: translated
-->

# OpenAI Codex

Coding-agent OpenAI для software-engineering workflows у app, IDE, CLI, web та automation surfaces.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: coding-agent
Основний сценарій використання: читати, редагувати, тестувати, перевіряти й автоматизувати зміни ПЗ через керовані OpenAI workflows Codex
Модель доступу: пропрієтарний продукт OpenAI з доступом через account, workspace або enterprise
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, пов’язаним CLI та integration tooling
Операційні вимоги: доступ Codex, entitlement account чи organization OpenAI, доступ до repository або workspace, налаштовані tool permissions і необов’язкові інтеграції IDE, CLI, GitHub, Slack, Linear, MCP чи automation
Режими інтеграції: Codex app, IDE extension, CLI, web, GitHub, Slack, Linear, local environments, worktrees, shell commands, MCP, plugins, GitHub Action, SDK, automations
Джерело: https://developers.openai.com/codex
Примітки щодо ризиків: coding-agent із високим рівнем довіри, доступом на читання й запис до repository, локальним або віддаленим виконанням, shell/tool permissions, automation surfaces і межами account/workspace; перед використанням із чутливими repositories перевірте sandboxing, створені diffs, provider credentials, repository instructions, розкриття secrets і approval gates.
```

## Огляд

OpenAI Codex — пропрієтарний coding agent для software-development workflows.

Він охоплює кілька product surfaces, зокрема app, IDE, CLI, web та automation workflows. Його роль ширша за code completion: Codex може працювати з repositories, пропонувати зміни, запускати commands або checks, використовувати налаштовані tools та інтегруватися з engineering workflows, зокрема GitHub, Slack, Linear, MCP, plugins і GitHub Actions.

## Відповідність AI Lab

OpenAI Codex належить до `agents/`, оскільки його основна задокументована роль — agent-like coding system для software-engineering tasks.

Це не лише запис model family. Використовуйте `models/` для окремих model families OpenAI, а цю сторінку — для продукту coding-agent Codex і його workflow surface.

Використовуйте OpenAI Codex як орієнтир для:

- пропрієтарних продуктів coding-agent;
- coding workflows у app, IDE, CLI, web та automation;
- workflows редагування й review repository;
- surfaces конфігурації agent, rules, hooks, skills, MCP і plugins;
- порівняння з Claude Code, coding agent GitHub Copilot, Devin, Cursor, Cline та Aider.

## Skills, plugins і MCP

Codex підтримує повторно використовувані Agent Skills і platform-specific plugins та може підключатися до MCP servers. Загальні пояснення й tutorials зберігаються централізовано:

- [Agent Skills](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/l10n/uk_UA/)
- [Установлення й виклик skills у Codex](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/l10n/uk_UA/#openai-codex)
- [Plugins](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/l10n/uk_UA/)
- [Model Context Protocol](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/)

Використовуйте цю product page для Codex-specific evaluation notes замість дублювання повних learning guides.

## Примітки щодо оцінювання

Перед упровадженням оцініть:

- модель доступу account, workspace й organization;
- межі local і remote execution;
- controls доступу до repository та worktree;
- approval behavior shell commands і tools;
- review створених diffs перед commit, push або створенням PR;
- межі довіри repository instructions, rules, hooks, plugin, MCP і skill;
- розкриття source code, secrets, logs і project context.

## Джерела

- Документація OpenAI Codex: https://developers.openai.com/codex
- Швидкий старт Codex: https://developers.openai.com/codex/quickstart