# Процесс выпуска версий Isaac Atlas

## Версионирование

Проект использует [Semantic Versioning](https://semver.org/lang/ru/):

- **MAJOR** — несовместимые изменения API
- **MINOR** — новая функциональность с обратной совместимостью
- **PATCH** — исправления багов с обратной совместимостью

### Пре-релизы

- `0.1.0-alpha.1` — альфа версия
- `0.1.0-beta.1` — бета версия
- `1.0.0-rc.1` — release candidate

---

## Процесс выпуска

### 1. Планирование

- Определить scope выпуска
- Проверить все задачи в milestone
- Установить дату релиза

### 2. Подготовка

```bash
# Создать ветку релиза
git checkout main
git pull
git checkout -b release/1.0.0

# Обновить версию в CMakeLists.txt
# Обновить CHANGELOG.md
# Обновить документацию

# Запустить полный набор тестов
ctest --output-on-failure

# Собрать релиз
cmake --build . --config Release
```

### 3. Release Candidate

```bash
# Создать тег
git tag -a v1.0.0-rc.1 -m "Release candidate 1.0.0"

# Push
git push origin main
git push origin v1.0.0-rc.1
```

### 4. Тестирование RC

- Ручное тестирование
- Тестирование на разных платформах
- Сбор обратной связи

### 5. Релиз

```bash
# Создать финальный тег
git tag -a v1.0.0 -m "Release 1.0.0"

# Push
git push origin main
git push origin v1.0.0

# Создать GitHub Release
# - Upload binaries
# - Changelog
# - Notes
```

---

## Чеклист релиза

### Перед релизом

- [ ] Все тесты проходят
- [ ] Документация обновлена
- [ ] CHANGELOG.md обновлён
- [ ] Версия обновлена в коде
- [ ] Release notes написаны
- [ ] Обратная связь от RC учтена
- [ ] Security audit пройден (для major releases)

### После релиза

- [ ] Создан branch для патчей
- [ ] Обновлён main с новой версии
- [ ] Объявление опубликовано
- [ ] Менторы уведомлены

---

## Типы релизов

### Major (1.0.0, 2.0.0, ...)

- Небрежимые изменения API
- Полная документация
- Полный security audit
- Длительное тестирование

### Minor (1.1.0, 1.2.0, ...)

- Новая функциональность
- Обновление документации
- Стандартное тестирование

### Patch (1.0.1, 1.0.2, ...)

- Исправления багов
- Минимальная документация
- Короткое тестирование

---

## Автоматизация

### CI/CD

```yaml
# Пример workflow
name: Release
on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build
        run: |
          mkdir build
          cd build
          cmake ..
          cmake --build . --config Release
      
      - name: Test
        run: cd build && ctest --output-on-failure
      
      - name: Upload
        uses: actions/upload-artifact@v3
        with:
          name: isaac-atlas-${{ github.ref_name }}
          path: build/bin/
```

---

## Релиз notes

### Шаблон

```markdown
# Release vX.Y.Z

## Что нового

### Новые возможности
- ...

### Улучшения
- ...

### Исправления
- ...

## Известные проблемы
- ...

## Благодарности
- ...
```

---

## Контакты

Для вопросов по процессу релизов:
- Открыть issue с меткой `release`
- Обсудить в discussion
