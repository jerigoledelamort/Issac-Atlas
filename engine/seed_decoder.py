"""
Seed Decoder for The Binding of Isaac: Repentance+

Decodes string start seeds (e.g. "BMR9 KSHY") into internal uint32 values,
and encodes uint32 values back into string seeds.

Algorithm reconstructed from FUN_009eb6b0 in isaac-ng.exe (Repentance+).
Source of truth: research/ghidra/Decomp/009eb6b0.c

Reference: research/rng/seed-decoding.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Константы алгоритма (восстановлены из FUN_009eb6b0)
# ---------------------------------------------------------------------------

#: Алфавит кодирования — 32 символа, каждый кодирует 5 бит (0..31).
#:
#: Из алфавита исключены символы, неоднозначные при визуальном чтении:
#: I (похож на L), O (похож на 0), U (похож на V), 5 (похож на S).
#:
#: Порядок символов в точности соответствует строковому литералу из
#: декомпилированной функции:
#:   "ABCDEFGHJKLMNPQRSTWXYZ01234V6789"
ALPHABET = "ABCDEFGHJKLMNPQRSTWXYZ01234V6789"

#: XOR-константа, применяемая после упаковки битов.
#: Восстановлена из выражения ``^ 0xfef7ffd`` в FUN_009eb6b0.
XOR_CONSTANT = 0x0FEF7FFD

#: Ожидаемая длина строкового сида (4 символа + пробел + 4 символа).
SEED_STRING_LENGTH = 9

#: Позиция пробела-разделителя в строке сида (индекс с нуля).
SPACE_POSITION = 4

#: Признак недопустимого символа в lookup table.
INVALID_CHAR = 0xFF


# ---------------------------------------------------------------------------
# Lookup table: символ ASCII -> 5-битное значение (0..31) или 0xFF
# ---------------------------------------------------------------------------

#: Таблица размером 256 байт, инициализируемая 0xFF.
#: Для каждого символа алфавита записывается его индекс (0..31).
#: Соответствует ``memset(local_110, 0xff, 0x100)`` и циклу заполнения
#: в FUN_009eb6b0.
_LOOKUP_TABLE = bytearray([INVALID_CHAR] * 256)
for _index, _char in enumerate(ALPHABET):
    _LOOKUP_TABLE[ord(_char)] = _index


# ---------------------------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------------------------

def _rol8(value: int, shift: int = 1) -> int:
    """Циклический сдвиг 8-битного значения влево на ``shift`` бит.

    Соответствует выражению из FUN_009eb6b0::

        cVar2 * '\\x02' - (cVar2 >> 7)

    где ``cVar2`` — signed char. В 8-битной беззнаковой арифметике это
    эквивалентно ``ROL8(cVar2, 1)``.
    """
    return ((value << shift) | (value >> (8 - shift))) & 0xFF


def _compute_checksum(seed: int) -> int:
    """Вычисляет 8-битную контрольную сумму значения сида.

    Алгоритм обрабатывает значение сида порциями по 5 бит (от младших к
    старшим). На каждой итерации берётся младший байт текущего значения,
    прибавляется к аккумулятору, после чего аккумулятор циклически
    сдвигается влево на 1 бит.

    Соответствует циклу из FUN_009eb6b0::

        bVar3 = 0;
        for (uVar6 = uVar4; uVar6 != 0; uVar6 = uVar6 >> 5) {
            cVar2 = bVar3 + (char)uVar6;
            bVar3 = cVar2 * '\\x02' - (cVar2 >> 7);  // ROL8(cVar2, 1)
        }

    Особые случаи:
        - При ``seed == 0`` цикл не выполняется ни разу, checksum = 0.
    """
    checksum = 0
    temp = seed & 0xFFFFFFFF
    while temp != 0:
        byte_val = temp & 0xFF
        checksum = _rol8((checksum + byte_val) & 0xFF, 1)
        temp >>= 5
    return checksum


# ---------------------------------------------------------------------------
# Результат декодирования
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class DecodeResult:
    """Результат декодирования строкового сида.

    Attributes:
        seed:     Внутреннее uint32 значение сида (0 при невалидной строке).
        is_valid: True, если строка прошла все проверки (формат,
                  алфавит, checksum).
    """

    seed: int
    is_valid: bool


# ---------------------------------------------------------------------------
# Публичный API: декодирование
# ---------------------------------------------------------------------------

def decode_seed(seed_string: str) -> int:
    """Декодирует строковый сид в uint32.

    Функция полностью повторяет логику ``FUN_009eb6b0``:

    1. Проверка длины строки (ровно 9 символов).
    2. Проверка пробела на позиции 4 (индекс с нуля).
    3. Декодирование 8 символов (позиция 4 — пробел — пропускается)
       через lookup table; недопустимый символ → возврат 0.
    4. Упаковка битов: 6 полных 5-битных значений + 2 старших бита
       7-го символа = 32 бита.
    5. XOR с константой ``0x0FEF7FFD``.
    6. Вычисление checksum и сравнение с контрольным байтом, собранным
       из младших 3 бит 7-го символа и 5 бит 8-го символа.
    7. При совпадении checksum возвращает uint32 сид, иначе 0.

    .. warning::
        Возврат 0 неоднозначен: 0 означает либо невалидную строку,
        либо валидную строку, декодирующуюся в сид 0.
        Для однозначной проверки валидности используйте
        :func:`decode_seed_safe`.

    Args:
        seed_string: Строка формата ``"XXXX XXXX"``.

    Returns:
        uint32 сид или 0 при ошибке.
    """
    result = decode_seed_safe(seed_string)
    return result.seed


def decode_seed_safe(seed_string: str) -> DecodeResult:
    """Декодирует строковый сид с явным указанием валидности.

    В отличие от :func:`decode_seed`, позволяет отличить невалидную
    строку от валидной строки с сидом 0.

    Args:
        seed_string: Строка формата ``"XXXX XXXX"``.

    Returns:
        :class:`DecodeResult` с полем ``seed`` и флагом ``is_valid``.
    """
    # --- Этап 1: проверка длины ---
    # Соответствует: if (param_1[4] == 9) — size-поле std::string == 9
    if len(seed_string) != SEED_STRING_LENGTH:
        return DecodeResult(seed=0, is_valid=False)

    # --- Этап 2: проверка пробела-разделителя ---
    # Соответствует: if (*(char *)(puVar1 + 1) == ' ')
    # puVar1 + 1 — смещение 4 байта от начала строки, т.е. индекс 4.
    if seed_string[SPACE_POSITION] != " ":
        return DecodeResult(seed=0, is_valid=False)

    # --- Этап 3: декодирование 8 символов через lookup table ---
    # Позиция 4 (пробел) пропускается. Остальные 8 позиций (0,1,2,3,5,6,7,8)
    # отображаются в выходной массив индексов 0..7:
    #   позиция < 5  → выходной индекс = позиция
    #   позиция >= 5 → выходной индекс = позиция - 1
    # Соответствует циклу ``do { if (uVar4 != 4) { ... } } while (uVar4 < 9)``
    values = [0] * 8
    for pos in range(SEED_STRING_LENGTH):
        if pos == SPACE_POSITION:
            continue
        if pos < SPACE_POSITION:
            out_idx = pos
        else:
            out_idx = pos - 1
        # local_110[*(char *)((int)puVar1 + uVar4)]
        decoded = _LOOKUP_TABLE[ord(seed_string[pos])]
        if decoded == INVALID_CHAR:
            return DecodeResult(seed=0, is_valid=False)
        values[out_idx] = decoded

    # --- Этап 4: упаковка битов ---
    # 6 полных 5-битных значений (values[0..5]) + 2 старших бита values[6].
    # Соответствует:
    #   ((((((v0 << 5 | v1) << 5 | v2) << 5 | v3) << 5 | v4) << 5 | v5)
    #       << 2 | (v6 >> 3)) ^ 0xfef7ffd
    packed = values[0]
    packed = (packed << 5) | values[1]
    packed = (packed << 5) | values[2]
    packed = (packed << 5) | values[3]
    packed = (packed << 5) | values[4]
    packed = (packed << 5) | values[5]
    packed = (packed << 2) | (values[6] >> 3)

    # --- Этап 5: XOR с константой ---
    seed = (packed ^ XOR_CONSTANT) & 0xFFFFFFFF

    # --- Этап 6: проверка checksum ---
    # Ожидаемый checksum: младшие 3 бита values[6] в позициях 5-7
    # и 5 бит values[7] в позициях 0-4.
    # Соответствует: (byte)(local_a << 5 | local_9)
    # где local_a = values[6], local_9 = values[7].
    expected_checksum = ((values[6] << 5) | values[7]) & 0xFF
    actual_checksum = _compute_checksum(seed)

    if actual_checksum != expected_checksum:
        return DecodeResult(seed=0, is_valid=False)

    return DecodeResult(seed=seed, is_valid=True)


# ---------------------------------------------------------------------------
# Публичный API: кодирование (обратное преобразование)
# ---------------------------------------------------------------------------

def encode_seed(seed: int) -> str:
    """Кодирует uint32 сид в строку формата ``"XXXX XXXX"``.

    Обратное преобразование к :func:`decode_seed`. Кодирование однозначно:
    каждому uint32 соответствует ровно одна валидная строка.

    Алгоритм:
    1. Отменить XOR: ``pre_xor = seed ^ 0x0FEF7FFD``.
    2. Извлечь 6 полных 5-битных значений и 2 старших бита 7-го символа.
    3. Вычислить checksum из значения сида.
    4. Извлечь младшие 3 бита 7-го символа и 5 бит 8-го символа из checksum.
    5. Собрать 7-й символ и отобразить все значения в символы алфавита.

    Args:
        seed: Внутренний uint32 сид.

    Returns:
        Строка формата ``"XXXX XXXX"``.
    """
    seed &= 0xFFFFFFFF

    # Шаг 1: отменить XOR
    pre_xor = seed ^ XOR_CONSTANT

    # Шаг 2: извлечь 5-битные значения из pre_xor
    v0 = (pre_xor >> 27) & 0x1F
    v1 = (pre_xor >> 22) & 0x1F
    v2 = (pre_xor >> 17) & 0x1F
    v3 = (pre_xor >> 12) & 0x1F
    v4 = (pre_xor >> 7) & 0x1F
    v5 = (pre_xor >> 2) & 0x1F
    v6_top2 = pre_xor & 0x3  # 2 старших бита 7-го символа

    # Шаг 3: вычислить checksum из сида
    checksum = _compute_checksum(seed)

    # Шаг 4: извлечь младшие 3 бита 7-го символа и 5 бит 8-го из checksum
    v6_bottom3 = (checksum >> 5) & 0x07
    v7 = checksum & 0x1F

    # Шаг 5: собрать 7-й символ (2 бита из сида + 3 бита из checksum)
    v6 = (v6_top2 << 3) | v6_bottom3

    # Шаг 6: отобразить значения в символы алфавита
    indices = [v0, v1, v2, v3, v4, v5, v6, v7]
    chars = [ALPHABET[i] for i in indices]

    return f"{chars[0]}{chars[1]}{chars[2]}{chars[3]} {chars[4]}{chars[5]}{chars[6]}{chars[7]}"


def is_valid_seed_string(seed_string: str) -> bool:
    """Проверяет, является ли строка валидным сидом.

    Args:
        seed_string: Строка для проверки.

    Returns:
        True, если строка декодируется валидно (формат, алфавит, checksum).
    """
    return decode_seed_safe(seed_string).is_valid
