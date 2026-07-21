"""
Unit-тесты для декодера/кодировщика сидов.

Тесты построены на основе анализа FUN_009eb6b0 из isaac-ng.exe (Repentance+).
Источник истины: research/ghidra/Decomp/009eb6b0.c

Стратегия тестирования:
    1. Известные пары (строка → uint32), вычисленные вручную по алгоритму.
    2. Round-trip: encode(decode(string)) == string для валидных сидов.
    3. Round-trip: decode(encode(uint32)) == uint32 для всех uint32.
    4. Невалидные строки (неправильная длина, нет пробела, плохие символы,
       неверный checksum).
    5. Граничные случаи (seed = 0, seed = 0xFFFFFFFF).
"""

from __future__ import annotations

import random
import sys
import os
from pathlib import Path

# Добавляем корень проекта в sys.path
_PROJECT_ROOT = str(Path(__file__).resolve().parents[1])
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import pytest

from engine.seed_decoder import (
    ALPHABET,
    XOR_CONSTANT,
    decode_seed,
    decode_seed_safe,
    encode_seed,
    is_valid_seed_string,
    _compute_checksum,
    _rol8,
    _LOOKUP_TABLE,
)


# ---------------------------------------------------------------------------
# Известные пары (вычислены вручную по алгоритму FUN_009eb6b0)
# ---------------------------------------------------------------------------

KNOWN_PAIRS = [
    # (seed_string, uint32, hex)
    # "BMR9 KSHY" — вычислено вручную:
    #   v = [1, 11, 15, 31, 9, 16, 7, 20]
    #   packed = 182449344 = 0x0ADFF4C0
    #   seed = 0x0ADFF4C0 ^ 0x0FEF7FFD = 0x05308B3D = 87067453
    #   checksum = 244 = 0xF4 = (7 << 5 | 20) & 0xFF → совпадает ✓
    ("BMR9 KSHY", 87067453, 0x05308B3D),

    # seed = 0 → pre_xor = 0x0FEF7FFD
    #   v0=1(B), v1=31(9), v2=23(1), v3=23(1), v4=31(9), v5=31(9)
    #   v6_top2=1, checksum=0 → v6_bottom3=0, v7=0
    #   v6=(1<<3|0)=8(J), v7=0(A)
    #   Строка: "B911 99JA"
    ("B911 99JA", 0, 0x00000000),

    # seed = 1 → pre_xor = 0x0FEF7FFC
    #   v0=1(B), v1=31(9), v2=23(1), v3=23(1), v4=31(9), v5=31(9)
    #   v6_top2=0, checksum: temp=1→byte=1→ROL8(1,1)=2→checksum=2
    #   v6_bottom3=0, v7=2(C)
    #   v6=0(A), v7=2(C)
    #   Строка: "B911 99AC"
    ("B911 99AC", 1, 0x00000001),
]


# ---------------------------------------------------------------------------
# Тесты: декодирование известных пар
# ---------------------------------------------------------------------------

class TestDecodeKnownPairs:
    """Проверка декодирования известных строковых сидов."""

    @pytest.mark.parametrize("seed_string,expected_uint,expected_hex", KNOWN_PAIRS)
    def test_decode_known_seed(self, seed_string, expected_uint, expected_hex):
        """Декодирование известной строки даёт ожидаемый uint32."""
        result = decode_seed_safe(seed_string)
        assert result.is_valid, f"Сид \"{seed_string}\" должен быть валидным"
        assert result.seed == expected_uint
        assert result.seed == expected_hex

    @pytest.mark.parametrize("seed_string,expected_uint,expected_hex", KNOWN_PAIRS)
    def test_decode_seed_returns_uint(self, seed_string, expected_uint, expected_hex):
        """Функция decode_seed возвращает uint32."""
        assert decode_seed(seed_string) == expected_uint


# ---------------------------------------------------------------------------
# Тесты: round-trip decode → encode → decode
# ---------------------------------------------------------------------------

class TestRoundTripStringToUint:
    """Round-trip: строка → uint32 → строка → uint32."""

    @pytest.mark.parametrize("seed_string,expected_uint,_", KNOWN_PAIRS)
    def test_roundtrip_known(self, seed_string, expected_uint, _):
        """decode → encode → decode даёт тот же uint32."""
        seed = decode_seed(seed_string)
        assert seed == expected_uint
        encoded = encode_seed(seed)
        assert encoded == seed_string, (
            f"encode({seed}) = \"{encoded}\", ожидается \"{seed_string}\""
        )

    @pytest.mark.parametrize("seed_string,_,__", KNOWN_PAIRS)
    def test_roundtrip_string_preserved(self, seed_string, _, __):
        """decode → encode восстанавливает исходную строку."""
        seed = decode_seed(seed_string)
        re_encoded = encode_seed(seed)
        assert re_encoded == seed_string


class TestRoundTripUintToString:
    """Round-trip: uint32 → строка → uint32 для произвольных значений."""

    @pytest.mark.parametrize("seed", [0, 1, 42, 1000, 123456789, 0xFFFFFFFF])
    def test_roundtrip_arbitrary_uint(self, seed):
        """encode → decode даёт исходный uint32."""
        encoded = encode_seed(seed)
        decoded = decode_seed(encoded)
        assert decoded == seed, (
            f"decode(encode({seed})) = {decoded}, ожидается {seed}"
        )

    def test_roundtrip_all_alphabet_first_chars(self):
        """Проверка с сидами, где первый символ перебирает весь алфавит."""
        for i in range(32):
            seed = i << 27  # первый символ = i
            encoded = encode_seed(seed)
            decoded = decode_seed(encoded)
            assert decoded == seed

    def test_roundtrip_random(self):
        """Round-trip для 1000 случайных uint32 значений."""
        rng = random.Random(42)
        for _ in range(1000):
            seed = rng.randint(0, 0xFFFFFFFF)
            encoded = encode_seed(seed)
            result = decode_seed_safe(encoded)
            assert result.is_valid
            assert result.seed == seed


# ---------------------------------------------------------------------------
# Тесты: невалидные строки
# ---------------------------------------------------------------------------

class TestInvalidSeeds:
    """Проверка отклонения невалидных строк."""

    def test_wrong_length_short(self):
        """Слишком короткая строка."""
        assert decode_seed("BMR9 KSH") == 0
        assert not is_valid_seed_string("BMR9 KSH")

    def test_wrong_length_long(self):
        """Слишком длинная строка."""
        assert decode_seed("BMR9 KSHYY") == 0
        assert not is_valid_seed_string("BMR9 KSHYY")

    def test_wrong_length_empty(self):
        """Пустая строка."""
        assert decode_seed("") == 0
        assert not is_valid_seed_string("")

    def test_no_space(self):
        """Нет пробела на позиции 4."""
        assert decode_seed("BMR9XKSHY") == 0
        assert not is_valid_seed_string("BMR9XKSHY")

    def test_space_wrong_position(self):
        """Пробел не на позиции 4."""
        assert decode_seed("BMR 9KSHY") == 0
        assert not is_valid_seed_string("BMR 9KSHY")

    def test_invalid_char_i(self):
        """Символ I не входит в алфавит."""
        assert decode_seed("BMR9 IKHY") == 0
        assert not is_valid_seed_string("BMR9 IKHY")

    def test_invalid_char_o(self):
        """Символ O не входит в алфавит."""
        assert decode_seed("BMR9 OKHY") == 0
        assert not is_valid_seed_string("BMR9 OKHY")

    def test_invalid_char_u(self):
        """Символ U не входит в алфавит."""
        assert decode_seed("BMR9 UKHY") == 0
        assert not is_valid_seed_string("BMR9 UKHY")

    def test_invalid_char_5(self):
        """Символ 5 не входит в алфавит."""
        assert decode_seed("BMR9 5KHY") == 0
        assert not is_valid_seed_string("BMR9 5KHY")

    def test_lowercase_rejected(self):
        """Строчные буквы не входят в алфавит (lookup table чувствительна к регистру)."""
        assert decode_seed("bmr9 kshy") == 0
        assert not is_valid_seed_string("bmr9 kshy")

    def test_bad_checksum(self):
        """Правильный формат и алфавит, но неверный checksum."""
        # Берём валидный сид и меняем последний символ
        # "BMR9 KSHY" валиден. Меняем Y (v7=20) на A (v7=0).
        # checksum изменится, но не совпадёт с ожидаемым.
        assert decode_seed("BMR9 KSHA") == 0
        assert not is_valid_seed_string("BMR9 KSHA")

    def test_bad_checksum_middle(self):
        """Меняем 7-й символ — нарушается checksum."""
        # "BMR9 KSHY" → меняем H (v6=7) на A (v6=0).
        # v6_top2 изменится (0>>3=0 вместо 7>>3=0), v6_bottom3 изменится (0 вместо 7).
        # seed может остаться тем же (v6_top2=0 в обоих случаях),
        # но checksum не совпадёт.
        result = decode_seed_safe("BMR9 KSAY")
        # Проверяем, что либо невалиден, либо декодируется в другой сид
        if result.is_valid:
            assert result.seed != 87067453


# ---------------------------------------------------------------------------
# Тесты: алфавит и lookup table
# ---------------------------------------------------------------------------

class TestAlphabet:
    """Проверка алфавита и lookup table."""

    def test_alphabet_length(self):
        """Алфавит содержит ровно 32 символа."""
        assert len(ALPHABET) == 32

    def test_alphabet_no_duplicates(self):
        """Все символы алфавита уникальны."""
        assert len(set(ALPHABET)) == 32

    def test_alphabet_excludes_i(self):
        """Буква I исключена из алфавита."""
        assert "I" not in ALPHABET

    def test_alphabet_excludes_o(self):
        """Буква O исключена из алфавита."""
        assert "O" not in ALPHABET

    def test_alphabet_excludes_u(self):
        """Буква U исключена из алфавита."""
        assert "U" not in ALPHABET

    def test_alphabet_excludes_5(self):
        """Цифра 5 исключена из алфавита."""
        assert "5" not in ALPHABET

    def test_lookup_table_all_valid_chars(self):
        """Каждый символ алфавита декодируется в свой индекс."""
        for index, char in enumerate(ALPHABET):
            assert _LOOKUP_TABLE[ord(char)] == index

    def test_lookup_table_invalid_chars(self):
        """Символы вне алфавита декодируются в 0xFF."""
        for byte_val in range(256):
            char = chr(byte_val)
            if char not in ALPHABET:
                assert _LOOKUP_TABLE[byte_val] == 0xFF

    def test_alphabet_exact_string(self):
        """Точное совпадение строки алфавита с декомпилированной функцией."""
        assert ALPHABET == "ABCDEFGHJKLMNPQRSTWXYZ01234V6789"


# ---------------------------------------------------------------------------
# Тесты: checksum
# ---------------------------------------------------------------------------

class TestChecksum:
    """Проверка алгоритма контрольной суммы."""

    def test_checksum_zero_seed(self):
        """Checksum для seed=0 равен 0 (цикл не выполняется)."""
        assert _compute_checksum(0) == 0

    def test_checksum_known_bmr9(self):
        """Checksum для сида BMR9 KSHY (0x05308B3D) равен 244."""
        assert _compute_checksum(0x05308B3D) == 244

    def test_checksum_known_seed_1(self):
        """Checksum для seed=1: temp=1→byte=1→ROL8(1,1)=2→checksum=2."""
        assert _compute_checksum(1) == 2

    def test_rol8(self):
        """Проверка циклического сдвига влево на 1 бит."""
        assert _rol8(0, 1) == 0
        assert _rol8(1, 1) == 2
        assert _rol8(128, 1) == 1       # 0x80 → 0x01
        assert _rol8(255, 1) == 255     # 0xFF → 0xFF
        assert _rol8(0x69, 1) == 0xD2   # 0110 1001 → 1101 0010


# ---------------------------------------------------------------------------
# Тесты: формат и структура encode
# ---------------------------------------------------------------------------

class TestEncodeFormat:
    """Проверка формата вывода encode_seed."""

    @pytest.mark.parametrize("seed", [0, 1, 42, 0xFFFFFFFF])
    def test_encode_format(self, seed):
        """Закодированная строка имеет формат XXXX XXXX (9 символов)."""
        result = encode_seed(seed)
        assert len(result) == 9
        assert result[4] == " "
        assert result[:4].isalpha() or any(c.isdigit() for c in result[:4])
        assert result[5:].isalpha() or any(c.isdigit() for c in result[5:])

    @pytest.mark.parametrize("seed", [0, 1, 42, 0xFFFFFFFF])
    def test_encode_chars_in_alphabet(self, seed):
        """Все символы закодированной строки входят в алфавит."""
        result = encode_seed(seed)
        for char in result:
            if char != " ":
                assert char in ALPHABET

    @pytest.mark.parametrize("seed", [0, 1, 42, 0xFFFFFFFF])
    def test_encoded_is_valid(self, seed):
        """Закодированная строка проходит валидацию."""
        encoded = encode_seed(seed)
        assert is_valid_seed_string(encoded)


# ---------------------------------------------------------------------------
# Тест: edge case — неоднозначность возврата 0
# ---------------------------------------------------------------------------

class TestZeroAmbiguity:
    """Проверка поведения при seed=0 (неоднозначность возврата 0)."""

    def test_zero_seed_valid(self):
        """Сид 0 кодируется в валидную строку."""
        encoded = encode_seed(0)
        assert is_valid_seed_string(encoded)

    def test_zero_seed_decodes_to_zero(self):
        """Декодирование строки для seed=0 даёт 0."""
        encoded = encode_seed(0)
        result = decode_seed_safe(encoded)
        assert result.is_valid
        assert result.seed == 0

    def test_decode_seed_safe_distinguishes(self):
        """decode_seed_safe отличает валидный seed=0 от невалидной строки."""
        valid_zero = decode_seed_safe(encode_seed(0))
        invalid = decode_seed_safe("INVALID!")
        assert valid_zero.is_valid
        assert valid_zero.seed == 0
        assert not invalid.is_valid
        assert invalid.seed == 0

    def test_decode_seed_cannot_distinguish(self):
        """decode_seed не может отличить seed=0 от ошибки (возвращает 0)."""
        valid_zero = decode_seed(encode_seed(0))
        invalid = decode_seed("INVALID!")
        # Оба возвращают 0 — это известное ограничение алгоритма
        assert valid_zero == 0
        assert invalid == 0
