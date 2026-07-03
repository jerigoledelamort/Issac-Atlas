# Research Log: The Binding of Isaac: Repentance

## Метаданные журнала

| Поле | Значение |
|------|----------|
| Статус | 🟡 Активен |
| Дата начала | *не указана* |
| Исследователь | *не указан* |
| Версия игры | *не указана* |

---

## Журнал исследования

| ID | Date | Object | Status | Description | Evidence |
|----|------|--------|--------|-------------|----------|
| 0001 | | Project | 🟢 Confirmed | Создан проект Ghidra | Ghidra project |
| 0002 | | Binary | 🟢 Confirmed | Импортирован isaac-ng.exe | Ghidra import |
| 0003 | | Binary | 🟢 Confirmed | Подтверждён формат PE | PE header analysis |
| 0004 | | Binary | 🟢 Confirmed | Подтверждена архитектура x86 | Ghidra analysis |
| 0005 | | Binary | 🟢 Confirmed | Получены параметры бинарника | PE header fields |
| 0006 | | Analysis | 🟢 Confirmed | Запущен Auto Analysis | Ghidra Auto Analysis |
| 0007 | | Analysis | 🟢 Confirmed | Выполнен полный Auto Analysis | Ghidra Auto Analysis completed |
| 0008 | | Binary | 🟢 Confirmed | Получен Binary Passport | PE header fields |
| 0009 | | Binary | 🟢 Confirmed | Автоматически обнаружено 20918 функций | Ghidra function list |
| 0010 | | Strings | 🟢 Confirmed | Обнаружено 16097 строк | Ghidra strings table |
| 0011 | | PDB | 🟢 Confirmed | PDB отсутствует (ссылка: isaac-ng_Submission.pdb) | PE debug directory |
| 0012 | | Namespaces | 🟢 Confirmed | Восстановлены namespaces: IsaacRepentancePlus, KAGE, luabridge, png, theoraplayer | Ghidra namespace analysis |
| 0013 | | Resources | 🟢 Confirmed | Подтверждены пути: resources/, resources/scripts/, resources/packed/ | String references |
| 0014 | | Resources | 🟢 Confirmed | Подтверждены packed-архивы: config.a, fonts.a, graphics.a, music.a, sfx.a, videos.a, animations.a | String references |
| 0015 | | XML | 🟢 Confirmed | Подтверждены XML-конфигурации: players.xml, items.xml, pocketitems.xml, preload.xml, ambush.xml, bossoverlays.xml, giantbook.xml | String references |
| 0016 | | Internal Strings | 🟢 Confirmed | Обнаружены: Binding of Isaac: Repentance+, IsaacIndicator, IconIsaacsRoom, ISAACNG_GSR, ISAACNG_SAVE04 | String table |
| 0017 | | XREF Analysis | 🟢 Confirmed | players.xml имеет 3 XREF. Функция FUN_006f3c00 занимается подготовкой XML-данных | Ghidra XREF analysis |
| 0018 | | Function | 🟢 Confirmed | FUN_006f3c00: выделение памяти, создание структур, копирование "players.xml", подготовка параметров парсинга | Ghidra decompiler |
| 0019 | | Entry Point | 🟢 Confirmed | entry → FUN_00cfe315 → FUN_00cfe390. FUN_00cfe390 выполняет инициализацию CRT, не содержит игровой логики | Ghidra call graph |
| 0020 | | x64dbg | 🟢 Confirmed | Подтверждены этапы запуска: Windows → ntdll.dll → TLS Callback → kernel32 → gdi32full → isaac-ng.exe | x64dbg session |
| 0021 | | Steam Integration | 🟢 Confirmed | Steam блокирует выполнение под отладчиком (Application load error T:0000065432) | x64dbg session |
| 0022 | | Lua VM | 🟢 Confirmed | FUN_008604C0 — главная функция инициализации Lua VM | Ghidra decompiler |
| 0023 | | Lua VM | 🟢 Confirmed | FUN_008604C0: создаёт Lua State, подключает стандартные библиотеки, регистрирует типы | Ghidra decompiler |
| 0024 | | Lua API | 🟢 Confirmed | FUN_00866960 — центральный реестр Lua API | Ghidra decompiler |
| 0025 | | Lua API | 🟢 Confirmed | FUN_00866960: создаёт userdata, metatable, регистрирует классы и методы | Ghidra decompiler |
| 0026 | | Lua Scripts | 🟢 Confirmed | FUN_0086E5E0 загружает enums.lua и main.lua | Ghidra decompiler |
| 0027 | | Lua Callbacks | 🟢 Confirmed | _RunCallback и _UnloadMod извлекаются через luaL_ref() и сохраняются | Ghidra decompiler |
| 0028 | | Lua Cleanup | 🟢 Confirmed | Глобальные переменные удаляются после инициализации (lua_pushnil + lua_setglobal) | Ghidra decompiler |
| 0029 | | Lua Classes | 🟢 Confirmed | Зарегистрированы классы: Entity, EntityPlayer, EntityNPC, EntityTear, Sprite, Vector, Color, KColor, EntityRef, ProjectileParams, ItemConfig, PathFinder, Random, BitSet128 | Ghidra decompiler |
| 0030 | | Lua API Mapping | 🟢 Confirmed | AddCoins → FUN_00759400, FireTear → FUN_00790AF0, AddCollectible → FUN_0075F0E0, FireBomb → FUN_007A0970 | Ghidra string references |
| 0031 | | Lua Register | 🟢 Confirmed | FUN_00876530 — RegisterClass (вызывает FUN_008a6d90) | Ghidra decompiler |
| 0032 | | Lua Register | 🟢 Confirmed | FUN_008a6d90 — создаёт Lua userdata/метатаблицу | Ghidra decompiler |
| 0033 | | Lua Register | 🟢 Confirmed | FUN_00876650/670/6b0/710/770 — семейство функций RegisterMethod | Ghidra decompiler |
| 0034 | | Lua RNG Class | 🟢 Confirmed | Класс RNG: GetSeed, SetSeed, RandomInt, RandomFloat | Ghidra string references |
| 0035 | | Lua ProjectileParams | 🟢 Confirmed | Класс ProjectileParams: Acceleration, Spread, HomingStrength, CurvingStrength | Ghidra string references |
| 0036 | | Lua Architecture | 🟢 Confirmed | API строится последовательными вызовами RegisterClass → RegisterMethod внутри FUN_00866960 | Ghidra decompiler |
| 0037 | | Environment | 🟢 Confirmed | Ghidra 12.1.2 установлена и настроена | Ghidra installation |
| 0038 | | RNG String | 🟢 Confirmed | Строка "RNG" подтверждена по адресу DAT_00b70764 | Ghidra data reference |
| 0039 | | ProjectileParams | 🟢 Confirmed | Класс ProjectileParams: HeightModifier и другие параметры | Ghidra string references |
| 0040 | | SSA Analysis | 🔴 Rejected | SSA-анализ через HighFunction/Pcode отклонён: слишком сложный, нестабильный API | Research evaluation |
| 0041 | | CALL Analysis | 🟢 Confirmed | Многие вызовы косвенные (CALL ESI/EDI), простой линейный обход недостаточен | Ghidra instruction analysis |
| 0042 | | GhidraScript | 🟢 Confirmed | Создан Java Ghidra Script ExtractLuaAPI.java | Script compilation successful |
| 0043 | | Architecture | 🟢 Confirmed | Централизованная регистрация Lua API — возможна автоматизация восстановления | FUN_00866960 analysis |
| 0044 | | | 🟡 Hypothesis | | |
| 0045 | | | 🟡 Hypothesis | | |
| 0046 | | `FUN_009eb6b0` | 🟢 Confirmed | Это НЕ RNG. Функция занимается исключительно декодированием пользовательского seed в `uint32`. Не использует LCG, не имеет внутреннего состояния генератора. | Ghidra decompiler, call graph analysis |
| 0047 | | `FUN_009eb6b0` | 🟢 Confirmed | Формат пользовательского seed: строка 9 символов `XXXX XXXX X` (4 символа + пробел + 4 символа + 1 checksum). Пробел на позиции 4. | Ghidra string validation code |
| 0048 | | `FUN_009eb6b0` | 🟢 Confirmed | Алфавит seed: `ABCDEFGHJKLMNPQRSTWXYZ01234V6789` (32 символа, Base32-подобный). Исключены неоднозначные символы: I, O, U, W, 5, 1, 2, 6, 8. | Ghidra lookup table construction |
| 0049 | | `FUN_009eb6b0` | 🟢 Confirmed | Lookup table размером 256 байт. Допустимые символы → 0..31, недопустимые → 0xFF. O(1) декодирование. | Ghidra decompiler |
| 0050 | | `FUN_009eb6b0` | 🟢 Confirmed | Bit packing: 8 символов × 5 бит, последовательная упаковка `((((a<<5)|b)<<5|c)...`. Итог: 32-битное значение. | Ghidra decompiler |
| 0051 | | `FUN_009eb6b0` | 🟢 Confirmed | XOR-константа: `0x0FEF7FFD`. Первая подтверждённая константа преобразования seed. | Ghidra decompiler |
| 0052 | | `FUN_009eb6b0` | 🟢 Confirmed | Checksum: 9-й символ не входит в значение, используется для проверки. Вычисляется из первых 8 символов, сравнивается с декодированным 9-м. При несовпадении — ошибка. | Ghidra decompiler, comparison logic |
| 0053 | | `FUN_009eb6b0` | 🟢 Confirmed | Возвращаемое значение: `uint32`. Это внутренний seed для системы RNG. Подтверждено разделение: String Seed → Decode → Internal Seed → RNG. | Ghidra return type analysis |
| 0054 | | Seed Pipeline | 🟡 High Probability | Следующая стадия (RNG initialization после получения `uint32`) пока НЕ найдена. Требуется дальнейший поиск. | Call graph from FUN_009eb6b0 |
| 0055 | | `FUN_009eb880` | 🟢 Confirmed | Инициализация RNG. Принимает готовый uint32 seed. Устанавливает initialized flag, текущее значение seed и три параметра сдвига. НЕ создает новый сид. | Ghidra decompiler, struct analysis |
| 0056 | | RNG Structure | 🟢 Confirmed | Структура RNG содержит: initialized flag, текущее значение seed, три параметра сдвига (shift values). | Ghidra struct analysis |
| 0057 | | `FUN_006ef890` | 🟢 Confirmed | Шаг RNG. Проверяет инициализацию и seed != 0. Обновляет seed по алгоритму XORSHIFT (Marsaglia): x ^= x >> a; x ^= x << b; x ^= x >> c. Не генерирует первоначальный сид. | Ghidra decompiler, algorithm analysis |
| 0058 | | RNG Algorithm | 🟢 Confirmed | Подтверждён алгоритм XORSHIFT (George Marsaglia). FUN_006ef890 вычисляет только следующее состояние генератора, требует предварительной инициализации. | Ghidra decompiler |
| 0059 | | RNG Pipeline | 🟢 Confirmed | Полная цепочка: uint32 StartSeed → FUN_009eb880(seed) → инициализация структуры RNG → FUN_006ef890() → следующее псевдослучайное значение. | Combined analysis |
| 0060 | `FUN_009e9430` | | 🟢 Confirmed | Функция копирования структуры (CopyFrom / operator=). К RNG и генерации сидов отношения практически не имеет. | Ghidra decompiler |
| 0061 | `FUN_00958cb0` | | 🟢 Confirmed | Не генерирует сид. Передает существующее значение в FUN_009eb880. Предположительно используется при загрузке сохранения, Continue, Daily Run, Challenge. | Ghidra call graph analysis |
| 0062 | `FUN_006f72f0` | | 🟢 Confirmed | Очищает состояние предыдущего ранa, вызывает FUN_006ef890() и FUN_009eb880(...). Один из ключевых этапов начала нового забега. Источник StartSeed внутри функции не найден. | Ghidra decompiler, call graph |
| 0063 | | StartSeed Source | 🔴 Not Found | Источник первоначального uint32 StartSeed при создании нового забега не найден. Текущая основная задача исследования. | Ongoing research |

---

## Статусы

| Статус | Значок | Описание |
|--------|--------|----------|
| Confirmed | 🟢 | Подтверждено данными из дизассемблера/декомпилятора |
| Hypothesis | 🟡 | Требует дополнительной проверки |
| Rejected | 🔴 | Опровергнуто данными |

---

## Шаблоны записей

### Для функций

```markdown
| ID | Date | Object | Status | Description | Evidence |
|----|------|--------|--------|-------------|----------|
| 00XX | YYYY-MM-DD | `sub_XXXXXX` | 🟡 | Предположительно инициализация RNG | Ссылка на псевдокод в research/pseudocode/ |
```

### Для структур данных

```markdown
| ID | Date | Object | Status | Description | Evidence |
|----|------|--------|--------|-------------|----------|
| 00XX | YYYY-MM-DD | `struct_XXXXXX` | 🟡 | Предположительно состояние этажа | Ссылка на экспорт в research/exports/ |
```

### для строк

```markdown
| ID | Date | Object | Status | Description | Evidence |
|----|------|--------|--------|-------------|----------|
| 00XX | YYYY-MM-DD | `str_XXXXXX` | 🟢 | Путь к файлу ресурсов | Адрес: 0xXXXXXX, контекст: вызов File::Open |
```

---

## Ссылки

- [project_map.md](project_map.md) — карта проекта
- [research/README.md](../research/README.md) — структура исследований
- [research/version.md](../research/version.md) — версия игры

---

## История изменений

| Дата | Автор | Изменения |
|------|-------|-----------|
| | | Initial research log |
| | | Added Binary Passport entries (0001-0011) |
| | | Added Lua VM and API entries (0022-0036) |
| | | Added Environment, RNG String, ProjectileParams, SSA Analysis, CALL Analysis, GhidraScript entries (0037-0043) |
| | | Added Seed Decoder entries (0046-0053) |
| | | Added RNG Architecture entries: FUN_009eb880, FUN_006ef890, RNG Structure, XORSHIFT algorithm, full pipeline, related functions (0055-0063) |
