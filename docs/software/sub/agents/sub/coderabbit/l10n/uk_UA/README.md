<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:f027a6fcee5fe877f5e65711b088d0d434ae1ffb
  mode: translated
-->

# CodeRabbit

Агент code review, планування й development workflow на основі ШІ для pull requests, Slack, IDE та CLI.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: агент code review і development workflow
Основний сценарій використання: перевіряти pull requests, планувати реалізації, надавати feedback щодо коду й підтримувати development workflows у Git, IDE, CLI та Slack
Модель доступу: пропрієтарна платформа CodeRabbit із доступом account, team і organization
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, публічною документацією та integrations
Операційні вимоги: доступ CodeRabbit, підключений Git provider, repository permissions, конфігурація team knowledge та необов’язкові Slack, IDE, CLI, Jira чи Linear integrations
Режими інтеграції: GitHub, GitLab, Azure DevOps, Bitbucket, pull requests, Slack agent, IDE extension, CLI tool, Jira, Linear, planning workflows, code review workflows, scheduled або message-triggered automations
Джерело: https://docs.coderabbit.ai/
Примітки щодо ризиків: review/workflow agent із високим рівнем довіри й доступом до repository, pull request, Slack, IDE, CLI, issue tracker і team knowledge; перевірте permission scopes, generated comments і fixes, planning outputs, automation triggers, credentials, secrets exposure та review людиною перед merge або execution.
```

## Огляд

CodeRabbit — платформа на основі ШІ для code review, планування й development workflows.

Вона поєднує pull-request review із workflow surfaces Slack, IDE extensions, CLI, issue planning та integrations із Git і issue-tracking platforms.

## Відповідність AI Lab

CodeRabbit належить до `agents/`, оскільки його основна задокументована роль — агентоподібна система для code review, планування та підтримки development workflow.

Використовуйте його як орієнтир для:

- агентів AI pull-request review;
- planning і coding assistance через Slack;
- review workflows у IDE та CLI;
- агентів якості коду з repository і team context;
- порівняння з Qodo та іншими review-focused agents.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- підтримку Git provider і issue tracker;
- області permissions repository та organization;
- межі Slack, IDE, CLI й automation;
- точність generated review і noise level;
- поведінку generated fix або PR;
- розкриття team knowledge і даних external tools;
- обов’язкове review людиною перед merge або task execution.

## Джерела

- Документація CodeRabbit: https://docs.coderabbit.ai/
- Вебсайт CodeRabbit: https://www.coderabbit.ai/
