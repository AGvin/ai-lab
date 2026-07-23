<!--
l10n:
  locale: uk_UA
  source_locale: default
  source_path: ../../README.md
  source_hash: gitblob:607fa9cb73165ae78b0fba20678cd0094bc48163
  mode: translated
-->

# Поняття

Практичні й фундаментальні поняття ШІ, організовані за темою та пріоритетом читання.

Пріоритет указує рекомендований порядок навчання для користувача, який переважно використовує моделі, налаштовує локальний inference та створює або експлуатує agent workflows.

## Переклади

- [English](../../)
- Українська

## [Основи й архітектура](../../sub/foundations-and-architecture/l10n/uk_UA/)

Ключові поняття, що пояснюють, чим є сучасні моделі ШІ та як співвідносяться їхні головні архітектурні сімейства.

### Основні

- [`foundation-models/`](../../sub/foundations-and-architecture/sub/foundation-models/l10n/uk_UA/) — великі моделі багаторазового використання, навчені на широких даних і адаптовані до багатьох подальших задач.
- [`large-language-models/`](../../sub/foundations-and-architecture/sub/large-language-models/l10n/uk_UA/) — орієнтовані на мову фундаментальні моделі, які прогнозують і генерують послідовності токенів.
- [`multimodal-models/`](../../sub/foundations-and-architecture/sub/multimodal-models/l10n/uk_UA/) — моделі, які обробляють або генерують кілька модальностей, зокрема текст, зображення, аудіо чи відео.

### Корисні

- [`transformers/`](../../sub/foundations-and-architecture/sub/transformers/l10n/uk_UA/) — архітектури нейронних мереж, побудовані навколо уваги й паралельного оброблення послідовностей.
- [`attention/`](../../sub/foundations-and-architecture/sub/attention/l10n/uk_UA/) — механізм, що зважує важливість елементів вхідних даних для операції моделі.
- [`mixture-of-experts/`](../../sub/foundations-and-architecture/sub/mixture-of-experts/l10n/uk_UA/) — розріджені архітектури моделей, які спрямовують кожен вхід через вибрані експертні компоненти.

### Спеціалізовані

- [`artificial-intelligence/`](../../sub/foundations-and-architecture/sub/artificial-intelligence/l10n/uk_UA/) — широка галузь систем, що виконують задачі сприйняття, міркування, генерації або ухвалення рішень.
- [`machine-learning/`](../../sub/foundations-and-architecture/sub/machine-learning/l10n/uk_UA/) — методи, які навчаються закономірностей із даних замість опори лише на явно запрограмовані правила.
- [`deep-learning/`](../../sub/foundations-and-architecture/sub/deep-learning/l10n/uk_UA/) — машинне навчання на основі нейронних мереж із багатьма шарами оброблення.
- [`neural-networks/`](../../sub/foundations-and-architecture/sub/neural-networks/l10n/uk_UA/) — параметризовані обчислювальні структури зі з’єднаних шарів або блоків оброблення.
- [`self-attention/`](../../sub/foundations-and-architecture/sub/self-attention/l10n/uk_UA/) — увага, обчислена між позиціями однієї послідовності.
- [`encoder-decoder/`](../../sub/foundations-and-architecture/sub/encoder-decoder/l10n/uk_UA/) — структури моделей, що кодують вхідні дані, генерують вихідні або поєднують обидві ролі.
- [`dense-and-sparse-models/`](../../sub/foundations-and-architecture/sub/dense-and-sparse-models/l10n/uk_UA/) — щільні моделі активують більшість параметрів для кожного входу, а розріджені — вибрані підмножини.

## [Використання моделей і генерація](../../sub/model-usage-and-generation/l10n/uk_UA/)

Поняття для ефективного використання навчених моделей через чати, API, застосунки й локальні середовища виконання.

### Основні

- [`tokens-and-tokenization/`](../../sub/model-usage-and-generation/sub/tokens-and-tokenization/l10n/uk_UA/) — процес поділу вхідних і вихідних даних на одиниці, які модель читає й генерує.
- [`context-window/`](../../sub/model-usage-and-generation/sub/context-window/l10n/uk_UA/) — обмежений обсяг токенізованої інформації, який модель може врахувати в одному запиті.
- [`prompting/`](../../sub/model-usage-and-generation/sub/prompting/l10n/uk_UA/) — надання інструкцій, контексту, прикладів і обмежень для спрямування моделі.
- [`system-prompts/`](../../sub/model-usage-and-generation/sub/system-prompts/l10n/uk_UA/) — високопріоритетні інструкції, що визначають роль, поведінку й операційні межі асистента.
- [`structured-output/`](../../sub/model-usage-and-generation/sub/structured-output/l10n/uk_UA/) — вихід моделі, обмежений машинозчитуваною структурою на кшталт JSON або схеми.
- [`hallucinations/`](../../sub/model-usage-and-generation/sub/hallucinations/l10n/uk_UA/) — непідтверджений або неправильний вихід моделі, поданий у правдоподібній формі.

### Корисні

- [`few-shot-prompting/`](../../sub/model-usage-and-generation/sub/few-shot-prompting/l10n/uk_UA/) — prompting із невеликою кількістю прикладів бажаної поведінки.
- [`sampling-parameters/`](../../sub/model-usage-and-generation/sub/sampling-parameters/l10n/uk_UA/) — параметри на кшталт temperature, top-p, top-k і seed, що впливають на вибір токенів.
- [`reasoning-models/`](../../sub/model-usage-and-generation/sub/reasoning-models/l10n/uk_UA/) — моделі, оптимізовані витрачати додаткові обчислення на багатоетапне розв’язання задач.
- [`model-capabilities-and-limitations/`](../../sub/model-usage-and-generation/sub/model-capabilities-and-limitations/l10n/uk_UA/) — практичні сильні сторони, межі й режими відмови конкретної моделі або розгортання.

### Спеціалізовані

- [`constrained-generation/`](../../sub/model-usage-and-generation/sub/constrained-generation/l10n/uk_UA/) — генерація, обмежена граматикою, схемою, набором токенів або іншим формальним обмеженням.
- [`chain-of-thought/`](../../sub/model-usage-and-generation/sub/chain-of-thought/l10n/uk_UA/) — проміжний текст міркування або внутрішні обчислення для підтримки багатоетапних відповідей.

## [Retrieval і знання](../../sub/retrieval-and-knowledge/l10n/uk_UA/)

Поняття для під’єднання моделей до зовнішньої інформації, придатних до пошуку документів і контексту, підкріпленого свідченнями.

### Основні

- [`rag/`](../../sub/retrieval-and-knowledge/sub/rag/l10n/uk_UA/) — Retrieval-Augmented Generation поєднує зовнішній retrieval із генерацією моделі.
- [`embeddings/`](../../sub/retrieval-and-knowledge/sub/embeddings/l10n/uk_UA/) — числові представлення, що розміщують семантично пов’язані елементи поруч у векторному просторі.
- [`chunking/`](../../sub/retrieval-and-knowledge/sub/chunking/l10n/uk_UA/) — поділ вихідного матеріалу на придатні до retrieval одиниці зі збереженням достатнього контексту.
- [`semantic-search/`](../../sub/retrieval-and-knowledge/sub/semantic-search/l10n/uk_UA/) — retrieval на основі значення, а не лише точних збігів слів.
- [`hybrid-search/`](../../sub/retrieval-and-knowledge/sub/hybrid-search/l10n/uk_UA/) — retrieval, що поєднує сигнали семантичного й лексичного пошуку.
- [`grounding/`](../../sub/retrieval-and-knowledge/sub/grounding/l10n/uk_UA/) — обмеження згенерованих тверджень наданими свідченнями, інструментами чи авторитетними джерелами.

### Корисні

- [`vector-search/`](../../sub/retrieval-and-knowledge/sub/vector-search/l10n/uk_UA/) — retrieval найближчих сусідів у векторах embeddings.
- [`vector-databases/`](../../sub/retrieval-and-knowledge/sub/vector-databases/l10n/uk_UA/) — системи зберігання й індексування, оптимізовані для векторів і пошуку подібності.
- [`keyword-search/`](../../sub/retrieval-and-knowledge/sub/keyword-search/l10n/uk_UA/) — лексичний retrieval за термінами, присутніми у вихідному тексті.
- [`reranking/`](../../sub/retrieval-and-knowledge/sub/reranking/l10n/uk_UA/) — модель релевантності другого етапу, що змінює порядок отриманих кандидатів.
- [`citations/`](../../sub/retrieval-and-knowledge/sub/citations/l10n/uk_UA/) — посилання, що пов’язують згенеровані твердження з підтвердними джерелами.
- [`metadata-filtering/`](../../sub/retrieval-and-knowledge/sub/metadata-filtering/l10n/uk_UA/) — обмеження retrieval за атрибутами джерела, дати, версії, tenant або політики доступу.

### Спеціалізовані

- [`bm25/`](../../sub/retrieval-and-knowledge/sub/bm25/l10n/uk_UA/) — імовірнісний метод лексичного ранжування, широко вживаний у retrieval документів.
- [`graph-rag/`](../../sub/retrieval-and-knowledge/sub/graph-rag/l10n/uk_UA/) — RAG, що використовує структури графа та зв’язки для формування контексту.
- [`knowledge-graphs/`](../../sub/retrieval-and-knowledge/sub/knowledge-graphs/l10n/uk_UA/) — структуровані представлення сутностей та їхніх зв’язків.

## [Агенти й автоматизація](../../sub/agents-and-automation/l10n/uk_UA/)

Поняття для налаштування систем ШІ, які планують, використовують інструменти, підтримують стан і виконують контрольовані дії.

### Основні

- [`ai-agents/`](../../sub/agents-and-automation/sub/ai-agents/l10n/uk_UA/) — системи ШІ, які досягають цілей завдяки рішенням моделі, інструментам, стану та ітеративним діям.
- [`agentic-workflows/`](../../sub/agents-and-automation/sub/agentic-workflows/l10n/uk_UA/) — контрольовані багатоетапні процеси, що поєднують рішення моделі з детермінованою логікою робочого процесу.
- [`tool-calling/`](../../sub/agents-and-automation/sub/tool-calling/l10n/uk_UA/) — вибір моделлю зареєстрованої зовнішньої операції та формування аргументів для її виконання.
- [`agent-state/`](../../sub/agents-and-automation/sub/agent-state/l10n/uk_UA/) — явні робочі дані, що відстежують поступ, рішення та проміжні результати.
- [`agent-memory/`](../../sub/agents-and-automation/sub/agent-memory/l10n/uk_UA/) — механізми збереження корисної інформації поза межами поточного запиту.
- [`planning/`](../../sub/agents-and-automation/sub/planning/l10n/uk_UA/) — вибір і впорядкування дій, потрібних для досягнення цілі.
- [`verification-and-reflection/`](../../sub/agents-and-automation/sub/verification-and-reflection/l10n/uk_UA/) — перевірка результатів і перегляд підходу за потреби.
- [`human-in-the-loop/`](../../sub/agents-and-automation/sub/human-in-the-loop/l10n/uk_UA/) — перевірка, схвалення або втручання людини на визначених етапах.
- [`idempotency/`](../../sub/agents-and-automation/sub/idempotency/l10n/uk_UA/) — проєктування дій так, щоб безпечне повторення не створювало дубльованих наслідків.
- [`failure-recovery/`](../../sub/agents-and-automation/sub/failure-recovery/l10n/uk_UA/) — безпечне відновлення поступу після збоїв моделі, інструмента, мережі чи робочого процесу.

### Корисні

- [`function-calling/`](../../sub/agents-and-automation/sub/function-calling/l10n/uk_UA/) — структурований інтерфейс інструментів, у якому вихід моделі визначає функцію та аргументи.
- [`model-context-protocol/`](../../sub/agents-and-automation/sub/model-context-protocol/l10n/uk_UA/) — відкритий client-server protocol для надання AI-застосункам tools, resources, prompts та пов’язаних capabilities.
- [`task-decomposition/`](../../sub/agents-and-automation/sub/task-decomposition/l10n/uk_UA/) — поділ великої задачі на менші одиниці, які можна перевірити.
- [`retries/`](../../sub/agents-and-automation/sub/retries/l10n/uk_UA/) — повторення допустимих невдалих операцій за обмеженими правилами.
- [`autonomy-levels/`](../../sub/agents-and-automation/sub/autonomy-levels/l10n/uk_UA/) — ступінь самостійності в ухваленні рішень, наданий системі ШІ.

### Спеціалізовані

- [`multi-agent-systems/`](../../sub/agents-and-automation/sub/multi-agent-systems/l10n/uk_UA/) — системи, у яких кілька агентів координуються, конкурують, перевіряють роботу або спеціалізуються.

## [Інференс і обслуговування моделей](../../sub/inference-and-serving/l10n/uk_UA/)

Поняття для локального запуску навчених моделей або надання їх як сервісів, а також розуміння використання ресурсів і продуктивності.

### Основні

- [`inference/`](../../sub/inference-and-serving/sub/inference/l10n/uk_UA/) — запуск навченої моделі для оброблення входу й створення виходу.
- [`quantization/`](../../sub/inference-and-serving/sub/quantization/l10n/uk_UA/) — зменшення числової точності для зниження вимог моделі до пам’яті й обчислень.
- [`numerical-precision/`](../../sub/inference-and-serving/sub/numerical-precision/l10n/uk_UA/) — числовий формат ваг, активацій і обчислень моделі.
- [`model-formats/`](../../sub/inference-and-serving/sub/model-formats/l10n/uk_UA/) — файлові формати й формати серіалізації для зберігання та завантаження артефактів моделі.
- [`gpu-offloading/`](../../sub/inference-and-serving/sub/gpu-offloading/l10n/uk_UA/) — перенесення вибраних обчислень або шарів моделі на GPU, коли інша робота залишається деінде.
- [`kv-cache/`](../../sub/inference-and-serving/sub/kv-cache/l10n/uk_UA/) — кешовані ключі й значення уваги, повторно використовувані під час авторегресійної генерації.
- [`latency/`](../../sub/inference-and-serving/sub/latency/l10n/uk_UA/) — час, потрібний для створення відповіді або досягнення визначеного етапу виходу.
- [`throughput/`](../../sub/inference-and-serving/sub/throughput/l10n/uk_UA/) — обсяг роботи моделі, виконаний за одиницю часу.
- [`performance-metrics/`](../../sub/inference-and-serving/sub/performance-metrics/l10n/uk_UA/) — показники часу до першого токена, токенів за секунду, затримки й використання пам’яті.

### Корисні

- [`model-serving/`](../../sub/inference-and-serving/sub/model-serving/l10n/uk_UA/) — надання інференсу через керований процес, API, чергу або сервіс середовища виконання.
- [`model-loading/`](../../sub/inference-and-serving/sub/model-loading/l10n/uk_UA/) — переміщення артефактів моделі до RAM, VRAM або керованої середовищем пам’яті для виконання.
- [`cpu-inference/`](../../sub/inference-and-serving/sub/cpu-inference/l10n/uk_UA/) — виконання обчислень моделі переважно на процесорах загального призначення.
- [`gpu-inference/`](../../sub/inference-and-serving/sub/gpu-inference/l10n/uk_UA/) — виконання обчислень моделі переважно на графічних процесорах для паралельних навантажень.
- [`context-caching/`](../../sub/inference-and-serving/sub/context-caching/l10n/uk_UA/) — повторне використання раніше обробленого контексту prompt для зменшення повторних обчислень.

### Спеціалізовані

- [`flash-attention/`](../../sub/inference-and-serving/sub/flash-attention/l10n/uk_UA/) — реалізації уваги, оптимізовані для зменшення обміну з пам’яттю й підвищення ефективності GPU.
- [`continuous-batching/`](../../sub/inference-and-serving/sub/continuous-batching/l10n/uk_UA/) — динамічне об’єднання активних inference-запитів для ефективнішого обслуговування.
- [`speculative-decoding/`](../../sub/inference-and-serving/sub/speculative-decoding/l10n/uk_UA/) — використання швидшого чернеткового процесу для пропонування токенів, які перевіряє цільова модель.

## [Навчання й адаптація](../../sub/training-and-adaptation/l10n/uk_UA/)

Поняття для навчання моделей або адаптації наявних моделей до задач, доменів, переваг та обмежень розгортання.

### Основні

- [`fine-tuning/`](../../sub/training-and-adaptation/sub/fine-tuning/l10n/uk_UA/) — продовження навчання моделі на цільових даних для зміни поведінки або продуктивності задачі.
- [`parameter-efficient-fine-tuning/`](../../sub/training-and-adaptation/sub/parameter-efficient-fine-tuning/l10n/uk_UA/) — методи адаптації, що навчають лише невелику частину параметрів моделі або додані компоненти.
- [`lora/`](../../sub/training-and-adaptation/sub/lora/l10n/uk_UA/) — Low-Rank Adaptation навчає компактні низькорангові оновлення замість усіх ваг базової моделі.
- [`qlora/`](../../sub/training-and-adaptation/sub/qlora/l10n/uk_UA/) — адаптація на основі LoRA з квантованою базовою моделлю для зменшення використання пам’яті.

### Корисні

- [`supervised-fine-tuning/`](../../sub/training-and-adaptation/sub/supervised-fine-tuning/l10n/uk_UA/) — fine-tuning на розмічених прикладах, які поєднують inputs із бажаними outputs.
- [`adapters/`](../../sub/training-and-adaptation/sub/adapters/l10n/uk_UA/) — невеликі навчувані модулі, приєднані до базової моделі для повторно використовуваної спеціалізації.
- [`instruction-tuning/`](../../sub/training-and-adaptation/sub/instruction-tuning/l10n/uk_UA/) — навчання моделі на прикладах «інструкція — відповідь» для кращого виконання задач.
- [`synthetic-data/`](../../sub/training-and-adaptation/sub/synthetic-data/l10n/uk_UA/) — дані навчання або оцінювання, згенеровані правилами, симуляціями чи моделями.
- [`datasets/`](../../sub/training-and-adaptation/sub/datasets/l10n/uk_UA/) — організовані колекції прикладів для навчання, адаптації або оцінювання.
- [`overfitting/`](../../sub/training-and-adaptation/sub/overfitting/l10n/uk_UA/) — ситуація, коли модель надто точно підлаштовується під навчальні дані й погано працює на нових прикладах.

### Спеціалізовані

- [`pretraining/`](../../sub/training-and-adaptation/sub/pretraining/l10n/uk_UA/) — масштабне початкове навчання, що створює базову модель із широкими можливостями.
- [`preference-optimization/`](../../sub/training-and-adaptation/sub/preference-optimization/l10n/uk_UA/) — методи навчання, які віддають перевагу відповідям, оціненим як кращі за даними про переваги.
- [`rlhf/`](../../sub/training-and-adaptation/sub/rlhf/l10n/uk_UA/) — Reinforcement Learning from Human Feedback використовує сигнали людських переваг для зміни поведінки моделі.
- [`dpo/`](../../sub/training-and-adaptation/sub/dpo/l10n/uk_UA/) — Direct Preference Optimization навчає безпосередньо на парах бажаних і відхилених відповідей.
- [`distillation/`](../../sub/training-and-adaptation/sub/distillation/l10n/uk_UA/) — навчання меншої чи простішої моделі імітувати потужнішу модель-учителя.
- [`pruning/`](../../sub/training-and-adaptation/sub/pruning/l10n/uk_UA/) — вилучення параметрів або структур моделі, які вважають непотрібними для цільової мети.

## [Мультимодальні й генеративні медіа](../../sub/multimodal-and-generative-media/l10n/uk_UA/)

Поняття для моделей і робочих процесів із зображеннями, аудіо, відео та поєднаннями модальностей.

### Основні

- [`vision-language-models/`](../../sub/multimodal-and-generative-media/sub/vision-language-models/l10n/uk_UA/) — моделі, що спільно обробляють візуальні входи й природну мову.
- [`image-generation/`](../../sub/multimodal-and-generative-media/sub/image-generation/l10n/uk_UA/) — створення зображень із тексту, зображень, макетів, масок чи інших умов.
- [`diffusion-models/`](../../sub/multimodal-and-generative-media/sub/diffusion-models/l10n/uk_UA/) — генеративні моделі, які навчаються обертати поступове додавання шуму.
- [`image-to-image/`](../../sub/multimodal-and-generative-media/sub/image-to-image/l10n/uk_UA/) — генерація перетвореного зображення з урахуванням наявного.
- [`inpainting/`](../../sub/multimodal-and-generative-media/sub/inpainting/l10n/uk_UA/) — повторна генерація вибраних замаскованих ділянок зображення.
- [`controlnet/`](../../sub/multimodal-and-generative-media/sub/controlnet/l10n/uk_UA/) — зумовлення diffusion-моделей структурними засобами: краями, глибиною чи позою.
- [`multimodal-context/`](../../sub/multimodal-and-generative-media/sub/multimodal-context/l10n/uk_UA/) — сукупна текстова, візуальна, аудіо-, відео- чи документна інформація в запиті моделі.

### Корисні

- [`text-to-image/`](../../sub/multimodal-and-generative-media/sub/text-to-image/l10n/uk_UA/) — генерація зображень з описів природною мовою.
- [`outpainting/`](../../sub/multimodal-and-generative-media/sub/outpainting/l10n/uk_UA/) — розширення зображення за його початкові межі.
- [`image-embeddings/`](../../sub/multimodal-and-generative-media/sub/image-embeddings/l10n/uk_UA/) — векторні подання для порівняння, пошуку чи класифікації візуального вмісту.
- [`speech-to-text/`](../../sub/multimodal-and-generative-media/sub/speech-to-text/l10n/uk_UA/) — перетворення усного мовлення на письмовий текст.
- [`text-to-speech/`](../../sub/multimodal-and-generative-media/sub/text-to-speech/l10n/uk_UA/) — синтез усного мовлення з письмового тексту.
- [`video-generation/`](../../sub/multimodal-and-generative-media/sub/video-generation/l10n/uk_UA/) — створення або перетворення послідовностей відеокадрів генеративними моделями.

### Спеціалізовані

- [`latent-space/`](../../sub/multimodal-and-generative-media/sub/latent-space/l10n/uk_UA/) — стиснене навчене подання, у якому генеративні моделі кодують і змінюють інформацію.
- [`audio-generation/`](../../sub/multimodal-and-generative-media/sub/audio-generation/l10n/uk_UA/) — створення музики, мовлення, звукових ефектів чи іншого аудіо генеративними моделями.

## [Безпека, приватність і надійність](../../sub/safety-privacy-and-reliability/l10n/uk_UA/)

Поняття для керування поведінкою моделей, захисту даних і зменшення операційних ризиків систем ШІ.

### Основні

- [`prompt-injection/`](../../sub/safety-privacy-and-reliability/sub/prompt-injection/l10n/uk_UA/) — вхід, створений для перевизначення чи маніпулювання інструкціями системи ШІ.
- [`indirect-prompt-injection/`](../../sub/safety-privacy-and-reliability/sub/indirect-prompt-injection/l10n/uk_UA/) — шкідливі або суперечливі інструкції в зовнішньому вмісті, який обробляє система ШІ.
- [`trust-boundaries/`](../../sub/safety-privacy-and-reliability/sub/trust-boundaries/l10n/uk_UA/) — явне розділення довірених інструкцій, систем, користувачів і недовірених даних.
- [`least-privilege/`](../../sub/safety-privacy-and-reliability/sub/least-privilege/l10n/uk_UA/) — надання системі ШІ лише дозволів, потрібних для поточної задачі.
- [`sandboxing/`](../../sub/safety-privacy-and-reliability/sub/sandboxing/l10n/uk_UA/) — ізоляція виконання для обмеження наслідків збоїв або шкідливої поведінки.
- [`secret-handling/`](../../sub/safety-privacy-and-reliability/sub/secret-handling/l10n/uk_UA/) — захист облікових даних, токенів, ключів та інших чутливих операційних даних.
- [`data-privacy/`](../../sub/safety-privacy-and-reliability/sub/data-privacy/l10n/uk_UA/) — контроль збирання, оброблення, зберігання й передавання особистих, конфіденційних або чутливих даних.
- [`retrieval-poisoning/`](../../sub/safety-privacy-and-reliability/sub/retrieval-poisoning/l10n/uk_UA/) — маніпулювання індексованими знаннями, щоб retrieval надавав оманливий або шкідливий контекст.

### Корисні

- [`guardrails/`](../../sub/safety-privacy-and-reliability/sub/guardrails/l10n/uk_UA/) — засоби перевірки, обмеження й моніторингу входів, виходів і дій моделі.
- [`data-residency/`](../../sub/safety-privacy-and-reliability/sub/data-residency/l10n/uk_UA/) — географічне або юрисдикційне місце зберігання чи оброблення даних.
- [`provenance/`](../../sub/safety-privacy-and-reliability/sub/provenance/l10n/uk_UA/) — відомості про походження, власність, перетворення й зберігання даних або артефактів моделі.
- [`content-moderation/`](../../sub/safety-privacy-and-reliability/sub/content-moderation/l10n/uk_UA/) — виявлення чи обмеження вмісту за політиками безпеки, права або платформи.

### Спеціалізовані

- [`jailbreaking/`](../../sub/safety-privacy-and-reliability/sub/jailbreaking/l10n/uk_UA/) — спроби обійти налаштовані обмеження безпеки або політик моделі.
- [`model-alignment/`](../../sub/safety-privacy-and-reliability/sub/model-alignment/l10n/uk_UA/) — спрямування поведінки моделі до визначених цілей, цінностей, політик або переваг.
- [`data-poisoning/`](../../sub/safety-privacy-and-reliability/sub/data-poisoning/l10n/uk_UA/) — псування даних навчання або адаптації для погіршення чи маніпулювання поведінкою моделі.

## [Оцінювання та експлуатація](../../sub/evaluation-and-operations/l10n/uk_UA/)

Поняття для вибору, тестування, спостереження й експлуатації систем ШІ за реальних обмежень якості, вартості та надійності.

### Основні

- [`evals/`](../../sub/evaluation-and-operations/sub/evals/l10n/uk_UA/) — повторювані тести відповідності моделі чи системи ШІ визначеним вимогам.
- [`model-selection/`](../../sub/evaluation-and-operations/sub/model-selection/l10n/uk_UA/) — вибір моделі за якістю задачі, можливостями, вартістю, затримкою, безпекою й обмеженнями розгортання.
- [`model-routing/`](../../sub/evaluation-and-operations/sub/model-routing/l10n/uk_UA/) — динамічний вибір моделі відповідно до запиту чи операційної політики.
- [`observability/`](../../sub/evaluation-and-operations/sub/observability/l10n/uk_UA/) — використання logs, metrics, traces і events для розуміння поведінки системи ШІ.
- [`tracing/`](../../sub/evaluation-and-operations/sub/tracing/l10n/uk_UA/) — запис послідовності операцій моделі, інструментів, retrieval і workflow для одного виконання.
- [`cost-management/`](../../sub/evaluation-and-operations/sub/cost-management/l10n/uk_UA/) — вимірювання й контроль витрат на моделі, інфраструктуру, сховища та інструменти.
- [`latency-and-throughput/`](../../sub/evaluation-and-operations/sub/latency-and-throughput/l10n/uk_UA/) — балансування часу відповіді й обсягу роботи за одиницю часу.
- [`quality-cost-tradeoffs/`](../../sub/evaluation-and-operations/sub/quality-cost-tradeoffs/l10n/uk_UA/) — вибір прийнятного балансу між якістю результату й операційними витратами.

### Корисні

- [`benchmarks/`](../../sub/evaluation-and-operations/sub/benchmarks/l10n/uk_UA/) — стандартизовані задачі чи datasets для порівняння моделей або систем.
- [`evaluation-datasets/`](../../sub/evaluation-and-operations/sub/evaluation-datasets/l10n/uk_UA/) — добірки прикладів для тестування якості, безпеки, retrieval або виконання задач.
- [`human-evaluation/`](../../sub/evaluation-and-operations/sub/human-evaluation/l10n/uk_UA/) — оцінювання результатів моделі людьми за явними критеріями.
- [`fallback-models/`](../../sub/evaluation-and-operations/sub/fallback-models/l10n/uk_UA/) — альтернативні моделі, коли бажана модель не працює, недоступна або перевищує межі політики.
- [`caching/`](../../sub/evaluation-and-operations/sub/caching/l10n/uk_UA/) — повторне використання попередніх результатів чи оброблених даних для зменшення повторної роботи.
- [`rate-limits/`](../../sub/evaluation-and-operations/sub/rate-limits/l10n/uk_UA/) — controls, що обмежують обсяг запитів за певний час.

### Спеціалізовані

- [`llm-as-a-judge/`](../../sub/evaluation-and-operations/sub/llm-as-a-judge/l10n/uk_UA/) — використання мовної моделі для оцінювання, ранжування чи критики результатів інших моделей.
- [`retrieval-evaluation/`](../../sub/evaluation-and-operations/sub/retrieval-evaluation/l10n/uk_UA/) — вимірювання того, чи повертає retrieval релевантні, повні й правильно ранжовані свідчення.
- [`reproducibility/`](../../sub/evaluation-and-operations/sub/reproducibility/l10n/uk_UA/) — можливість повторити оцінювання чи workflow за порівнюваних умов і результатів.
