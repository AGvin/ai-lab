<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:30f605afb269a5612fdff3e647e48472eae27e72
  mode: translated
-->

# Model Context Protocol (MCP)

Model Context Protocol — відкритий протокол для підключення AI applications до зовнішніх tools, контекстних даних, повторно використовуваних prompts і пов’язаних capabilities через узгоджений client-server interface.

## Переклади

- [English](../../)
- Українська

## Шлях навчання

- [Використання Model Context Protocol](../../sub/using/l10n/uk_UA/) — вибір, налаштування, перевірка, захист, оновлення й видалення MCP servers.
- [Створення MCP servers](../../sub/creating/l10n/uk_UA/) — побудова server із tools, resources, prompts, tests, authorization і deployment safeguards.
- [Agent Skills](../../../agent-skills/l10n/uk_UA/) — повторно використовувані workflows, які можуть оркеструвати capabilities, надані через MCP.
- [Plugins](../../../plugins/l10n/uk_UA/) — platform-specific packages, які можуть налаштовувати або поширювати MCP integrations.

## Призначення

Без спільного протоколу кожній AI application і зовнішній integration потрібен власний adapter. MCP визначає спільну поведінку discovery, invocation, lifecycle і transport, щоб сумісні hosts та servers могли взаємодіяти без окремого connector для кожної пари.

MCP стандартизує обмін контекстом. Він не визначає, як application вибирає model, планує agent workflow, зберігає memory, оцінює results або вирішує, чи можна довіряти отриманому context.

## Архітектура

MCP використовує три ролі учасників:

- **Host** — AI application, яка координує MCP connections і вирішує, як capabilities надаються model або user.
- **Client** — компонент host, що підтримує одне connection з одним MCP server.
- **Server** — локальна або віддалена program, що надає capabilities і contextual information.

Host може створити кілька clients, кожний із яких підтримує незалежне connection з іншим server.

## Основні server primitives

MCP servers можуть надавати три основні primitives:

- **Tools** — виконувані operations, наприклад query до API, зміна file або виконання database command.
- **Resources** — контекстні data, наприклад file contents, database records, schemas або API responses.
- **Prompts** — повторно використовувані interaction templates, instructions або examples.

Clients знаходять capabilities через protocol methods, а не припускають наявність фіксованого list. Servers також можуть повідомляти clients про зміни підтримуваних lists.

Control зазвичай відрізняється залежно від primitive:

- prompts зазвичай вибирає user;
- resources зазвичай вибирає й керує application;
- tools зазвичай вибирає model відповідно до host і user policy.

Host залишається відповідальним за consent, authorization, presentation і approval.

## Client capabilities

Залежно від узгодженої підтримки servers можуть запитувати capabilities від client, зокрема:

- model sampling через host application;
- user elicitation для додаткового input або confirmation;
- structured logging і progress reporting.

Ці capabilities узгоджуються й не гарантовано доступні в кожній реалізації client або server.

## Lifecycle і capability negotiation

MCP є stateful. Connection починається з initialization, узгодження protocol version, обміну identity та оголошення capabilities. Client і server повинні використовувати лише взаємно підтримувані features та мають завершити connection, якщо не можуть узгодити сумісну protocol version.

Capability negotiation важливе, оскільки реалізації MCP можуть підтримувати різні protocol versions, primitives, notifications, authorization methods або optional client features.

## Data і transport layers

Data layer MCP використовує повідомлення JSON-RPC 2.0 для requests, responses, notifications, lifecycle operations і methods окремих primitives.

Transport layer переносить ці повідомлення. Основні transports:

- **stdio** — прямий обмін через standard input і standard output із локальним server process;
- **Streamable HTTP** — HTTP-based communication для локальних або віддалених servers із optional streaming і звичайними HTTP authentication mechanisms.

Той самий server concept може працювати локально або віддалено. Назва «MCP server» описує його protocol role, а не фізичне розташування.

Для stdio servers звичайні logs не можна писати в stdout, оскільки stdout переносить protocol messages. Для diagnostics використовуйте stderr або file.

## MCP і tool calling

[Tool calling](../../../tool-calling/l10n/uk_UA/) — model-facing поведінка вибору доступної operation і формування arguments. MCP є одним зі способів, яким AI application може знаходити й надавати external operations і context цьому tool-calling layer.

Model може використовувати tools без MCP, а MCP server може надавати більше, ніж executable tools, оскільки resources і prompts також є protocol primitives.

## MCP і function calling

[Function calling](../../../function-calling/l10n/uk_UA/) зазвичай описує structured model API, де доступні functions представлені schemas, а model повертає function name з arguments.

MCP працює на ширшій application-integration boundary. Він визначає client-server discovery, lifecycle, capability negotiation, context primitives, invocation, notifications і transports. MCP host може перетворювати знайдені MCP tools у function- або tool-calling format, очікуваний вибраним model provider.

## MCP і Agent Skills

[Agent Skill](../../../agent-skills/l10n/uk_UA/) пакує procedural knowledge: коли workflow застосовується, які steps виконати, які evidence зібрати та де потрібні approvals.

MCP надає capabilities і context. Skill може вказувати agent використовувати один або кілька MCP tools чи resources, але skill не створює connection і не надає permissions.

Приклад:

- MCP server надає `list_failed_jobs` і `retry_job`;
- troubleshooting skill визначає diagnosis, evidence collection, approval перед retry і post-action verification.

## MCP і plugins

[Plugin](../../../plugins/l10n/uk_UA/) — platform-specific installation і distribution package. Він може містити skills, hooks, agents, commands, connector declarations або MCP server configuration.

MCP — це protocol; plugin — packaging. Установлення plugin, який налаштовує MCP, створює окремі trust boundaries для plugin і server.

## MCP і звичайні API

MCP server часто обгортає звичайний API, локальну application, database, filesystem або service. MCP не замінює underlying API, а надає стандартизований AI-facing integration layer навколо нього.

Фактична portability залежить від підтримки protocol version, authentication, optional capabilities, tool schemas, host policies і implementation quality.

## Безпека й межі довіри

Підключення MCP server розширює trust boundary host. Перевіряйте:

- хто керує й підтримує server;
- чи працює він локально або віддалено;
- до яких files, services, accounts і credentials він має access;
- які tools можуть спричинити writes, commands, purchases, messages або інші side effects;
- які data надсилаються network;
- як зберігаються й обмежуються authentication tokens;
- чи містять tool outputs або resources недовірені instructions;
- чи запитує host approval перед consequential actions;
- як контролюються server updates, dependencies і supply-chain risks.

Protocol compatibility не є security endorsement. Hosts мають застосовувати least privilege, explicit approval gates, input і output validation, logging та isolation відповідно до наслідків кожної capability.

Servers повинні реалізувати справжню authorization для protected actions. Session identifiers не є authentication. Hosts не повинні покладатися лише на tool descriptions або model judgment для enforcement access control.

## Практичний приклад

Database MCP server може надавати:

- resource зі schema database;
- prompt із прикладами safe queries;
- read-only query tool;
- administrative mutation tool, доступний лише за суворішої permission policy.

Host знаходить ці capabilities, вирішує, які з них увімкнути, надає дозволені tool schemas model, отримує user approval за потреби, викликає вибрану operation і повертає result у application workflow.

## Обмеження

MCP автоматично не забезпечує:

- безпечні або правильні tools;
- trustworthy server output;
- сумісну behavior у кожному host;
- authorization, відповідну requested action;
- sandboxing локального process;
- protection від prompt injection або malicious contextual data;
- правильні model decisions щодо часу й способу використання capability;
- стабільну compatibility за різних protocol versions або optional features.

Розглядайте MCP як interoperability protocol, що все одно потребує product-level security, permissions, validation, observability і lifecycle management.

## Джерела

- Документація MCP: https://modelcontextprotocol.io/docs/
- Огляд архітектури: https://modelcontextprotocol.io/docs/learn/architecture
- Специфікація MCP: https://modelcontextprotocol.io/specification/
- Створення MCP server: https://modelcontextprotocol.io/docs/develop/build-server
- Найкращі практики безпеки: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- Організація MCP на GitHub: https://github.com/modelcontextprotocol
