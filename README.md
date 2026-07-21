# Isaac Atlas

**Isaac Atlas** — исследовательская платформа для полного воспроизведения генерации мира
**The Binding of Isaac: Repentance+** и последующего построения базы данных всех внутренних сидов.

## Архитектура

Проект состоит из двух независимых частей:

- **engine/** — библиотека воспроизведения генерации (чистая логика, без GUI).
  Декодирование сидов, воспроизведение RNG, генерация мира, сериализация, верификация.
- **atlas/** — пользовательское приложение поверх engine.
  CLI, GUI, REST API, веб-интерфейс, поиск, анализ.

Engine не зависит от Atlas. Atlas использует Engine через публичный API.

## Структура

```
isaac-atlas/
├── engine/                # Библиотека (Isaac Engine)
│   └── seed_decoder.py    # Декодер сидов (FUN_009EB6B0)
│
├── atlas/                 # Приложение (Isaac Atlas)
│   └── cli.py             # Командная строка
│
├── research/              # Исследования и RE
│   ├── binary-passport.md # PE-заголовки, хеши, метаданные isaac-ng.exe
│   ├── hashes.md          # Криптографические хеши файлов
│   ├── version.md         # Версия игры
│   ├── rng/               # Исследование RNG
│   │   ├── rng-architecture.md  # Архитектура RNG (XORSHIFT, функции)
│   │   └── seed-decoding.md    # Спецификация декодера сидов
│   ├── ghidra/            # Проект Ghidra + декомпиляция
│   └── original/          # Оригинальные файлы игры (бинарники, ресурсы)
│
├── docs/                  # Документация
│   ├── project_map.md     # Карта бинарника (функции, строки, подсистемы)
│   ├── research_log.md    # Журнал исследований (80 записей)
│   ├── artifacts.md       # Каталог RE-артефактов
│   ├── progress_report.md # Отчёт о прогрессе
│   ├── specifications/    # Формальные спецификации
│   ├── guides/            # Руководства
│   └── decisions/         # Архитектурные решения (ADR)
│
└── tests/                 # Тесты
    ├── conftest.py
    └── test_seed_decoder.py
```

## Философия

1. **Сначала исследование** — изучение оригинальной игры
2. **Потом документация** — фиксация обнаруженных закономерностей
3. **Потом реализация** — код на основе документации
4. **Потом тестирование** — проверка совпадения с оригиналом
5. **Только потом перебор** — enumerator и database

См. [MISSION.md](MISSION.md) и [RULES.md](RULES.md).

## Быстрый старт

```bash
# Тесты
python -m pytest tests/ -v

# CLI
python -m atlas.cli decode-seed "BMR9 KSHY"
python -m atlas.cli encode-seed 87067453
python -m atlas.cli validate-seed "BMR9 KSHY"
```

## Документация

| Документ | Описание |
|----------|----------|
| [MISSION.md](MISSION.md) | Философия и цели |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Архитектура системы |
| [ROADMAP.md](ROADMAP.md) | План разработки |
| [RULES.md](RULES.md) | Правила разработки |

## Лицензия

MIT — см. [LICENSE.md](LICENSE.md).
