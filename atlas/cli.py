#!/usr/bin/env python3
"""
Isaac Atlas CLI — командная строка Isaac Atlas.

Использование:
    isaac-atlas decode-seed "BMR9 KSHY"
    isaac-atlas encode-seed 87067453
    isaac-atlas encode-seed 0x05308B3D
"""

from __future__ import annotations

import argparse
import os
import sys

# Добавляем корень проекта в sys.path для импорта engine.utils
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from engine.seed_decoder import (
    decode_seed_safe,
    encode_seed,
    is_valid_seed_string,
)


def cmd_decode_seed(args: argparse.Namespace) -> int:
    """Декодирует строковый сид в uint32."""
    seed_string = args.seed_string
    result = decode_seed_safe(seed_string)

    if not result.is_valid:
        print(f"Ошибка: невалидный сид \"{seed_string}\"", file=sys.stderr)
        return 1

    seed = result.seed
    print(f"Seed:   {seed_string}")
    print(f"UInt32: {seed}")
    print(f"Hex:    0x{seed:08X}")
    return 0


def cmd_encode_seed(args: argparse.Namespace) -> int:
    """Кодирует uint32 сид в строку."""
    # Разбор значения: поддерживает decimal и 0x-prefixed hex
    value_str = args.seed_value
    try:
        if value_str.lower().startswith("0x"):
            seed = int(value_str, 16)
        else:
            seed = int(value_str)
    except ValueError:
        print(f"Ошибка: невалидное число \"{value_str}\"", file=sys.stderr)
        return 1

    if seed < 0 or seed > 0xFFFFFFFF:
        print(f"Ошибка: значение должно быть в диапазоне 0..4294967295", file=sys.stderr)
        return 1

    seed_string = encode_seed(seed)
    print(f"Seed:   {seed_string}")
    print(f"UInt32: {seed}")
    print(f"Hex:    0x{seed:08X}")
    return 0


def cmd_validate_seed(args: argparse.Namespace) -> int:
    """Проверяет валидность строкового сида."""
    seed_string = args.seed_string
    if is_valid_seed_string(seed_string):
        print(f"Валидный сид: {seed_string}")
        return 0
    else:
        print(f"Невалидный сид: {seed_string}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    """Создаёт парсер аргументов CLI."""
    parser = argparse.ArgumentParser(
        prog="isaac-atlas",
        description="Isaac Atlas CLI — утилиты для The Binding of Isaac: Repentance+",
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # decode-seed
    decode_parser = subparsers.add_parser(
        "decode-seed",
        help="Декодировать строковый сид в uint32",
        description="Декодирует строковый сид (XXXX XXXX) во внутренний uint32.",
    )
    decode_parser.add_argument(
        "seed_string",
        help='Строковый сид, например "BMR9 KSHY"',
    )
    decode_parser.set_defaults(func=cmd_decode_seed)

    # encode-seed
    encode_parser = subparsers.add_parser(
        "encode-seed",
        help="Кодировать uint32 в строковый сид",
        description="Кодирует внутренний uint32 в строковый сид (XXXX XXXX).",
    )
    encode_parser.add_argument(
        "seed_value",
        help="uint32 значение (decimal или 0x-prefixed hex)",
    )
    encode_parser.set_defaults(func=cmd_encode_seed)

    # validate-seed
    validate_parser = subparsers.add_parser(
        "validate-seed",
        help="Проверить валидность строкового сида",
        description="Проверяет, является ли строка валидным сидом.",
    )
    validate_parser.add_argument(
        "seed_string",
        help='Строковый сид, например "BMR9 KSHY"',
    )
    validate_parser.set_defaults(func=cmd_validate_seed)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Точка входа CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
