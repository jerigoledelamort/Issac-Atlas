# Reverse Engineering Artifacts

## PDB Reference

| Параметр | Значение | Статус |
|----------|----------|--------|
| Status | 🟢 Confirmed | 🟢 Confirmed |
| Artifact | isaac-ng_Submission.pdb | 🟢 Confirmed |

**Description:**

В бинарнике присутствует ссылка на PDB-файл `isaac-ng_Submission.pdb`.

Соответствующий PDB отсутствует.

Это подтверждает, что оригинальная сборка была создана с использованием PDB.

---

## Binary Artifacts

| Параметр | Значение | Статус |
|----------|----------|--------|
| Auto Analysis | Completed successfully | 🟢 Confirmed |
| Functions Discovered | 20918 | 🟢 Confirmed |
| Strings Discovered | 16097 | 🟢 Confirmed |

---

## Resource Archives

**Status:** 🟢 Confirmed

| Архив | Путь |
|-------|------|
| config.a | resources/packed/config.a |
| fonts.a | resources/packed/fonts.a |
| graphics.a | resources/packed/graphics.a |
| music.a | resources/packed/music.a |
| sfx.a | resources/packed/sfx.a |
| videos.a | resources/packed/videos.a |
| animations.a | resources/packed/animations.a |

---

## XML Configurations

**Status:** 🟢 Confirmed

| Файл | Назначение |
|------|------------|
| players.xml | Конфигурация игроков |
| items.xml | Конфигурация предметов |
| pocketitems.xml | Конфигурация карманных предметов |
| preload.xml | Предзагрузка ресурсов |
| ambush.xml | Конфигурация засад |
| bossoverlays.xml | Оверлеи боссов |
| giantbook.xml | Конфигурация книги гигантов |

---

## Lua Scripts

**Status:** 🟢 Confirmed

| Скрипт | Путь |
|--------|------|
| main.lua | resources/scripts/main.lua |
| enums.lua | resources/scripts/enums.lua |

---

## Lua VM Functions

**Status:** 🟢 Confirmed

| Функция | Адрес | Назначение |
|---------|-------|------------|
| FUN_008604C0 | 0x008604C0 | Полная инициализация Lua VM |
| FUN_00866960 | 0x00866960 | Регистрация Lua API (реестр) |
| FUN_0086E5E0 | 0x0086E5E0 | Загрузка Lua-скриптов |

---

## Lua API Entry Points

**Status:** 🟢 Confirmed

| Точка входа | Описание |
|-------------|----------|
| _RunCallback | Обязательная точка входа Lua-модов (извлекается через luaL_ref) |
| _UnloadMod | Обязательная точка входа Lua-модов (извлекается через luaL_ref) |

---

## Lua API Mappings

**Status:** 🟢 Confirmed

| Lua метод | C++ функция | Адрес |
|-----------|-------------|-------|
| AddCoins | FUN_00759400 | 0x00759400 |
| FireTear | FUN_00790AF0 | 0x00790AF0 |
| AddCollectible | FUN_0075F0E0 | 0x0075F0E0 |
| FireBomb | FUN_007A0970 | 0x007A0970 |

---

## Lua Registered Classes

**Status:** 🟢 Confirmed

| Класс | Класс | Класс |
|-------|-------|-------|
| Entity | EntityPlayer | EntityNPC |
| EntityTear | Sprite | Vector |
| Color | KColor | EntityRef |
| ProjectileParams | ItemConfig | PathFinder |
| Random | BitSet128 | RNG |

---

## Lua RNG Class

**Status:** 🟢 Confirmed

| Метод | Статус |
|-------|--------|
| GetSeed | 🟢 Confirmed |
| SetSeed | 🟢 Confirmed |
| RandomInt | 🟢 Confirmed |
| RandomFloat | 🟢 Confirmed |

---

## Lua ProjectileParams Class

**Status:** 🟢 Confirmed

| Поле | Статус |
|------|--------|
| Acceleration | 🟢 Confirmed |
| Spread | 🟢 Confirmed |
| HomingStrength | 🟢 Confirmed |
| CurvingStrength | 🟢 Confirmed |

---

## Lua Registration Functions

**Status:** 🟢 Confirmed

### RegisterClass

| Функция | Адрес | Назначение |
|---------|-------|------------|
| FUN_00876530 | 0x00876530 | RegisterClass (вызывает FUN_008a6d90) |
| FUN_008a6d90 | 0x008a6d90 | Создаёт Lua userdata/метатаблицу |

### RegisterMethod

| Функция | Адрес | Назначение |
|---------|-------|------------|
| FUN_00876650 | 0x00876650 | RegisterMethod (сигнатура тип 1) |
| FUN_00876670 | 0x00876670 | RegisterMethod (сигнатура тип 2) |
| FUN_008766b0 | 0x008766b0 | RegisterMethod (сигнатура тип 3) |
| FUN_00876710 | 0x00876710 | RegisterMethod (сигнатура тип 4) |
| FUN_00876770 | 0x00876770 | RegisterMethod (сигнатура тип 5) |

---

## Ghidra Scripts

**Status:** 🟢 Confirmed

| Скрипт | Язык | Статус | Назначение |
|--------|------|--------|------------|
| ExtractLuaAPI.java | Java | 🟢 Confirmed | Извлечение Lua API через анализ CALL инструкций |
| ExtractLuaAPI_SSA.java | Java | 🔴 Rejected | SSA-анализ через HighFunction/Pcode (отклонён) |

**ExtractLuaAPI.java возможности:**
- Открытие функции регистрации FUN_00866960
- Обход инструкций
- Анализ CALL инструкций
- Вывод информации о вызовах
- Компилируется и запускается в Ghidra 12.1.2

---

## Notes

| Примечание | Статус |
|------------|--------|
| PDB файл не найден в текущей директории | 🟢 Confirmed |
| Ссылка на PDB извлечена из PE header | 🟢 Confirmed |
| PDB отсутствует — обычная ситуация для релизной сборки | 🟢 Confirmed |
| Steam блокирует выполнение под отладчиком | 🟢 Confirmed |

---

## History

| Дата | Изменения |
|------|-----------|
| 2026 | Initial artifact documentation |
| 2026 | Added Resource Archives, XML Configurations, Lua Scripts |
| 2026 | Added Lua VM Functions, Lua API Entry Points, Lua API Mappings, Lua Registered Classes |
| 2026 | Added Lua RNG Class, Lua ProjectileParams Class, Lua Registration Functions |
| 2026 | Added Ghidra Scripts section (ExtractLuaAPI.java, ExtractLuaAPI_SSA.java) |
