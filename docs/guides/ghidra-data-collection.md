# Руководство по сбору данных после автоматического анализа Ghidra

## Назначение

Этот документ описывает данные, которые необходимо собрать **сразу после завершения автоматического анализа** Ghidra, перед началом ручного исследования.

## Статус

| Поле | Значение |
|------|----------|
| Статус | 🟢 Готово |
| Версия | 1.0 |
| Дата создания | 06.07.2026 |

---

## Обязательные данные для сбора

### 1. Информация об исполняемом файле

**Источник:** Ghidra → File → Program Properties

| Данные | Куда записать |
|--------|---------------|
| Имя файла | [project_map.md](../project_map.md#executable-information) |
| Размер | [project_map.md](../project_map.md#executable-information) |
| Архитектура | [project_map.md](../project_map.md#executable-information) |
| Компилятор | [project_map.md](../project_map.md#executable-information) |
| Language ID | [project_map.md](../project_map.md#executable-information) |

### 2. Точка входа

**Источник:** Ghidra → Symbol Tree → Entry Points

| Данные | Куда записать |
|--------|---------------|
| Адрес точки входа | [project_map.md](../project_map.md#entry-point) |
| Функция | [project_map.md](../project_map.md#entry-point) |

### 3. Импортированные библиотеки

**Источник:** Ghidra → Symbol Tree → Imports

| Данные | Куда записать |
|--------|---------------|
| Список библиотек | [project_map.md](../project_map.md#imported-libraries) |
| Функции импорта | [project_map.md](../project_map.md#imported-libraries) |

### 4. Экспортированные символы

**Источник:** Ghidra → Symbol Tree → Exports

| Данные | Куда записать |
|--------|---------------|
| Список экспортов | [project_map.md](../project_map.md#exported-symbols) |

### 5. RTTI / Классы

**Источник:** Ghidra → Symbol Tree → Classes (если доступно)

| Данные | Куда записать |
|--------|---------------|
| Список классов | [project_map.md](../project_map.md#rtti) |
| Vtables | [project_map.md](../project_map.md#rtti) |

### 6. Строки

**Источник:** Ghidra → Search → For Strings...

| Данные | Куда записать |
|--------|---------------|
| Пути к файлам | [project_map.md](../project_map.md#strings) |
| Сообщения об ошибках | [project_map.md](../project_map.md#strings) |
| Отладочные строки | [project_map.md](../project_map.md#strings) |

### 7. Функции

**Источник:** Ghidra → Symbol Tree → Functions

| Данные | Куда записать |
|--------|---------------|
| Список функций | [research/exports/functions.csv](../../research/exports/) |
| Адреса функций | [research/exports/functions.csv](../../research/exports/) |
| Сигнатуры | [research/exports/functions.csv](../../research/exports/) |

### 8. Граф вызовов

**Источник:** Ghidra → Windows → Function Graph

| Данные | Куда записать |
|--------|---------------|
| Граф entry point | [research/callgraphs/entry_point.png](../../research/callgraphs/) |
| Графы основных функций | [research/callgraphs/](../../research/callgraphs/) |

### 9. Определённые типы данных

**Источник:** Ghidra → Data Type Manager

| Данные | Куда записать |
|--------|---------------|
| Структуры | [research/exports/structures.xml](../../research/exports/) |
| Перечисления | [research/exports/enumerations.xml](../../research/exports/) |
| Классы | [research/exports/classes.xml](../../research/exports/) |

---

## Чек-лист сбора данных

- [ ] Executable Information заполнен
- [ ] Entry Point записан
- [ ] Imported Libraries экспортированы
- [ ] Exported Symbols экспортированы
- [ ] RTTI данные собраны
- [ ] Strings экспортированы
- [ ] Function list экспортирован
- [ ] Call graphs сохранены
- [ ] Data types экспортированы
- [ ] Project Ghidra сохранён в `research/ghidra/`

---

## Рекомендуемый порядок действий

1. **Завершить автоматический анализ** Ghidra (дождаться 100%)
2. **Сохранить проект Ghidra** в `research/ghidra/<project_name>.ghidra`
3. **Экспортировать символы** через скрипт или вручную
4. **Заполнить project_map.md** доступными данными
5. **Создать первую запись** в research_log.md
6. **Начать ручное исследование**

---

## Ссылки

- [project_map.md](../project_map.md) — карта проекта
- [research_log.md](../research_log.md) — журнал исследования
- [research/README.md](../../research/README.md) — структура исследований
