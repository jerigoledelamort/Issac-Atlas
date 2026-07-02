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
| 0001 | | | 🟡 Hypothesis | | |
| 0002 | | | 🟡 Hypothesis | | |
| 0003 | | | 🟡 Hypothesis | | |

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
| | | |
