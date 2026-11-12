"""Shared setup for the tests: makes scripts/build_site.py importable."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_site  # noqa: E402

__all__ = ["ROOT", "build_site"]
