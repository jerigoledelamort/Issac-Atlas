# Binary Passport — isaac-ng.exe

## Метаданные

| Поле | Значение |
|------|----------|
| Статус | ✅ Confirmed |
| Дата обновления | 06.07.2026 |
| Источник | Прямой анализ исследуемого экземпляра `isaac-ng.exe` |

---

## Общая информация

| Параметр | Значение | Статус |
|----------|----------|--------|
| Game | The Binding of Isaac: Repentance+ Beta | 🟢 Confirmed |
| Version | v1.9.7.17 | 🟢 Confirmed |
| Executable | isaac-ng.exe | 🟢 Confirmed |
| Platform | Windows | 🟢 Confirmed |
| Architecture | x86 (PE32) | 🟢 Confirmed |

---

## Криптографические хеши

| Параметр | Значение | Статус |
|----------|----------|--------|
| SHA-256 | `3BDFC8BAE0DC7E334B76009D0AD45DFBB16EE5F00C06FFBC3A0094E34DD44616B` | 🟢 Confirmed |
| MD5 | `2FA5097A4EF74194821D13A5CAE7B304` | 🟢 Confirmed |
| Размер файла | 9 362 440 bytes | 🟢 Confirmed |

---

## IMAGE_FILE_HEADER

| Параметр | Значение | Статус |
|----------|----------|--------|
| Machine | `0x014C` (Intel x86) | 🟢 Confirmed |
| NumberOfSections | 6 | 🟢 Confirmed |
| TimeDateStamp | `0x69E6E3A7` | 🟢 Confirmed |
| PointerToSymbolTable | `0` | 🟢 Confirmed |
| NumberOfSymbols | `0` | 🟢 Confirmed |
| SizeOfOptionalHeader | `0xE0` | 🟢 Confirmed |
| Characteristics | `0x0122` | 🟢 Confirmed |

### Characteristics (разбор)

| Флаг | Значение | Описание |
|------|----------|----------|
| `0x0002` | EXECUTABLE_IMAGE | Файл является исполняемым |
| `0x0020` | LARGE_ADDRESS_AWARE | Поддержка больших адресов |
| `0x0100` | 32BIT_MACHINE | 32-битная машина |

---

## IMAGE_OPTIONAL_HEADER

| Параметр | Значение | Статус |
|----------|----------|--------|
| Magic | `0x10B` (PE32) | 🟢 Confirmed |
| Linker Version | 14.29 | 🟢 Confirmed |
| SizeOfCode | `0x716200` | 🟢 Confirmed |
| SizeOfInitializedData | `0x14C000` | 🟢 Confirmed |
| SizeOfUninitializedData | `0` | 🟢 Confirmed |
| AddressOfEntryPoint (RVA) | `0x00E310` | 🟢 Confirmed |
| BaseOfCode | `0x1000` | 🟢 Confirmed |
| BaseOfData | `0x718000` | 🟢 Confirmed |
| ImageBase | `0x00400000` | 🟢 Confirmed |
| SectionAlignment | `0x1000` | 🟢 Confirmed |
| FileAlignment | `0x0200` | 🟢 Confirmed |
| SizeOfImage | `0x92C000` | 🟢 Confirmed |
| SizeOfHeaders | `0x400` | 🟢 Confirmed |
| Checksum | `0` | 🟢 Confirmed |
| Subsystem | Windows GUI | 🟢 Confirmed |
| DLLCharacteristics | `0x8140` | 🟢 Confirmed |
| LoaderFlags | `0` | 🟢 Confirmed |
| NumberOfRvaAndSizes | 16 | 🟢 Confirmed |

### DLLCharacteristics (разбор)

| Флаг | Значение | Описание |
|------|----------|----------|
| `0x0040` | HIGH_ENTROPY_VA | Поддержка ASLR с высокой энтропией |
| `0x0100` | NX_COMPAT | Совместимость с DEP (Data Execution Prevention) |
| `0x8000` | TERMINAL_SERVER_AWARE | Совместимость с Terminal Server |

---

## Sections

**Status:** 🟢 Confirmed

| № | Секция | Статус |
|---|--------|--------|
| 1 | `.text` | 🟢 Confirmed |
| 2 | `.rdata` | 🟢 Confirmed |
| 3 | `.data` | 🟢 Confirmed |
| 4 | `.rsrc` | 🟢 Confirmed |
| 5 | `.reloc` | 🟢 Confirmed |
| 6 | `.bind` | 🟢 Confirmed |

---

## Сводка

```
┌─────────────────────────────────────────────────────────────┐
│                    BINARY PASSPORT                           │
│                    isaac-ng.exe                              │
├─────────────────────────────────────────────────────────────┤
│  Game:      The Binding of Isaac: Repentance+ Beta           │
│  Version:   v1.9.7.17                                        │
│  Platform:  Windows                                          │
│  Arch:      x86 (PE32)                                       │
│  ImageBase: 0x00400000                                       │
│  EntryRVA:  0x00E310                                         │
│  Size:      9 362 440 bytes                                  │
│  Sections:  6 (.text, .rdata, .data, .rsrc, .reloc, .bind)   │
│  Linker:    14.29                                            │
│  Subsystem: Windows GUI                                      │
├─────────────────────────────────────────────────────────────┤
│  SHA-256:   3BDFC8BA...44616B                                │
│  MD5:       2FA5097A...7B304                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## Ссылки

- [version.md](version.md) — информация о версии игры
- [hashes.md](hashes.md) — криптографические хеши файлов
- [../docs/project_map.md](../docs/project_map.md) — карта проекта
- [../docs/research_log.md](../docs/research_log.md) — журнал исследований

---

## История изменений

| Дата | Автор | Изменения |
|------|-------|-----------|
| 06.07.2026 | NLP-Core-Team | Initial binary passport — полные данные PE-заголовков, хеши, метаданные |
