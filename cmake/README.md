# CMake Modules

## Назначение

CMake модули и конфигурации сборки.

## Структура

```
cmake/
├── modules/         # Пользовательские CMake модули
└── config/          # Конфигурации сборки
```

## Использование

```cmake
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules")
```
