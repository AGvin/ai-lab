<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:85e2befb5ac7474862ab91c55640ce57dd8bc49a
  mode: translated
-->

# Jules

Автономний coding-agent Google для асинхронних задач розробки ПЗ.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: coding-agent
Основний сценарій використання: асинхронно працювати над coding-задачами, зокрема реалізацією, виправленням bugs, tests і процесами review на кшталт pull request
Модель доступу: пропрієтарний продукт Google із доступом через account і plan
Ліцензія: пропрієтарна
Модель вихідного коду: продукт із закритим кодом, публічною документацією та інтеграціями екосистеми Google
Операційні вимоги: доступ Jules, Google account або plan entitlement, підключений repository чи task workspace, налаштовані permissions та необов’язкові CLI або API integrations
Режими інтеграції: Web app, repositories, GitHub workflows, asynchronous tasks, task plans, tests, pull requests, CLI, API, Gemini models
Джерело: https://jules.google/
Примітки щодо ризиків: асинхронний coding-agent із високим рівнем довіри й доступом до repository, tasks, tests і pull-request workflows; перед використанням із чутливими репозиторіями перевірте repository permissions, generated diffs, test logs, account permissions, task scope, CLI/API credentials і approval gates людини.
```

## Огляд

Jules — автономний coding-agent Google для асинхронних задач розробки ПЗ.

Він позиціонується як агент, здатний у background працювати над призначеними coding-задачами, створювати code changes, запускати або аналізувати tests і повертати роботу на review розробника.

## Відповідність AI Lab

Jules належить до `agents/`, оскільки його основна задокументована роль — агентоподібна coding-система, а не code editor чи orchestration framework.

Використовуйте його як орієнтир для:

- керованих Google coding agents;
- асинхронного виконання задач розробки ПЗ;
- підключених до репозиторію процесів implementation, bug-fix і tests;
- розширення coding-agent продуктів через CLI та API;
- порівняння з coding agent GitHub Copilot, OpenAI Codex, Claude Code і Devin.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- модель account, plan і availability;
- підключення repository та межі permissions;
- task planning і review workflow;
- перевірку generated code і test results;
- оброблення CLI та API credentials;
- controls privacy і training data;
- approval gates merge, deployment та release.

## Джерела

- Вебсайт Jules: https://jules.google/
- Google Labs Jules: https://labs.google/jules
