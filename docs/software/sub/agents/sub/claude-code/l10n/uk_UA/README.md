<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:f0f09a1088ba7e2737b47d745050608af01b6e75
  mode: translated
-->

# Claude Code

Coding-agent Anthropic для terminal, editor, desktop, browser і automation workflows.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: Coding agent
Основний сценарій використання: читання, редагування, тестування й перевірка змін codebase через керовані Anthropic агентні coding workflows
Модель доступу: пропрієтарний продукт Anthropic із доступом через account, subscription або organization
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, пов’язаними client tools і documentation
Операційні вимоги: доступ Claude Code, entitlement account або organization Anthropic, доступ до local project чи remote workspace, налаштовані permissions tools і shell та необов’язкові integrations IDE, MCP, CI/CD або automation
Режими інтеграції: Terminal, VS Code, JetBrains IDEs, desktop app, browser, Slack, Git repositories, shell commands, MCP servers, GitHub Actions, GitLab CI, background agents, scheduled tasks, Agent SDK
Джерело: https://code.claude.com/docs/en/overview
Примітки щодо ризиків: пропрієтарний coding-agent із високим рівнем довіри, доступом на читання й запис до repository, виконанням shell, integrations MCP/tools, background або scheduled execution і межами cloud/account; перед використанням із sensitive repositories перевіряйте command approvals, generated diffs, permissions provider account, repository instructions, exposure secrets, behavior remote sessions і human review gates.
```

## Огляд

Claude Code — агентний coding tool Anthropic для workflows розроблення ПЗ.

Він працює через terminal, IDE, desktop, browser та automation surfaces. Його роль ширша за inline code completion: він може досліджувати codebase, редагувати files, запускати commands чи tests, допомагати з Git workflows, використовувати configured tools і підтримувати agentic coding workflows, що поширюються на CI/CD, background work, scheduled tasks та SDK integrations.

## Відповідність AI Lab

Claude Code належить до `agents/`, оскільки його основна задокументована роль — agent-like coding system, що безпосередньо працює з repositories, tools, commands і developer workflows.

Це не framework оркестрації агентів. Використовуйте `agent-orchestration/` для frameworks, runtimes або control planes, які координують кілька agents чи agent workflows.

Використовуйте Claude Code як орієнтир для:

- proprietary agentic coding products;
- terminal та IDE coding-agent workflows;
- редагування repository з виконанням shell і tests;
- доступу coding-agent до tools через MCP;
- background, scheduled, CI/CD та SDK-based agent workflows;
- порівняння з open-source coding agents, зокрема Aider, Cline, Goose і mini-SWE-agent.

## Skills, plugins і MCP

Claude Code підтримує standalone Agent Skills, Claude-specific plugins і MCP servers. Централізовані посібники:

- [Agent Skills](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/l10n/uk_UA/)
- [Установлення й виклик skills у Claude Code](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/l10n/uk_UA/#claude-code)
- [Plugins](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/l10n/uk_UA/)
- [Model Context Protocol](../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/)

## Примітки щодо оцінювання

Перед упровадженням оцініть:

- модель доступу account, subscription і organization;
- межі доступу до repository та workspace;
- behavior схвалення й виконання shell commands;
- review generated diffs перед commit, push або створенням PR;
- межі довіри repository instructions і memory;
- permissions MCP servers і tool scopes;
- межі background agent, scheduled task, desktop, browser і cloud sessions;
- exposure source code, credentials, logs і private project context.

## Джерела

- Огляд Claude Code: https://code.claude.com/docs/en/overview
- Швидкий старт Claude Code: https://code.claude.com/docs/en/quickstart
- Web entry point Claude Code: https://claude.ai/code
