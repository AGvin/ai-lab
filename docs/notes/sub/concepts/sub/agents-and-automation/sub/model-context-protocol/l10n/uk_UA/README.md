<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: sha256:eb620b23a77fb434594bbff9beb32b5698483193dc35fab53ceea7a7ef77e977
  mode: translated
-->

# Model Context Protocol (MCP)

Model Context Protocol — відкритий протокол для підключення AI applications до зовнішніх tools, контекстних даних, повторно використовуваних prompts і пов’язаних capabilities через узгоджений client-server interface.

## Переклади

- [English](../../)
- Українська

## Призначення

Без спільного протоколу кожній AI application і зовнішній integration потрібен власний adapter. MCP визначає спільну поведінку discovery, invocation, lifecycle і transport, щоб сумісні hosts та servers могли взаємодіяти без окремого connector для кожної пари.

MCP стандартизує обмін контекстом. Він не визначає, як application вибирає модель, планує agent workflow, зберігає memory, оцінює результати або вирішує, чи можна довіряти отриманому контексту.

## Архітектура

MCP використовує три ролі учасників:

- **Host** — AI application, яка координує MCP connections і вирішує, як capabilities надаються моделі або користувачу.
- **Client** — компонент host, що підтримує одне з’єднання з одним MCP server.
- **Server** — локальна або віддалена програма, що надає capabilities і контекстну інформацію.

Host може створити кілька clients, кожний із яких підтримує незалежне з’єднання з іншим server.

## Основні server primitives

MCP servers можуть надавати три основні primitives:

- **Tools** — виконувані операції, наприклад запит до API, зміна файла або виконання database command.
- **Resources** — контекстні дані, наприклад вміст файлів, database records, schemas або API responses.
- **Prompts** — повторно використовувані interaction templates, instructions або examples.

Clients знаходять capabilities через methods протоколу, а не припускають наявність фіксованого списку. Servers також можуть повідомляти clients про зміни підтримуваних списків.

## Client capabilities

Залежно від узгодженої підтримки servers можуть запитувати capabilities від client, зокрема:

- model sampling через host application;
- user elicitation для додаткового input або confirmation;
- structured logging і progress reporting.

Ці capabilities узгоджуються й не гарантовано доступні в кожній реалізації client або server.

## Lifecycle і capability negotiation

MCP є stateful protocol. З’єднання починається з initialization, узгодження protocol version, обміну identity та оголошення capabilities. Client і server повинні використовувати лише взаємно підтримувані features та мають завершити з’єднання, якщо не можуть узгодити сумісну версію протоколу.

Capability negotiation важливе, оскільки реалізації MCP можуть підтримувати різні protocol versions, primitives, notifications, authorization methods або необов’язкові client features.

## Data і transport layers

Data layer MCP використовує повідомлення JSON-RPC 2.0 для requests, responses, notifications, lifecycle operations і methods окремих primitives.

Transport layer переносить ці повідомлення. Основні transports:

- **stdio** — прямий обмін через standard input і standard output із локальним server process;
- **Streamable HTTP** — HTTP-based communication для локальних або віддалених servers із необов’язковим streaming і звичайними HTTP authentication mechanisms.

Той самий тип server може працювати локально або віддалено. Назва «MCP server» описує роль у протоколі, а не фізичне розташування.

## MCP і tool calling

[Tool calling](../../../tool-calling/l10n/uk_UA/) — model-facing поведінка вибору доступної операції та формування аргументів. MCP є одним зі способів, яким AI application може знаходити й надавати зовнішні operations та context цьому tool-calling layer.

Модель може використовувати tools без MCP, а MCP server може надавати не лише executable tools, оскільки resources і prompts також є primitives протоколу.

## MCP і function calling

[Function calling](../../../function-calling/l10n/uk_UA/) зазвичай описує structured model API, де доступні functions представлені schemas, а модель повертає назву function та arguments.

MCP працює на ширшій межі application integration. Він визначає client-server discovery, lifecycle, capability negotiation, context primitives, invocation, notifications і transports. MCP host може перетворювати знайдені MCP tools у формат function або tool calling, очікуваний вибраним model provider.

## MCP, звичайні API та plugins

MCP server часто обгортає звичайний API, локальну application, database, filesystem або service. MCP не замінює underlying API, а надає стандартизований AI-facing integration layer навколо нього.

На відміну від platform-specific plugin system, MCP призначений для повторного використання між сумісними hosts. Фактична portability усе одно залежить від підтримки protocol version, authentication, optional capabilities, tool schemas, host policies і якості реалізації.

## Безпека й межі довіри

Підключення MCP server розширює trust boundary host. Перевіряйте:

- хто керує й підтримує server;
- чи працює він локально або віддалено;
- до яких файлів, services, accounts і credentials він має доступ;
- які tools можуть спричинити writes, commands, purchases, messages або інші side effects;
- які дані надсилаються мережею;
- як зберігаються й обмежуються authentication tokens;
- чи містять tool outputs або resources недовірені instructions;
- чи запитує host схвалення перед consequential actions;
- як контролюються server updates, dependencies і supply-chain risks.

Сумісність із протоколом не є підтвердженням безпеки. Hosts мають застосовувати least privilege, explicit approval gates, input та output validation, logging і isolation відповідно до наслідків кожної capability.

## Практичний приклад

Database MCP server може надавати:

- resource зі схемою database;
- prompt із прикладами безпечних queries;
- read-only query tool;
- administrative mutation tool, доступний лише за суворішої permission policy.

Host знаходить ці capabilities, вирішує, які з них увімкнути, надає дозволені tool schemas моделі, отримує схвалення користувача за потреби, викликає вибрану operation і повертає result у application workflow.

## Обмеження

MCP автоматично не забезпечує:

- безпечні або правильні tools;
- надійний output server;
- сумісну поведінку в кожному host;
- authorization, відповідну запитаній дії;
- sandboxing локального process;
- захист від prompt injection або шкідливих контекстних даних;
- правильні рішення моделі щодо часу й способу використання capability;
- стабільну сумісність за різних protocol versions або optional features.

Розглядайте MCP як interoperability protocol, що все одно потребує product-level security, permissions, validation, observability і lifecycle management.

## Джерела

- Документація MCP: https://modelcontextprotocol.io/docs/
- Огляд архітектури: https://modelcontextprotocol.io/docs/learn/architecture
- Специфікація MCP: https://modelcontextprotocol.io/specification/
- Організація MCP на GitHub: https://github.com/modelcontextprotocol
