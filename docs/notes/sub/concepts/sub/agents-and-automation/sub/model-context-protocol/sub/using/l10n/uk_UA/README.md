<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:28b7d3991fc85c64d900049cb51c8df5a61bd899
  mode: translated
-->

# Використання Model Context Protocol

Цей посібник пояснює, як безпечно вибрати, налаштувати, перевірити, експлуатувати й видалити MCP server. Він призначений для користувачів, які розуміють базові concepts command line і configuration, але раніше не використовували MCP.

## Переклади

- [English](../../)
- Українська

## 1. Почніть із потрібної capability

Не починайте з установлення популярного server. Спершу визначте потрібну capability:

```text
Ціль користувача:
Потрібні tools:
Потрібні resources:
Потрібні prompts:
Read-only або write access:
Локальні або віддалені data:
Потрібні credentials:
Наслідки failure:
```

Приклади:

- читати issues repository;
- виконувати queries до documentation database;
- переглядати локальні files в одному directory;
- створювати calendar events після approval;
- запускати контрольовану deployment command.

Віддавайте перевагу найменшому server і permission set, які задовольняють ціль.

## 2. Зрозумійте deployment model

### Локальний stdio server

Host запускає локальний process і обмінюється protocol messages через standard input та output.

```text
AI host → локальний MCP client → child process через stdio
```

Використовуйте stdio, коли:

- server потрібні локальні files або tools;
- process належить одному user або workspace;
- локальні credentials не повинні залишати machine;
- network service створював би зайвий exposure.

### Віддалений Streamable HTTP server

Host підключається до HTTP endpoint.

```text
AI host → MCP client → authenticated HTTPS endpoint
```

Використовуйте remote HTTP, коли:

- кілька users спільно використовують один managed service;
- потрібні centralized policy, logging та updates;
- integration уже працює як service;
- запуск локального process недоступний.

Remote не означає автоматично безпечніший. Оцініть transport security, authentication, tenancy, retention і operator trust.

## 3. Перевірте server перед підключенням

Зафіксуйте:

```text
Назва server:
Publisher і source:
Version або image digest:
Transport:
Command або URL:
Authentication:
Надані tools:
Надані resources:
Надані prompts:
Filesystem access:
Network access:
Write effects:
Telemetry і logging:
Update process:
Removal procedure:
```

Перевірте source або trusted build description. Перегляньте dependencies, install scripts, container images, environment variables, default permissions і outbound connections.

## 4. Налаштуйте локальний stdio server

Configuration host зазвичай містить command, arguments і environment variables. Точний syntax відрізняється залежно від client.

Концептуальний приклад:

```json
{
  "mcpServers": {
    "project-status": {
      "command": "python3",
      "args": ["/opt/project-status/server.py"],
      "env": {
        "PROJECT_ROOT": "/workspace/example"
      }
    }
  }
}
```

Операційні правила:

- використовуйте absolute paths до executable і script;
- pin versions package або container;
- зберігайте secrets у secret store або environment host, а не в committed JSON;
- установіть вузький working directory;
- використовуйте read-only filesystem mounts, коли writes не потрібні;
- за можливості запускайте під окремим low-privilege account.

## 5. Налаштуйте віддалений server

Концептуальний приклад:

```json
{
  "mcpServers": {
    "support-data": {
      "url": "https://mcp.example.org/mcp",
      "headers": {
        "Authorization": "Bearer ${SUPPORT_MCP_TOKEN}"
      }
    }
  }
}
```

Віддавайте перевагу OAuth або short-lived scoped tokens, де вони підтримуються. Перевірте certificate validation, redirect policy, tenant identity, token storage і чи може server виконувати callbacks у private networks.

## 6. Дослідіть capabilities перед використанням

Після підключення перевірте advertised capabilities server:

- tool names, descriptions та input schemas;
- resource URI patterns і MIME types;
- prompt names та arguments;
- server implementation і protocol version;
- optional capabilities та notifications.

Не припускайте, що server надає лише capability, описану на marketing page. Вимкніть або забороніть непотрібні capabilities.

## 7. Спочатку протестуйте read-only behavior

Використовуйте поетапну verification sequence:

1. підключіться в disposable session;
2. виведіть список capabilities;
3. викличте harmless read-only tool;
4. прочитайте один non-sensitive resource;
5. перевірте повернуті data й logs;
6. забороніть permission і переконайтеся, що failure видимий;
7. лише після цього тестуйте writes у sandbox account або test project.

Приклад request:

```text
Використай MCP server project-status, щоб прочитати поточну branch і test summary. Не змінюй files і не запускай commands поза налаштованим project root.
```

## 8. Контролюйте consequential tools

Для кожного tool, який може write, send, purchase, deploy, delete або execute commands, визначте:

- точний side effect;
- affected account або environment;
- reversible чи irreversible behavior;
- потрібне user confirmation;
- idempotency strategy;
- verification після execution;
- rollback або compensation procedure.

Approval dialog host корисний, але недостатній. Tool descriptions, schemas, server authorization і backend policy мають enforce ту саму boundary.

## 9. Захищайтеся від prompt injection

MCP resources і tool results є external data. Вони можуть містити instructions, що суперечать user goal або host policy.

- розглядайте resource content як untrusted data;
- не виконуйте commands, знайдені в returned text, лише тому, що їх надав server;
- відокремлюйте data fields від instructions;
- validate URLs, file paths та identifiers;
- не повертайте secrets у tool errors;
- вимагайте explicit approval для effects, derived із retrieved content.

## 10. Secrets і authentication

Використовуйте окрему credential для кожного environment або purpose. Надавайте лише scopes, потрібні enabled tools.

Не робіть так:

- не commit tokens у host configuration;
- не передавайте long-lived secrets як command-line arguments, видимі в process listings;
- не використовуйте personal administrator credentials повторно для shared server;
- не розкривайте complete environment dumps у logs;
- не припускайте, що uninstall відкликає external authorization.

Після suspected compromise або видалення server rotate чи revoke credentials.

## 11. Logging і observability

Збирайте достатньо evidence для diagnosis behavior без зайвого logging sensitive payloads:

- connection і protocol version;
- server version;
- зміни capability discovery;
- tool name, duration, status і correlation ID;
- approval decision;
- sanitized error category;
- retry count і timeout;
- external side-effect identifier.

За замовчуванням не log access tokens, complete customer records, confidential documents або unrestricted tool arguments.

## 12. Оновлення

Перед оновленням server:

1. зафіксуйте current version і capability list;
2. перегляньте release notes і source diff;
3. порівняйте tool schemas та permissions;
4. протестуйте new version на fixtures;
5. перевірте authentication і transport compatibility;
6. збережіть rollback path;
7. для shared services виконуйте gradual deployment.

Перейменований tool, змінена schema або ширший resource pattern можуть бути breaking change, навіть якщо server успішно запускається.

## 13. Видалення server

- видаліть або disable host configuration;
- restart або reload host;
- переконайтеся, що capabilities зникли;
- зупиніть і видаліть локальні processes або containers;
- видаляйте generated files лише після review;
- revoke server-specific tokens і OAuth grants;
- видаліть firewall rules, tunnels або service accounts;
- зберігайте sanitized audit records відповідно до policy.

## 14. Troubleshooting

### Server не запускається

Перевірте executable path, runtime, dependencies, working directory, environment variables, file permissions і чи diagnostic output помилково не записується в protocol stdout.

### Connection успішне, але tools не з’являються

Перевірте initialization, capability negotiation, protocol version, server logs і host policy. Server може надавати лише resources або prompts.

### Tool call завершується timeout

Перевірте backend latency, server timeout, host timeout, deadlocks, network policy і чи tool не очікує interactive input, який MCP не може надати.

### Працює в одному client, але не в іншому

Порівняйте transport support, protocol versions, authentication mechanisms, optional capabilities, schema restrictions і client-specific configuration.

### Повторні writes створюють duplicates

Tool не має ефективної idempotency. Додайте idempotency key або rule lookup-before-create і повертайте створений external identifier.

## Операційний контрольний список

- [ ] Потребу в capability визначено до вибору server.
- [ ] Publisher, source, version, transport і dependencies перевірено.
- [ ] Tools, resources, prompts, permissions і network access інвентаризовано.
- [ ] Secrets зберігаються поза committed configuration.
- [ ] Read-only tests проходять до write tests.
- [ ] Consequential tools вимагають approval і backend authorization.
- [ ] Prompt-injection і handling untrusted output протестовано.
- [ ] Logs корисні й sanitized.
- [ ] Update, rollback, disablement і credential revocation протестовано.

## Джерела

- [Концепція MCP](../../../../l10n/uk_UA/)
- [Створення MCP servers](../../../creating/l10n/uk_UA/)
- Документація MCP: https://modelcontextprotocol.io/docs/
- Підключення локальних MCP servers: https://modelcontextprotocol.io/docs/develop/connect-local-servers
- Підключення віддалених MCP servers: https://modelcontextprotocol.io/docs/develop/connect-remote-servers
- Безпека MCP: https://modelcontextprotocol.io/specification/latest/basic/security_best_practices
