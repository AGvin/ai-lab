<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: sha256:42c7009436c785cb3c31a33fd084f296c93827ee1940da1a0c8aef2ac40f1b6a
  mode: translated
-->

# OpenCode

OpenCode — застосунок і runtime coding-agent із відкритим кодом, доступний через terminal, desktop та IDE interfaces.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: застосунок і runtime AI coding-agent
Основний сценарій використання: дослідження, планування, редагування й перевірка змін codebase за допомогою налаштовуваних моделей, агентів, tools і політик схвалення
Модель доступу: локальний застосунок із відкритим кодом із зовнішніми model providers або керованим OpenCode доступом до моделей
Модель вартості: OpenCode безплатний за ліцензією MIT; model providers і hosted model access можуть мати окрему оплату за використання або підписку
Ліцензія: MIT
Модель вихідного коду: відкритий код
Операційні вимоги: установлений OpenCode, доступ до проєкту й облікові дані вибраного model provider
Режими інтеграції: Terminal UI, non-interactive CLI, desktop app, IDE extension, project instructions, custom agents, skills, custom tools і MCP servers
Джерело: https://github.com/anomalyco/opencode
Примітки щодо ризиків: OpenCode може читати й змінювати файли, виконувати shell-команди, звертатися до зовнішніх tools і використовувати мережеві сервіси. Його permission system надає механізми схвалення, але агент не sandboxed; перед використанням із чутливими проєктами перевіряйте permissions, diffs, commands, MCP servers, provider credentials та repository instructions.
Остання перевірка: 2026-07-17
```

## Огляд

OpenCode — продукт coding-agent, а не звичайний редактор коду. Він може аналізувати проєкт, використовувати керовані моделлю tools, змінювати файли, виконувати команди й підтримувати project-specific instructions, тоді як користувач працює через terminal, desktop client або IDE integration.

Команда `/init` аналізує поточний проєкт і створює файл `AGENTS.md`. Commit цього файла дає змогу зберігати структуру, conventions і workflow guidance репозиторію разом із кодом.

## Агенти й режими роботи

OpenCode підтримує налаштовувані primary agents і subagents. Вбудовані або власні агенти можуть використовувати різні моделі, prompts, descriptions, tools і permission rules.

Типові ролі:

- build agent, якому дозволено редагувати файли й запускати схвалені команди;
- plan або review agent, який може досліджувати репозиторій, але не змінювати його;
- спеціалізовані subagents для exploration, review, research або обмежених задач.

Агентів можна налаштовувати в `opencode.json` або Markdown-файлах у глобальних чи локальних для проєкту каталогах агентів.

## Tools, skills і MCP

OpenCode містить tools для дослідження репозиторію, редагування файлів, пошуку, виконання shell, запитів до language server та пов’язаних coding operations. Він також може завантажувати повторно використовувані skills, custom tools і сервери Model Context Protocol.

Підтримка MCP дає зовнішнім серверам змогу надавати OpenCode додаткові tools. Наявність tool не означає довіру: окремо перевіряйте кожний MCP server, його credentials, network access, data exposure і command surface. Архітектуру протоколу описано на сторінці [Model Context Protocol](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/).

## Permissions і межа безпеки

Permission може визначати для дії один із режимів:

- `allow` — виконувати без додаткового запиту на схвалення;
- `ask` — вимагати схвалення користувача;
- `deny` — блокувати дію.

Правила можуть бути глобальними, прив’язаними до tool, command pattern або path чи перевизначеними для конкретного агента. Це дає змогу дозволити read-only аналіз, вимагати схвалення для edits або заборонити такі команди, як `git push`.

Permissions — операційний контроль, а не security sandbox. Дозволена дія агента виконується з доступом, доступним процесу OpenCode. Коли потрібна сильніша ізоляція, використовуйте засоби ОС, containers, disposable worktrees, обмежені credentials або інший sandbox.

## Моделі й постачальники

OpenCode може підключатися до кількох model providers і підтримує вибір моделі для кожного агента. Provider credentials можна налаштувати безпосередньо, а OpenCode Zen пропонує куруваний hosted catalog моделей, яким керує проєкт OpenCode.

Вибір provider оцінюйте окремо від клієнта:

- політика data retention і training;
- регіональна й організаційна доступність;
- authentication і зберігання секретів;
- context limits моделі та якість tool calling;
- ціна, rate limits і fallback behavior.

## Установлення й використання у Windows

Офіційні варіанти встановлення включають install script проєкту, package managers, release binaries і container image. У Windows доступне встановлення через Chocolatey та Scoop; офіційна документація зазначає, що підтримка встановлення через Bun у Windows ще розвивається.

Для розроблення у Windows порівняйте native installation із WSL з огляду на розміщення репозиторію, shell tooling, filesystem performance, credential handling і відповідність production environment. Не вважайте WSL обов’язковим, коли native workflow вже підтримує потрібні tools.

## Відповідність AI Lab

OpenCode належить до `agents/`, оскільки його канонічна роль — виконання coding-agent workflows. Desktop та IDE surfaces є клієнтами того самого агентного продукту, а не окремими редакторами коду.

Використовуйте цю сторінку як довідку для:

- terminal-first і multi-surface coding-agent workflows;
- локальних для репозиторію instructions у `AGENTS.md`;
- налаштовуваних primary agents і subagents;
- деталізованих permissions для commands, paths, tools і agents;
- MCP-enabled development tools;
- порівняння з Pi, OMP, Cline, Claude Code та OpenAI Codex.

## Контрольний список оцінювання

Перед упровадженням OpenCode перевірте:

- установлення й оновлення в цільовій операційній системі;
- підтримку та якість вибраних моделей і providers;
- пріоритет repository instructions і межі довіри;
- схвалення file edits, shell commands, external directories, skills і MCP tools;
- workflow перевірки diff і rollback;
- поведінку в non-interactive або automated execution;
- зберігання credentials і мережеве розкриття даних;
- потребу в додатковому sandboxing для репозиторію.

## Джерела

- Вебсайт OpenCode: https://opencode.ai/
- Документація OpenCode: https://opencode.ai/docs/
- Агенти: https://opencode.ai/docs/agents/
- Permissions: https://opencode.ai/docs/permissions/
- Tools: https://opencode.ai/docs/tools/
- Репозиторій вихідного коду: https://github.com/anomalyco/opencode
- Модель безпеки: https://github.com/anomalyco/opencode/security
