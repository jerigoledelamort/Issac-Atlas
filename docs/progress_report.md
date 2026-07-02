# Reverse Engineering Progress Report

## Метаданные

| Поле | Значение |
|------|----------|
| Дата | 2024 |
| Этап | Stage 1 — Reverse Engineering |
| Статус | 🟡 В процессе |

---

## Выполнено

### 1. Подготовлена среда Reverse Engineering

**Status:** 🟢 Confirmed

- Ghidra 12.1.2 установлена и настроена
- Создан отдельный проект Ghidra
- Импортирован isaac-ng.exe
- Выполнен полный Auto Analysis
- Анализ успешно завершён

**Результаты анализа:**

| Параметр | Значение |
|----------|----------|
| Functions | 20 918 |
| Strings | 16 097 |
| Imports | Распознаны успешно |
| Symbols | Отсутствуют (release build) |
| PDB | Отсутствует (ссылка: isaac-ng_Submission.pdb) |

---

### 2. Найдена и исследована инициализация Lua

**Status:** 🟢 Confirmed

**Функция:** `FUN_008604C0`

**Установлено:**

- Создание Lua VM
- `luaL_newstate()` / `lua_newstate()`
- Регистрация panic handler
- Подключение стандартных библиотек
- Загрузка скриптов:
  - `resources/scripts/enums.lua`
  - `resources/scripts/main.lua`
- Получение `_RunCallback`
- Получение `_UnloadMod`

---

### 3. Найдена регистрация Lua API

**Status:** 🟢 Confirmed

**Функция:** `FUN_00866960`

**Назначение:** Регистрирует игровые классы Lua

---

### 4. Исследован механизм регистрации класса RNG

**Status:** 🟢 Confirmed

**Последовательность:**

```
FUN_00876530()
  ↓
FUN_008a6d90()
  ↓
Создание Lua userdata / metatable
```

**Строка:** `"RNG"` по адресу `DAT_00b70764`

---

### 5. Подтверждены методы класса RNG

**Status:** 🟢 Confirmed

| Метод | Статус |
|-------|--------|
| GetSeed | 🟢 Confirmed |
| SetSeed | 🟢 Confirmed |
| RandomInt | 🟢 Confirmed |
| RandomFloat | 🟢 Confirmed |

---

### 6. Подтверждён экспорт ProjectileParams

**Status:** 🟢 Confirmed

| Поле | Статус |
|------|--------|
| ProjectileParams | 🟢 Confirmed |
| Acceleration | 🟢 Confirmed |
| Spread | 🟢 Confirmed |
| HomingStrength | 🟢 Confirmed |
| CurvingStrength | 🟢 Confirmed |
| HeightModifier | 🟢 Confirmed |

---

### 7. Исследование автоматизации

#### SSA-анализ через HighFunction/Pcode

**Status:** 🔴 Rejected

**Причина:**

- Слишком сложный для текущей задачи
- Зависимость от нестабильного API
- Не требуется для исследования Lua API

#### Линейный обход CALL-инструкций

**Status:** 🟢 Confirmed

**Выяснено:**

- Многие вызовы являются косвенными: `CALL ESI`, `CALL EDI`
- Простой анализ CALL недостаточен

---

### 8. Создан первый рабочий GhidraScript

**Status:** 🟢 Confirmed

**Скрипт:** `ExtractLuaAPI.java`

**Возможности:**

- Открытие функции регистрации
- Обход инструкций
- Анализ CALL
- Вывод информации о вызовах

**Статус компиляции:** ✅ Успешно (Ghidra 12.1.2)

---

## Главный вывод

> **Подтверждено существование централизованной регистрации Lua API.**
>
> Вся система биндингов проходит через единый регистратор (`FUN_00866960`).
>
> Это означает, что возможно **автоматическое восстановление практически всего Lua API игры**.

---

## Следующий этап

### ExtractLuaAPI Version 2

**Цель:** Использовать модель программы Ghidra (Reference API и Function References) вместо простого линейного обхода инструкций.

**Необходимо автоматически получать:**

- [ ] Классы
- [ ] Методы
- [ ] Адреса C++ функций
- [ ] Порядок регистрации

**После завершения автоматизации:** Продолжить исследование RNG.

---

## История изменений

| Дата | Изменения |
|------|-----------|
| | Initial report |
