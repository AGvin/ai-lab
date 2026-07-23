<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:b8b7fab17b82c08a8cc7c59a45140611348257f2
  mode: translated
-->

# OpenCode

OpenCode — застосунок і runtime AI coding-agent із відкритим кодом, доступний через terminal, desktop та IDE interfaces.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: застосунок і runtime AI coding-agent
Основний сценарій використання: дослідження, планування, редагування й перевірка змін codebase за допомогою налаштовуваних models, agents, tools і approval policies
Модель доступу: локальний застосунок із відкритим кодом із зовнішніми model providers або керованим OpenCode доступом до models
Модель вартості: OpenCode безплатний за ліцензією MIT; model providers і hosted model access можуть мати окрему оплату за використання або subscription
Ліцензія: MIT
Модель вихідного коду: відкритий код
Операційні вимоги: установлений OpenCode, доступ до project і credentials вибраного model provider
Режими інтеграції: Terminal UI, non-interactive CLI, desktop app, IDE extension, project instructions, custom agents, skills, custom tools і MCP servers
Джерело: https://github.com/anomalyco/opencode
Примітки щодо ризиків: OpenCode може читати й змінювати files, виконувати shell commands, звертатися до external tools і використовувати network-backed services. Його permission system надає approval controls, але agent не sandboxed; перед використанням із чутливими projects перевіряйте permissions, diffs, commands, MCP servers, provider credentials і repository instructions.
Остання перевірка: 2026-07-17
```

## Огляд

OpenCode — продукт coding-agent, а не звичайний code editor. Він може аналізувати project, використовувати model-driven tools, змінювати files, виконувати commands і підтримувати project-specific instructions, тоді як користувач працює через terminal, desktop client або IDE integration.

Команда `/init` аналізує поточний project і створює файл `AGENTS.md`. Commit цього файла дає змогу зберігати repository-specific structure, conventions і workflow guidance разом із codebase.

## Агенти й режими роботи

OpenCode підтримує налаштовувані primary agents і subagents. Вбудовані або custom agents можуть використовувати різні models, prompts, descriptions, tools і permission rules.

Типові ролі:

- build agent, якому дозволено редагувати files і запускати схвалені commands;
- plan або review agent, який може досліджувати repository, але не змінювати його;
- спеціалізовані subagents для exploration, review, research або обмежених tasks.

Agents можна налаштовувати в `opencode.json` або як Markdown files у global чи project-local agent directories.

## Tools, skills, plugins і MCP

OpenCode містить tools для дослідження repository, редагування files, search, виконання shell, запитів до language server і пов’язаних coding operations. Він також може завантажувати reusable skills, custom tools, OpenCode-specific plugins і Model Context Protocol servers.

Для понять і cross-platform workflows використовуйте централізовані guides:

- [Agent Skills](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/l10n/uk_UA/)
- [Установлення, виклик і permissions skills в OpenCode](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/agent-skills/sub/platform-support/l10n/uk_UA/#opencode)
- [Plugins](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/plugins/l10n/uk_UA/)
- [Model Context Protocol](../../../../../../../notes/sub/concepts/sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/)

Plugins OpenCode — executable JavaScript або TypeScript extensions, які не взаємозамінні з Agent Skills чи plugin packages іншої платформи. Використовуйте neutral skill directory, коли не потрібні OpenCode-specific lifecycle або runtime extension.

Підтримка MCP дає зовнішнім servers змогу надавати OpenCode додаткові tools. Наявність tool не означає довіру: кожний MCP server, його credentials, network access, data exposure і command surface потрібно перевіряти окремо.

## Permissions і межа безпеки

Permission може визначати для дії один із режимів:

- `allow` — виконувати без додаткового approval prompt;
- `ask` — вимагати user approval;
- `deny` — блокувати дію.

Rules можуть бути global, tool-specific, command-pattern-specific, path-specific або перевизначеними для конкретного agent. Це дає змогу дозволити read-only analysis, вимагати approval для edits або заборонити commands, наприклад `git push`.

Permissions — операційний контроль, а не security sandbox. Дозволена дія agent виконується з доступом, доступним process OpenCode. Коли потрібна сильніша ізоляція, використовуйте operating-system isolation, containers, disposable worktrees, restricted credentials або інший sandbox.

## Models і providers

OpenCode може підключатися до кількох model providers і підтримує вибір model для кожного agent. Provider credentials можна налаштувати безпосередньо, а OpenCode Zen пропонує curated hosted model catalog, яким керує project OpenCode.

Вибір provider оцінюйте окремо від client:

- data retention і training policy;
- regional та organizational availability;
- authentication і secret storage;
- model context limits і tool-calling quality;
- pricing, rate limits і fallback behavior.

## Установлення й використання у Windows

Офіційні installation options включають install script project, package managers, release binaries і container image. У Windows доступне встановлення через Chocolatey та Scoop; офіційна документація зазначає, що підтримка Bun-based Windows installation ще розвивається.

Для development у Windows порівняйте native installation із WSL з огляду на repository location, shell tooling, filesystem performance, credential handling і parity з production environment. Не вважайте WSL обов’язковим, коли native workflow уже підтримує потрібні tools.

## Відповідність AI Lab

OpenCode належить до `agents/`, оскільки його canonical role — виконання coding-agent workflows. Desktop та IDE surfaces є clients того самого agent product, а не окремими code editors.

Використовуйте цю сторінку як довідку для:

- terminal-first і multi-surface coding-agent workflows;
- repository-local instructions у `AGENTS.md`;
- налаштовуваних primary agents і subagents;
- granular permissions для commands, paths, tools і agents;
- skills, plugins і MCP-enabled development tools;
- порівняння з Pi, OMP, Cline, Claude Code та OpenAI Codex.

## Контрольний список оцінювання

Перед упровадженням OpenCode перевірте:

- installation і update behavior у цільовій operating system;
- support і quality вибраних models і providers;
- precedence repository instructions і trust boundaries;
- approval behavior для file edits, shell commands, external directories, skills, plugins і MCP tools;
- workflow перевірки diff і rollback;
- behavior у non-interactive або automated execution;
- credential storage і network-data exposure;
- чи потрібен додатковий sandboxing для repository.

## Джерела

- Вебсайт OpenCode: https://opencode.ai/
- Документація OpenCode: https://opencode.ai/docs/
- Agents: https://opencode.ai/docs/agents/
- Skills: https://opencode.ai/docs/skills/
- Plugins: https://opencode.ai/docs/plugins/
- Permissions: https://opencode.ai/docs/permissions/
- Tools: https://opencode.ai/docs/tools/
- Repository вихідного коду: https://github.com/anomalyco/opencode
- Security model: https://github.com/anomalyco/opencode/security