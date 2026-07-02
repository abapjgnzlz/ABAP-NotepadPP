#!/usr/bin/env python3
"""
ABAP-NotepadPP

Main build script.
"""

from src.abap_notepadpp.config import (
    OUTPUT_XML,
    VERSION,
    ensure_directories,
    print_configuration,
)
from src.abap_notepadpp.repository import KeywordRepository
from src.abap_notepadpp.validator import (
    KeywordValidator,
    ValidationError,
)
from src.abap_notepadpp.xml_writer import XMLWriter


def main() -> int:

    print_configuration()

    ensure_directories()

    print("Loading keyword database...")

    repository = KeywordRepository()

    keywords = repository.load()

    print(f"Loaded {len(keywords)} keywords")

    print()

    print("Validating...")

    validator = KeywordValidator()

    try:

        validator.validate(keywords)

    except ValidationError as ex:

        print()

        print("Validation failed")

        print("-----------------")

        print(ex)

        return 1

    print("Validation successful")

    print()

    print("Statistics")

    print("----------")

    statistics = validator.summary(keywords)

    for category, total in statistics.items():

        print(f"{category:20} {total}")

    print()

    print("Generating XML...")

    writer = XMLWriter()

    writer.write(
        keywords,
        OUTPUT_XML,
    )

    print()

    print("Done")

    print(f"Output : {OUTPUT_XML}")

    print(f"Version: {VERSION}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())