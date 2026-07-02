"""
Command-line interface for ABAP-NotepadPP.
"""

from __future__ import annotations

from pathlib import Path
from time import perf_counter

from .config import (
    OUTPUT_XML,
    VERSION,
    ensure_directories,
    print_configuration,
)
from .repository import KeywordRepository
from .validator import KeywordValidator, ValidationError
from .xml_writer import XMLWriter


class Application:

    def __init__(self) -> None:

        self.repository = KeywordRepository()
        self.validator = KeywordValidator()
        self.writer = XMLWriter()

    def run(self) -> int:

        started = perf_counter()

        print_configuration()

        ensure_directories()

        print("Loading database...")

        keywords = self.repository.load()

        print(f"Loaded {len(keywords)} keywords")

        print()

        print("Validating...")

        try:

            self.validator.validate(keywords)

        except ValidationError as ex:

            print()

            print("ERROR")

            print("----------------------------------------")

            print(ex)

            return 1

        print("Validation OK")

        print()

        print("Statistics")

        print("----------------------------------------")

        statistics = self.validator.summary(keywords)

        total = 0

        for category, amount in statistics.items():

            total += amount

            print(f"{category:<20} {amount:>6}")

        print("----------------------------------------")

        print(f"{'TOTAL':<20} {total:>6}")

        print()

        print("Generating XML...")

        self.writer.write(
            keywords=keywords,
            output_file=OUTPUT_XML,
        )

        elapsed = perf_counter() - started

        print()

        print("Generation completed successfully")

        print(f"Output : {OUTPUT_XML}")

        print(f"Version: {VERSION}")

        print(f"Time   : {elapsed:.3f}s")

        return 0


def main() -> int:
    """
    CLI entry point.
    """

    app = Application()

    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())