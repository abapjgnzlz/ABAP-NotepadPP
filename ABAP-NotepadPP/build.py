#!/usr/bin/env python3
"""
ABAP-NotepadPP build entry point.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

from abap_notepadpp.cli import main


if __name__ == "__main__":
    raise SystemExit(main())