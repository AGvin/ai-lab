<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:a97621bb05780fbb51df061445b57e48c77d49d4
  mode: translated
-->

# Hunk

Hunk — open-source review-first terminal diff viewer для інтерактивного перегляду багатофайлових наборів змін, зокрема змін, створених coding agents.

## Переклади

- [English](../../)
- Українська

## Metadata

```text
Тип ресурсу: термінальний інструмент code review і перегляду diff
Основний сценарій: інтерактивна перевірка змін, створених агентом або людиною, перед прийняттям, commit чи merge
Модель доступу: open-source локальний CLI і terminal UI
Модель вартості: безкоштовний
Ліцензія: MIT
Модель вихідного коду: Open source
Експлуатаційні вимоги: Node.js 18+ для встановлення через npm; macOS, Linux або Windows; рекомендовано Git; необов’язкові пакети Homebrew або Nix
Режими інтеграції: Git, Jujutsu, Sapling, пряме порівняння файлів, patch input, pager і difftool workflows, live review sessions під керуванням агента, sidecar-файли agent context та вбудовуваний компонент OpenTUI
Джерело: https://github.com/modem-dev/hunk
Примітки щодо ризиків: Hunk покращує видимість набору змін, але не доводить його правильність чи безпечність. Зберігайте тести, статичний аналіз, security review і людське схвалення. Live agent control використовує локальний loopback session service, тому перевіряйте межі sandbox і локальної мережі перед наданням агенту доступу.
Востаннє перевірено: 2026-07-17
```

## Огляд

Hunk показує набір змін як інтерактивний термінальний потік review замість звичайного текстового diff. Він надає sidebar-навігацію між файлами, syntax highlighting, split і stacked layouts, керування клавіатурою та мишею, inline-анотації агентів і watch mode для автоматичного оновлення активного review.

Hunk сам не є code-review agent. Він представляє зміни та анотації для перевірки, тоді як аналіз і рішення review залишаються за людиною або зовнішнім агентом.

## Основні можливості

- Перегляд багатофайлових змін working tree і commits в одному навігаційному інтерфейсі.
- Додавання untracked files до Git working-tree review, керованого Hunk.
- Перемикання між split, stacked і responsive automatic layouts.
- Оновлення Git-backed і direct-file review через watch mode.
- Відображення inline AI- або agent-notes біля відповідного місця diff.
- Робота через клавіатуру, мишу, pager і Git difftool workflows.
- Виявлення Git, Jujutsu і Sapling workspaces та використання їхнього native revision syntax.
- Порівняння пар файлів або відображення patches зі standard input.
- Надання diff renderer як компонента OpenTUI для інших застосунків.

## Встановлення

Установіть npm-пакет `hunkdiff` глобально:

```bash
npm install --global hunkdiff
```

Установлений executable має назву `hunk`. Користувачі Homebrew можуть установити підтримувану formula:

```bash
brew install hunk
```

Користувачі Nix можуть використати пакет, експортований у `flake.nix` репозиторію.

Перевірте встановлення:

```bash
hunk --version
hunk
```

## Workflows перевірки

### Git working tree і commits

```bash
hunk diff
hunk diff --watch
hunk show
hunk show HEAD~1
```

`hunk diff` перевіряє поточні зміни репозиторію та за замовчуванням включає untracked files. `hunk show` перевіряє commit; без revision використовується останній commit.

### Прямі файли та patches

```bash
hunk diff before.ts after.ts
hunk diff before.ts after.ts --watch
git diff --no-color | hunk patch -
```

Ці режими корисні для перегляду згенерованих результатів, експортованих patches або файлів поза звичайним Git changeset.

### Jujutsu і Sapling

Hunk автоматично виявляє Jujutsu і Sapling workspaces. У таких репозиторіях `hunk diff` і `hunk show` приймають native revsets. Вибраний version-control backend також можна перевизначити в конфігурації.

## Перевірка за участю агента

Hunk може відкрити запущений terminal review зовнішньому coding agent:

1. Відкрийте `hunk diff` або `hunk show` у терміналі під контролем користувача.
2. Запустіть `hunk skill path` і надайте агенту знайдений Hunk review skill.
3. Попросіть агента інспектувати й керувати live Hunk session через commands `hunk session`.

Типові неінтерактивні commands агента:

```bash
hunk session list
hunk session get --repo .
hunk session review --repo . --json
hunk session navigate --repo . --file src/App.tsx --hunk 2
hunk session comment add --repo . --file src/App.tsx --new-line 42 --summary "Check this boundary condition"
```

Агент може інспектувати структуру review, переміщатися у видимому UI, оновлювати вміст і додавати inline notes. Додавання raw patch необов’язкове; запитуйте його лише тоді, коли агенту потрібен повний unified diff.

Замість live session параметр `--agent-context` може завантажувати попередньо створені agent annotations із JSON sidecar file.

## Конфігурація

Hunk читає користувацьку або репозиторну TOML-конфігурацію з:

```text
~/.config/hunk/config.toml
.hunk/config.toml
```

Налаштовуються theme, layout mode, version-control backend, watch mode, обробка untracked files, line numbers, wrapping, видимість menu, agent notes і прозоре тло термінала.

Hunk також можна налаштувати як Git pager:

```bash
git config --global core.pager "hunk pager"
```

Власна команда `hunk diff` є кращою, коли потрібно включати untracked files, оскільки Git сам визначає, що передавати pager.

## Сильні сторони

- Надає сфокусовану людську review surface для великих змін, створених агентами.
- Зберігає навігацію, syntax highlighting і annotations у термінальному workflow.
- Відокремлює генерацію коду від явної перевірки замість автоматичного прийняття змін агента.
- Підтримує кілька систем контролю версій і raw patch input.
- Дозволяє агенту супроводжувати live review, поки користувач контролює видиму session.
- Може використовуватися як opt-in command без заміни редактора або coding agent.

## Компроміси й обмеження

- Hunk є інструментом представлення й review, а не заміною тестів, linters, static analysis або security scanning.
- Inline agent notes можуть бути неповними, шумними або неправильними й потребують людського судження.
- Він не надає structural diffing рівня syntax-aware інструментів, таких як Difftastic.
- Live session control залежить від локального loopback service, який може бути недоступним із обмеженого agent sandbox.
- Watch behavior відрізняється між version-control backends; Jujutsu і Sapling можуть використовувати polling.
- Глобальна конфігурація pager змінює звичайний Git output і має бути перевірена до широкого впровадження.
- Проєкт розвивається, тому commands, packaging і session interfaces слід звіряти з установленим release.

## Відповідність AI Lab

Hunk належить до `development/code-review-tools/`, оскільки його основна роль — інтерактивно представляти й анотувати набори змін коду. Інтеграція з агентом дозволяє зовнішньому агенту брати участь у review, але Hunk не поводиться самостійно як code-review agent.

Використовуйте цю сторінку як довідку для:

- людської перевірки змін coding agents;
- термінальної навігації diff і changesets;
- agent annotations, прив’язаних до точних місць diff;
- review workflows для Git, Jujutsu і Sapling;
- порівняння з Lumen, Difftastic, Delta та іншими diff-viewing tools.

## Посилання

- Репозиторій і основна документація: https://github.com/modem-dev/hunk
- Настанова з agent workflows: https://github.com/modem-dev/hunk/blob/main/docs/agent-workflows.md
- Hunk review skill: https://github.com/modem-dev/hunk/blob/main/skills/hunk-review/SKILL.md
- Настанова з компонента OpenTUI: https://github.com/modem-dev/hunk/blob/main/docs/opentui-component.md
- Ліцензія: https://github.com/modem-dev/hunk/blob/main/LICENSE
