<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:965891d5cb5cb7a1a3911fb7e04c58e2dbff28a0
  mode: translated
-->

# Agent Skills

Agent Skills — це переносні папки з інструкціями та необов’язковими допоміжними ресурсами, які навчають AI application виконувати повторюваний клас задач.

Skill є процедурним знанням. Він описує **як працювати**, тоді як tools надають operations, які може виконувати application, а models — можливості reasoning і generation.

## Переклади

- [English](../../)
- Українська

## Навчальний маршрут

- [Використання Agent Skills](../../sub/using/l10n/uk_UA/) — установлення, виклик, оновлення, видалення, перевірка й діагностика skills.
- [Створення Agent Skills](../../sub/creating/l10n/uk_UA/) — проєктування й побудова skill від мінімального `SKILL.md` до scripts, references, testing і publication.
- [Підтримка платформ](../../sub/platform-support/l10n/uk_UA/) — порівняння підтримуваних clients та їхніх моделей установлення й виклику.
- [Джерела й колекції](../../sub/sources/l10n/uk_UA/) — standards, catalogs, installers і рекомендовані сторонні collections.

## Основна структура

Відкритий формат Agent Skills вимагає directory з entrypoint `SKILL.md`:

```text
skill-name/
├── SKILL.md          # Обов’язкові metadata й instructions
├── scripts/          # Необов’язкові executable helpers
├── references/       # Необов’язкова документація, що завантажується за потреби
├── assets/           # Необов’язкові templates і output resources
└── ...               # Необов’язкові client-specific files
```

`SKILL.md` починається з YAML frontmatter і продовжується Markdown-інструкціями:

```markdown
---
name: release-notes
description: Draft release notes from merged changes. Use when preparing a software release or changelog.
---

# Release notes workflow

1. Identify the release range.
2. Group changes by user impact.
3. Separate breaking changes and migrations.
4. Verify every claim against the source changes.
```

Стандарт вимагає `name` і `description`. Він також визначає необов’язкові поля, зокрема `license`, `compatibility`, `metadata` та експериментальне `allowed-tools`. Окремі clients можуть додавати власні metadata або controls виклику.

## Виявлення, активація й виконання

Skills зазвичай завантажуються через progressive disclosure.

### 1. Виявлення

На початку session client надає model компактний catalog. Зазвичай він містить name і description кожного skill, а не повні instructions.

Тому description має два призначення:

- пояснювати, що робить skill;
- указувати, коли його слід вибрати.

Надто нечіткий description може ніколи не збігтися із задачею. Надто широкий може активувати skill для нерелевантної роботи.

### 2. Активація

Коли поточна задача відповідає skill, client завантажує повне тіло `SKILL.md` у working context. Активація може бути:

- **автоматичною** — model вибирає skill, бо його description відповідає задачі;
- **явною** — користувач викликає skill за name, command, mention або через platform-specific UI.

Деякі collections розрізняють **user-invoked** orchestration skills і **model-invoked** discipline skills. Це convention колекції або client, а не обов’язкове поле відкритого формату.

### 3. Виконання

Model дотримується завантаженого workflow. Далі вона може:

- читати referenced files;
- запускати bundled scripts;
- використовувати tools, надані host;
- запитувати схвалення користувача;
- викликати сумісні supporting skills;
- створювати artifact або виконувати зовнішню дію.

Допоміжні ресурси завантажуються лише за потреби, що зменшує звичайний context footprint.

## Skills у chat та agent environments

Skill не потребує автономного coding agent. Conversational host, наприклад ChatGPT, може виявити й активувати skill у звичайному chat.

Різниця полягає в execution environment:

| Середовище | Поведінка skill |
|---|---|
| Chat без зовнішніх tools | Застосовує instructions у розмові та створює text або artifacts, доступні в chat. |
| Chat із files або connectors | Може дотримуватися того самого workflow, читаючи files або працюючи з connected systems. |
| Coding agent із доступом до repository та shell | Може редагувати files, запускати tests, перевіряти diffs і виконувати довші tool-driven sequences. |
| Automated agent runtime | Може виконувати workflow із налаштованими permissions, schedules і approval policies. |

Skill визначає процедуру. Tools, permissions, sandbox і approvals host визначають, які дії реально можуть бути виконані.

## Пов’язані поняття

| Поняття | Значення | Зв’язок зі skill |
|---|---|---|
| **Prompt** | Instructions і context, надіслані model для однієї interaction або reusable template. | Skill містить instructions, але додає packaging, discovery metadata, resources і reusable lifecycle. |
| **Tool** | Executable operation, наприклад читання file, запит до API або запуск command. | Skill пояснює model, коли й як використовувати tools; він не надає їх автоматично. |
| **MCP** | Client-server protocol для надання AI applications tools, resources і prompts. | MCP може надавати capabilities, якими керує skill. Див. [Model Context Protocol](../../../model-context-protocol/l10n/uk_UA/). |
| **Plugin** | Platform-specific extension package, що може містити skills, agents, hooks, tools або MCP configuration. | Plugin може поширювати один або кілька skills. Див. [Plugins](../../../plugins/l10n/uk_UA/). |
| **Repository instructions** | Постійний project context, наприклад conventions і commands. | Використовуйте для facts, які мають бути присутні завжди; skill — для procedures, що завантажуються лише коли релевантні. |

## Переносність і client extensions

Формат Agent Skills стандартизує вміст skill directory. Він не вимагає, щоб кожний client використовував однаковий installation path, invocation syntax, permission model, UI metadata або plugin packaging.

Переносні skills мають:

- зберігати валідним стандартний entrypoint `SKILL.md`;
- описувати environmental requirements у `compatibility` або documentation;
- не припускати наявність client-specific tools, якщо dependency не зазначена явно;
- відокремлювати client-specific metadata від portable workflow;
- надавати fallbacks, коли preferred tool недоступний.

## Безпека й межа довіри

Сторонній skill є executable guidance, наданим model. Розглядайте його як software supply-chain input, навіть якщо він містить лише Markdown.

Перед установленням перевірте:

- повний `SKILL.md`, а не лише description;
- scripts та їхні dependencies;
- network access і credential requirements;
- referenced files і generated commands;
- requested tools і write permissions;
- update mechanism і ownership джерела;
- чи можуть instructions розкрити secrets або project data;
- чи мають actions approval і rollback points.

Skill може наказати agent запускати небезпечні commands або надсилати sensitive data. Установлення не є security endorsement. Застосовуйте least privilege, sandboxing, review gates, pinned versions і source verification відповідно до наслідків workflow.

## Джерела

- Огляд Agent Skills: https://agentskills.io/home
- Специфікація Agent Skills: https://agentskills.io/specification
- Посібник із додавання підтримки clients: https://agentskills.io/client-implementation/adding-skills-support
