# Руководство для разработчиков Isaac Atlas

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd isaac-atlas
```

### 2. Установка зависимостей

#### Windows

```powershell
# Требуется:
# - Visual Studio 2022 с C++ workload
# - CMake 3.20+
# - Python 3.9+

# Установка vcpkg (опционально)
git clone https://github.com/Microsoft/vcpkg.git
.\vcpkg\bootstrap-vcpkg.bat
```

#### Linux

```bash
# Требуется:
# - GCC 11+ или Clang 13+
# - CMake 3.20+
# - Python 3.9+

sudo apt-get install build-essential cmake python3
```

#### macOS

```bash
# Требуется:
# - Xcode Command Line Tools
# - CMake 3.20+
# - Python 3.9+

xcode-select --install
brew install cmake python3
```

### 3. Сборка Engine

```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug
cmake --build . --target engine
```

### 4. Сборка Atlas

```bash
cmake --build . --target atlas
```

### 5. Запуск тестов

```bash
ctest --output-on-failure
```

---

## Структура проекта

```
isaac-atlas/
├── engine/              # Библиотека воспроизведения
├── atlas/               # Пользовательское приложение
├── shared/              # Общие компоненты
├── research/            # Исследования
├── reverse/             # Reverse Engineering
├── docs/                # Документация
├── tests/               # Тесты
├── examples/            # Примеры
└── scripts/             # Скрипты
```

См. [ARCHITECTURE.md](ARCHITECTURE.md) для деталей.

---

## Настройка окружения

### IDE

#### Visual Studio

1. Открыть корневую папку как CMake проект
2. Выбрать конфигурацию (Debug/Release)
3. Выбрать целевую платформу

#### CLion

1. File → Open → выбрать корень проекта
2. CMake автоматически обнаружится
3. Настроить toolchain при необходимости

#### VS Code

1. Установить расширения:
   - C/C++ Extension Pack
   - CMake Tools
   - Python
2. Открыть папку проекта
3. CMake Tools автоматически настроится

### Pre-commit хуки

```bash
# Установка pre-commit
pip install pre-commit
pre-commit install

# Проверка всех файлов
pre-commit run --all-files
```

---

## Процесс разработки

### 1. Выбор задачи

- Проверить [TODO.md](TODO.md)
- Проверить открытые issue
- Обсудить новую идею в discussion

### 2. Создание ветки

```bash
git checkout main
git pull
git checkout -b feature/<название>
```

### 3. Исследование (если требуется)

Для новой функциональности:

1. Создать исследование в `research/<тема>/`
2. Задокументировать гипотезы
3. Собрать данные
4. Получить подтверждение
5. Установить статус «Подтверждено»

### 4. Реализация

1. Написать код
2. Написать тесты
3. Обновить документацию
4. Проверить стиль кода

### 5. Тестирование

```bash
# Unit тесты
ctest -R unit

# Integration тесты
ctest -R integration

# Verification тесты (требуют оригинал)
ctest -R verification
```

### 6. Коммит

```bash
git add <файлы>
git commit -m "feat(engine): описание изменений"
```

### 7. Pull Request

1. Push ветки
2. Создать PR на GitHub
3. Пройти code review
4. Исправить замечания
5. Merge после approval

---

## Тестирование

### Типы тестов

| Тип | Расположение | Запуск |
|-----|--------------|--------|
| Unit | `tests/unit/` | `ctest -R unit` |
| Integration | `tests/integration/` | `ctest -R integration` |
| Verification | `tests/verification/` | `ctest -R verification` |
| Regression | `tests/regression/` | `ctest -R regression` |
| Benchmarks | `tests/benchmarks/` | `ctest -R benchmark` |

### Написание тестов

```cpp
// Пример unit теста
TEST(RngTest, NextProducesExpectedSequence) {
    Rng rng(12345);
    EXPECT_EQ(rng.next(), 0x12345678);
    EXPECT_EQ(rng.next(), 0x87654321);
}

// Пример verification теста
TEST(VerificationTest, WorldMatchesOriginal) {
    World generated = engine.generate(12345);
    World original = loadOriginalWorld(12345);
    EXPECT_EQ(generated, original);
}
```

### Тестовые данные

Тестовые данные хранятся в `tests/data/`.

```
tests/data/
├── seeds/           # Seed'ы для тестов
├── worlds/          # Ожидаемые миры
└── fixtures/        # Фикстуры
```

---

## Отладка

### Логирование

Engine использует централизованное логирование:

```cpp
LOG_DEBUG("RNG state: {}", state);
LOG_INFO("Generated room at ({}, {})", x, y);
LOG_WARNING("Room placement failed after {} attempts", attempts);
LOG_ERROR("Failed to generate floor {}", floor);
```

### Отладка в IDE

#### Visual Studio

1. Установить точку останова
2. F5 для запуска отладки
3. Использовать Watch, Locals, Call Stack

#### CLion

1. Установить точку останова
2. Debug кнопка
3. Использовать Debugger tool window

#### VS Code

1. Установить точку останова
2. F5 для запуска
3. Использовать Run and Debug panel

### Отладка тестов

```bash
# Запуск конкретного теста
ctest -R RngTest --output-on-failure

# Запуск с отладчиком
ctest -R RngTest --debug

# Запуск с verbose
ctest -R RngTest -V
```

---

## Профилирование

### Инструменты

| Платформа | Инструмент |
|-----------|------------|
| Windows | Visual Studio Profiler, VTune |
| Linux | perf, valgrind, hotspot |
| macOS | Instruments, Xcode Profiler |
| Кроссплатформенный | Tracy, Superluminal |

### Запуск профилирования

```bash
# Сборка с профилированием
cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_PROFILING=ON

# Запуск с Tracy
./engine_profiled
```

Результаты сохраняются в `profiling/`.

---

## Документирование

### Типы документов

| Тип | Расположение | Формат |
|-----|--------------|--------|
| API Docs | `docs/api/` | Markdown + Doxygen |
| Guides | `docs/guides/` | Markdown |
| Specifications | `docs/specifications/` | Markdown |
| Decisions | `docs/decisions/` | Markdown (ADR) |
| Research | `research/` | Markdown |

### ADR (Architectural Decision Record)

```markdown
# ADR-001: Переименование engine/database/ в engine/storage/

## Статус
Принято

## Контекст
Каталог engine/database/ создавал путаницу с корневым database/...

## Решение
Переименовать engine/database/ в engine/storage/...

## Последствия
- Требуется обновление документации
- Изменение в include путях
```

---

## Частые задачи

### Добавить новый модуль в Engine

1. Создать каталог в `engine/<модуль>/`
2. Создать README.md
3. Добавить в CMakeLists.txt
4. Обновить ARCHITECTURE.md

### Добавить новое исследование

1. Создать каталог в `research/<тема>/`
2. Создать hypothesis.md
3. Документировать процесс
4. Установить статус

### Добавить тест

1. Создать файл в `tests/<тип>/`
2. Написать тест
3. Добавить в CMakeLists.txt
4. Запустить `ctest`

### Обновить документацию

1. Изменить Markdown файл
2. Проверить ссылки
3. Commit с типом `docs`

---

## Troubleshooting

### Сборка не удаётся

```bash
# Очистить build
rm -rf build/
mkdir build && cd build

# Пересоздать кэш
cmake .. -DCMAKE_BUILD_TYPE=Debug

# Собрать заново
cmake --build .
```

### Тесты падают

```bash
# Запустить с verbose
ctest -V

# Запустить конкретный тест
ctest -R <тест_name> --output-on-failure

# Проверить тестовые данные
ls tests/data/
```

### Проблемы с зависимостями

```bash
# Обновить подмодули
git submodule update --init --recursive

# Переустановить зависимости через vcpkg
vcpkg install <package>
```

---

## Контакты и поддержка

- **Issues:** GitHub Issues для багов и фич
- **Discussions:** GitHub Discussions для вопросов
- **Email:** См. MAINTAINERS.md (будет создан)

---

## Дополнительные ресурсы

- [CONTRIBUTING.md](CONTRIBUTING.md) — Правила вклада
- [RULES.md](RULES.md) — Правила разработки
- [STYLE_GUIDE.md](STYLE_GUIDE.md) — Стиль кода
- [ARCHITECTURE.md](ARCHITECTURE.md) — Архитектура
- [ROADMAP.md](ROADMAP.md) — План разработки
