# Research Log: The Binding of Isaac: Repentance

## Метаданные журнала

| Поле | Значение |
|------|----------|
| Статус | 🟡 Активен |
| Дата начала | 06.07.2026 |
| Исследователь | *не указан* |
| Версия игры | v1.9.7.17 |
| Дата обновления | 06.07.2026 |

---

## Журнал исследования

| ID | Date | Object | Status | Description | Evidence |
|----|------|--------|--------|-------------|----------|
| 0001 | 06.07.2026 | Project | 🟢 Confirmed | Создан проект Ghidra | Ghidra project |
| 0002 | 06.07.2026 | Binary | 🟢 Confirmed | Импортирован isaac-ng.exe | Ghidra import |
| 0003 | 06.07.2026 | Binary | 🟢 Confirmed | Подтверждён формат PE | PE header analysis |
| 0004 | 06.07.2026 | Binary | 🟢 Confirmed | Подтверждена архитектура x86 | Ghidra analysis |
| 0005 | 06.07.2026 | Binary | 🟢 Confirmed | Получены параметры бинарника | PE header fields |
| 0006 | 06.07.2026 | Analysis | 🟢 Confirmed | Запущен Auto Analysis | Ghidra Auto Analysis |
| 0007 | 06.07.2026 | Analysis | 🟢 Confirmed | Выполнен полный Auto Analysis | Ghidra Auto Analysis completed |
| 0008 | 06.07.2026 | Binary | 🟢 Confirmed | Получен Binary Passport | PE header fields |
| 0009 | 06.07.2026 | Binary | 🟢 Confirmed | Автоматически обнаружено 20918 функций | Ghidra function list |
| 0010 | 06.07.2026 | Strings | 🟢 Confirmed | Обнаружено 16097 строк | Ghidra strings table |
| 0011 | 06.07.2026 | PDB | 🟢 Confirmed | PDB отсутствует (ссылка: isaac-ng_Submission.pdb) | PE debug directory |
| 0012 | 06.07.2026 | Namespaces | 🟢 Confirmed | Восстановлены namespaces: IsaacRepentancePlus, KAGE, luabridge, png, theoraplayer | Ghidra namespace analysis |
| 0013 | 06.07.2026 | Resources | 🟢 Confirmed | Подтверждены пути: resources/, resources/scripts/, resources/packed/ | String references |
| 0014 | 06.07.2026 | Resources | 🟢 Confirmed | Подтверждены packed-архивы: config.a, fonts.a, graphics.a, music.a, sfx.a, videos.a, animations.a | String references |
| 0015 | 06.07.2026 | XML | 🟢 Confirmed | Подтверждены XML-конфигурации: players.xml, items.xml, pocketitems.xml, preload.xml, ambush.xml, bossoverlays.xml, giantbook.xml | String references |
| 0016 | 06.07.2026 | Internal Strings | 🟢 Confirmed | Обнаружены: Binding of Isaac: Repentance+, IsaacIndicator, IconIsaacsRoom, ISAACNG_GSR, ISAACNG_SAVE04 | String table |
| 0017 | 06.07.2026 | XREF Analysis | 🟢 Confirmed | players.xml имеет 3 XREF. Функция FUN_006f3c00 занимается подготовкой XML-данных | Ghidra XREF analysis |
| 0018 | 06.07.2026 | Function | 🟢 Confirmed | FUN_006f3c00: выделение памяти, создание структур, копирование "players.xml", подготовка параметров парсинга | Ghidra decompiler |
| 0019 | 06.07.2026 | Entry Point | 🟢 Confirmed | entry → FUN_00cfe315 → FUN_00cfe390. FUN_00cfe390 выполняет инициализацию CRT, не содержит игровой логики | Ghidra call graph |
| 0020 | 06.07.2026 | x64dbg | 🟢 Confirmed | Подтверждены этапы запуска: Windows → ntdll.dll → TLS Callback → kernel32 → gdi32full → isaac-ng.exe | x64dbg session |
| 0021 | 06.07.2026 | Steam Integration | 🟢 Confirmed | Steam блокирует выполнение под отладчиком (Application load error T:0000065432) | x64dbg session |
| 0022 | 06.07.2026 | Lua VM | 🟢 Confirmed | FUN_008604C0 — главная функция инициализации Lua VM | Ghidra decompiler |
| 0023 | 06.07.2026 | Lua VM | 🟢 Confirmed | FUN_008604C0: создаёт Lua State, подключает стандартные библиотеки, регистрирует типы | Ghidra decompiler |
| 0024 | 06.07.2026 | Lua API | 🟢 Confirmed | FUN_00866960 — центральный реестр Lua API | Ghidra decompiler |
| 0025 | 06.07.2026 | Lua API | 🟢 Confirmed | FUN_00866960: создаёт userdata, metatable, регистрирует классы и методы | Ghidra decompiler |
| 0026 | 06.07.2026 | Lua Scripts | 🟢 Confirmed | FUN_0086E5E0 загружает enums.lua и main.lua | Ghidra decompiler |
| 0027 | 06.07.2026 | Lua Callbacks | 🟢 Confirmed | _RunCallback и _UnloadMod извлекаются через luaL_ref() и сохраняются | Ghidra decompiler |
| 0028 | 06.07.2026 | Lua Cleanup | 🟢 Confirmed | Глобальные переменные удаляются после инициализации (lua_pushnil + lua_setglobal) | Ghidra decompiler |
| 0029 | 06.07.2026 | Lua Classes | 🟢 Confirmed | Зарегистрированы классы: Entity, EntityPlayer, EntityNPC, EntityTear, Sprite, Vector, Color, KColor, EntityRef, ProjectileParams, ItemConfig, PathFinder, Random, BitSet128 | Ghidra decompiler |
| 0030 | 06.07.2026 | Lua API Mapping | 🟢 Confirmed | AddCoins → FUN_00759400, FireTear → FUN_00790AF0, AddCollectible → FUN_0075F0E0, FireBomb → FUN_007A0970 | Ghidra string references |
| 0031 | 06.07.2026 | Lua Register | 🟢 Confirmed | FUN_00876530 — RegisterClass (вызывает FUN_008a6d90) | Ghidra decompiler |
| 0032 | 06.07.2026 | Lua Register | 🟢 Confirmed | FUN_008a6d90 — создаёт Lua userdata/метатаблицу | Ghidra decompiler |
| 0033 | 06.07.2026 | Lua Register | 🟢 Confirmed | FUN_00876650/670/6b0/710/770 — семейство функций RegisterMethod | Ghidra decompiler |
| 0034 | 06.07.2026 | Lua RNG Class | 🟢 Confirmed | Класс RNG: GetSeed, SetSeed, RandomInt, RandomFloat | Ghidra string references |
| 0035 | 06.07.2026 | Lua ProjectileParams | 🟢 Confirmed | Класс ProjectileParams: Acceleration, Spread, HomingStrength, CurvingStrength | Ghidra string references |
| 0036 | 06.07.2026 | Lua Architecture | 🟢 Confirmed | API строится последовательными вызовами RegisterClass → RegisterMethod внутри FUN_00866960 | Ghidra decompiler |
| 0037 | 06.07.2026 | Environment | 🟢 Confirmed | Ghidra 12.1.2 установлена и настроена | Ghidra installation |
| 0038 | 06.07.2026 | RNG String | 🟢 Confirmed | Строка "RNG" подтверждена по адресу DAT_00b70764 | Ghidra data reference |
| 0039 | 06.07.2026 | ProjectileParams | 🟢 Confirmed | Класс ProjectileParams: HeightModifier и другие параметры | Ghidra string references |
| 0040 | 06.07.2026 | SSA Analysis | 🔴 Rejected | SSA-анализ через HighFunction/Pcode отклонён: слишком сложный, нестабильный API | Research evaluation |
| 0041 | 06.07.2026 | CALL Analysis | 🟢 Confirmed | Многие вызовы косвенные (CALL ESI/EDI), простой линейный обход недостаточен | Ghidra instruction analysis |
| 0042 | 06.07.2026 | GhidraScript | 🟢 Confirmed | Создан Java Ghidra Script ExtractLuaAPI.java | Script compilation successful |
| 0043 | 06.07.2026 | Architecture | 🟢 Confirmed | Централизованная регистрация Lua API — возможна автоматизация восстановления | FUN_00866960 analysis |
| 0044 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Это НЕ RNG. Функция занимается исключительно декодированием пользовательского seed в `uint32`. Не использует LCG, не имеет внутреннего состояния генератора. | Ghidra decompiler, call graph analysis |
| 0045 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Формат пользовательского seed: строка 9 символов `XXXX XXXX X` (4 символа + пробел + 4 символа + 1 checksum). Пробел на позиции 4. | Ghidra string validation code |
| 0046 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Алфавит seed: `ABCDEFGHJKLMNPQRSTWXYZ01234V6789` (32 символа, Base32-подобный). Исключены неоднозначные символы: I, O, U, W, 5, 1, 2, 6, 8. | Ghidra lookup table construction |
| 0047 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Lookup table размером 256 байт. Допустимые символы → 0..31, недопустимые → 0xFF. O(1) декодирование. | Ghidra decompiler |
| 0048 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Bit packing: 8 символов × 5 бит, последовательная упаковка `((((a<<5)|b)<<5|c)...`. Итог: 32-битное значение. | Ghidra decompiler |
| 0049 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | XOR-константа: `0x0FEF7FFD`. Первая подтверждённая константа преобразования seed. | Ghidra decompiler |
| 0050 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Checksum: 9-й символ не входит в значение, используется для проверки. Вычисляется из первых 8 символов, сравнивается с декодированным 9-м. При несовпадении — ошибка. | Ghidra decompiler, comparison logic |
| 0051 | 06.07.2026 | `FUN_009eb6b0` | 🟢 Confirmed | Возвращаемое значение: `uint32`. Это внутренний seed для системы RNG. Подтверждено разделение: String Seed → Decode → Internal Seed → RNG. | Ghidra return type analysis |
| 0052 | 06.07.2026 | Seed Pipeline | 🟡 High Probability | Следующая стадия (RNG initialization после получения `uint32`) пока НЕ найдена. Требуется дальнейший поиск. | Call graph from FUN_009eb6b0 |
| 0053 | 06.07.2026 | `FUN_009eb880` | 🟢 Confirmed | Инициализация RNG. Принимает готовый uint32 seed. Устанавливает initialized flag, текущее значение seed и три параметра сдвига. НЕ создает новый сид. | Ghidra decompiler, struct analysis |
| 0054 | 06.07.2026 | RNG Structure | 🟢 Confirmed | Структура RNG содержит: initialized flag, текущее значение seed, три параметра сдвига (shift values). | Ghidra struct analysis |
| 0055 | 06.07.2026 | `FUN_006ef890` | 🟢 Confirmed | Шаг RNG. Проверяет инициализацию и seed != 0. Обновляет seed по алгоритму XORSHIFT (Marsaglia): x ^= x >> a; x ^= x << b; x ^= x >> c. Не генерирует первоначальный сид. | Ghidra decompiler, algorithm analysis |
| 0056 | 06.07.2026 | RNG Algorithm | 🟢 Confirmed | Подтверждён алгоритм XORSHIFT (George Marsaglia). FUN_006ef890 вычисляет только следующее состояние генератора, требует предварительной инициализации. | Ghidra decompiler |
| 0057 | 06.07.2026 | RNG Pipeline | 🟢 Confirmed | Полная цепочка: uint32 StartSeed → FUN_009eb880(seed) → инициализация структуры RNG → FUN_006ef890() → следующее псевдослучайное значение. | Combined analysis |
| 0058 | 06.07.2026 | `FUN_009e9430` | 🟢 Confirmed | Функция копирования структуры (CopyFrom / operator=). К RNG и генерации сидов отношения практически не имеет. | Ghidra decompiler |
| 0059 | 06.07.2026 | `FUN_00958cb0` | 🟢 Confirmed | Не генерирует сид. Передает существующее значение в FUN_009eb880. Предположительно используется при загрузке сохранения, Continue, Daily Run, Challenge. | Ghidra call graph analysis |
| 0060 | 06.07.2026 | `FUN_006f72f0` | 🟢 Confirmed | Очищает состояние предыдущего ранa, вызывает FUN_006ef890() и FUN_009eb880(...). Один из ключевых этапов начала нового забега. Источник StartSeed внутри функции не найден. | Ghidra decompiler, call graph |
| 0061 | 06.07.2026 | StartSeed Source | 🔴 Not Found | Источник первоначального uint32 StartSeed при создании нового забега не найден. Текущая основная задача исследования. | Ongoing research |
| 0062 | 06.07.2026 | Binary | 🟢 Confirmed | Подтверждена версия игры: The Binding of Isaac: Repentance+ Beta, v1.9.7.17 | Direct binary analysis |
| 0063 | 06.07.2026 | Binary | 🟢 Confirmed | Подтверждены хеши isaac-ng.exe: SHA-256 3BDFC8BA...44616B, MD5 2FA5097A...7B304, размер 9 362 440 байт | Direct binary analysis |
| 0064 | 06.07.2026 | Binary | 🟢 Confirmed | IMAGE_FILE_HEADER: Machine 0x014C (Intel x86), 6 секций, TimeDateStamp 0x69E6E3A7, Characteristics 0x0122 | PE header analysis |
| 0065 | 06.07.2026 | Binary | 🟢 Confirmed | IMAGE_OPTIONAL_HEADER: Magic 0x10B (PE32), Linker 14.29, ImageBase 0x00400000, EntryRVA 0x00E310, SizeOfImage 0x92C000, Subsystem Windows GUI, DLLCharacteristics 0x8140 | PE header analysis |
| 0066 | 06.07.2026 | Binary | 🟢 Confirmed | Секции: .text, .rdata, .data, .rsrc, .reloc, .bind (6 секций) | PE section analysis |
| 0067 | 06.07.2026 | Binary Passport | 🟢 Confirmed | Создан полный binary-passport.md с PE-заголовками, хешами и метаданными | research/binary-passport.md |
| 0068 | 06.07.2026 | `FUN_009eb7f0` | 🟢 Confirmed | Это НЕ функция создания StartSeed. Обработчик Lua API: Seeds:SetStartSeed(). Принимает строковый пользовательский сид, вызывает FUN_009eb6b0 (String2Seed) для получения uint32, передаёт его в FUN_009eb880 (инициализация RNG). Назначение: установка пользовательского Custom Seed. | Ghidra decompiler, call graph, Lua API string references |
| 0069 | 06.07.2026 | `FUN_009eb880` | 🟢 Confirmed | Инициализация структуры RNG подтверждена. Принимает готовый uint32 seed, сохраняет seed. Если seed == 0 — вызывает FUN_006eeF60 для получения резервного ненулевого значения. Устанавливает параметры XORSHIFT: shift1=3, shift2=17, shift3=25. Прогревает внутреннее состояние RNG. НЕ создаёт первоначальный StartSeed. | Ghidra decompiler, struct analysis |
| 0070 | 06.07.2026 | `FUN_0040cf50` | 🟢 Confirmed | Вспомогательная функция копирования std::string. Реализация с Small String Optimization (SSO). Не относится к генерации сидов. Используется только для копирования строки перед дальнейшей обработкой. | Ghidra decompiler |
| 0071 | 06.07.2026 | `FUN_00917a50` | 🟢 Confirmed | Загрузка пользовательского профиля / восстановление состояния. Вызов FUN_009eb880 внутри используется для восстановления уже существующего состояния RNG. Функция НЕ создаёт новый StartSeed. | Ghidra decompiler, call graph analysis |
| 0072 | 06.07.2026 | StartSeed Source | 🟢 Confirmed | Из шести известных вызовов FUN_009eb880 исследованы и классифицированы: FUN_009eb7f0 — Lua SetStartSeed (Custom Seed); FUN_00958cb0 — использует уже существующий seed; FUN_00917a50 — восстановление состояния из профиля; FUN_00948fc0 — исследована частично, создание StartSeed не подтверждено; FUN_006f72f0 — подготовка уже существующего забега; FUN_009eb950 — ещё не исследована. Подтверждений, что какая-либо из исследованных функций создаёт первоначальный StartSeed, не найдено. | Call graph analysis, decompiler |

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
| 06.07.2026 | - | Initial research log |
| 06.07.2026 | - | Added Binary Passport entries (0001-0011) |
| 06.07.2026 | - | Added Lua VM and API entries (0022-0036) |
| 06.07.2026 | - | Added Environment, RNG String, ProjectileParams, SSA Analysis, CALL Analysis, GhidraScript entries (0037-0043) |
| 06.07.2026 | - | Added Seed Decoder entries (0044-0051) |
| 06.07.2026 | - | Added RNG Architecture entries: FUN_009eb880, FUN_006ef890, RNG Structure, XORSHIFT algorithm, full pipeline, related functions (0053-0061) |
| 06.07.2026 | - | Added Binary Passport entries: version, hashes, PE headers, sections (0062-0067) |
| 06.07.2026 | - | Added FUN_009eb7f0 Lua SetStartSeed analysis (0068) |
| 06.07.2026 | - | Added FUN_009eb880 detailed RNG init analysis with shift params and FUN_006eeF60 fallback (0069) |
| 06.07.2026 | - | Added FUN_0040cf50 std::string copy with SSO (0070) |
| 06.07.2026 | - | Added FUN_00917a50 profile restore analysis (0071) |
| 06.07.2026 | - | Updated StartSeed Source: 6 FUN_009eb880 callers classified, no initial StartSeed creation confirmed (0072) |
