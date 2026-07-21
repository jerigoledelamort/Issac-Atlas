"""
Pytest configuration — добавляет корень проекта в sys.path.

Это позволяет импортировать модули из engine/ и atlas/ без установки пакета.
"""

import sys
from pathlib import Path

_PROJECT_ROOT = str(Path(__file__).resolve().parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
