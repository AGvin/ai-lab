<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:7574162426b88c21e9e82ec01013042c9fd8d678
  mode: translated
-->

# Використання Agent Skills

Цей посібник пояснює, як безпечно впровадити наявний Agent Skill, перевірити його доступність, викликати й підтримувати з часом.

## Переклади

- [English](../../)
- Українська

## Перед установленням

1. Переконайтеся, що цільовий client підтримує Agent Skills або plugin format колекції.
2. Прочитайте `SKILL.md` skill та всі bundled scripts.
3. Перевірте license, maintenance status, compatibility requirements і update mechanism.
4. Визначте кожний tool, credential, network destination і writable path, які він може використовувати.
5. Вирішіть, чи skill має бути project-local або user-global.

Використовуйте project-local installation, коли workflow належить одному repository і має перевірятися разом із code. Використовуйте user-global installation для персональних workflows, безпечних і корисних у непов’язаних projects.

## Моделі встановлення

### Копіювання directory skill

Найпереносніший спосіб — скопіювати повний directory skill у location, який сканує client:

```text
<client-skill-root>/release-notes/
├── SKILL.md
├── references/
└── scripts/
```

Не копіюйте лише `SKILL.md`, якщо він посилається на supporting files.

### Використання installer

Community installers, наприклад `skills.sh`, можуть копіювати вибрані skills у підтримувані clients:

```bash
npx skills@latest add owner/repository
```

Installer зменшує ручну роботу з paths, але не робить source надійним. Перевірте вибрану version і результуючі files перед наданням широких permissions.

### Установлення plugin

Деякі products поширюють collections як managed plugins. Plugin може надавати skills разом із hooks, agents, MCP servers або configuration. Plugin commands є platform-specific; див. [Використання Plugins](../../../plugins/sub/using/l10n/uk_UA/).

## Явний і автоматичний виклик

### Явний виклик

Використовуйте command, mention або skill picker платформи, коли потрібен конкретний workflow:

```text
/grill-me
```

```text
Use the diagnosing-bugs skill for this failure.
```

Явний виклик кращий, коли:

- задача має високі наслідки;
- кілька skills можуть відповідати запиту;
- потрібен user-invoked orchestration flow;
- ви тестуєте новий skill;
- automatic discovery ненадійний.

### Автоматичний виклик

Client може автоматично вибрати skill, коли задача відповідає його description. Хороший test prompt має описувати реальну задачу, а не називати skill:

```text
Investigate why this test fails intermittently. Reproduce it, isolate the cause, and add a regression test before changing production code.
```

Якщо diagnostic skill активується правильно, response має дотримуватися визначеного process, а не одразу вгадувати fix.

## Підтвердження активації

Clients по-різному показують activation. Використовуйте одну або кілька перевірок:

- перевірте UI на active skill indicator;
- запитайте client, які skill instructions він завантажив;
- переконайтеся, що з’являються очікувані workflow steps;
- перегляньте logs або tool calls, якщо client їх показує;
- тимчасово додайте однозначну, але безпечну test instruction;
- вимкніть skill і порівняйте behavior.

Не покладайтеся лише на схожість final answer. Перевіряйте спостережувані workflow requirements.

## Комбінування skills

Skills можна поєднувати, коли responsibilities залишаються чіткими. Практичний engineering flow може використовувати:

1. `grill-with-docs` для уточнення requirements і terminology;
2. `to-spec` для фіксації узгодженого design;
3. `tdd` під час implementation;
4. `code-review` перед commit.

Не активуйте кілька skills, кожний із яких претендує на той самий stage. Конфліктні instructions збільшують context use й ускладнюють audit.

## Оновлення

Виберіть одну update model:

- **Managed subscription** — plugin або marketplace оновлює installed package.
- **Pinned copy** — зберігайте перевірену version у repository й оновлюйте через звичайний code review.
- **Forked copy** — підтримуйте local adaptations і періодично узгоджуйте upstream changes.

Для consequential workflows записуйте source repository і revision. Перевіряйте diffs перед update, оскільки навіть зміна лише Markdown може змінити commands, permissions або data handling.

## Видалення або вимкнення

Залежно від client, видаліть skill directory, uninstall його plugin, вимкніть у Skills UI або забороніть доступ через skill permission rules.

Після видалення:

- restart або reload client за потреби;
- переконайтеся, що skill більше не з’являється в discovery metadata;
- видаліть hooks або MCP configuration, установлені plugin;
- відкличте credentials, створені лише для skill.

## Усунення проблем

### Skill не виявляється

Перевірте:

- directory location;
- точне uppercase filename `SKILL.md`;
- валідний YAML frontmatter;
- обов’язкові поля `name` і `description`;
- відповідність directory name назві skill;
- client permissions і disabled patterns;
- чи потрібен restart або plugin reload.

### Skill не активується автоматично

Поліпште description, додавши конкретні tasks і trigger phrases. Перевірте positive prompts, які мають активувати skill, і близькі negative prompts, які не повинні його активувати.

### Skill активується надто часто

Звузьте description. Укажіть qualifying condition і виключіть суміжні tasks у body. Використовуйте explicit invocation для широких orchestration skills.

### Script завершується помилкою

Перевірте runtime, working directory, executable permission, dependency versions, environment variables і network access. Skill має завершуватися з чітким повідомленням, а не непомітно продовжувати з partial results.

### Різні clients поводяться по-різному

Відкритий формат не стандартизує всю client behavior. Порівняйте installation paths, supported frontmatter extensions, tool names, permission models і invocation syntax у [Підтримці платформ](../../../platform-support/l10n/uk_UA/).

## Контрольний список безпечного впровадження

- [ ] Source і revision записані.
- [ ] `SKILL.md` перевірено.
- [ ] Scripts і dependencies перевірено.
- [ ] Required permissions мінімізовано.
- [ ] Positive activation test проходить.
- [ ] Negative activation test проходить.
- [ ] Failure і rollback behavior протестовано.
- [ ] Update policy вибрано.

## Джерела

- Специфікація Agent Skills: https://agentskills.io/specification
- Оптимізація descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Підтримка платформ: ../../../platform-support/l10n/uk_UA/
- Джерела й колекції: ../../../sources/l10n/uk_UA/
