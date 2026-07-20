<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:14c675dccd7c8b38973abfb550812c8aab66ac39
  mode: translated
-->

# Використання плагінів ШІ

Цей посібник пояснює, як оцінювати, встановлювати, перевіряти, оновлювати, вимикати й видаляти AI plugin, не припускаючи, що всі платформи використовують однаковий формат plugin.

## Переклади

- [English](../../)
- Українська

## 1. Визначте ecosystem plugin

Перед виконанням будь-якої команди визначте цільовий host:

- OpenAI ChatGPT або Codex;
- Claude Code;
- Cursor;
- OpenCode;
- інша явно задокументована платформа.

Plugin, створений для одного host, може містити корисні переносні skills, але його manifest, hooks, connector declarations і marketplace metadata зазвичай не можна без змін установити в іншому host.

## 2. Перевірте перед установленням

Зафіксуйте:

```text
Назва plugin:
Publisher:
Source repository:
Version або commit:
Target host:
Marketplace:
Bundled skills:
Bundled agents або commands:
Hooks:
MCP servers:
Connectors і OAuth scopes:
Executable code:
Network destinations:
Writable paths:
Update policy:
Uninstall behavior:
```

Перевіряйте весь package, а не лише його marketplace description. Особливо перевірте startup hooks, shell commands, install scripts, MCP configuration, external asset loading, telemetry та credential requirements.

## 3. Виберіть модель установлення

### Установлення з marketplace

Використовуйте marketplace, коли потрібні керовані discovery та updates:

```text
/plugin install package-name@marketplace-name
```

Точна команда залежить від host. Marketplace entry — це канал поширення, а не незалежна security review.

### Пряме встановлення з repository

Деякі hosts приймають Git repository або URL. Фіксуйте tag або commit, якщо host це підтримує. Не виконуйте installation instructions, скопійовані з неперевіреної branch.

### Локальне development installation

Використовуйте локальну directory plugin під час розроблення або аудиту. Тримайте її поза production projects, доки не зрозумієте hooks, permissions і cleanup behavior.

## 4. Установлюйте з мінімальними привілеями

Перед увімкненням plugin:

1. вимкніть непотрібні connectors;
2. використовуйте read-only credentials, де це можливо;
3. обмежте filesystem scope;
4. вимагайте approval для shell commands і writes;
5. використовуйте disposable repository або test workspace;
6. зберігайте secrets поза directory plugin;
7. забороніть optional telemetry до завершення перевірки.

Plugin, який містить лише Markdown skills, усе одно може змінювати поведінку agent. Plugin із hooks або code додатково розширює execution boundary.

## 5. Приклади для платформ

### Claude Code

Зареєструйте marketplace і встановіть package:

```text
/plugin marketplace add owner/repository
/plugin install plugin-name@marketplace-name
```

Еквівалентні shell commands використовують `claude plugin`. Skills plugin зазвичай мають namespace, наприклад:

```text
/plugin-name:release-notes
```

### OpenAI Codex

Використовуйте Plugins browser у підтримуваних ChatGPT/Codex surfaces або `/plugins` у Codex CLI, де це доступно. Перед увімкненням plugin перевірте connector і MCP dependencies, а потім за потреби почніть нову session, щоб bundled skills були виявлені.

### Cursor

Установіть із Cursor Marketplace або використайте підтримувану chat command:

```text
/add-plugin plugin-name
```

Перевірте, чи package містить rules, skills, agents, commands, hooks або MCP configuration. Не припускайте, що desktop, CLI, SSH і background-agent surfaces мають однакову plugin behavior.

### OpenCode

Plugins OpenCode — це JavaScript або TypeScript extensions, які завантажуються з configuration або plugin directories. Розглядайте їх executable code як application extensions, а не переносні Agent Skills. Використовуйте нейтральні skill directories, коли OpenCode-specific runtime behavior не потрібна.

## 6. Перевірте після установлення

Не зупиняйтеся на повідомленні про успішне встановлення. Перевірте observable state:

- показано очікувану version plugin;
- з’явилися лише очікувані skills, commands, agents, hooks, connectors і MCP servers;
- positive test викликає потрібну capability;
- близький negative test її не активує;
- denied tools залишаються denied;
- consequential actions запитують approval;
- немає неочікуваних process, network call або file modification;
- нова session завантажує той самий package state.

Для plugin із кількома skills спочатку тестуйте кожний skill окремо, а вже потім їх composition.

## 7. Оновлюйте безпечно

Update може змінити instructions, code, permissions, dependencies, network access або marketplace metadata.

Перед оновленням:

1. зафіксуйте поточну встановлену version;
2. прочитайте release notes і source diff;
3. перевірте нові hooks, connectors, MCP servers і secrets;
4. відтворіть update у test environment;
5. повторіть activation і permission tests;
6. збережіть rollback path до попередньої version.

Для workflows із repository write access, production credentials, messaging, payments або deployment capabilities використовуйте pinned чи явно схвалені updates.

## 8. Disable і remove

Використовуйте **disable**, коли досліджуєте behavior або тимчасово прибираєте capabilities зі збереженням configuration. Використовуйте **remove**, коли package більше не потрібен або йому не довіряють.

Після видалення перевірте, що host більше не надає:

- bundled skills і commands;
- custom agents;
- lifecycle hooks;
- MCP server entries;
- connector authorizations;
- cached executables або generated files;
- environment variables і secrets, створені лише для plugin.

Окремо відкличте external tokens, якщо uninstall не робить це автоматично.

## 9. Усунення проблем

### Установлено, але не видно

- перезапустіть host або почніть нову session;
- перевірте, що package відповідає поточним host і version;
- перевірте marketplace та organization policy;
- дослідіть manifest parsing errors;
- переконайтеся, що plugin enabled, а не лише downloaded.

### Skills видно, але вони не активуються

- перевірте descriptions у bundled `SKILL.md`;
- протестуйте explicit invocation;
- перевірте namespace syntax;
- переконайтеся, що host завантажив саме перевірену вами version plugin.

### Hook або MCP не запускається

- перевірте runtime і dependency versions;
- перевірте command paths та working directories;
- перевірте environment variables і доступність secrets;
- запустіть компонент безпосередньо в обмеженому test environment;
- не вимикайте approval або sandbox controls лише для приховування помилки.

### Після видалення поведінка лишилася

Знайдіть у host configuration generated MCP entries, copied skills, hook registrations, cached packages і connector authorizations. За потреби порівняйте з clean profile.

## Операційний контрольний список

- [ ] Визначено правильні host і plugin ecosystem.
- [ ] Зафіксовано publisher, source, version і license.
- [ ] Перевірено manifest, skills, code, hooks, MCP, connectors і telemetry.
- [ ] Permissions мінімізовано.
- [ ] Спочатку виконано installation у test environment.
- [ ] Positive, negative, permission і failure tests проходять.
- [ ] Визначено update і rollback policy.
- [ ] Перевірено disable, uninstall і credential revocation procedures.

## Джерела

- Поняття plugin: ../../
- Створення plugins: ../../../creating/l10n/uk_UA/
- Підтримка платформ Agent Skills: ../../../../agent-skills/sub/platform-support/l10n/uk_UA/
- Plugins OpenAI: https://developers.openai.com/codex/plugins
- Plugins Claude Code: https://code.claude.com/docs/en/plugins
- Plugins Cursor: https://cursor.com/docs/plugins
- Plugins OpenCode: https://opencode.ai/docs/plugins/
