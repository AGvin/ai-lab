<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:c8f1f84f23900252ee9058f5a1803727d8799738
  mode: translated
-->

# Cline

Coding-agent і agent runtime з відкритим кодом для editor, terminal, SDK та automation workflows.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: coding-agent
Основний сценарій використання: планувати, редагувати, запускати й перевіряти зміни codebase через агентний процес, інтегрований з інструментами розробника
Модель доступу: agent runtime із відкритим кодом, локальним використанням та обліковими даними зовнішнього постачальника моделей
Ліцензія: Apache-2.0
Модель вихідного коду: відкритий код
Операційні вимоги: extension, CLI, SDK або runtime Cline; облікові дані вибраного постачальника моделей; доступ до репозиторію; налаштовані дозволи tool, shell, MCP й automation
Режими інтеграції: VS Code, JetBrains, terminal, SDK, Git repositories, shell commands, MCP servers, model providers, browser і network-capable tools, automation workflows
Джерело: https://github.com/cline/cline
Примітки щодо ризиків: coding-agent із високим рівнем довіри, доступом на запис до репозиторію, виконанням shell, інтеграціями MCP/tool та необов’язковими automation workflows; перед використанням із чутливими репозиторіями перевірте схвалення команд, створені diffs, облікові дані постачальника, дозволи MCP servers, інструкції репозиторію, розкриття секретів, browser/network access і sandboxing.
```

## Огляд

Cline — coding-agent і agent runtime з відкритим кодом для процесів розробника.

Він може працювати через інтеграції редактора, terminal workflows та SDK. Його роль ширша за простого chat assistant: він може досліджувати codebase, планувати зміни, редагувати файли, викликати інструменти, запускати команди й інтегруватися з агентними процесами, як-от MCP-backed tools та automation.

## Відповідність AI Lab

Cline належить до `agents/`, оскільки його основна задокументована роль — агентоподібний coding assistant і runtime, що безпосередньо працює з репозиторіями та інструментами розробника.

Він суміжний з agent orchestration, оскільки надає runtime, SDK, automation та multi-agent capabilities, але канонічним об’єктом усе одно є coding-agent, а не універсальний orchestration framework.

Використовуйте Cline як орієнтир для:

- інтегрованих у редактор процесів coding-agent;
- редагування репозиторію з контрольними точками схвалення людиною;
- виконання tool і shell із coding-agent;
- автоматизації розробника з підтримкою MCP;
- порівняння з Aider, Pi, Goose, Claude Code і Codex CLI;
- оцінювання agent runtimes для editor, terminal, SDK та automation use cases.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- відповідність процесу editor, terminal або SDK;
- підтримку model providers і оброблення credentials;
- межі довіри instructions і rules репозиторію;
- модель схвалення й виконання shell-команд;
- процес review створених diffs;
- дозволи MCP servers та області tools;
- межі browser, network і filesystem access;
- поведінку в headless, CI, scheduled або multi-agent automation modes.

## Джерела

- Вебсайт Cline: https://cline.bot
- Документація Cline: https://docs.cline.bot
- GitHub Cline: https://github.com/cline/cline
