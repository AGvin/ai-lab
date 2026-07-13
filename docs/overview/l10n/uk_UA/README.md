<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:549e7d4d96d70f24a8385a3b2c9a933e255dbeeb
  mode: translated
-->

# Огляд

Практична лабораторія ШІ для моделей, інструментів, локального inference, benchmarks, нотаток про обладнання та automation workflows.

## Переклади

- [English](../../)
- Українська

## Структура документації

Використовуйте `docs/` як контейнер документації рівня репозиторію.

Використовуйте `sub/` для дочірніх вузлів документації всередині іменованого вузла.

Не створюйте `docs/README.md`.

## Вузли документації

- [`docs/software/`](../../software/l10n/uk_UA/) — пов’язане зі ШІ ПЗ, inference tools, workflow engines, development workflows, редактори коду, агенти, assistants, automation tools, платформи й моделі.
- [`docs/notes/`](../../notes/l10n/uk_UA/) — поняття, benchmarks, порівняння та практичні нотатки про ШІ.

## Поточні області software

- [`inference/`](../../software/sub/inference/l10n/uk_UA/) — локальне й self-hosted виконання моделей.
- [`workflow-engines/`](../../software/sub/workflow-engines/l10n/uk_UA/) — AI workflow engines та UIs.
- [`development-workflows/`](../../software/sub/development-workflows/l10n/uk_UA/) — інструменти, що структурують розроблення ПЗ за допомогою ШІ через довговічні специфікації, плани, задачі, валідацію та етапи реалізації.
- [`code-editors/`](../../software/sub/code-editors/l10n/uk_UA/) — редактори коду й екосистеми editor extensions.
- [`agents/`](../../software/sub/agents/l10n/uk_UA/) — агентоподібні системи ШІ.
- [`agent-orchestration/`](../../software/sub/agent-orchestration/l10n/uk_UA/) — системи, frameworks, runtimes і control planes для координації чи запуску агентів ШІ.
- [`assistants/`](../../software/sub/assistants/l10n/uk_UA/) — розмовні assistants ШІ.
- [`automation/`](../../software/sub/automation/l10n/uk_UA/) — засоби автоматизації для суміжних зі ШІ workflows.
- [`model-platforms/`](../../software/sub/model-platforms/l10n/uk_UA/) — платформи моделей, datasets та інструментів ШІ.
- [`models/`](../../software/sub/models/l10n/uk_UA/) — сімейства моделей та окремі моделі ШІ.

## Поточні області notes

- [`concepts/`](../../notes/sub/concepts/l10n/uk_UA/) — пояснення понять ШІ.
- [`benchmarks/`](../../notes/sub/benchmarks/l10n/uk_UA/) — довідкові ресурси benchmark і leaderboard.
- [`comparisons/`](../../notes/sub/comparisons/l10n/uk_UA/) — порівняння для підтримки рішень щодо моделей, інструментів, workflows, платформ і систем ШІ.

## Assets

Використовуйте `assets/` усередині вузла документації для допоміжних файлів цього вузла.

Надавайте перевагу типізованим підкаталогам:

```text
assets/
  images/
  screenshots/
  diagrams/
  pdf/
  samples/
  exports/
  files/
```

Ролі каталогів:

- `images/` — загальні зображення документації.
- `screenshots/` — screenshots UI.
- `diagrams/` — діаграми, charts, схеми й візуальні пояснення.
- `pdf/` — PDF-файли.
- `samples/` — малі зразки inputs, configs, prompts, datasets або прикладів.
- `exports/` — експортовані артефакти, створені інструментами чи workflows.
- `files/` — інші допоміжні файли, що не належать до типізованих каталогів.

Приклад:

```text
docs/software/sub/code-editors/sub/vs-code/
  README.md
  assets/
    images/
      interface.png
    screenshots/
      extension-settings.png
    pdf/
      reference.pdf
    files/
      uncommon-reference-file.ext
```

Настанови:

- Зберігайте assets поряд із вузлом документації, що їх використовує.
- Використовуйте типізовані asset folders замість розміщення файлів безпосередньо в `assets/`.
- Використовуйте `files/` для рідкісних або різнорідних типів файлів замість одноразових каталогів.
- Створюйте лише каталоги, що містять реальні файли.
- Використовуйте спільні assets батьківського рівня лише тоді, коли той самий файл повторно використовують кілька дочірніх сторінок.

## Правила розширення

Створюйте нові вузли документації лише за наявності реального вмісту.

Створюйте `assets/` і типізовані asset subdirectories лише тоді, коли вузол документації має реальні допоміжні файли.

Використовуйте `assets/files/` для рідкісних типів допоміжних файлів, що не виправдовують окремого типізованого каталогу.

Використовуйте одну канонічну сторінку для кожного продукту, моделі, платформи, assistant, агента, редактора, extension або tool. Додавайте дочірні вузли лише тоді, коли конкретний сценарій використання має достатньо вмісту для окремої сторінки.
