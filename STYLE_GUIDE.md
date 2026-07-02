# Руководство по стилю кода Isaac Atlas

## Общие принципы

### 1. Читаемость прежде всего

Код читается чаще, чем пишется. Пишите код для людей, а не для машин.

### 2. Консистентность

Стиль должен быть единообразным во всём проекте. Следуйте существующему стилю.

### 3. Простота

Избегайте излишней сложности. Простой код легче поддерживать.

---

## C++ (Engine)

### Стандарт

- **C++17** или **C++20** (по настроенному компилятору)
- Избегать неопределённого поведения
- Использовать `constexpr` где возможно

### Именование

#### Классы и структуры

```cpp
// PascalCase
class WorldGenerator;
struct RoomData;
enum class FloorType;
```

#### Функции и методы

```cpp
// camelCase
void generateWorld();
int getSeed() const;
bool isValid() const;
```

#### Переменные

```cpp
// camelCase для локальных
int currentSeed;
std::vector<Room> roomList;

// snake_case для членов класса (с префиксом m_)
int m_seed;
std::vector<Room> m_rooms;
```

#### Константы

```cpp
// UPPER_SNAKE_CASE
constexpr int MAX_FLOORS = 10;
constexpr float ROOM_SIZE = 13.0f;
```

#### Пространства имён

```cpp
// lowercase с подчёркиваниями
namespace isaac_engine {
namespace rng {
namespace generation {
```

### Форматирование

#### Отступы

```cpp
// 4 пробела, не табы
void function() {
    if (condition) {
        // код
    }
}
```

#### Фигурные скобки

```cpp
// K&R стиль для функций
void function() {
    // тело
}

// Для control statements
if (condition) {
    // тело
} else {
    // тело
}
```

#### Максимальная длина строки

- **100 символов** максимум
- Переносить длинные выражения

#### Пустые строки

```cpp
// Одна пустая строка между функциями
void firstFunction() { }

void secondFunction() { }

// Внутри функции — по смыслу
void complexFunction() {
    // Инициализация
    int a = 0;
    int b = 0;
    
    // Вычисления
    a = calculateA();
    b = calculateB();
    
    // Результат
    return a + b;
}
```

### Документирование

#### Публичные API

```cpp
/// <summary>
/// Генерирует мир для заданного seed'а.
/// </summary>
/// <param name="seed">Внутренний seed игры.</param>
/// <param name="floor">Номер этажа (0-9).</param>
/// <returns>Сгенерированный мир.</returns>
/// <remarks>
/// Алгоритм основан на исследовании: research/generation/floor-layout.md
/// </remarks>
World generateWorld(int seed, int floor);
```

#### Внутренние функции

```cpp
// Краткий комментарий для сложных участков
// Вычисляем смещение комнаты на основе RNG последовательности
int offset = calculateOffset(rng.next(), roomType);
```

### Обработка ошибок

```cpp
// Использовать исключения для ошибок
if (!isValid) {
    throw GenerationError("Invalid seed value");
}

// Использовать optional для ожидаемых «пустых» значений
std::optional<Room> findSpecialRoom(SpecialRoomType type);

// Использовать expected/result дляrecoverable ошибок
Result<World, GenerationError> tryGenerate();
```

### Умные указатели

```cpp
// Предпочитать уникальные указатели
std::unique_ptr<Generator> generator;

// Делённые указатели только при необходимости
std::shared_ptr<Cache> sharedCache;

// Избегать сырых указателей для владения
Room* room; // Только для невладеющих ссылок
```

---

## Python (скрипты)

### Стандарт

- **Python 3.9+**
- Следовать [PEP 8](https://pep8.org/)

### Именование

```python
# Классы — PascalCase
class WorldGenerator:
    pass

# Функции и переменные — snake_case
def generate_world():
    pass

current_seed = 12345

# Константы — UPPER_SNAKE_CASE
MAX_FLOORS = 10
```

### Документирование

```python
def generate_world(seed: int, floor: int) -> World:
    """
    Генерирует мир для заданного seed'а.
    
    Args:
        seed: Внутренний seed игры.
        floor: Номер этажа (0-9).
    
    Returns:
        Сгенерированный мир.
    
    Raises:
        GenerationError: Если seed невалиден.
    
    Note:
        Алгоритм основан на исследовании: research/generation/floor-layout.md
    """
    pass
```

---

## Документация (Markdown)

### Заголовки

```markdown
# Заголовок 1 (только один на файл)
## Заголовок 2
### Заголовок 3
```

### Код

````markdown
```cpp
// Указывать язык для подсветки
void function() { }
```

```python
# Указывать язык для подсветки
def function():
    pass
```
````

### Ссылки

```markdown
[Текст ссылки](path/to/file.md)

[Ссылка с заголовком](path/to/file.md "Заголовок")
```

### Таблицы

```markdown
| Колонка 1 | Колонка 2 | Колонка 3 |
|-----------|-----------|-----------|
| Данные 1  | Данные 2  | Данные 3  |
```

---

## Git

### Сообщения коммитов

```
feat(engine): добавить модуль верификации RNG

- Реализован класс RngVerifier
- Добавлены тесты сравнения с оригиналом
- Обновлена документация API

Closes #42
```

### Ветки

```
feature/engine-rng-module
fix/atlas-cli-seed-parsing
docs/architecture-update
```

---

## Проверка стиля

### Автоматические инструменты

| Язык | Инструмент | Команда |
|------|------------|---------|
| C++ | clang-format | `clang-format -i file.cpp` |
| C++ | clang-tidy | `clang-tidy file.cpp` |
| Python | black | `black file.py` |
| Python | flake8 | `flake8 file.py` |
| Python | mypy | `mypy file.py` |
| Markdown | markdownlint | `markdownlint file.md` |

### Pre-commit хуки

Рекомендуется настроить pre-commit хуки для автоматической проверки.

---

## Антипаттерны

### Запрещено

```cpp
// Магические числа
int value = 42; // ❌

// Разрешено
constexpr int MAX_ITEMS = 42; // ✅

// Глубокая вложенность
if (a) {
    if (b) {
        if (c) {
            // ❌
        }
    }
}

// Ранний возврат
if (!a) return;
if (!b) return;
// ✅
```

### Нежелательно

```cpp
// Слишком длинные функции (>50 строк)
// Слишком большие классы (>500 строк)
// God objects (классы, делающие всё)
```

---

## Примеры

### Хороший класс

```cpp
/// <summary>
/// Генератор комнат для этажа.
/// </summary>
class RoomGenerator {
public:
    /// <summary>
    /// Создаёт генератор с заданным RNG.
    /// </summary>
    explicit RoomGenerator(std::shared_ptr<Rng> rng);
    
    /// <summary>
    /// Генерирует布局 комнат.
    /// </summary>
    std::vector<Room> generateLayout(int floor);

private:
    std::shared_ptr<Rng> m_rng;
    
    Room generateSpecialRoom(SpecialRoomType type);
    void placeRoom(Room& room, int x, int y);
};
```

### Хорошая функция

```cpp
/// <summary>
/// Вычисляет позицию комнаты на основе RNG.
/// </summary>
/// <param name="rng">Генератор случайных чисел.</param>
/// <param name="grid">Сетка этажа.</param>
/// <returns>Позиция комнаты или null если невозможно.</returns>
std::optional<Position> calculateRoomPosition(
    Rng& rng,
    const FloorGrid& grid
) {
    // Попыток размещения: 10
    constexpr int MAX_ATTEMPTS = 10;
    
    for (int attempt = 0; attempt < MAX_ATTEMPTS; ++attempt) {
        int x = rng.nextInt(grid.width());
        int y = rng.nextInt(grid.height());
        
        if (grid.canPlace(x, y)) {
            return Position{x, y};
        }
    }
    
    return std::nullopt;
}
```

---

## Обновления

Руководство обновляется по мере необходимости.
Все изменения обсуждаются в issue и фиксируются в ADR.

**Последнее обновление:** 2024
