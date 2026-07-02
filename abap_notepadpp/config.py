"""
Project configuration.

All project paths and constants are centralized here.
"""

from pathlib import Path

###############################################################################
# Project paths
###############################################################################

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SRC_DIR = PROJECT_ROOT / "src"

KEYWORDS_DIR = PROJECT_ROOT / "keywords"

TEMPLATES_DIR = PROJECT_ROOT / "templates"

DIST_DIR = PROJECT_ROOT / "dist"

TESTS_DIR = PROJECT_ROOT / "tests"

DOCS_DIR = PROJECT_ROOT / "docs"

###############################################################################
# Output files
###############################################################################

OUTPUT_XML = DIST_DIR / "ABAP_S4HANA2023.xml"

###############################################################################
# Metadata
###############################################################################

PROJECT_NAME = "ABAP-NotepadPP"

VERSION = "0.1.0-alpha.1"

AUTHOR = "Jesus Gonzalez"

TARGET_ABAP = "SAP S/4HANA 2023"

###############################################################################
# XML
###############################################################################

XML_ENCODING = "UTF-8"

XML_INDENT = "    "

###############################################################################
# Supported keyword file extensions
###############################################################################

SUPPORTED_EXTENSIONS = (
    ".yaml",
    ".yml",
)

###############################################################################
# Logging
###############################################################################

LOG_LEVEL = "INFO"

###############################################################################
# Helper functions
###############################################################################


def ensure_directories() -> None:
    """
    Creates all required project directories if they do not exist.
    """

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    KEYWORDS_DIR.mkdir(parents=True, exist_ok=True)

    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    TESTS_DIR.mkdir(parents=True, exist_ok=True)


def print_configuration() -> None:
    """
    Prints the current configuration.
    """

    print("=" * 60)

    print(PROJECT_NAME)

    print("=" * 60)

    print(f"Version       : {VERSION}")

    print(f"Target        : {TARGET_ABAP}")

    print(f"Keywords      : {KEYWORDS_DIR}")

    print(f"Templates     : {TEMPLATES_DIR}")

    print(f"Output XML    : {OUTPUT_XML}")

    print()
