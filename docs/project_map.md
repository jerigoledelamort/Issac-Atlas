# Project Map: The Binding of Isaac: Repentance

## Метаданные документа

| Поле | Значение |
|------|----------|
| Статус | 🟡 В заполнении |
| Исследуемая версия | v1.9.7.17 |
| Дата начала | 06.07.2026 |
| Дата обновления | 06.07.2026 |
| Исследователь | *не указан* |

---

## Binary Passport

> Полная спецификация: [research/binary-passport.md](../research/binary-passport.md)

| Параметр | Значение | Статус |
|----------|----------|--------|
| Game | The Binding of Isaac: Repentance+ Beta | 🟢 Confirmed |
| Version | v1.9.7.17 | 🟢 Confirmed |
| Executable | isaac-ng.exe | 🟢 Confirmed |
| Executable Format | Portable Executable (PE) | 🟢 Confirmed |
| Architecture | x86 (PE32, 32-bit) | 🟢 Confirmed |
| Platform | Windows | 🟢 Confirmed |
| Endianness | Little Endian | 🟢 Confirmed |
| Compiler | Microsoft Visual Studio (Linker 14.29) | 🟢 Confirmed |
| Image Base | 0x00400000 | 🟢 Confirmed |
| AddressOfEntryPoint (RVA) | 0x00E310 | 🟢 Confirmed |
| Minimum Address | 0x00400000 | 🟢 Confirmed |
| Maximum Address | 0x00D2B807 | 🟢 Confirmed |
| Relocatable | true | 🟢 Confirmed |
| Section Alignment | 0x1000 (4096) | 🟢 Confirmed |
| File Alignment | 0x0200 (512) | 🟢 Confirmed |
| SizeOfImage | 0x92C000 | 🟢 Confirmed |
| SizeOfCode | 0x716200 | 🟢 Confirmed |
| SizeOfInitializedData | 0x14C000 | 🟢 Confirmed |
| Subsystem | Windows GUI | 🟢 Confirmed |
| DLLCharacteristics | 0x8140 (HIGH_ENTROPY_VA, NX_COMPAT, TERMINAL_SERVER_AWARE) | 🟢 Confirmed |
| Characteristics | 0x0122 (EXECUTABLE_IMAGE, LARGE_ADDRESS_AWARE, 32BIT_MACHINE) | 🟢 Confirmed |
| Sections | 6 (.text, .rdata, .data, .rsrc, .reloc, .bind) | 🟢 Confirmed |
| Auto Analysis | Completed successfully | 🟢 Confirmed |
| Functions Discovered | 20918 | 🟢 Confirmed |
| Strings Discovered | 16097 | 🟢 Confirmed |
| PDB Status | Absent (reference: isaac-ng_Submission.pdb) | 🟢 Confirmed |
| SHA-256 | 3BDFC8BAE0DC7E334B76009D0AD45DFBB16EE5F00C06FFBC3A0094E34DD44616B | 🟢 Confirmed |
| MD5 | 2FA5097A4EF74194821D13A5CAE7B304 | 🟢 Confirmed |
| File Size | 9 362 440 bytes | 🟢 Confirmed |

---

## Executable Information

| Параметр | Значение | Статус |
|----------|----------|--------|
| Имя файла | isaac-ng.exe | 🟢 Confirmed |
| Путь | *не указан* | 🟡 |
| Размер (байт) | 9 362 440 | 🟢 Confirmed |
| Архитектура | x86 (PE32) | 🟢 Confirmed |
| Компилятор | Microsoft Visual Studio (Linker 14.29) | 🟢 Confirmed |
| Дата компиляции | TimeDateStamp: 0x69E6E3A7 | 🟢 Confirmed |
| CRC32 | Checksum: 0 (не используется) | 🟢 Confirmed |
| SHA-256 | 3BDFC8BAE0DC7E334B76009D0AD45DFBB16EE5F00C06FFBC3A0094E34DD44616B | 🟢 Confirmed |
| MD5 | 2FA5097A4EF74194821D13A5CAE7B304 | 🟢 Confirmed |

---

## Entry Point

**Status:** 🟢 Confirmed

| Параметр | Значение |
|----------|----------|
| Адрес точки входа | entry |
| Функция | FUN_00cfe315 → FUN_00cfe390 |
| Описание | Инициализация CRT и раннего окружения процесса. Не содержит игровой логики. |

```
entry
  ↓
FUN_00cfe315
  ↓
FUN_00cfe390 (CRT initialization only)
```

---

## Namespaces

**Status:** 🟢 Confirmed

| Namespace | Подтверждённое использование |
|-----------|-----------------------------|
| IsaacRepentancePlus | Игровой код |
| KAGE | Игровой код |
| luabridge | LuaBridge интеграция |
| png | Обработка PNG |
| theoraplayer | Встроенный проигрыватель видео Theora |

---

## Imported Libraries

**Status:** 🟢 Confirmed

| Библиотека | Статус |
|------------|--------|
| ADVAPI32.dll | 🟢 Confirmed |
| API-MS-WIN-CRT-* | 🟢 Confirmed |
| BCRYPT.dll | 🟢 Confirmed |
| DBGHELP.dll | 🟢 Confirmed |
| EOSSDK-WIN32-SHIPPING.dll | 🟢 Confirmed |
| GDI32.dll | 🟢 Confirmed |
| KERNEL32.dll | 🟢 Confirmed |
| LIBCURL.dll | 🟢 Confirmed |
| LUA5.3.3R.dll | 🟢 Confirmed |
| MSVCP140.dll | 🟢 Confirmed |
| OLE32.dll | 🟢 Confirmed |
| OPENAL32.dll | 🟢 Confirmed |
| OPENGL32.dll | 🟢 Confirmed |
| SHELL32.dll | 🟢 Confirmed |
| SDL2.dll | 🟢 Confirmed |
| STEAM_API.dll | 🟢 Confirmed |
| USER32.dll | 🟢 Confirmed |
| VCRUNTIME140.dll | 🟢 Confirmed |
| WINMM.dll | 🟢 Confirmed |

### Критические импорты

| Функция | Библиотека | Адрес | Назначение |
|---------|------------|-------|------------|
| 06.07.2026 | | 06.07.2026 | |
| 06.07.2026 | | 06.07.2026 | |

---

## Exported Symbols

| Символ | Адрес | Тип | Описание |
|--------|-------|-----|----------|
| 06.07.2026 | | 06.07.2026 | |
| 06.07.2026 | | 06.07.2026 | |

---

## RTTI (Run-Time Type Information)

### Известные классы

| Имя класса | Адрес vtable | Размер | Наследование |
|------------|--------------|--------|--------------|
| 06.07.2026 | | 06.07.2026 | |
| 06.07.2026 | | 06.07.2026 | |

### Иерархия классов

```
// Диаграмма иерархии
```

---

## Strings

### Пути и файлы

**Status:** 🟢 Confirmed

| Строка | Адрес | Контекст |
|--------|-------|----------|
| resources/ | 06.07.2026 | Базовая директория ресурсов |
| resources/scripts/ | 06.07.2026 | Скрипты Lua |
| resources/scripts/main.lua | 06.07.2026 | Главный скрипт |
| resources/scripts/enums.lua | 06.07.2026 | Скрипт перечислений |
| resources/packed/ | 06.07.2026 | Директория packed-архивов |
| resources/packed/config.a | 06.07.2026 | Архив конфигураций |
| resources/packed/fonts.a | 06.07.2026 | Архив шрифтов |
| resources/packed/graphics.a | 06.07.2026 | Архив графики |
| resources/packed/music.a | 06.07.2026 | Архив музыки |
| resources/packed/sfx.a | 06.07.2026 | Архив звуковых эффектов |
| resources/packed/videos.a | 06.07.2026 | Архив видео |
| resources/packed/animations.a | 06.07.2026 | Архив анимаций |

### XML-конфигурации

**Status:** 🟢 Confirmed

| Файл | Статус |
|------|--------|
| players.xml | 🟢 Confirmed |
| items.xml | 🟢 Confirmed |
| pocketitems.xml | 🟢 Confirmed |
| preload.xml | 🟢 Confirmed |
| ambush.xml | 🟢 Confirmed |
| bossoverlays.xml | 🟢 Confirmed |
| giantbook.xml | 🟢 Confirmed |

### Отладочные строки

**Status:** 🟢 Confirmed

| Строка | Контекст |
|--------|----------|
| Binding of Isaac: Repentance+ | Название игры |
| IsaacIndicator | Внутренний идентификатор |
| IconIsaacsRoom | Внутренний идентификатор |
| ISAACNG_GSR | Внутренний идентификатор |
| ISAACNG_SAVE04 | Внутренний идентификатор сохранения |

---

## Major Subsystems

### Подсистема: XML Processing

**Status:** 🟢 Confirmed

| Параметр | Значение |
|----------|----------|
| Адрес функции | FUN_006f3c00 |
| Назначение | Подготовка XML-данных к парсингу |
| XREF count | 3 (для players.xml) |

**Описание:**

Функция выполняет подготовительный этап перед разбором XML:
- Выделяет память
- Создаёт внутренние структуры
- Копирует строку "players.xml"
- Подготавливает параметры для дальнейшего парсинга

Сам XML внутри функции не разбирается.

**Известные функции:**

| Функция | Адрес | Назначение | Статус |
|---------|-------|------------|--------|
| FUN_006f3c00 | 0x006f3c00 | Подготовка XML-данных | 🟢 Confirmed |

---

### Подсистема: Lua VM Initialization

**Status:** 🟢 Confirmed

| Параметр | Значение |
|----------|----------|
| Главная функция инициализации | FUN_008604C0 |
| Функция регистрации API | FUN_00866960 |
| Функция загрузки скриптов | FUN_0086E5E0 |

**Описание:**

FUN_008604C0 отвечает за полную инициализацию Lua VM:
1. Создаётся Lua State (luaL_newstate() / lua_newstate())
2. Подключаются стандартные библиотеки Lua через luaL_requiref()
3. Регистрируются C++ типы и классы (FUN_00866960)
4. Загружаются встроенные Lua-скрипты:
   - resources/scripts/enums.lua
   - resources/scripts/main.lua
5. Извлекаются функции _RunCallback и _UnloadMod через luaL_ref()
6. Глобальные переменные удаляются (lua_pushnil() + lua_setglobal())

**Известные функции:**

| Функция | Адрес | Назначение | Статус |
|---------|-------|------------|--------|
| FUN_008604C0 | 0x008604C0 | Полная инициализация Lua VM | 🟢 Confirmed |
| FUN_00866960 | 0x00866960 | Регистрация Lua API (реестр) | 🟢 Confirmed |
| FUN_0086E5E0 | 0x0086E5E0 | Загрузка Lua-скриптов | 🟢 Confirmed |

---

### Подсистема: Lua API Registry

**Status:** 🟢 Confirmed

FUN_00866960 регистрирует весь Lua API игры:
- Создаёт userdata
- Создаёт metatable
- Регистрирует классы
- Регистрирует методы
- Экспортирует функции движка в Lua

**Структура регистрации:**
```
Создать тип
  ↓
Назначить __call
  ↓
Зарегистрировать методы
  ↓
Зарегистрировать свойства
```

**Функции регистрации классов:**

| Функция | Адрес | Назначение | Статус |
|---------|-------|------------|--------|
| FUN_00876530 | 0x00876530 | RegisterClass (вызывает FUN_008a6d90) | 🟢 Confirmed |
| FUN_008a6d90 | 0x008a6d90 | Создаёт Lua userdata/метатаблицу | 🟢 Confirmed |

**Функции регистрации методов:**

| Функция | Адрес | Назначение | Статус |
|---------|-------|------------|--------|
| FUN_00876650 | 0x00876650 | RegisterMethod (сигнатура тип 1) | 🟢 Confirmed |
| FUN_00876670 | 0x00876670 | RegisterMethod (сигнатура тип 2) | 🟢 Confirmed |
| FUN_008766b0 | 0x008766b0 | RegisterMethod (сигнатура тип 3) | 🟢 Confirmed |
| FUN_00876710 | 0x00876710 | RegisterMethod (сигнатура тип 4) | 🟢 Confirmed |
| FUN_00876770 | 0x00876770 | RegisterMethod (сигнатура тип 5) | 🟢 Confirmed |

**Зарегистрированные классы:**

| Класс | Статус |
|-------|--------|
| Entity | 🟢 Confirmed |
| EntityPlayer | 🟢 Confirmed |
| EntityNPC | 🟢 Confirmed |
| EntityTear | 🟢 Confirmed |
| Sprite | 🟢 Confirmed |
| Vector | 🟢 Confirmed |
| Color | 🟢 Confirmed |
| KColor | 🟢 Confirmed |
| EntityRef | 🟢 Confirmed |
| ProjectileParams | 🟢 Confirmed |
| ItemConfig | 🟢 Confirmed |
| PathFinder | 🟢 Confirmed |
| Random | 🟢 Confirmed |
| BitSet128 | 🟢 Confirmed |
| RNG | 🟢 Confirmed |

**Класс RNG — подтверждённые методы:**

| Метод | Статус |
|-------|--------|
| GetSeed | 🟢 Confirmed |
| SetSeed | 🟢 Confirmed |
| RandomInt | 🟢 Confirmed |
| RandomFloat | 🟢 Confirmed |

**Класс ProjectileParams — подтверждённые поля:**

| Поле | Статус |
|------|--------|
| Acceleration | 🟢 Confirmed |
| Spread | 🟢 Confirmed |
| HomingStrength | 🟢 Confirmed |
| CurvingStrength | 🟢 Confirmed |

**Известные маппинги Lua API → C++:**

| Lua метод | C++ функция | Статус |
|-----------|-------------|--------|
| AddCoins | FUN_00759400 | 🟢 Confirmed |
| FireTear | FUN_00790AF0 | 🟢 Confirmed |
| AddCollectible | FUN_0075F0E0 | 🟢 Confirmed |
| FireBomb | FUN_007A0970 | 🟢 Confirmed |

---

### Подсистема: *название*

| Параметр | Значение |
|----------|----------|
| Адрес начала | 06.07.2026 |
| Адрес окончания | 06.07.2026 |
| Размер | 06.07.2026 |
| Зависимости | 06.07.2026 |

**Описание:**

**Известные функции:**

| Функция | Адрес | Назначение | Статус |
|---------|-------|------------|--------|
| 06.07.2026 | | 06.07.2026 | 🟡 |
| 06.07.2026 | | 06.07.2026 | 🟡 |

---

## Call Graph

### Уровень 0: Entry Point

**Status:** 🟢 Confirmed

```
entry
└── FUN_00cfe315
    └── FUN_00cfe390 (CRT initialization)
```

### Уровень 1: Инициализация процесса

**Status:** 🟢 Confirmed (x64dbg)

```
Windows
  ↓
ntdll.dll
  ↓
TLS Callback
  ↓
kernel32
  ↓
gdi32full
  ↓
isaac-ng.exe
```

После передачи управления isaac-ng.exe выполнение доходит до кода приложения.

### Уровень 2: Игровой цикл

*Требуется дополнительное исследование*

---

## Notes

### Общие наблюдения

**Status:** 🟢 Confirmed

- Исследуемый exe является полноценным нативным C++ приложением
- Активно используется LuaBridge
- Игровые данные хранятся в packed-архивах (.a)
- XML используется как конфигурационный слой
- Существует отдельный этап подготовки XML перед разбором
- Entry Point содержит только код запуска CRT
- Игровой код начинается значительно позже инициализации процесса
- Lua VM инициализируется через FUN_008604C0
- Lua API регистрируется через FUN_00866960
- _RunCallback и _UnloadMod являются обязательными точками входа Lua-модов
- Регистрация классов: FUN_00876530 → FUN_008a6d90
- Регистрация методов: семейство FUN_00876650-FUN_00876770
- Класс RNG экспортирует GetSeed, SetSeed, RandomInt, RandomFloat
- Класс ProjectileParams экспортирует Acceleration, Spread, HomingStrength, CurvingStrength, HeightModifier
- **Централизованная регистрация Lua API позволяет автоматизировать восстановление API**
- Многие вызовы косвенные (CALL ESI/EDI) — простой линейный обход недостаточен

### Вопросы для исследования

- Анализ загруженного процесса (требуется обход Steam-защиты)
- Исследование функций после инициализации CRT
- Анализ packed-архивов формата .a
- Автоматизация переименования функций через Lua API registry
- **Приоритет:** ExtractLuaAPI v2 — использование Reference API вместо линейного обхода

### Связанные документы

- [research_log.md](research_log.md) — журнал исследования
- [research/hashes.md](../research/hashes.md) — хеши файлов
- [research/version.md](../research/version.md) — версия игры

---

## История изменений

| Дата | Автор | Изменения |
|------|-------|-----------|
| 06.07.2026 | NLP-Core-Team | Обновлён Binary Passport: версия v1.9.7.17, хеши, полные PE-заголовки, размер файла, секции |
| 2026 | 06.07.2026 | |
