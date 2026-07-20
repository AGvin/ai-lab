<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:50dca5b1fe4a23f55045f7ca530d73791bd47c1b
  mode: translated
-->

# Aider

Terminal-based інструмент AI pair programming і coding-agent для безпосередньої роботи з локальними Git-репозиторіями.

## Переклади

- [English](../../)
- Українська

## Метадані

```text
Тип ресурсу: coding-agent
Основний сценарій використання: редагувати, рефакторити й підтримувати код у локальному Git-репозиторії через terminal chat workflow
Модель доступу: CLI-інструмент із відкритим кодом, локальним використанням та обліковими даними зовнішнього постачальника моделей
Ліцензія: Apache-2.0
Модель вихідного коду: відкритий код
Операційні вимоги: Aider CLI, локальний Git-репозиторій, облікові дані вибраного постачальника моделей і локальний filesystem access до цільового codebase
Режими інтеграції: Terminal, Git repositories, model providers, local files, editor workflows, command-line development workflows
Джерело: https://github.com/Aider-AI/aider
Примітки щодо ризиків: coding-agent із високим рівнем довіри й локальним доступом на запис до репозиторію; перевіряйте створені diffs перед commit або push, захищайте секрети в codebase, обмежуйте credentials постачальника й не запускайте недовірений згенерований код без sandboxing.
```

## Огляд

Aider — terminal-based інструмент AI pair programming, що безпосередньо працює з локальними Git-репозиторіями.

Він дає розробнику змогу обговорювати codebase з моделлю, додавати файли до робочого контексту, запитувати зміни, перевіряти diffs та інтегрувати зміни у звичайний Git workflow.

## Відповідність AI Lab

Aider належить до `agents/`, оскільки його основна задокументована роль — агентоподібний coding assistant, що безпосередньо редагує файли репозиторію.

Це не фреймворк оркестрації агентів. Використовуйте `agent-orchestration/` для frameworks, runtimes або control planes, які координують кілька агентів чи агентних процесів.

Використовуйте Aider як орієнтир для:

- terminal-first процесів coding-agent;
- локального редагування репозиторію з Git integration;
- порівняння з Pi, Cline, Goose, Claude Code і Codex CLI;
- оцінювання low-overhead процесів AI pair programming;
- розуміння вимог безпеки запису до репозиторію для coding agents.

## Примітки щодо оцінювання

Перед впровадженням оцініть:

- підтримуваних model providers і оброблення credentials;
- поведінку Git workflow і межі commits;
- процес review diff перед commit або push;
- роботу з великими репозиторіями та multi-file edits;
- розкриття вихідного коду й секретів model providers;
- локальне виконання команд і безпеку згенерованого коду;
- відповідність наявним editor, terminal і repository workflows.

## Джерела

- Вебсайт Aider: https://aider.chat
- Документація Aider: https://aider.chat/docs/
- GitHub Aider: https://github.com/Aider-AI/aider
