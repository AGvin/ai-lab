<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:501046b3bbd242a2ce33db6b3bf4b33db5cadf45
  mode: translated
-->

# OpenAI Codex

Coding-agent OpenAI для процесів програмної інженерії в app, IDE, CLI, web та automation surfaces.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: coding-agent
Основний сценарій використання: читати, редагувати, тестувати, перевіряти й автоматизувати зміни ПЗ через керовані OpenAI процеси Codex
Модель доступу: пропрієтарний продукт OpenAI з доступом через обліковий запис, workspace або enterprise
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, пов’язаним CLI та інструментами інтеграції
Операційні вимоги: доступ Codex, entitlement облікового запису чи організації OpenAI, доступ до репозиторію або workspace, налаштовані дозволи інструментів та необов’язкові інтеграції IDE, CLI, GitHub, Slack, Linear, MCP чи автоматизації
Режими інтеграції: Codex app, IDE extension, CLI, web, GitHub, Slack, Linear, local environments, worktrees, shell commands, MCP, plugins, GitHub Action, SDK, automations
Джерело: https://developers.openai.com/codex
Примітки щодо ризиків: coding-agent із високим рівнем довіри, доступом на читання й запис до репозиторію, локальним або віддаленим виконанням, дозволами shell та інструментів, automation surfaces і межами облікового запису чи workspace; перед використанням із чутливими репозиторіями перевірте sandboxing, створені diffs, облікові дані постачальника, інструкції репозиторію, розкриття секретів і approval gates.
```

## Огляд

OpenAI Codex — пропрієтарний coding-agent для процесів розробки ПЗ.

Він охоплює кілька продуктових поверхонь: app, IDE, CLI, web та automation workflows. Його роль ширша за code completion: Codex може працювати з репозиторіями, пропонувати зміни, запускати команди чи перевірки, використовувати налаштовані інструменти й інтегруватися з інженерними процесами GitHub, Slack, Linear, MCP, plugins і GitHub Actions.

## Відповідність AI Lab

OpenAI Codex належить до `agents/`, оскільки його основна задокументована роль — агентоподібна coding-система для задач програмної інженерії.

Це не лише запис сімейства моделей. Використовуйте `models/` для окремих сімейств моделей OpenAI, а цю сторінку — для продукту coding-agent Codex і його робочих поверхонь.

Використовуйте OpenAI Codex як орієнтир для:

- пропрієтарних продуктів coding-agent;
- coding-процесів у app, IDE, CLI, web та automation;
- процесів редагування й review репозиторію;
- поверхонь конфігурації агента, rules, hooks, skills, MCP і plugins;
- порівняння з Claude Code, coding agent GitHub Copilot, Devin, Cursor, Cline і Aider.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- модель доступу облікового запису, workspace й організації;
- межі локального та віддаленого виконання;
- controls доступу до репозиторію й worktree;
- поведінку схвалення shell-команд та інструментів;
- review створених diffs перед commit, push або створенням PR;
- межі довіри інструкцій, rules, hooks, plugins, MCP і skills;
- розкриття вихідного коду, секретів, журналів і контексту проєкту.

## Джерела

- Документація OpenAI Codex: https://developers.openai.com/codex
- Швидкий старт Codex: https://developers.openai.com/codex/quickstart
