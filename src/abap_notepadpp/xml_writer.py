"""
XML writer for Notepad++ User Defined Language.
"""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from .config import TEMPLATES_DIR
from .models import Category, Keyword


class XMLWriter:
    """
    Generates the Notepad++ UDL XML file.
    """

    def __init__(self) -> None:

        self.environment = Environment(
            loader=FileSystemLoader(TEMPLATES_DIR),
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def write(
        self,
        keywords: list[Keyword],
        output_file: Path,
    ) -> None:

        template = self.environment.get_template(
            "udl.xml.j2"
        )

        context = {
            "keywords": self._build_keywords(keywords),
        }

        xml = template.render(**context)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_file.write_text(
            xml,
            encoding="utf-8",
        )

    def _build_keywords(
        self,
        keywords: list[Keyword],
    ) -> str:
        """
        Build the Keywords1 section.

        Future versions will distribute the keywords
        among Keywords1..Keywords8.
        """

        values = sorted(
            {
                keyword.keyword
                for keyword in keywords
            }
        )

        return " ".join(values)

    def filter_by_category(
        self,
        keywords: list[Keyword],
        category: Category,
    ) -> list[Keyword]:

        return [
            keyword
            for keyword in keywords
            if keyword.category == category
        ]